---
page_id: coding-little-go-book-section-getting-started-c2e397c0
page_kind: source
summary: Getting Started: 10 source-backed entries and 2 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-getting-started-c2e397c0@4ae5beabcef7f01605713b459ea2387b
---

# Getting Started

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-getting-started-osx-linux-a98a170a]] - narrower source section: Getting Started / OSX / Linux
- [[coding-little-go-book-section-getting-started-windows-20ce4fc9]] - narrower source section: Getting Started / Windows
- [[coding-little-go-book-section-introduction-9630c91e]] - previous source section: Introduction
- [[coding-little-go-book-section-chapter-1-the-basics-45e21143]] - next source section: Chapter 1 - The Basics

## Statements by subsection

### Getting Started / OSX / Linux

- Download the tar.gz for your platform. For OSX, you'll most likely be interested in go#.#.#.darwin-amd64-osx10.8.tar.gz , where #.#.# is the latest version of Go. Extract the file to /usr/local via tar -C /usr/local -xzf go#.#.#.darwin-amd64-osx10.8.tar.gz . Set up two environment variables: 1. GOPATH points to your workspace, for me, that's $HOME/code/go . 2. We need to append Go's binary to our PATH . You can set these up from a shell: _(coding_little_go_book.pdf (source-range-23d24eb1-00026))_
- echo 'export GOPATH=$HOME/code/go' >> $HOME/.profile echo 'export PATH=$PATH:/usr/local/go/bin' >> $HOME/.profile You'll want to activate these variables. You can close and reopen your shell, or you can run source $HOME/.profile . Type and you'll hopefully get an output that looks like go _(coding_little_go_book.pdf (source-range-23d24eb1-00027))_

### Getting Started / Windows

- Download the latest zip file. If you're on an x64 system, you'll want go#.#.#.windows-amd64.zip , where #.#.# is the latest version of Go. Unzip it at a location of your choosing. c:\Go is a good choice. Set up two environment variables: 1. GOPATH points to your workspace. That might be something like c:\users\goku\work\go . 2. Add c:\Go\bin to your PATH environment variable. Environment variables can be set through the Environment Variables button on the Advanced tab of the System control panel. Some versions of Windows provide this control panel through the Advanced System Settings option inside the System control panel. Open a command prompt and type go version . You'll hopefully get an output that looks like go version go1.3.3 windows/amd64 . _(coding_little_go_book.pdf (source-range-23d24eb1-00030))_
- Some versions of Windows provide this control panel through the Advanced System Settings option inside the System control panel. _(coding_little_go_book.pdf (source-range-23d24eb1-00030))_

## Technical atoms

### Technical frame 1: Getting Started

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00023))_

> If you're looking to play a little with Go, you should check out the Go Playground which lets you run code online without having to install anything. This is also the most common way to share Go code when seeking help in Go's discussion forum and places like StackOverflow. Installing Go is straightforward. You can install it from source, but I suggest you use one of the pre-compiled binaries. When you go to the download page, you'll see installers for various platforms. Let's avoid these and learn how to set up Go ourselves. As you'll see, it isn't hard. Except for simple examples, Go is designed to work when your code is inside a workspace. The workspace is a folder composed of bin , pkg and src subfolders. You might be tempted to force Go to follow your own style - don't. Normally, I put my projects inside of ~/code . For example, ~/code/blog contains my blog. For Go, my workspace is ~/code/go and my Gopowered blog would be in ~/code/go/src/blog . In short, create a go folder with a src subfolder wherever you expect

### Technical frame 2: Getting Started

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00023))_

> If you're looking to play a little with Go, you should check out the Go Playground which lets you run code online without having to install anything.
