---
page_id: javascriptallonge-recipe-quasi-literals
page_kind: recipe
summary: quasi-literals: reusable source-backed pattern with 6 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: quasi-literals
projection_coverage: recipe-javascriptallonge-recipe-quasi-literals@ac99ff95783ae008526398e28c35e965
---

# quasi-literals

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-quasi-literals-6d1aa137]].
- Evidence roles: decision, constraint, explanation, procedure, example.

## Applicability And Rationale

- Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-0e12e052-01500))_
- A quasi-literal can contain an expression to be evaluated. _(javascriptallonge.pdf (source-range-0e12e052-01502))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-0e12e052-01502))_
- Aquasi-literal is computationally equivalent to an expression using + . _(javascriptallonge.pdf (source-range-0e12e052-01505))_
- Quasi-literals are expressions that resemble their result. _(javascriptallonge.pdf (source-range-0e12e052-01508))_
- However, there is a big semantic difference between a quasi-literal and an expression. _(javascriptallonge.pdf (source-range-0e12e052-01508))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01501)_

```
`foobar`
//=> 'foobar'
`fizz` + `buzz`
//=> 'fizzbuzz'
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01504)_

```
`A popular number for nerds is ${40 + 2}`
//=> 'A popular number for nerds is 42'
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01507)_

```
'A popular number for nerds is ' + (40 + 2)
//=> 'A popular number for nerds is 42'
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01509)_

```
'A popular number for nerds is' + (40 + 2)
//=> 'A popular number for nerds is42'
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-quasi-literals-6d1aa137]]
