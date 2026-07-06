---
page_id: javascriptallonge-section-reassignment-mixing-let-and-const-var-91a401bc
page_kind: source
summary: Reassignment / mixing let and const / var: 15 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-reassignment-mixing-let-and-const-var-91a401bc@1bf3dd9aaacc50a4674f411274d44271
---

# Reassignment / mixing let and const / var

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-reassignment-mixing-let-and-const-e64fdef1]] - broader source section: Reassignment / mixing let and const

## Statements

- JavaScript has one more way to bind a name to a value, var . 71 var looks a lot like let : _(javascriptallonge.pdf (source-range-c98ab3e6-01182))_
- But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations: _(javascriptallonge.pdf (source-range-c98ab3e6-01186))_
- Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All var declarations behave as if they were hoisted to the top of the function, a little like function declarations. _(javascriptallonge.pdf (source-range-c98ab3e6-01188))_
- But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. Note this example of a function that uses a helper: _(javascriptallonge.pdf (source-range-c98ab3e6-01189))_
- In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped. _(javascriptallonge.pdf (source-range-c98ab3e6-01195))_
- A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. _(javascriptallonge.pdf (source-range-c98ab3e6-01189))_
- In that way, var is a little like const and let , we should always declare and bind names before using them. _(javascriptallonge.pdf (source-range-c98ab3e6-01195))_

## Technical atoms

### Technical frame 1: Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01186))_

> But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01183))_

<a id="atom-technical-atom-6e452de411e16590"></a>
```
const factorial = (n) => {
let x = n;
if (x === 1) {
return 1;
}
else {
--x;
return n * factorial(x);
}
}
factorial(5)
//=> 120
const factorial2 = (n) => {
var x = n;
if (x === 1) {
return 1;
}
else {
--x;
```

### Technical frame 2: Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01186))_

> But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01185))_

<a id="atom-technical-atom-6e2cbfbebb95da01"></a>
```
return n * factorial2(x);
}
}
factorial2(5)
//=> 120
```

### Technical frame 3: Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01188))_

> Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All var declarations behave as if they were hoisted to the top of the function, a little like function declarations.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01187))_

<a id="atom-technical-atom-bccd27cd263f4eda"></a>
```
(() => {
var age = 49;
if (true) {
var age = 50;
}
return age;
})()
//=> 50
```
