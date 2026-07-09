---
page_id: javascriptallonge-recipe-evaluation-time
page_kind: recipe
summary: evaluation time: reusable source-backed pattern with 3 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: evaluation-time
projection_coverage: recipe-javascriptallonge-recipe-evaluation-time@76aa46aea79aaf982619fb118000bd93
---

# evaluation time

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-evaluation-time-ba7a0853]].
- Evidence roles: decision, explanation, example.

## Applicability And Rationale

- Like any other expression, quasi-literals are evaluated late , when that line or lines of code is evaluated. _(javascriptallonge.pdf (source-range-c98ab3e6-01488))_
- Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-c98ab3e6-01491))_
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. _(javascriptallonge.pdf (source-range-c98ab3e6-01491))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01490)_

```
const name = "Harry";
const greeting = (name) => `Hello my name is ${name}`;
greeting('Arthur Dent')
//=> 'Hello my name is Arthur Dent'
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01493)_

```
const greeting = (name) => 'Hello my name is ' + name;
greeting('Arthur Dent')
//=> 'Hello my name is Arthur Dent'
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-evaluation-time-ba7a0853]]
