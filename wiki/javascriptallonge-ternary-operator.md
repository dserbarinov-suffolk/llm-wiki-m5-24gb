---
page_id: javascriptallonge-ternary-operator
page_kind: concept
summary: Ternary Operator: 1 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-ternary-operator@2a2f281950e2d7c1bfcddc810a211788
---

# Ternary Operator

What [[javascriptallonge]] covers about ternary operator:

## Statements

### Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

- JavaScript inherited an operator from the C family of languages, the ternary operator. It's the only operator that takes three arguments. It looks like this: first ? second : third . It evaluates first , and if first is 'truthy', it evaluates second and that is its value. If first is not truthy, it evaluates third and that is its value. _(javascriptallonge.pdf (source-range-c98ab3e6-00750))_


## Technical atoms

### Technical frame 1: Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00756))_

> Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00754))_

<a id="atom-technical-atom-f9b7fc7f4a1c8300"></a>
```
true ? 'Hello' : 'Good bye'
//=> 'Hello'
0 ? 'Hello' : 'Good bye'
//=> 'Good bye'
[1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal'
//=> 'Pentatonic'
```


## Related pages

### Source structure

- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-the-ternary-operator-b715a907]] - source section: Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

### Shared technical atoms

- [[javascriptallonge-truthiness]] - shared technical atoms: Truthiness shares technical record from Picking the Bean: Choice and Truthiness / truthiness and the ternary operator: true ? 'Hello' : 'Good bye' //=> 'Hello' 0 ? 'Hello' : 'Good bye' //=> 'Good bye' [1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal' //=> 'Pentatonic' (1 shared atom(s))

### Shared claims

- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from Picking the Bean: Choice and Truthiness / truthiness and the ternary operator: JavaScript inherited an operator from the C family of languages, the ternary operator. It's the only operator that takes three arguments. It looks like this: first ? ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
