---
page_id: javascriptallonge-recipe-const
page_kind: recipe
summary: const: reusable source-backed pattern with 11 statement(s) and 9 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: const
projection_coverage: recipe-javascriptallonge-recipe-const@a47d45788889d3e9e8e85b869b19e899
---

# const

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-const-96382167]].
- Evidence roles: decision, explanation, constraint, example, structured-state.

## Applicability And Rationale

- Another way to write our 'circumference' function would be to pass PI along with the diameter argument, something like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00400))_
- This differs from our example above in that there is only one environment, rather than two. _(javascriptallonge.pdf (source-range-c98ab3e6-00404))_
- We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name. _(javascriptallonge.pdf (source-range-c98ab3e6-00404))_
- JavaScript gives us a way to do that, the const keyword. _(javascriptallonge.pdf (source-range-c98ab3e6-00405))_
- We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const : _(javascriptallonge.pdf (source-range-c98ab3e6-00405))_
- That's much better than what we were writing. _(javascriptallonge.pdf (source-range-c98ab3e6-00407))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00401)_

```
(diameter, PI) => diameter * PI
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00403)_

```
((diameter, PI) => diameter * PI)(2, 3.14159265)
//=> 6.2831853
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00406)_

```
(diameter) => {
const PI = 3.14159265;
return diameter * PI
}
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00410)_

```
((diameter) =>
((PI) =>
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00411)_

```
diameter * PI)(3.14159265))(2)
Or:
((diameter, PI) => diameter * PI)(2, 3.14159265)
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00412)_

```
//=> 6.2831853
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-const-96382167]]
