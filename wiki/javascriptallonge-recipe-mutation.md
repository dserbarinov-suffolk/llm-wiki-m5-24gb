---
page_id: javascriptallonge-recipe-mutation
page_kind: recipe
summary: Mutation: reusable source-backed pattern with 13 statement(s) and 7 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: mutation
projection_coverage: recipe-javascriptallonge-recipe-mutation@a41177b47edd28b2ee5b030987b93da9
---

# Mutation

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-mutation-ae8039d8]].
- Evidence roles: decision, constraint, procedure, explanation, example.

## Applicability And Rationale

- In JavaScript, almost every type of value can mutate . _(javascriptallonge.pdf (source-range-c98ab3e6-01099))_
- Recall that you can access a value from within an array or an object using [] . _(javascriptallonge.pdf (source-range-c98ab3e6-01099))_
- Specifically, arrays and objects can mutate. _(javascriptallonge.pdf (source-range-c98ab3e6-01099))_
- Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. _(javascriptallonge.pdf (source-range-c98ab3e6-01105))_
- Both halloween and allHallowsEve are bound to the same array value within the local environment. _(javascriptallonge.pdf (source-range-c98ab3e6-01107))_
- In each of these examples, we have created two aliases for the same value. _(javascriptallonge.pdf (source-range-c98ab3e6-01109))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01100)_

```
const oneTwoThree = [1, 2, 3];
oneTwoThree[0] = 'one';
oneTwoThree
//=> [ 'one', 2, 3 ]
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01102)_

```
const oneTwoThree = [1, 2, 3];
oneTwoThree[3] = 'four';
oneTwoThree
//=> [ 1, 2, 3, 'four' ]
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01104)_

```
const name = {firstName: 'Leonard', lastName: 'Braithwaite'};
name.middleName = 'Austin'
name
//=> { firstName: 'Leonard',
#
lastName: 'Braithwaite',
#
middleName: 'Austin' }
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01106)_

```
const allHallowsEve = [2012, 10, 31]
const halloween = allHallowsEve;
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01108)_

```
const allHallowsEve = [2012, 10, 31];
(function (halloween) {
// ...
})(allHallowsEve);
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01111)_

```
const allHallowsEve = [2012, 10, 31];
(function (halloween) {
halloween = [2013, 10, 31];
})(allHallowsEve);
allHallowsEve
//=> [2012, 10, 31]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-mutation-ae8039d8]]
