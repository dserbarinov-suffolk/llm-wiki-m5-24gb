---
page_id: javascriptallonge-truthiness-and-operators
page_kind: concept
summary: truthiness and operators: 11 accepted assertion(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_e7ed86092161f3fb@6f7eca3eef2790d9e7e68e9998dfda1b
---

# truthiness and operators

Source: [[javascriptallonge]]

## Statements

- , && , and || are a little more subtle than our examples above implied. (javascriptallonge.pdf p.96)
- It always returns false if its argument is truthy, and true is its argument is not truthy:. (javascriptallonge.pdf p.96)
- Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. (javascriptallonge.pdf p.96-97)
- So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user. (javascriptallonge.pdf p.96-97)
- , && and || do not necessarily evaluate to true or false . (javascriptallonge.pdf p.97)
- If we look at our examples above, we see that when we pass true and false to && and || , we do indeed get true or false as a result. (javascriptallonge.pdf p.97)
- They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && . (javascriptallonge.pdf p.97)
- This is not a subtle distinction. (javascriptallonge.pdf p.97)
- We've seen the ternary operator: It is a control-flow operator, not a logical operator. (javascriptallonge.pdf p.97)
- The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. (javascriptallonge.pdf p.98)
- This is more than just an optimization. (javascriptallonge.pdf p.98)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
!5
//=> false
!undefined
//=> true
```

<a id="atom-2"></a>
**Atom:** rule

```
But when we pass other values, we no longer get true or false :
```

<a id="atom-3"></a>
**Atom:** code block

```
1 || 2
//=> 1
null && undefined
//=> null
undefined && null
//=> undefined
```

<a id="atom-4"></a>
**Atom:** code block

```
const even = (n) =>
n === 0 || (n !== 1 && even(n - 2))
even(42)
//=> true
```
