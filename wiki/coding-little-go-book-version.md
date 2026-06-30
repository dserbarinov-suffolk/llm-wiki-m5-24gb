---
page_id: coding-little-go-book-version
page_kind: concept
summary: Version: 3 statement(s) and 1 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-version@405323ff63d36b857c1170a5af4b19e0
---

# Version

What [[coding-little-go-book]] covers about version:

## Statements

### Getting Started / Windows

- Download the latest zip file. If you're on an x64 system, you'll want go#.#.#.windows-amd64.zip , where #.#.# is the latest version of Go. Unzip it at a location of your choosing. c:\Go is a good choice. Set up two environment variables: 1. GOPATH points to your workspace. That might be something like c:\users\goku\work\go . 2. Add c:\Go\bin to your PATH environment variable. Environment variables can be set through the Environment Variables button on the Advanced tab of the System control panel. Some versions of Windows provide this control panel through the Advanced System Settings option inside the System control panel. Open a command prompt and type go version . You'll hopefully get an output that looks like go version go1.3.3 windows/amd64 . _(coding_little_go_book.pdf (source-range-23d24eb1-00030))_

### Chapter 3 - Maps, Arrays and Slices / Slices

- The third version is a nil slice and is used in conjunction with append , when the number of elements is unknown. _(coding_little_go_book.pdf (source-range-23d24eb1-00226))_

- The last version lets us specify an initial capacity; useful if we have a general idea of how many elements we'll need. _(coding_little_go_book.pdf (source-range-23d24eb1-00227))_


## Technical atoms

### Technical frame 1: Chapter 3 - Maps, Arrays and Slices / Slices

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00230))_

> Slices as wrappers to arrays is a powerful concept. Many languages have the concept of slicing an array. Both JavaScript and Ruby arrays have a slice method. You can also get a slice in Ruby by using [START..END] or in Python via [START:END] . However, in these languages, a slice is actually a new array with the values of the original copied over. If we take Ruby, what's the output of the following?

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00228))_

> Even when you know the size, append can be used.


## Related pages

- [[coding-little-go-book-slice]] - shared statements and technical atoms: Slice shares source evidence from Chapter 3 - Maps, Arrays and Slices / Slices: The third version is a nil slice and is used in conjunction with append , when the number of elements is unknown.; Slice shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: Even when you know the size, append can be used. (1 shared statement(s), 1 shared atom(s))
- [[coding-little-go-book-array]] - shared technical atoms: Array shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: Even when you know the size, append can be used. (1 shared atom(s))
- [[coding-little-go-book-language]] - shared technical atoms: Language shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: Even when you know the size, append can be used. (1 shared atom(s))
- [[coding-little-go-book-ruby]] - shared technical atoms: Ruby shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: Even when you know the size, append can be used. (1 shared atom(s))
- [[coding-little-go-book-value]] - shared technical atoms: Value shares technical record from Chapter 3 - Maps, Arrays and Slices / Slices: Even when you know the size, append can be used. (1 shared atom(s))

## Source

- [[coding-little-go-book]]
