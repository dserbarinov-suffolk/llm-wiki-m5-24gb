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
projection_coverage: recipe-javascriptallonge-recipe-javascript-s-generators@b8aaea4a0a2e73c16809dec0d70cf6b0
---

# javascript's generators

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-javascript-s-generators-702895b8]].
- Evidence roles: decision, constraint, explanation, example, structured-state.

## Applicability And Rationale

- It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator. _(javascriptallonge.pdf (source-range-c98ab3e6-01657))_
- Given the title of this chapter, it is not a surprise that JavaScript makes this possible. _(javascriptallonge.pdf (source-range-c98ab3e6-01657))_
- We can write an iterator, but use a generation style of programming. _(javascriptallonge.pdf (source-range-c98ab3e6-01658))_
- An iterator written in a generation style is called a generator . _(javascriptallonge.pdf (source-range-c98ab3e6-01658))_
- This makes sense, because empty never yields anything. _(javascriptallonge.pdf (source-range-c98ab3e6-01663))_
- Generator functions can take an argument. _(javascriptallonge.pdf (source-range-c98ab3e6-01664))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01662)_

```
function * empty () {};
empty().next()
//=>
{"done":true}
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01666)_

```
function * only (something) {
yield something;
};
only("you").next()
//=>
{"done":false, value: "you"}
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01668)_

```
only("you").next()
//=>
{"done":false, value: "you"}
only("the lonely").next()
//=>
{"done":false, value: "the lonely"}
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01670)_

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
- Source section: [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-javascript-s-generators-702895b8]]
