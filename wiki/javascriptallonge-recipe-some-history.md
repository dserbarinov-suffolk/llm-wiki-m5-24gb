---
page_id: javascriptallonge-recipe-some-history
page_kind: recipe
summary: some history: reusable source-backed pattern with 17 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: some-history
projection_coverage: recipe-javascriptallonge-recipe-some-history@0db02128dd1565d448eafcccdb16a9e1
---

# some history

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-garbage-garbage-everywhere-some-history-a956a93b]].
- Evidence roles: decision, constraint, definition, explanation, procedure, structured-state, example.

## Applicability And Rationale

- In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. _(javascriptallonge.pdf (source-range-0e12e052-01026))_
- The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells. _(javascriptallonge.pdf (source-range-0e12e052-01027))_
- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. _(javascriptallonge.pdf (source-range-0e12e052-01027))_
- Lisp's basic data type is often said to be the list, but in actuality it was the 'cons cell,' the term used to describe two 15-bit values stored in one word. _(javascriptallonge.pdf (source-range-0e12e052-01027))_
- Lists were represented as linked lists of cons cells, with each cell's head pointing to an element and the tail pointing to another cons cell. _(javascriptallonge.pdf (source-range-0e12e052-01028))_
- Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being the others), and computers in the late 1950s were extremely small and slow by today's standards. _(javascriptallonge.pdf (source-range-0e12e052-01029))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01031)_

```
const cons = (a, d) => [a, d],
car
= ([a, d]) => a,
cdr
= ([a, d]) => d;
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01033)_

```
const oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, null)))));
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01034)_

```
oneToFive
//=> [1,[2,[3,[4,[5,null]]]]]
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01036)_

```
const node5 = [5,null],
node4 = [4, node5],
node3 = [3, node4],
node2 = [2, node3],
node1 = [1, node2];
const oneToFive = node1;
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01038)_

```
car(oneToFive)
//=> 1
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01041)_

```
cdr(oneToFive)
//=> [2,[3,[4,[5,null]]]]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-garbage-garbage-everywhere-some-history-a956a93b]]
