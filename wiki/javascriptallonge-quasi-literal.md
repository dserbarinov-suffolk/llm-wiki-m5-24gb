---
page_id: javascriptallonge-quasi-literal
page_kind: concept
summary: quasi-literals: 6 accepted assertion(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_47946ded39bed72e@d1e0f55ffd5516d06fad0eb91dd8ef6d
---

# quasi-literals

Source: [[javascriptallonge]]

## Statements

- Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. (javascriptallonge.pdf p.203)
- A quasi-literal can contain an expression to be evaluated. (javascriptallonge.pdf p.203)
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. (javascriptallonge.pdf p.203)
- Aquasi-literal is computationally equivalent to an expression using + . (javascriptallonge.pdf p.203)
- Quasi-literals are expressions that resemble their result. (javascriptallonge.pdf p.204)
- However, there is a big semantic difference between a quasi-literal and an expression. (javascriptallonge.pdf p.204)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
`foobar`
//=> 'foobar'
`fizz` + `buzz`
//=> 'fizzbuzz'
```

<a id="atom-2"></a>
**Atom:** code block

```
`A popular number for nerds is ${40 + 2}`
//=> 'A popular number for nerds is 42'
```

<a id="atom-3"></a>
**Atom:** code block

```
'A popular number for nerds is ' + (40 + 2)
//=> 'A popular number for nerds is 42'
```

<a id="atom-4"></a>
**Atom:** code block

```
'A popular number for nerds is' + (40 + 2)
//=> 'A popular number for nerds is42'
```
