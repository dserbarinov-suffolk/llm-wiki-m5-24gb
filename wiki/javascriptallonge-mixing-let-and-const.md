---
page_id: javascriptallonge-mixing-let-and-const
page_kind: concept
summary: topic-concept: 7 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_13d86437f23edf7d@f6b0c25e55ac3a5329bda5cb6e66a826
---

# mixing let and const

Source: [[javascriptallonge]]

## Statements

- The suggestion is that shadowing a variable is confusing code. (javascriptallonge.pdf p.150)
- Shadowing a let with a const does not change our ability to rebind the variable in its original scope. (javascriptallonge.pdf p.150)
- Shadowing a const with a let does not permit it to be rebound in its original scope. (javascriptallonge.pdf p.151)

## Technical atoms

<a id="atom-1"></a>
**Atom:** rule

```
If you dislike deliberately shadowing variables, you'll probably take an even more opprobrious view of mixing const and let semantics with a shadowed variable:
```

<a id="atom-2"></a>
**Atom:** code block

```
(() => {
let age = 49;
if (true) {
const age = 50;
}
age = 51;
return age;
})()
//=> 51
```

<a id="atom-3"></a>
**Atom:** code block

```
(() => {
const age = 49;
if (true) {
let age = 50;
}
age = 52;
return age;
})()
//=> ERROR: age is read-only
```


## Related pages

- [[javascriptallonge-why-const-and-let-were-invented]] - contextualizes: source-supported topic dependency
