---
page_id: javascriptallonge-recipe-generators-are-coroutines
page_kind: recipe
summary: generators are coroutines: reusable source-backed pattern with 22 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: generators-are-coroutines
projection_coverage: recipe-javascriptallonge-recipe-generators-are-coroutines@7d662bdec8bffe7358be50c424952d95
---

# generators are coroutines

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-generators-are-coroutines-e97b031c]].
- Evidence roles: decision, explanation, constraint, example.

## Applicability And Rationale

- This is where generators behave very, very differently from ordinary functions. _(javascriptallonge.pdf (source-range-0e12e052-01675))_
- - The iterator is in a nascent or 'newborn' state. _(javascriptallonge.pdf (source-range-0e12e052-01677))_
- - When we call interator.next() , the body of our generator begins to be evaluated. _(javascriptallonge.pdf (source-range-0e12e052-01678))_
- - The body of our generator runs until it returns, ends, or encounters a yield statement, which is yield 1; . _(javascriptallonge.pdf (source-range-0e12e052-01679))_
- - The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-0e12e052-01682))_
- - The iterator resumes execution from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-0e12e052-01683))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01674)_

```
const oneTwoThree = function * () {
yield 1;
yield 2;
yield 3;
};
oneTwoThree().next()
//=>
{"done":false, value: 1}
oneTwoThree().next()
//=>
{"done":false, value: 1}
oneTwoThree().next()
//=>
{"done":false, value: 1}
const iterator = oneTwoThree();
iterator.next()
//=>
{"done":false, value: 1}
iterator.next()
//=>
{"done":false, value: 2}
iterator.next()
//=>
{"done":false, value: 3}
iterator.next()
//=>
{"done":true}
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01701)_

```
const oneTwoThree = function () {
let state = 'newborn';
return {
next () {
switch (state) {
case 'newborn':
state = 1;
return {value: 1};
case 1:
state = 2;
return {value: 2}
case 2:
state = 3;
return {value: 3}
case 3:
return {done: true};
}
}
}
};
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-generators-are-coroutines-e97b031c]]
