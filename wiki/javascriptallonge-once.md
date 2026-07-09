---
page_id: javascriptallonge-once
page_kind: concept
summary: topic-concept: 9 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_d960f31821fe8164@d92e820b72f03a7e5811307992ce9cc8
---

# Once

Source: [[javascriptallonge]]

## Statements

- once is an extremely helpful combinator. (javascriptallonge.pdf p.88)
- It ensures that a function can only be called, well, once . (javascriptallonge.pdf p.88)
- That function will call your function once, and thereafter will return undefined whenever it is called. (javascriptallonge.pdf p.88)
- (Note: There are some subtleties with decorators like once that involve the intersection of state with methods. (javascriptallonge.pdf p.88)

## Rules

- It ensures that a function can only be called, well, once . (javascriptallonge.pdf p.88)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const once = (fn) => {
let done = false;
return function () {
return done ? void 0 : ((done = true), fn.apply(this, arguments))
}
}
```

<a id="atom-2"></a>
**Atom:** code block

```
const askedOnBlindDate = once(
() => "sure, why not?"
);
askedOnBlindDate()
//=> 'sure, why not?'
askedOnBlindDate()
//=> undefined
askedOnBlindDate()
//=> undefined
```


## Related pages

- [[javascriptallonge-maybe]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-left-variadic-functions]] - contextualizes: source-supported topic dependency
