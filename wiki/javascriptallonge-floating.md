---
page_id: javascriptallonge-floating
page_kind: concept
summary: floating: 7 accepted assertion(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_c7e19ae4e4f430b4@69a9a634999eff7f949f29a136560902
---

# floating

Source: [[javascriptallonge]]

## Statements

- But we mentioned that numbers are represented internally as floating point, meaning that they need not be just integers. (javascriptallonge.pdf p.25)
- We can , for example, write 1.5 or 33.33 , and JavaScript represents these literals as floating point numbers. (javascriptallonge.pdf p.25)
- It's tempting to think we now have everything we need to do things like handle amounts of money, but as the late John Belushi would say, 'Nooooooooooooooooooooo.' A computer's internal representation for a floating point number is binary, while our literal number was in base ten. (javascriptallonge.pdf p.25)
- This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2. (javascriptallonge.pdf p.25)
- But as a rule, if you need to work with real numbers, you should have more than a nodding acquaintance with the IEEE Standard for Floating-Point Arithmetic 15 . (javascriptallonge.pdf p.26)
- For example, '$43.21' will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21 . (javascriptallonge.pdf p.26)
- In this book, we need not think about such details, but outside of this book, we must. (javascriptallonge.pdf p.26)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
1.0
//=> 1
1.0 + 1.0
//=> 2
1.0 + 1.0 + 1.0
//=> 3
```

<a id="atom-2"></a>
**Atom:** table

```text
13 http://en.wikipedia.org/wiki/Double-precision_floating-point_format
14 Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js , it will happily report that the answer is 18014398509481982 . But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations.
```

<a id="atom-3"></a>
**Atom:** code block

```
0.1
//=> 0.1
0.1 + 0.1
//=> 0.2
0.1 + 0.1 + 0.1
//=> 0.30000000000000004
```

<a id="atom-4"></a>
**Atom:** example

```
This kind of 'inexactitude' can be ignored when performing calculations that have an acceptable deviation. For example, when centering some text on a page, as long as the difference between what you might calculate longhand and JavaScript's calculation is less than a pixel, there is no observable error.
```

<a id="atom-5"></a>
**Atom:** rule

```
Professional programmers almost never use floating point numbers to represent monetary amounts.
```
