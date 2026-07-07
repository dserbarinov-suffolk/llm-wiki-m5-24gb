---
page_id: javascriptallonge-recipe-quasi-literals
page_kind: recipe
summary: quasi-literals: reusable source-backed pattern with 6 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: quasi-literals
projection_coverage: recipe-javascriptallonge-recipe-quasi-literals@45d7967f5081ce1aed9f4831d1ffb553
---

# quasi-literals

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-quasi-literals-e514ae04]].
- Evidence roles: decision, constraint, explanation, procedure, example.

## Applicability And Rationale

- Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-c98ab3e6-01477))_
- A quasi-literal can contain an expression to be evaluated. _(javascriptallonge.pdf (source-range-c98ab3e6-01479))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-c98ab3e6-01479))_
- Aquasi-literal is computationally equivalent to an expression using + . _(javascriptallonge.pdf (source-range-c98ab3e6-01482))_
- Quasi-literals are expressions that resemble their result. _(javascriptallonge.pdf (source-range-c98ab3e6-01485))_
- However, there is a big semantic difference between a quasi-literal and an expression. _(javascriptallonge.pdf (source-range-c98ab3e6-01485))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01478)_

```
`foobar`
//=> 'foobar'
`fizz` + `buzz`
//=> 'fizzbuzz'
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01481)_

```
`A popular number for nerds is ${40 + 2}`
//=> 'A popular number for nerds is 42'
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01484)_

```
'A popular number for nerds is ' + (40 + 2)
//=> 'A popular number for nerds is 42'
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01486)_

```
'A popular number for nerds is' + (40 + 2)
//=> 'A popular number for nerds is42'
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-quasi-literals-e514ae04]]
