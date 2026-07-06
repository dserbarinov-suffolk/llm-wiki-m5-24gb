---
page_id: javascriptallonge-recipe-generators-are-coroutines
page_kind: recipe
summary: generators are coroutines: reusable source-backed pattern with 22 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: generators-are-coroutines
projection_coverage: recipe-javascriptallonge-recipe-generators-are-coroutines@c3ba35eecef4f8ceed7339c8ac3a66bc
---

# generators are coroutines

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-generators-are-coroutines-bceb595a]].
- Evidence roles: decision, explanation, constraint, example.

## Applicability And Rationale

- This is where generators behave very, very differently from ordinary functions. _(javascriptallonge.pdf (source-range-c98ab3e6-01649))_
- The iterator is in a nascent or 'newborn' state. _(javascriptallonge.pdf (source-range-c98ab3e6-01651))_
- When we call interator.next() , the body of our generator begins to be evaluated. _(javascriptallonge.pdf (source-range-c98ab3e6-01652))_
- The body of our generator runs until it returns, ends, or encounters a yield statement, which is yield 1; . _(javascriptallonge.pdf (source-range-c98ab3e6-01653))_
- The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-c98ab3e6-01656))_
- The iterator resumes execution from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-c98ab3e6-01657))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01648)_

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

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01675)_

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
- Source section: [[javascriptallonge-section-generators-are-coroutines-bceb595a]]
