---
page_id: javascriptallonge-operator
page_kind: concept
summary: Operator: 0 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-operator@483742d4f3f0c33cefa10986b8c594d8
---

# Operator

What [[javascriptallonge]] covers about operator:

## Statements


## Technical atoms

### Technical frame 1: truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00760))_

> Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00759))_

<a id="atom-technical-atom-cb98425a31f8e87a"></a>
```
!5
//=> false
!undefined
//=> true
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-truthiness]] - shared technical atoms: Truthiness shares technical record from truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))

## Source

- [[javascriptallonge]]
