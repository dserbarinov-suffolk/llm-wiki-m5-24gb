---
page_id: javascriptallonge-destructuring-parameters
page_kind: concept
summary: topic-concept: 7 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_10bc0502113d3d0b@136e5686e0241e74f704818f3529d0f1
---

# destructuring parameters

Source: [[javascriptallonge]]

## Statements

- There is only one difference: We have not tried gathering. (javascriptallonge.pdf p.107)
- This is very useful indeed, and we'll see more of it in a moment. (javascriptallonge.pdf p.108)
- 59 Gathering in parameters has a long history, and the usual terms are to call gathering 'pattern matching' and to call a name that is bound to gathered values a 'rest parameter.' The term 'rest' is perfectly compatible with gather: 'Rest' is the noun, and 'gather' is the verb. (javascriptallonge.pdf p.108)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
foo()
bar("smaug")
baz(1, 2, 3)
```

<a id="atom-2"></a>
**Atom:** code block

```
const foo = () => ...
const bar = (name) => ...
const baz = (a, b, c) => ...
```

<a id="atom-3"></a>
**Atom:** code block

```
const numbers = (...nums) => nums;
numbers(1, 2, 3, 4, 5)
//=> [1,2,3,4,5]
const headAndTail = (head, ...tail) => [head, tail];
headAndTail(1, 2, 3, 4, 5)
//=> [1,[2,3,4,5]]
```


## Related pages

- [[javascriptallonge-destructuring-is-not-pattern-matching]] - contextualizes: source-supported topic dependency
