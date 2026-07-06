---
page_id: javascriptallonge-recipe-literal-object-syntax
page_kind: recipe
summary: literal object syntax: reusable source-backed pattern with 8 statement(s) and 10 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: literal-object-syntax
projection_coverage: recipe-javascriptallonge-recipe-literal-object-syntax@1c3f0d20aae4eb54b7f009b4b446ed08
---

# literal object syntax

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-plain-old-javascript-objects-literal-object-syntax-df2a27da]].
- Evidence roles: decision, explanation, constraint, procedure, example.

## Applicability And Rationale

- JavaScript has a literal syntax for creating objects. _(javascriptallonge.pdf (source-range-c98ab3e6-01068))_
- Two objects created with separate evaluations have differing identities, just like arrays: _(javascriptallonge.pdf (source-range-c98ab3e6-01070))_
- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-c98ab3e6-01072))_
- Names needn't be alphanumeric strings. _(javascriptallonge.pdf (source-range-c98ab3e6-01074))_
- If the name is an alphanumeric string conforming to the same rules as names of variables, there's a simplified syntax for accessing the values: _(javascriptallonge.pdf (source-range-c98ab3e6-01076))_
- Expressions can be used for keys as well. _(javascriptallonge.pdf (source-range-c98ab3e6-01078))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01069)_

```
{ year: 2012, month: 6, day: 14 }
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01071)_

```
{ year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 }
//=> false
Objects use [] to access the values by name, using a string:
{ year: 2012, month: 6, day: 14 }['day']
//=> 14
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01073)_

```
const unique = () => [],
x = unique(),
y = unique(),
z = unique(),
o = { a: x, b: y, c: z };
o['a'] === x && o['b'] === y && o['c'] === z
//=> true
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01075)_

```
{ 'first name': 'reginald', 'last name': 'lewis' }['first name']
//=> 'reginald'
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01077)_

```
const date = { year: 2012, month: 6, day: 14 };
date['day'] === date.day
//=> true
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01079)_

```
{
["p" + "i"]: 3.14159265
}
//=> {"pi":3.14159265}
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-plain-old-javascript-objects-literal-object-syntax-df2a27da]]
