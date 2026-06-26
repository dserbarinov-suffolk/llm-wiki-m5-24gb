---
page_id: coding-learn-go-with-tests-excerpt-section-go-modules-7321aa8b
page_kind: source
summary: Go modules?: 15 source-backed entries and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-go-modules-7321aa8b@136a17a7062d7a77fe8b645c0aa2df1b
---

# Go modules?

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- However, if you are using Go 1.16 or later, the tests will likely not run. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00025))_
- If the tests pass, then you are probably using an earlier version of Go. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00025))_
- The next step is to run the tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00025))_
- If the tests pass, then you are probably using an earlier version of Go. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00025))_
- Luckily, the problem is easy to fix. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00027))_
- In future chapters, you will need to run go mod init SOMENAME in each _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00029))_
- The name of the module, example.com/hello, usually refers to a URL where the module can be found and downloaded. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00029))_
- We can get back to testing and learning Go now since the tests should run, even on Go 1.16. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00029))_
- For now, your module file is minimal, and you can leave it that way. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00029))_
- For compatibility with tools we'll start using soon, make sure your module's name has a dot somewhere in it, like the dot in .com of example.com/hello. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00029))_
- The name of the module, example.com/hello, usually refers to a URL where the module can be found and downloaded. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00029))_
- new folder before running commands like go test or go build . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00030))_

## Technical atoms

```
$ go test
go: cannot find main module; see 'go help modules'
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00026))_

```
module example.com/hello
go 1.16
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00028))_

> To read more about modules, you can check out the reference in the Golang documentation.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00029))_
