---
page_id: javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-50e42ba0
page_kind: source
summary: A Warm Cup: Basic Strings and Quasi-Literals: 25 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-50e42ba0@d65dc6a9e972258d8ec2bf8e9b0cd43b
---

# A Warm Cup: Basic Strings and Quasi-Literals

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-quasi-literals-6d1aa137]] - narrower source section: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals
- [[javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-evaluation-time-1634aeef]] - narrower source section: A Warm Cup: Basic Strings and Quasi-Literals / evaluation time
- [[javascriptallonge-section-recipes-with-data-57848af5]] - previous source section: Recipes with Data
- [[javascriptallonge-section-served-by-the-pot-collections-14399de3]] - next source section: Served by the Pot: Collections

## Statements

- Coffee and a Book An expression is any valid unit of code that resolves to a value.-Mozilla Development Network: Expressions and operators 87 _(javascriptallonge.pdf (source-range-0e12e052-01494))_
- There are operators that can be used on strings. The most common is + , it concatenates : _(javascriptallonge.pdf (source-range-0e12e052-01496))_
- String manipulation is extremely common in programming. Writing is a big part of what makes us human, and strings are how JavaScript and most other languages represent writing. _(javascriptallonge.pdf (source-range-0e12e052-01498))_
- For example, the escape sequence \n inserts a newline character in a string literal, like this: 'first line\nsecond line' . _(javascriptallonge.pdf (source-range-0e12e052-01495))_

## Statements by subsection

### A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

- JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a string literal, but is actually an expression. Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-0e12e052-01500))_
- Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-0e12e052-01502))_
- Aquasi-literal is computationally equivalent to an expression using + . So the above expression could also be written: _(javascriptallonge.pdf (source-range-0e12e052-01505))_
- However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following: _(javascriptallonge.pdf (source-range-0e12e052-01508))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-0e12e052-01502))_

### A Warm Cup: Basic Strings and Quasi-Literals / evaluation time

- Like any other expression, quasi-literals are evaluated late , when that line or lines of code is evaluated. _(javascriptallonge.pdf (source-range-0e12e052-01511))_
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-0e12e052-01514))_
- Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-0e12e052-01514))_
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. _(javascriptallonge.pdf (source-range-0e12e052-01514))_

## Technical atoms

### Technical frame 1: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01502))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01501))_

```
`foobar`
//=> 'foobar'
`fizz` + `buzz`
//=> 'fizzbuzz'
```
