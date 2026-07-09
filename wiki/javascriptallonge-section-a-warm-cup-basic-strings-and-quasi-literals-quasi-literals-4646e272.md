---
page_id: javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-quasi-literals-4646e272
page_kind: source
summary: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: 11 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-quasi-literals-4646e272@7b76a6101f7dd2c7e5e038d848df7433
---

# A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-evaluation-time-ba7a0853]] - next source section: A Warm Cup: Basic Strings and Quasi-Literals / evaluation time

### Source structure

- [[javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-519b0d4d]] - broader source section: A Warm Cup: Basic Strings and Quasi-Literals

### Recipes

- [[javascriptallonge-recipe-quasi-literals]] - recipe pattern: quasi-literals

### Topics

- [[javascriptallonge-quasi-literal]] - topic hub: opens the topic page for Quasi Literal

## Statements

- JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a string literal, but is actually an expression. Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-c98ab3e6-01477))_
- Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-c98ab3e6-01479))_
- Aquasi-literal is computationally equivalent to an expression using + . So the above expression could also be written: _(javascriptallonge.pdf (source-range-c98ab3e6-01482))_
- However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following: _(javascriptallonge.pdf (source-range-c98ab3e6-01485))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-c98ab3e6-01479))_

## Technical atoms

### Technical frame 1: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01479))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01478))_

<a id="atom-technical-atom-852bc8ae09d13507"></a>
```
`foobar`
//=> 'foobar'
`fizz` + `buzz`
//=> 'fizzbuzz'
```

### Technical frame 2: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01485))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01484))_

<a id="atom-technical-atom-b488782759861923"></a>
```
'A popular number for nerds is ' + (40 + 2)
//=> 'A popular number for nerds is 42'
```

### Technical frame 3: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01485))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01486))_

<a id="atom-technical-atom-d77f5a39206ae844"></a>
```
'A popular number for nerds is' + (40 + 2)
//=> 'A popular number for nerds is42'
```
