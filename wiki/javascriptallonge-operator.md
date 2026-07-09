---
page_id: javascriptallonge-operator
page_kind: concept
summary: Operator: 1 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-operator@ddca7b6dc4dbd7680484fcb67f7ba04f
---

# Operator

What [[javascriptallonge]] covers about operator:

## Statements

### Picking the Bean: Choice and Truthiness / truthiness and operators

- We've seen the ternary operator: It is a control-flow operator, not a logical operator. The same is true of && and || . Consider this tail-recursive function that determines whether a positive integer is even: _(javascriptallonge.pdf (source-range-c98ab3e6-00774))_


## Technical atoms

### Technical frame 1: Picking the Bean: Choice and Truthiness / truthiness and operators

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

### Source structure

- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-operators-44549e80]] - source section: Picking the Bean: Choice and Truthiness / truthiness and operators
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-the-ternary-operator-b715a907]] - source section: Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

### Shared technical atoms

- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-truthiness]] - shared technical atoms: Truthiness shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))

## Source

- [[javascriptallonge]]
