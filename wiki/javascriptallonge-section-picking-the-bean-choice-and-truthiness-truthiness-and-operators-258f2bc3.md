---
page_id: javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-operators-258f2bc3
page_kind: source
summary: Picking the Bean: Choice and Truthiness / truthiness and operators: 12 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-operators-258f2bc3@a2f5c26376ac97b2fcea885f4fa0e3ad
---

# Picking the Bean: Choice and Truthiness / truthiness and operators

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-the-ternary-operator-e084b4d4]] - previous source section: Picking the Bean: Choice and Truthiness / truthiness and the ternary operator
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-and-are-control-flow-operators-517bcbb3]] - next source section: Picking the Bean: Choice and Truthiness / || and && are control-flow operators

### Source structure

- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-acd18cc3]] - broader source section: Picking the Bean: Choice and Truthiness

## Statements

- Our logical operators ! , && , and || are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-c98ab3e6-00771))_
- Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user. _(javascriptallonge.pdf (source-range-c98ab3e6-00773))_
- First, and unlike ! , && and || do not necessarily evaluate to true or false . To be precise: _(javascriptallonge.pdf (source-range-c98ab3e6-00775))_
- If we look at our examples above, we see that when we pass true and false to && and || , we do indeed get true or false as a result. But when we pass other values, we no longer get true or false : _(javascriptallonge.pdf (source-range-c98ab3e6-00782))_
- In JavaScript, && and || aren't boolean logical operators in the logical sense. They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && . _(javascriptallonge.pdf (source-range-c98ab3e6-00784))_
- This is not a subtle distinction. _(javascriptallonge.pdf (source-range-c98ab3e6-00785))_
- So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user. _(javascriptallonge.pdf (source-range-c98ab3e6-00773))_
