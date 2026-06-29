---
page_id: coding-learn-go-with-tests-excerpt-module
page_kind: concept
summary: Go modules?: 9 statement(s) and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-module@dc99de7d5a895e714533c34d7a1f0d7c
---

# Go modules?

What [[coding-learn-go-with-tests-excerpt]] covers about go modules?:

## Statements

### Hello, World / Go modules?

- The next step is to run the tests. Enter go test in your terminal. If the tests pass, then you are probably using an earlier version of Go. However, if you are using Go 1.16 or later, the tests will likely not run. Instead, you will see an error message like this in the terminal: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00025))_

- What's the problem? In a word, modules. Luckily, the problem is easy to fix. Enter go mod init example.com/hello in your terminal. That will create a new file with the following contents: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00027))_

- This file tells the go tools essential information about your code. If you planned to distribute your application, you would include where the code was available for download as well as information about dependencies. The name of the module, example.com/hello, usually refers to a URL where the module can be found and downloaded. For compatibility with tools we'll start using soon, make sure your module's name has a dot somewhere in it, like the dot in .com of example.com/hello. For now, your module file is minimal, and you can leave it that way. To read more about modules, you can check out the reference in the Golang documentation. We can get back to testing and learning Go now since the tests should run, even on Go 1.16. In future chapters, you will need to run go mod init SOMENAME in each _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_


## Technical atoms

### Technical frame 1: Hello, World / Go modules?

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00027))_

> What's the problem? In a word, modules. Luckily, the problem is easy to fix. Enter go mod init example.com/hello in your terminal. That will create a new file with the following contents:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00026))_

```
$ go test
go: cannot find main module; see 'go help modules'
```

### Technical frame 2: Hello, World / Go modules?

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_

> This file tells the go tools essential information about your code. If you planned to distribute your application, you would include where the code was available for download as well as information about dependencies. The name of the module, example.com/hello, usually refers to a URL where the module can be found and downloaded. For compatibility with tools we'll start using soon, make sure your module's name has a dot somewhere in it, like the dot in .com of example.com/hello. For now, your mod

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00028))_

```
module example.com/hello
go 1.16
```

### Technical frame 3: Hello, World / Go modules?

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00027))_

> What's the problem? In a word, modules. Luckily, the problem is easy to fix. Enter go mod init example.com/hello in your terminal. That will create a new file with the following contents:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_

> To read more about modules, you can check out the reference in the Golang documentation.


## Related pages

- [[coding-learn-go-with-tests-excerpt-hello]] - shared statements and technical atoms: Hello, World shares source evidence from Hello, World / Go modules?: The next step is to run the tests. Enter go test in your terminal. If the tests pass, then you are probably using an earlier version of Go. However, if you are using ... [truncated]; Hello, World shares technical record from Hello, World / Go modules?: $ go test go: cannot find main module; see 'go help modules' (9 shared statement(s), 3 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-test]] - shared statements and technical atoms: Test shares source evidence from Hello, World / Go modules?: The next step is to run the tests. Enter go test in your terminal. If the tests pass, then you are probably using an earlier version of Go. However, if you are using ... [truncated]; Test shares technical record from Hello, World / Go modules?: $ go test go: cannot find main module; see 'go help modules' (1 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-section-hello-world-go-modules-3cb7c993]] - source section: Hello, World / Go modules? shares source evidence from Hello, World / Go modules?: The next step is to run the tests. Enter go test in your terminal. If the tests pass, then you are probably using an earlier version of Go. However, if you are using ... [truncated]; Hello, World / Go modules? shares technical record from Hello, World / Go modules?: $ go test go: cannot find main module; see 'go help modules' (9 shared statement(s), 3 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
