---
page_id: javascriptallonge-recipe-destructuring-arrays
page_kind: recipe
summary: destructuring arrays: reusable source-backed pattern with 4 statement(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: destructuring-arrays
projection_coverage: recipe-javascriptallonge-recipe-destructuring-arrays@fb01cdbd1fa0be72478dd6e365f0f864
---

# destructuring arrays

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-arrays-19594149]].
- Evidence roles: decision, explanation, constraint, example.

## Applicability And Rationale

- There is another way to extract elements from arrays: Destructuring , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-0e12e052-00835))_
- The line const wrapped = [something]; is interesting. _(javascriptallonge.pdf (source-range-0e12e052-00838))_
- The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . _(javascriptallonge.pdf (source-range-0e12e052-00841))_
- We could do the same thing with (name) => name[1] , but destructuring is code that resembles the data it consumes, a valuable coding style. _(javascriptallonge.pdf (source-range-0e12e052-00843))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00836)_

```
const wrap = (something) => [something];
Let’s expand it to use a block and an extra name:
const wrap = (something) => {
const wrapped = [something];
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00837)_

```
const wrap = (something) => {
const wrapped = [something]
return wrapped;
}
wrap("package")
//=> ["package"]
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00840)_

```
const unwrap = (wrapped) => {
const [something] = wrapped;
return something;
}
unwrap(["present"])
//=> "present"
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00842)_

```
const surname = (name) => {
const [first, last] = name;
return last;
}
surname(["Reginald", "Braithwaite"])
//=> "Braithwaite"
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00845)_

```
const description = (nameAndOccupation) => {
const [[first, last], occupation] = nameAndOccupation;
return `${first} is a ${occupation}`;
}
description([["Reginald", "Braithwaite"], "programmer"])
//=> "Reginald is a programmer"
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-arrays-19594149]]
