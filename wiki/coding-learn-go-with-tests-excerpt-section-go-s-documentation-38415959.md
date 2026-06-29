---
page_id: coding-learn-go-with-tests-excerpt-section-go-s-documentation-38415959
page_kind: source
summary: Go's documentation: 10 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-go-s-documentation-38415959@ba8b58ed762a07c5541264cccc462b4a
---

# Go's documentation

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-hello-world-72ad81c1]] - previous source section: Hello, World
- [[coding-learn-go-with-tests-excerpt-section-hello-you-ec883754]] - next source section: Hello, YOU
- [[coding-learn-go-with-tests-excerpt-documentation]] - topic hub: opens the topic page for Documentation

## Statements

- Another quality-of-life feature of Go is the documentation. We just saw the documentation for the fmt package at the official package viewing website, and Go also provides ways for quickly getting at the documentation offline. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00037))_
- Go has a built-in tool, doc, which lets you examine any package installed on your system, or the module you're currently working on. To view that same documentation for the Printing verbs: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00038))_
- Go's second tool for viewing documentation is the pkgsite command, which powers Go's official package viewing website. You can install pkgsite with go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run it with pkgsite -open . . Go's install command will download the source files from that repository and build them into an executable binary. For a default installation of Go, that executable will be in $HOME/go/bin for Linux and macOS, and %USERPROFILE%\go\bin for Windows. If you have not already added those paths to your $PATH var, you might want to do so to make running go-installed commands easier. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00040))_
- The vast majority of the standard library has excellent documentation with examples. Navigating to http://localhost:8080/testing would be worthwhile to see what's available to you. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00041))_
- You can install pkgsite with go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run it with pkgsite -open . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00040))_

## Technical atoms

### Technical frame 1: Go's documentation

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00040))_

> Go's second tool for viewing documentation is the pkgsite command, which powers Go's official package viewing website. You can install pkgsite with go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run it with pkgsite -open . . Go's install command will download the source files from that repository and build them into an executable binary. For a default installation of Go, that executable will be in $HOME/go/bin for Linux and macOS, and %USERPROFILE%\go\bin for Windows. If you have not 

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00039))_

```
$ go doc fmt
package fmt // import "fmt"
Package fmt implements formatted I/O with functions analogous to C's 
printf and
scanf. The format 'verbs' are derived from C's but are simpler.
# Printing
The verbs:
General:
%v  the value in a default format
       when printing structs, the plus flag (%+v) adds field names
   %#v a Go-syntax representation of the value
   %T  a Go-syntax representation of the type of the value
   %%  a literal percent sign; consumes no value
...
```
