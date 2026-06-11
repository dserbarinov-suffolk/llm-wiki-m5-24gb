# Vim + tmux with unified LSP keybindings (Python / TypeScript / React), no root

A from-scratch replication guide for the development environment on this
machine: latest Vim and tmux built from source into `~/.local`, one LSP
client driving both **pyright** (Python) and **typescript-language-server**
(TS/TSX/JS/JSX), so *go to definition*, *hover type hints*, *references*,
and *rename* use **identical keybindings in every language**. Everything
installs to user space — no `sudo` anywhere.

Each step lists exact commands. Issues encountered on the original setup are
called out inline as **Gotcha** blocks so you recognize them when they bite.

## Preconditions

- macOS on Apple Silicon (arm64). Intel works too — substitute `x86_64`/`x64`
  in download URLs.
- Xcode Command Line Tools installed (`xcode-select -p` prints a path;
  if not: `xcode-select --install` — this is the one step that may prompt
  for an admin-approved install on managed machines).
- Default shell bash; PATH additions go in `~/.bash_profile`.
- `~/.local/bin` on PATH. If missing, run:

```bash
mkdir -p ~/.local/bin ~/.local/src ~/.local/etc
printf '\nexport PATH="$HOME/.local/bin:$PATH"\n' >> ~/.bash_profile
source ~/.bash_profile
```

## Step 0 — Corporate TLS interception (skip on a home network)

On networks with SSL inspection (here: Netskope), tools that bundle their own
certificate store (`node`, `npm`, `uv`) reject every HTTPS connection with
errors like `SELF_SIGNED_CERT_IN_CHAIN` or `invalid peer certificate:
UnknownIssuer`, while plain `curl` works (it uses the macOS keychain).

Diagnose: inspect the chain a known host serves. If the issuer is your
employer/proxy rather than a public CA, you are being intercepted:

```bash
echo | openssl s_client -connect registry.npmjs.org:443 -showcerts 2>/dev/null | grep -E "s:|i:"
```

Fix properly (do **not** disable TLS verification): export the proxy CA from
the keychains into a PEM bundle and point the tools at it. Replace `netskope`
/ `goskope` with strings matching your proxy's certificate names from the
diagnose step:

```bash
security find-certificate -a -p /Library/Keychains/System.keychain > ~/.local/etc/corp-ca.pem
security find-certificate -a -p /System/Library/Keychains/SystemRootCertificates.keychain >> ~/.local/etc/corp-ca.pem
security find-certificate -a -c netskope -p >> ~/.local/etc/corp-ca.pem
security find-certificate -a -c goskope  -p >> ~/.local/etc/corp-ca.pem

printf '\nexport NODE_EXTRA_CA_CERTS="$HOME/.local/etc/corp-ca.pem"\nexport UV_NATIVE_TLS=true\n' >> ~/.bash_profile
source ~/.bash_profile
```

> **Gotcha:** the proxy CA may live in a different keychain than expected.
> If npm still fails after adding the System keychain, run the
> `find-certificate -c <name>` variants against the *default* keychain (no
> path argument) as shown above — that searches the login keychain too.

> **Gotcha:** `npm config set cafile <path>` is also worth setting
> (`npm config set cafile=$HOME/.local/etc/corp-ca.pem`), but verify it stuck
> with `npm config get cafile` — a failed set is silent.
> `NODE_EXTRA_CA_CERTS` covers node-based tools that ignore npm config
> (pyright's downloader, coc, etc.).

## Step 1 — node (user-space tarball, needed for both language servers)

Find the current LTS at <https://nodejs.org/dist/> and substitute the version:

```bash
cd ~/.local/src
curl -fL -o node.tar.gz https://nodejs.org/dist/v24.16.0/node-v24.16.0-darwin-arm64.tar.gz
tar xzf node.tar.gz && rm node.tar.gz
ln -sf ~/.local/src/node-v24.16.0-darwin-arm64/bin/node ~/.local/bin/node
ln -sf ~/.local/src/node-v24.16.0-darwin-arm64/bin/npm  ~/.local/bin/npm
ln -sf ~/.local/src/node-v24.16.0-darwin-arm64/bin/npx  ~/.local/bin/npx
node --version
```

## Step 2 — language servers and tools via npm

Point npm's global prefix at user space, then install:

```bash
npm config set prefix ~/.local
npm install -g typescript typescript-language-server pyright prettier
which typescript-language-server pyright-langserver
```

> **Gotcha:** an intercepting proxy may **403-block very new package
> tarballs** it hasn't scanned yet (here: `prettier-3.8.4.tgz` was blocked
> while everything else installed). On `npm error E403` for one package, try
> a slightly older release: `npm install -g prettier@3.6.2`.

## Step 3 — build Vim from source with `+python3`

```bash
cd ~/.local/src
git clone --depth 1 https://github.com/vim/vim.git vim-src
cd vim-src
```

Vim needs a Python with both a shared library (`libpython3.X.dylib`) and
headers. The macOS CLT Python often fails vim's link test. The cleanest
no-root source is a `uv`-managed Python:

```bash
curl -fLsS https://astral.sh/uv/install.sh | sh     # installs uv to ~/.local/bin
uv python install 3.12                              # add --native-tls behind an intercepting proxy
# Find the install path (substitute the exact version below):
ls ~/.local/share/uv/python/
P=~/.local/share/uv/python/cpython-3.12.13-macos-aarch64-none
```

Configure and build. The two extra variables are load-bearing (see gotcha):

```bash
LDFLAGS="-L$P/lib" vi_cv_dll_name_python3="$P/lib/libpython3.12.dylib" \
./configure --prefix=$HOME/.local --with-features=huge \
    --enable-python3interp=dynamic --with-python3-command=$P/bin/python3.12 \
    --disable-gui --without-x --enable-terminal
make -j8
make install
```

Verify — both lines matter (the second proves the interpreter actually loads
at runtime, not just that the flag is compiled in):

```bash
~/.local/bin/vim --version | grep -o '[+-]python3[^ ]*'   # expect: +python3/dyn
~/.local/bin/vim -es -c 'py3 import sys; print(sys.version)' -c 'qa!'
```

> **Gotcha:** without `LDFLAGS`, configure's "compile and link flags for
> Python 3 are sane" check fails with `ld: library 'python3.12' not found` —
> it looks only in Python's `config-3.12-darwin` directory, but the dylib
> lives in `lib/`. Configure then *silently* disables python3 and the build
> completes as `-python3`. Always check the link-test result in
> `src/auto/config.log` if the feature flag comes out wrong.

> **Gotcha:** `vi_cv_dll_name_python3` pins the exact dylib path vim will
> `dlopen` at runtime. Without it, dynamic loading may look for a bare
> `libpython3.12.dylib` on standard paths and fail.

## Step 4 — build tmux from source (libevent first)

```bash
cd ~/.local/src
curl -fL -o libevent.tar.gz https://github.com/libevent/libevent/releases/download/release-2.1.12-stable/libevent-2.1.12-stable.tar.gz
tar xzf libevent.tar.gz
cd libevent-2.1.12-stable
./configure --prefix=$HOME/.local --disable-openssl
make -j8 && make install

cd ~/.local/src
curl -fL -o tmux.tar.gz https://github.com/tmux/tmux/releases/download/3.6b/tmux-3.6b.tar.gz
tar xzf tmux.tar.gz
cd tmux-3.6b
CPPFLAGS="-I$HOME/.local/include" LDFLAGS="-L$HOME/.local/lib" \
./configure --prefix=$HOME/.local --disable-utf8proc
make -j8 && make install
~/.local/bin/tmux -V
```

> **Gotcha:** tmux ≥3.6 aborts configure on macOS with
> `must give --enable-utf8proc or --disable-utf8proc`. Without root you don't
> have utf8proc; `--disable-utf8proc` is fine (slightly less precise emoji
> width handling).

## Step 5 — ripgrep and fzf binaries

```bash
cd ~/.local/src
curl -fL -o rg.tar.gz https://github.com/BurntSushi/ripgrep/releases/download/14.1.1/ripgrep-14.1.1-aarch64-apple-darwin.tar.gz
tar xzf rg.tar.gz
cp ripgrep-14.1.1-aarch64-apple-darwin/rg ~/.local/bin/

# Check https://github.com/junegunn/fzf/releases for the current version:
curl -fL -o fzf.tgz https://github.com/junegunn/fzf/releases/download/v0.73.1/fzf-0.73.1-darwin_arm64.tar.gz
tar xzf fzf.tgz && mv fzf ~/.local/bin/

rg --version && fzf --version
```

> **Gotcha:** scripting "latest release" via `api.github.com` hits the
> unauthenticated rate limit (60 req/hr) quickly and starts returning 403.
> Hard-coded direct release URLs are more reliable for a one-time setup.

## Step 6 — vim-plug and the vimrc

```bash
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
cp ~/.vimrc ~/.vimrc.backup 2>/dev/null   # keep your old config
```

Write `~/.vimrc`. The design: one LSP plugin (`yegappan/lsp`, pure vim9script
— no node/python dependency inside vim), servers registered per filetype, and
**all bindings applied buffer-locally on the `LspAttached` event** — which is
what makes them identical across languages by construction.

```bash
cat > ~/.vimrc <<'VIMRC'
" Unified LSP: Python and TS/React share one set of bindings.
"   gd definition | gy type-def | gi implementation | gr references
"   K hover | <leader>rn rename | <leader>qf code action
"   ]d/[d diagnostics | <leader>d list | <leader>h toggle auto-hover
let mapleader = ","

call plug#begin()
Plug 'yegappan/lsp'
Plug 'junegunn/fzf'
Plug 'junegunn/fzf.vim'
Plug 'christoomey/vim-tmux-navigator'
call plug#end()

syntax on
set number autoindent encoding=utf-8
set nobackup nowritebackup           " language servers dislike backup files
set updatetime=300                   " CursorHold delay -> auto-hover latency
set signcolumn=yes
set tabstop=4 shiftwidth=4 expandtab
set ttimeoutlen=10
nnoremap <space> za

" --- LSP servers (adjust paths if your prefix differs) ---
let s:lsp_servers = [
\   #{
\       name: 'pyright',
\       filetype: ['python'],
\       path: expand('~/.local/bin/pyright-langserver'),
\       args: ['--stdio'],
\       workspaceConfig: #{
\           python: #{ pythonPath: getcwd() .. '/.venv/bin/python' },
\       },
\   },
\   #{
\       name: 'tsserver',
\       filetype: ['typescript', 'typescriptreact', 'javascript', 'javascriptreact'],
\       path: expand('~/.local/bin/typescript-language-server'),
\       args: ['--stdio'],
\   },
\ ]
let s:lsp_options = #{
\   autoComplete: v:true,
\   showDiagWithSign: v:true,
\   autoHighlightDiags: v:true,
\   useQuickfixForLocations: v:false,
\   showDiagInPopup: v:true,
\ }
autocmd User LspSetup call LspOptionsSet(s:lsp_options)
autocmd User LspSetup call LspAddServer(s:lsp_servers)

" --- One set of keybindings for every language with a server attached ---
function! s:OnLspAttached() abort
    let b:lsp_attached = 1
    nnoremap <buffer> <silent> gd         :LspGotoDefinition<CR>
    nnoremap <buffer> <silent> <c-]>      :LspGotoDefinition<CR>
    nnoremap <buffer> <silent> gy         :LspGotoTypeDef<CR>
    nnoremap <buffer> <silent> gi         :LspGotoImpl<CR>
    nnoremap <buffer> <silent> gr         :LspShowReferences<CR>
    nnoremap <buffer> <silent> K          :LspHover<CR>
    nnoremap <buffer> <silent> <leader>rn :LspRename<CR>
    nnoremap <buffer> <silent> <leader>qf :LspCodeAction<CR>
    vnoremap <buffer> <silent> <leader>qf :LspCodeAction<CR>
    nnoremap <buffer> <silent> ]d         :LspDiag next<CR>
    nnoremap <buffer> <silent> [d         :LspDiag prev<CR>
    nnoremap <buffer> <silent> <leader>aj :LspDiag next<CR>
    nnoremap <buffer> <silent> <leader>ak :LspDiag prev<CR>
    nnoremap <buffer> <silent> <leader>d  :LspDiag show<CR>
    nnoremap <buffer> <silent> <leader>o  :LspOutline<CR>
    nnoremap <buffer> <silent> <leader>f  :LspFormat<CR>
endfunction
autocmd User LspAttached call s:OnLspAttached()

" --- Auto-hover: type of the symbol under the cursor after it rests ---
let g:auto_hover = 1
function! s:AutoHover() abort
    if g:auto_hover && get(b:, 'lsp_attached', 0) && mode() ==# 'n'
        silent! LspHover
    endif
endfunction
function! s:ToggleAutoHover() abort
    let g:auto_hover = !g:auto_hover
    echo 'auto-hover ' .. (g:auto_hover ? 'on' : 'off')
endfunction
augroup lsp_auto_hover
    autocmd!
    autocmd CursorHold * call s:AutoHover()
augroup END
nnoremap <silent> <leader>h :call <SID>ToggleAutoHover()<CR>

" --- fzf / ripgrep ---
let $FZF_DEFAULT_COMMAND = 'rg --files --hidden --glob "!**/.git/*"'
let $FZF_DEFAULT_OPTS = '--layout=reverse --info=inline --height=40%'
nnoremap <silent> <C-p>     :Files<CR>
nnoremap <silent> <leader>b :Buffers<CR>
nnoremap <leader>/ :Rg<Space>
function! s:RgWordUnderCursor() abort
    let word = expand('<cword>')
    if !empty(word)
        execute 'Rg ' .. word
    else
        echo 'No word under the cursor.'
    endif
endfunction
nnoremap <silent> <leader>g :call <SID>RgWordUnderCursor()<CR>

" --- tmux integration: C-h/j/k/l across vim splits AND tmux panes ---
let g:tmux_navigator_no_mappings = 1
nnoremap <silent> <C-h>  :<C-U>TmuxNavigateLeft<CR>
nnoremap <silent> <C-j>  :<C-U>TmuxNavigateDown<CR>
nnoremap <silent> <C-k>  :<C-U>TmuxNavigateUp<CR>
nnoremap <silent> <C-l>  :<C-U>TmuxNavigateRight<CR>
nnoremap <silent> <C-\>  :<C-U>TmuxNavigatePrevious<CR>

" --- Filetype indentation/folding ---
augroup filetype_settings
    autocmd!
    autocmd FileType javascript,javascriptreact,typescript,typescriptreact
        \ setlocal tabstop=2 shiftwidth=2 expandtab foldmethod=syntax foldlevel=99
    autocmd FileType json setlocal tabstop=2 shiftwidth=2 expandtab foldmethod=syntax
    autocmd FileType css setlocal tabstop=2 shiftwidth=2 expandtab
    autocmd FileType html setlocal tabstop=4 shiftwidth=4 expandtab
    autocmd FileType python setlocal tabstop=4 shiftwidth=4 softtabstop=4
        \ textwidth=79 expandtab autoindent fileformat=unix
        \ foldmethod=indent foldlevel=99
augroup END

augroup python_whitespace
    autocmd!
    autocmd FileType python highlight BadWhitespace ctermbg=red guibg=red
    autocmd FileType python match BadWhitespace /\s\+$/
augroup END
VIMRC
```

Install the plugins headlessly:

```bash
~/.local/bin/vim -es -u ~/.vimrc -c 'PlugInstall --sync' -c 'qa!' < /dev/null
ls ~/.vim/plugged/    # expect: lsp, fzf, fzf.vim, vim-tmux-navigator
```

## Step 7 — the tmux config

```bash
cat > ~/.tmux.conf <<'TMUXCONF'
# macOS ships an old ncurses terminfo db without tmux-256color
set -g default-terminal "screen-256color"
set -ga terminal-overrides ",xterm-256color:RGB"

set -g mouse on
set -g history-limit 50000
set -sg escape-time 0          # no Esc delay in vim
set -g focus-events on
set -g base-index 1
setw -g pane-base-index 1
setw -g mode-keys vi

bind | split-window -h -c "#{pane_current_path}"
bind - split-window -v -c "#{pane_current_path}"
bind c new-window -c "#{pane_current_path}"

bind -T copy-mode-vi v send -X begin-selection
bind -T copy-mode-vi y send -X copy-pipe-and-cancel "pbcopy"

# Seamless vim <-> tmux pane navigation (christoomey/vim-tmux-navigator).
# NOTE: literal alternation instead of the upstream nested-optional regex —
# macOS grep mishandles ')?g?(' adjacency and never matches plain 'vim'.
is_vim="ps -o state= -o comm= -t '#{pane_tty}' \
    | grep -iqE '^[^TXZ ]+ +([^ ]+/)?(vim|view|vimdiff|gvim|nvim|fzf)$'"
bind -n C-h if-shell "$is_vim" "send-keys C-h" "select-pane -L"
bind -n C-j if-shell "$is_vim" "send-keys C-j" "select-pane -D"
bind -n C-k if-shell "$is_vim" "send-keys C-k" "select-pane -U"
bind -n C-l if-shell "$is_vim" "send-keys C-l" "select-pane -R"
bind -n 'C-\' if-shell "$is_vim" "send-keys 'C-\\'" "select-pane -l"

bind -r H resize-pane -L 5
bind -r J resize-pane -D 5
bind -r K resize-pane -U 5
bind -r L resize-pane -R 5

set -g status-style "bg=colour235,fg=colour248"
set -g status-left "#[bold]#S "
set -g status-right "%H:%M %d-%b"
setw -g window-status-current-style "bg=colour239,fg=colour255,bold"
TMUXCONF
```

> **Gotcha:** the widely-copied upstream `is_vim` pattern
> (`...(\S+\/)?g?(view|l?n?vim?x?|fzf)(diff)?$`) **silently never matches**
> on macOS: BSD grep's regex engine mishandles the `)?g?(` adjacent-optionals
> sequence (and `\S` isn't portable ERE). The result is that `C-h/j/k/l` work
> in vim but won't hop from a shell pane back into vim. The literal
> alternation above behaves identically and actually works.

> **Gotcha:** you cannot test these bindings with `tmux send-keys` — that
> injects keys directly into the pane, *bypassing* the client key table.
> Test from a real attached client, or invoke the `if-shell` logic manually.

> **Gotcha:** if tmux was already running when you wrote the config, the
> server won't have read it. `tmux source-file ~/.tmux.conf` or
> `tmux kill-server` and start fresh.

## Step 8 — per-project Python setup

pyright resolves imports per project. In each Python repo, add a
`pyrightconfig.json` at the root pointing at the venv and source layout, e.g.:

```json
{
    "venvPath": ".",
    "venv": ".venv",
    "extraPaths": ["harness/src"],
    "exclude": [".venv", "**/__pycache__"]
}
```

## Step 9 — verify end to end

```bash
tmux new -s dev
```

Inside, open any Python file from a project with a venv, and any `.tsx` file
from a project with `node_modules` + `tsconfig.json`, and check:

1. Resting the cursor on a variable pops its type (e.g.
   `(variable) findings: LintFindings` / `const visible: WikiPage[]`).
2. `gd` on a cross-file call jumps to the definition; `C-o` jumps back.
3. `gr` opens a location list of references across the project.
4. A deliberate type error shows an `E>` sign within a second or two;
   `]d` jumps to it.
5. `C-h` / `C-l` move between vim splits and tmux panes with the same keys.
6. `,h` toggles the auto-hover if it feels chatty; `K` is always manual hover.

For TS the language server needs the project's `typescript` and `@types/*`
packages: `npm install` in the project first, and check `npx tsc --noEmit`
passes so you know the project itself is sane before judging the LSP.

## Issue summary (what bit us, in one table)

| Symptom | Cause | Fix |
|---|---|---|
| npm/uv: `SELF_SIGNED_CERT_IN_CHAIN` / `UnknownIssuer` | Corporate TLS interception (Netskope) | Step 0: CA bundle + `NODE_EXTRA_CA_CERTS` + `UV_NATIVE_TLS` |
| npm `E403` on one specific tarball | Proxy blocks unscanned new releases | Install a slightly older version |
| vim builds but `-python3` | Link test fails: dylib not in python's config dir | `LDFLAGS=-L$P/lib` + `vi_cv_dll_name_python3=...` at configure |
| tmux configure aborts re: utf8proc | tmux ≥3.6 requires explicit choice on macOS | `--disable-utf8proc` |
| `C-h` won't leave a shell pane into vim | macOS grep bug vs upstream `is_vim` regex | Literal-alternation pattern (Step 7) |
| GitHub API 403 when scripting downloads | Unauthenticated rate limit | Direct release URLs |
| tmux config seems ignored | Server predates config file | `tmux source-file` or `kill-server` |
