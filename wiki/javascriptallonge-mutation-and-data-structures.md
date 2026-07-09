---
page_id: javascriptallonge-mutation-and-data-structures
page_kind: concept
summary: topic-concept: 15 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_e67925382f31ba2e@6afb76c3a6dfdfee720b133795c989aa
---

# mutation and data structures

Source: [[javascriptallonge]]

## Statements

- In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about. (javascriptallonge.pdf p.143)
- Mutation is a surprisingly complex subject. (javascriptallonge.pdf p.143)
- It is possible to compute anything without ever mutating an existing entity. (javascriptallonge.pdf p.143)
- By this pattern, we would be happy to use mutation to construct the list while running mapWith . (javascriptallonge.pdf p.143)
- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. (javascriptallonge.pdf p.143)
- While we're executing the mapWith function, we're constructing a new linked list. (javascriptallonge.pdf p.143)
- The gathering operation [a, b, ..ThreeToFive] is slower, but 'safer. (javascriptallonge.pdf p.145)
- We just use the data, and the less we mutate it, the fewer the times we have to think about whether making changes will be 'safe.'. (javascriptallonge.pdf p.145)

## Rules

- We just use the data, and the less we mutate it, the fewer the times we have to think about whether making changes will be 'safe.'. (javascriptallonge.pdf p.145)

## Technical atoms

<a id="atom-1"></a>
**Atom:** example

```
But after returning the new list, we then become conservative about mutation. This also makes sense: Linked lists often use structure sharing. For example:
```

<a id="atom-2"></a>
**Atom:** code block

```
const EMPTY = {};
const OneToFive = { first: 1,
rest: {
first: 2,
rest: {
first: 3,
rest: {
first: 4,
rest: {
first: 5,
rest: EMPTY } } } } };
OneToFive
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\
r","rest":{"first":"five","rest":{}}}}}}
const ThreeToFive = OneToFive.rest.rest;
ThreeToFive
//=> {"first":3,"rest":{"first":4,"rest":{"first":5,"rest":{}}}}
ThreeToFive.first = "three";
ThreeToFive.rest.first = "four";
ThreeToFive.rest.rest.first = "five";
ThreeToFive
//=> {"first":"three","rest":{"first":"four","rest":{"first":"five","rest":{}}\
}}
OneToFive
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\
r","rest":{"first":"five","rest":{}}}}}}
Changes made to ThreeToFive affect OneToFive, because they share the same structure. When we
wrote ThreeToFive = OneToFive.rest.rest;, we weren’t making a brand new copy of {"first":3,"rest":{"firs
we were getting a reference to the same chain of nodes.
Structure sharing like this is what makes linked lists so fast for taking everything but the first item
```

<a id="atom-3"></a>
**Atom:** code block

```
const OneToFive = [1, 2, 3, 4, 5];
OneToFive
//=> [1,2,3,4,5]
const [a, b, ...ThreeToFive] = OneToFive;
```

<a id="atom-4"></a>
**Atom:** code block

```
OneToFive
//=> [1,2,3,4,5]
const [a, b, ...ThreeToFive] =
ThreeToFive
//=> [3, 4, 5]
ThreeToFive[0] = "three";
ThreeToFive[1] = "four";
ThreeToFive[2] = "five";
ThreeToFive
//=> ["three","four","five"]
OneToFive
//=> [1,2,3,4,5]
```

<a id="atom-5"></a>
**Atom:** rule

```
We don't have to remember to use copying operations when we pass it as a value to a function, or extract some data from it.
```


## Related pages

- [[javascriptallonge-building-with-mutation]] - contextualizes: source-supported topic dependency
