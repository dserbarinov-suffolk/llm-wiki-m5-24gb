---
page_id: coding-learn-go-with-tests-excerpt-module
page_kind: concept
summary: Go modules?: 9 statement(s) and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-module@f1c9255679c1daa6284a542f64e35154
---

# Go modules?

What [[coding-learn-go-with-tests-excerpt]] covers about go modules?:

## Statements

- However, if you are using Go 1.16 or later, the tests will likely not run. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00025))_
- The next step is to run the tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00025))_
- If the tests pass, then you are probably using an earlier version of Go. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00025))_
- Luckily, the problem is easy to fix. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00027))_
- For now, your module file is minimal, and you can leave it that way. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00029))_
- The name of the module, example.com/hello, usually refers to a URL where the module can be found and downloaded. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00029))_
- For compatibility with tools we'll start using soon, make sure your module's name has a dot somewhere in it, like the dot in .com of example.com/hello. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00029))_
- We can get back to testing and learning Go now since the tests should run, even on Go 1.16. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00029))_
- In future chapters, you will need to run go mod init SOMENAME in each _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00029))_

## Technical atoms

> Context: What's the problem? In a word, modules. Luckily, the problem is easy to fix. Enter go mod init example.com/hello in your terminal. That will create a new file with the following contents:
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00027))_

```
module	example.com/hello go	1.16
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00028))_

> Context: What's the problem? In a word, modules. Luckily, the problem is easy to fix. Enter go mod init example.com/hello in your terminal. That will create a new file with the following contents:
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00027))_

> To read more about modules, you can check out the reference in the Golang documentation.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00029))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
