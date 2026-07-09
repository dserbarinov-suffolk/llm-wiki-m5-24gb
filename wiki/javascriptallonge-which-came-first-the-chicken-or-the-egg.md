---
page_id: javascriptallonge-which-came-first-the-chicken-or-the-egg
page_kind: concept
summary: topic-concept: 6 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_a2820eaabb6d05db@940032b74a382050eb686875fc8f8322
---

# which came first, the chicken or the egg?

Source: [[javascriptallonge]]

## Statements

- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. (javascriptallonge.pdf p.47)
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. (javascriptallonge.pdf p.48)

## Rules

- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. (javascriptallonge.pdf p.47)

## Technical atoms

<a id="atom-1"></a>
**Atom:** rule

```
If you don't want your code to operate directly within the global environment, what can you do?
```

<a id="atom-2"></a>
**Atom:** code block

```
// top of the file
(() => {
// ... lots of JavaScript ...
})();
// bottom of the file
```


## Related pages

- [[javascriptallonge-shadowy-variables-from-a-shadowy-planet]] - contextualizes: source-supported topic dependency
