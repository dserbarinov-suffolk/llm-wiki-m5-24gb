---
page_id: coding-little-go-book-section-getting-started-osx-linux-a98a170a
page_kind: source
summary: Getting Started / OSX / Linux: 3 source-backed entries and 0 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-getting-started-osx-linux-a98a170a@270c6a105498d8bb3527054c234c24f4
---

# Getting Started / OSX / Linux

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-getting-started-c2e397c0]] - broader source section: Getting Started
- [[coding-little-go-book-section-getting-started-windows-20ce4fc9]] - next source section: Getting Started / Windows

## Statements

- Download the tar.gz for your platform. For OSX, you'll most likely be interested in go#.#.#.darwin-amd64-osx10.8.tar.gz , where #.#.# is the latest version of Go. Extract the file to /usr/local via tar -C /usr/local -xzf go#.#.#.darwin-amd64-osx10.8.tar.gz . Set up two environment variables: 1. GOPATH points to your workspace, for me, that's $HOME/code/go . 2. We need to append Go's binary to our PATH . You can set these up from a shell: _(coding_little_go_book.pdf (source-range-23d24eb1-00026))_
- echo 'export GOPATH=$HOME/code/go' >> $HOME/.profile echo 'export PATH=$PATH:/usr/local/go/bin' >> $HOME/.profile You'll want to activate these variables. You can close and reopen your shell, or you can run source $HOME/.profile . Type and you'll hopefully get an output that looks like go _(coding_little_go_book.pdf (source-range-23d24eb1-00027))_
