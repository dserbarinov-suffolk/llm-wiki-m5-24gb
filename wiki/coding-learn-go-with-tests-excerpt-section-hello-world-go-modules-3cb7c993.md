---
page_id: coding-learn-go-with-tests-excerpt-section-hello-world-go-modules-3cb7c993
page_kind: source
summary: Hello, World / Go modules?: 15 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-hello-world-go-modules-3cb7c993@fa82a3a07981c2a9c2fe0bac4ae83693
---

# Hello, World / Go modules?

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-hello-world-72ad81c1]] - broader source section: Hello, World
- [[coding-learn-go-with-tests-excerpt-section-hello-world-how-to-test-b6606620]] - previous source section: Hello, World / How to test
- [[coding-learn-go-with-tests-excerpt-section-hello-world-back-to-testing-7ab34920]] - next source section: Hello, World / Back to Testing

## Statements

- The next step is to run the tests. Enter go test in your terminal. If the tests pass, then you are probably using an earlier version of Go. However, if you are using Go 1.16 or later, the tests will likely not run. Instead, you will see an error message like this in the terminal: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00025))_
- What's the problem? In a word, modules. Luckily, the problem is easy to fix. Enter go mod init example.com/hello in your terminal. That will create a new file with the following contents: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00027))_
- This file tells the go tools essential information about your code. If you planned to distribute your application, you would include where the code was available for download as well as information about dependencies. The name of the module, example.com/hello, usually refers to a URL where the module can be found and downloaded. For compatibility with tools we'll start using soon, make sure your module's name has a dot somewhere in it, like the dot in .com of example.com/hello. For now, your module file is minimal, and you can leave it that way. To read more about modules, you can check out the reference in the Golang documentation. We can get back to testing and learning Go now since the tests should run, even on Go 1.16. In future chapters, you will need to run go mod init SOMENAME in each _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_
- If the tests pass, then you are probably using an earlier version of Go. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00025))_
- The name of the module, example.com/hello, usually refers to a URL where the module can be found and downloaded. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_
- new folder before running commands like go test or go build . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00030))_

## Technical atoms

### Technical frame 1: Hello, World / Go modules?

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_

> This file tells the go tools essential information about your code. If you planned to distribute your application, you would include where the code was available for download as well as information about dependencies. The name of the module, example.com/hello, usually refers to a URL where the module can be found and downloaded. For compatibility with tools we'll start using soon, make sure your module's name has a dot somewhere in it, like the dot in .com of example.com/hello. For now, your mod

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00028))_

```
module example.com/hello
go 1.16
```

### Technical frame 2: Hello, World / Go modules?

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00027))_

> What's the problem? In a word, modules. Luckily, the problem is easy to fix. Enter go mod init example.com/hello in your terminal. That will create a new file with the following contents:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00029))_

> To read more about modules, you can check out the reference in the Golang documentation.
