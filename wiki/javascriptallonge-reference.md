---
page_id: javascriptallonge-reference
page_kind: concept
summary: Reference: 4 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-reference@2924582c2da1c189de437d0c6782ba59
---

# Reference

What [[javascriptallonge]] covers about reference:

## Statements

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities

- You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same contents. Reference types do not. _(javascriptallonge.pdf (source-range-c98ab3e6-00178))_

### And also: / call by sharing

- Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-c98ab3e6-00319))_

### Garbage, Garbage Everywhere / some history

- Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is faster than copying a bunch of elements. _(javascriptallonge.pdf (source-range-c98ab3e6-01042))_

### Garbage, Garbage Everywhere / so why arrays

- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-c98ab3e6-01052))_


## Technical atoms

### Technical frame 1: And also: / call by sharing

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00323))_

> 26 Unless the argument is NaN , which isn't equal to anything, including itself . NaN in JavaScript behaves a lot like NULL in SQL.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00322))_

<a id="atom-technical-atom-300f3bd87e349a64"></a>
```
(value) =>
((ref1, ref2) => ref1 === ref2)(value, value)
```

### Technical frame 2: Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01037))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01036))_

<a id="atom-technical-atom-72419095758d2e69"></a>
```
const node5 = [5,null],
node4 = [4, node5],
node3 = [3, node4],
node2 = [2, node3],
node1 = [1, node2];
const oneToFive = node1;
```

### Technical frame 3: Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01039))_

> car is very fast, it simply extracts the first element of the cons cell.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01038))_

<a id="atom-technical-atom-9d951d32dc76b51e"></a>
```
car(oneToFive)
//=> 1
```

### Technical frame 4: Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01042))_

> Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is fas

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01041))_

<a id="atom-technical-atom-c04ec28db918d40d"></a>
```
cdr(oneToFive)
//=> [2,[3,[4,[5,null]]]]
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-list]] - shared technical atoms: List shares technical record from Garbage, Garbage Everywhere / some history: const node5 = [5,null], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; const oneToFive = node1; (3 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from And also: / call by sharing: Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, ... [truncated]; Javascript shares technical record from Garbage, Garbage Everywhere / some history: const node5 = [5,null], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; const oneToFive = node1; (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-type]] - shared statements and technical atoms: Type shares source evidence from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities: You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same cont ... [truncated]; Type shares technical record from And also: / call by sharing: (value) => ((ref1, ref2) => ref1 === ref2)(value, value) (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms: Element shares source evidence from Garbage, Garbage Everywhere / so why arrays: Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained la ... [truncated]; Element shares technical record from Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-structure]] - shared statements and technical atoms: Structure shares source evidence from Garbage, Garbage Everywhere / some history: Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of ar ... [truncated]; Structure shares technical record from Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from And also: / call by sharing: (value) => ((ref1, ref2) => ref1 === ref2)(value, value) (1 shared atom(s))
- [[javascriptallonge-copy]] - shared technical atoms: Copy shares technical record from Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared atom(s))
- [[javascriptallonge-data]] - shared technical atoms: Data shares technical record from Garbage, Garbage Everywhere / some history: car(oneToFive) //=> 1 (1 shared atom(s))

## Source

- [[javascriptallonge]]
