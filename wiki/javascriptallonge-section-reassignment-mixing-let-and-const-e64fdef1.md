---
page_id: javascriptallonge-section-reassignment-mixing-let-and-const-e64fdef1
page_kind: source
summary: Reassignment / mixing let and const: 21 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-reassignment-mixing-let-and-const-e64fdef1@a94b2ac3d3d88150a6fde6354dd99637
---

# Reassignment / mixing let and const

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-reassignment-why-const-and-let-were-invented-5a788884]] - next source section: Reassignment / why const and let were invented

### Source structure

- [[javascriptallonge-section-reassignment-66d414a1]] - broader source section: Reassignment
- [[javascriptallonge-section-reassignment-mixing-let-and-const-var-91a401bc]] - narrower source section: Reassignment / mixing let and const / var

## Statements

- Some programmers dislike deliberately shadowing variables. The suggestion is that shadowing a variable is confusing code. If you buy that argument, the way that shadowing works in JavaScript exists to protect us from accidentally shadowing a variable when we move code around. _(javascriptallonge.pdf (source-range-c98ab3e6-01175))_
- Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And: _(javascriptallonge.pdf (source-range-c98ab3e6-01178))_
- Shadowing a const with a let does not permit it to be rebound in its original scope. _(javascriptallonge.pdf (source-range-c98ab3e6-01180))_

## Statements by subsection

### Reassignment / mixing let and const / var

- JavaScript has one more way to bind a name to a value, var . 71 var looks a lot like let : _(javascriptallonge.pdf (source-range-c98ab3e6-01182))_
- But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations: _(javascriptallonge.pdf (source-range-c98ab3e6-01186))_
- Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All var declarations behave as if they were hoisted to the top of the function, a little like function declarations. _(javascriptallonge.pdf (source-range-c98ab3e6-01188))_
- But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. Note this example of a function that uses a helper: _(javascriptallonge.pdf (source-range-c98ab3e6-01189))_
- In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped. _(javascriptallonge.pdf (source-range-c98ab3e6-01195))_
- A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. _(javascriptallonge.pdf (source-range-c98ab3e6-01189))_
- In that way, var is a little like const and let , we should always declare and bind names before using them. _(javascriptallonge.pdf (source-range-c98ab3e6-01195))_

## Technical atoms

### Technical frame 1: Reassignment / mixing let and const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01178))_

> Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01177))_

<a id="atom-technical-atom-6a4dfd38d219fc66"></a>
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
