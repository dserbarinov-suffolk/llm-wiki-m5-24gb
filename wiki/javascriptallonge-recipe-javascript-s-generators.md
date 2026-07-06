---
page_id: javascriptallonge-recipe-javascript-s-generators
page_kind: recipe
summary: javascript's generators: reusable source-backed pattern with 9 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: javascript-s-generators
projection_coverage: recipe-javascriptallonge-recipe-javascript-s-generators@8d1cfa923856d2d81820289c1a893004
---

# javascript's generators

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-javascript-s-generators-34e25b0e]].
- Evidence roles: decision, constraint, explanation, example, structured-state.

## Applicability And Rationale

- It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator. _(javascriptallonge.pdf (source-range-c98ab3e6-01631))_
- Given the title of this chapter, it is not a surprise that JavaScript makes this possible. _(javascriptallonge.pdf (source-range-c98ab3e6-01631))_
- An iterator written in a generation style is called a generator . _(javascriptallonge.pdf (source-range-c98ab3e6-01632))_
- We can write an iterator, but use a generation style of programming. _(javascriptallonge.pdf (source-range-c98ab3e6-01632))_
- This makes sense, because empty never yields anything. _(javascriptallonge.pdf (source-range-c98ab3e6-01637))_
- Generator functions can take an argument. _(javascriptallonge.pdf (source-range-c98ab3e6-01638))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01636)_

```
function * empty () {};
empty().next()
//=>
{"done":true}
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01640)_

```
function * only (something) {
yield something;
};
only("you").next()
//=>
{"done":false, value: "you"}
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01642)_

```
only("you").next()
//=>
{"done":false, value: "you"}
only("the lonely").next()
//=>
{"done":false, value: "the lonely"}
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01644)_

```
const sixteen = only("sixteen");
sixteen.next()
//=>
{"done":false, value: "sixteen"}
sixteen.next()
//=>
{"done":true}
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-javascript-s-generators-34e25b0e]]
