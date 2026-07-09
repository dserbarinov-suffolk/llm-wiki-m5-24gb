---
page_id: javascriptallonge-some-history
page_kind: concept
summary: some history: 16 accepted assertion(s) and 8 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_3deb4bcc9994a88f@fb51271585c3d5e3e8bb2cd531199831
---

# some history

Source: [[javascriptallonge]]

## Statements

- In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. (javascriptallonge.pdf p.129)
- Lisp's basic data type is often said to be the list, but in actuality it was the 'cons cell,' the term used to describe two 15-bit values stored in one word. (javascriptallonge.pdf p.129)
- The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells. (javascriptallonge.pdf p.129)
- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. (javascriptallonge.pdf p.129)
- Lists were represented as linked lists of cons cells, with each cell's head pointing to an element and the tail pointing to another cons cell. (javascriptallonge.pdf p.129)
- Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being the others), and computers in the late 1950s were extremely small and slow by today's standards. (javascriptallonge.pdf p.129)
- Although the 704 used core memory, it still used vacuum tubes for its logic. (javascriptallonge.pdf p.129)
- This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . (javascriptallonge.pdf p.130)
- car is very fast, it simply extracts the first element of the cons cell. (javascriptallonge.pdf p.130)
- In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. (javascriptallonge.pdf p.130)
- Getting one reference to a structure that already exists is faster than copying a bunch of elements. (javascriptallonge.pdf p.130)
- There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. (javascriptallonge.pdf p.130)
- So now we understand that in Lisp, a lot of things use linked lists, and they do that in part because it was what the hardware made possible. (javascriptallonge.pdf p.130)
- That being said, it is easy to understand and helps us grasp how literals and destructuring works, and how recursive algorithms ought to mirror the self-similarity of the data structures they manipulate. (javascriptallonge.pdf p.130)
- And so it is today that languages like JavaScript have arrays that are slow to split into the equivalent of a car / cdr pair, but instructional examples of recursive programs still have echoes of their Lisp origins. (javascriptallonge.pdf p.130)
- We'll look at linked lists again when we look at Plain Old JavaScript Objects. (javascriptallonge.pdf p.130)

## Technical atoms

<a id="atom-1"></a>
**Atom:** table

```text
some history
Once upon a time, there was a programming language called Lisp 65 , an acronym for LISt Processing. 66 Lisp was one of the very first high-level languages, the very first implementation was written for the IBM 704 67 computer. (The very first FORTRAN implementation was also written for the 704).
The 704 had a 36-bit word, meaning that it was very fast to store and retrieve 36-bit values. The CPU's instruction set featured two important macros: CAR would fetch 15 bits representing the Contents of the Address part of the Register, while CDR would fetch the Contents of the Decrement part of the Register.
65 https://en.wikipedia.org/wiki/Lisp_
67 https://en.wikipedia.org/wiki/IBM_704
66 Lisp is still very much alive, and one of the most interesting and exciting programming languages in use today is Clojure, a Lisp dialect that runs on the JVM, along with its sibling ClojureScript, Clojure that transpiles to JavaScript.
```

<a id="atom-2"></a>
**Atom:** rule

```
If you had two 15-bit values and wished to write them to the register, the CONS macro would take the values and write them to a 36-bit word.
```

<a id="atom-3"></a>
**Atom:** code block

```
const cons = (a, d) => [a, d],
car
= ([a, d]) => a,
cdr
= ([a, d]) => d;
```

<a id="atom-4"></a>
**Atom:** code block

```
const oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, null)))));
```

<a id="atom-5"></a>
**Atom:** code block

```
oneToFive
//=> [1,[2,[3,[4,[5,null]]]]]
```

<a id="atom-6"></a>
**Atom:** code block

```
const node5 = [5,null],
node4 = [4, node5],
node3 = [3, node4],
node2 = [2, node3],
node1 = [1, node2];
const oneToFive = node1;
```

<a id="atom-7"></a>
**Atom:** code block

```
car(oneToFive)
//=> 1
```

<a id="atom-8"></a>
**Atom:** code block

```
cdr(oneToFive)
//=> [2,[3,[4,[5,null]]]]
```
