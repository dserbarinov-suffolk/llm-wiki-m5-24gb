---
page_id: javascriptallonge-mutation
page_kind: concept
summary: Mutation: 4 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-mutation@1f7c4e49f683c50c6e8b2e0d981faebb
---

# Mutation

What [[javascriptallonge]] covers about mutation:

## Statements

### Mutation / mutation and data structures

- Mutation is a surprisingly complex subject. It is possible to compute anything without ever mutating an existing entity. Languages like Haskell 70 don't permit mutation at all. In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about. _(javascriptallonge.pdf (source-range-c98ab3e6-01118))_

- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists from Plain Old JavaScript Objects. While we're executing the mapWith function, we're constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith . _(javascriptallonge.pdf (source-range-c98ab3e6-01119))_


## Technical atoms

### Technical frame 1: Mutation / mutation and data structures

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01126))_

> The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. '

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01124))_

<a id="atom-technical-atom-d83812ebf043293f"></a>
```
const OneToFive = [1, 2, 3, 4, 5];
OneToFive
//=> [1,2,3,4,5]
const [a, b, ...ThreeToFive] = OneToFive;
```

### Technical frame 2: Mutation / mutation and data structures

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01126))_

> The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. '

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01125))_

<a id="atom-technical-atom-2e3f7352ee1f9aeb"></a>
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

### Technical frame 3: Mutation / mutation and data structures

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01126))_

> The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. '

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01127))_

<a id="atom-technical-atom-3d29236dca19d99c"></a>
> We don't have to remember to use copying operations when we pass it as a value to a function, or extract some data from it.


## Related pages

### Source structure

- [[javascriptallonge-section-mutation-ae8039d8]] - source section: Mutation shares source evidence from Mutation: In JavaScript, almost every type of value can mutate . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall t ... [truncated]; Mutation shares technical record from Mutation: const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree //=> [ 'one', 2, 3 ] (25 shared statement(s), 14 shared atom(s))

### Shared claims

- [[javascriptallonge-pattern]] - shared statements: Pattern shares source evidence from Mutation / mutation and data structures: One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists f ... [truncated] (2 shared statement(s))

## Source

- [[javascriptallonge]]
