---
page_id: javascriptallonge-destructuring-is-not-pattern-matching
page_kind: concept
summary: topic-concept: 13 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_98c47d64fd9b3b12@ca3ab4d8d0af91b61327112679954ca4
---

# destructuring is not pattern matching

Source: [[javascriptallonge]]

## Statements

- If it does , assignments are made where appropriate. (javascriptallonge.pdf p.105)
- That match would fail because the array doesn't have an element to assign to what . (javascriptallonge.pdf p.106)
- But this is not how JavaScript works. (javascriptallonge.pdf p.106)
- JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. (javascriptallonge.pdf p.106)
- From its very inception, JavaScript has striven to avoid catastrophic errors. (javascriptallonge.pdf p.106)
- As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. (javascriptallonge.pdf p.106)
- This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. (javascriptallonge.pdf p.106)

## Rules

- As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. (javascriptallonge.pdf p.106)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const [what] = [];
```

<a id="atom-2"></a>
**Atom:** code block

```
const [what] = [];
what
//=> undefined
const [which, what,
who
//=> undefined
```

<a id="atom-3"></a>
**Atom:** code block

```
const [...they] = [];
they
//=> []
const [which, what, .
they
//=> []
```


## Related pages

- [[javascriptallonge-gathering]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-destructuring-parameters]] - contextualizes: source-supported topic dependency
