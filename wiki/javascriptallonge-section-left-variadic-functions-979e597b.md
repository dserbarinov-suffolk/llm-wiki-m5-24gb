---
page_id: javascriptallonge-section-left-variadic-functions-979e597b
page_kind: source
summary: Left-Variadic Functions: 10 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-left-variadic-functions-979e597b@caf8f582e8b28b41d3414217d6cda8a0
---

# Left-Variadic Functions

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-once-70058fab]] - previous source section: Once
- [[javascriptallonge-section-a-history-lesson-bd8ecbcc]] - next source section: a history lesson

## Statements

- A variadic function is a function that is designed to accept a variable number of arguments. 52 In JavaScript, you can make a variadic function by gathering parameters. For example: _(javascriptallonge.pdf (source-range-c98ab3e6-00700))_
- This can be useful when writing certain kinds of destructuring algorithms. For example, we might want to have a function that builds some kind of team record. It accepts a coach, a captain, and an arbitrary number of players. Easy in ECMAScript 2015: _(javascriptallonge.pdf (source-range-c98ab3e6-00702))_
- 52 English is about as inconsistent as JavaScript: Functions with a fixed number of arguments can be unary, binary, ternary, and so forth. But can they be 'variary?' No! They have to be 'variadic.' _(javascriptallonge.pdf (source-range-c98ab3e6-00704))_
- ECMAScript 2015 only permits gathering parameters from the end of the parameter list. Not the beginning. What to do? _(javascriptallonge.pdf (source-range-c98ab3e6-00706))_
- For example, we might want to have a function that builds some kind of team record. _(javascriptallonge.pdf (source-range-c98ab3e6-00702))_
- ECMAScript 2015 only permits gathering parameters from the end of the parameter list. _(javascriptallonge.pdf (source-range-c98ab3e6-00706))_

## Technical atoms

### Technical frame 1: Left-Variadic Functions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00702))_

> This can be useful when writing certain kinds of destructuring algorithms. For example, we might want to have a function that builds some kind of team record. It accepts a coach, a captain, and an arbitrary number of players. Easy in ECMAScript 2015:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00701))_

<a id="atom-technical-atom-f8f8ac50da4371b1"></a>
```
const abccc = (a, b, ...c) => {
console.log(a);
console.log(b);
console.log(c);
};
abccc(1, 2, 3, 4, 5)
1
2
[3,4,5]
```
