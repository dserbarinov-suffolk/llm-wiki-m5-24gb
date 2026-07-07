---
page_id: javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-operators-44549e80
page_kind: source
summary: Picking the Bean: Choice and Truthiness / truthiness and operators: 12 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-operators-44549e80@5581b82a2b957f9c46d11243fc27d823
---

# Picking the Bean: Choice and Truthiness / truthiness and operators

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-the-ternary-operator-b715a907]] - previous source section: Picking the Bean: Choice and Truthiness / truthiness and the ternary operator
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-and-are-control-flow-operators-c8371217]] - next source section: Picking the Bean: Choice and Truthiness / || and && are control-flow operators

### Source structure

- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-d2a76f30]] - broader source section: Picking the Bean: Choice and Truthiness

## Statements

- Our logical operators ! , && , and || are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-c98ab3e6-00758))_
- Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user. _(javascriptallonge.pdf (source-range-c98ab3e6-00760))_
- First, and unlike ! , && and || do not necessarily evaluate to true or false . To be precise: _(javascriptallonge.pdf (source-range-c98ab3e6-00762))_
- If we look at our examples above, we see that when we pass true and false to && and || , we do indeed get true or false as a result. But when we pass other values, we no longer get true or false : _(javascriptallonge.pdf (source-range-c98ab3e6-00769))_
- In JavaScript, && and || aren't boolean logical operators in the logical sense. They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && . _(javascriptallonge.pdf (source-range-c98ab3e6-00771))_
- This is not a subtle distinction. _(javascriptallonge.pdf (source-range-c98ab3e6-00772))_
- So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user. _(javascriptallonge.pdf (source-range-c98ab3e6-00760))_
