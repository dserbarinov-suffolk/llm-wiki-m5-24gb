---
page_id: javascriptallonge-recipe-why-the-six-edition
page_kind: recipe
summary: why the 'six' edition?: reusable source-backed pattern with 15 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: why-the-six-edition
projection_coverage: recipe-javascriptallonge-recipe-why-the-six-edition@a9867fd64aeaea651fbd98ff7df9cd1d
---

# why the 'six' edition?

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-a-pull-of-the-lever-prefaces-about-javascript-allong-why-the-six-edition-35c3fb78]].
- Evidence roles: decision, constraint, explanation, example.

## Applicability And Rationale

- Features like destructuring, block-structured variables, iterables, generators, and the class keyword are poised to make JavaScript programming more expressive. _(javascriptallonge.pdf (source-range-0e12e052-00023))_
- ECMAScript 2015 (formerly called ECMAScript 6 or 'ES6'), is ushering in a very large number of improvements to the way programmers can write small, powerful components and combine them into larger, fully featured programs. _(javascriptallonge.pdf (source-range-0e12e052-00023))_
- For example, JavaScript did not include block-structured variables. _(javascriptallonge.pdf (source-range-0e12e052-00024))_
- Over time, programmers discovered ways to roll their own versions of important features. _(javascriptallonge.pdf (source-range-0e12e052-00024))_
- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. _(javascriptallonge.pdf (source-range-0e12e052-00024))_
- And the variable i is scoped locally to the code within the braces. _(javascriptallonge.pdf (source-range-0e12e052-00027))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00026)_

```
for (int i = 0; i < array.length; ++i) {
// ...
}
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00028)_

```
var i;
for (i = 0; i < array.length; ++i) {
(function (i) {
// ...
})(i)
}
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00031)_

```
def foo (first, *rest)
# ...
end
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00033)_

```
function foo () {
var first = arguments[0],
rest
= [].slice.call(arguments, 1);
// ...
}
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00037)_

```
for (let i = 0; i < array.length; ++i) {
// ...
}
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00039)_

```
function foo (first, ...rest) {
// ...
}
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-a-pull-of-the-lever-prefaces-about-javascript-allong-why-the-six-edition-35c3fb78]]
