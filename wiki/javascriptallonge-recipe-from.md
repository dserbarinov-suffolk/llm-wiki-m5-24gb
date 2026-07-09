---
page_id: javascriptallonge-recipe-from
page_kind: recipe
summary: from: reusable source-backed pattern with 7 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: from
projection_coverage: recipe-javascriptallonge-recipe-from@a60db96da2b4a57f409c12bf8f3ac297
---

# from

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-98745d63]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- No, of course not, we can do anything we like with them. _(javascriptallonge.pdf (source-range-c98ab3e6-01581))_
- One useful thing is to write a .from function that gathers an iterable into a particular collection type. _(javascriptallonge.pdf (source-range-c98ab3e6-01582))_
- As you recall, functions are mutable objects. _(javascriptallonge.pdf (source-range-c98ab3e6-01584))_
- And we can assign properties to functions with a . _(javascriptallonge.pdf (source-range-c98ab3e6-01584))_
- We can do the same with our own collections. _(javascriptallonge.pdf (source-range-c98ab3e6-01584))_
- And if we assign a function to a property, we've created a method. _(javascriptallonge.pdf (source-range-c98ab3e6-01584))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01583)_

```
Array.from(UpTo1000)
//=> [1,81,121,361,441,841,961]
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01586)_

```
Stack3.from = function (iterable) {
const stack = this();
for (let element of iterable) {
stack.push(element);
}
return stack;
}
Pair1.from = (iterable) =>
(function iterationToList (iteration) {
const {done, value} = iteration.next();
return done ? EMPTY : Pair1(value, iterationToList(iteration));
})(iterable[Symbol.iterator]())
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01588)_

```
const numberList = Pair1.from(untilWith((x) => x > 10, Numbers));
Pair1.from(Squares)
//=> {"first":0,
"rest":{"first":1,
"rest":{"first":4,
"rest":{ ...
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-98745d63]]
