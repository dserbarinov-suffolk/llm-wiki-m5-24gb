---
page_id: javascriptallonge-section-var-446841c5
page_kind: source
summary: var: 15 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-var-446841c5@ea511f0d38041b24a7b8d8672c0c96bf
---

# var

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-mixing-let-and-const-485aff44]] - previous source section: mixing let and const
- [[javascriptallonge-section-why-const-and-let-were-invented-218b7467]] - next source section: why const and let were invented

## Statements

- JavaScript has one more way to bind a name to a value, var . 71 var looks a lot like let : _(javascriptallonge.pdf (source-range-c98ab3e6-01163))_
- But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations: _(javascriptallonge.pdf (source-range-c98ab3e6-01167))_
- Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All var declarations behave as if they were hoisted to the top of the function, a little like function declarations. _(javascriptallonge.pdf (source-range-c98ab3e6-01169))_
- But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. Note this example of a function that uses a helper: _(javascriptallonge.pdf (source-range-c98ab3e6-01170))_
- In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped. _(javascriptallonge.pdf (source-range-c98ab3e6-01176))_
- A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. _(javascriptallonge.pdf (source-range-c98ab3e6-01170))_
- In that way, var is a little like const and let , we should always declare and bind names before using them. _(javascriptallonge.pdf (source-range-c98ab3e6-01176))_

## Technical atoms

### Technical frame 1: var

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01167))_

> But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01164))_

<a id="atom-technical-atom-ce362bfbb51880b9"></a>
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

### Technical frame 2: var

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01167))_

> But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01166))_

<a id="atom-technical-atom-ee34a34b88967961"></a>
```
return n * factorial2(x);
}
}
factorial2(5)
//=> 120
```

### Technical frame 3: var

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01169))_

> Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All var declarations behave as if they were hoisted to the top of the function, a little like function declarations.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01168))_

<a id="atom-technical-atom-bd739848728b2b19"></a>
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
