---
page_id: javascriptallonge-once
page_kind: concept
summary: Once: 4 accepted assertion(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_02ffebf67d509caa@5f20481e83b3f24f6b3358e92fb0562b
---

# Once

Source: [[javascriptallonge]]

## Statements

- once is an extremely helpful combinator. (javascriptallonge.pdf p.88)
- It ensures that a function can only be called, well, once . (javascriptallonge.pdf p.88)
- That function will call your function once, and thereafter will return undefined whenever it is called. (javascriptallonge.pdf p.88)
- (Note: There are some subtleties with decorators like once that involve the intersection of state with methods. (javascriptallonge.pdf p.88)

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
