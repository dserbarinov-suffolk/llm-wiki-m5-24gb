---
page_id: javascriptallonge-section-garbage-garbage-everywhere-8c9764a5
page_kind: source
summary: Garbage, Garbage Everywhere: 19 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-garbage-garbage-everywhere-8c9764a5@80785f802fbf146626e5b92c7b2c0290
---

# Garbage, Garbage Everywhere

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-composing-and-decomposing-data-99b4771a]] - previous source section: Composing and Decomposing Data
- [[javascriptallonge-section-plain-old-javascript-objects-ae9a88a3]] - next source section: Plain Old JavaScript Objects

### Source structure

- [[javascriptallonge-section-garbage-garbage-everywhere-so-why-arrays-35221ee3]] - narrower source section: Garbage, Garbage Everywhere / so why arrays
- [[javascriptallonge-section-garbage-garbage-everywhere-some-history-d0580aea]] - narrower source section: Garbage, Garbage Everywhere / some history

## Statements

- We have now seen how to use Tail Calls to execute mapWith in constant space: _(javascriptallonge.pdf (source-range-c98ab3e6-00997))_
- But when we try it on very large arrays, we discover that it is still very slow. Much slower than the built-in .map method for arrays. The right tool to discover why it's still slow is a memory profiler, but a simple inspection of the program will reveal the following: _(javascriptallonge.pdf (source-range-c98ab3e6-00999))_
- Every time we call mapWith , we're calling [...prepend, fn(first)] . To do that, we take the array in prepend and push fn(first) onto the end, creating a new array that will be passed to the next invocation of mapWith . _(javascriptallonge.pdf (source-range-c98ab3e6-01000))_
- The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend . _(javascriptallonge.pdf (source-range-c98ab3e6-01002))_
- We may not be creating 3,000 stack frames, but we are creating three thousand new arrays and copying elements into each and every one of them. Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another. _(javascriptallonge.pdf (source-range-c98ab3e6-01003))_
- Key Point : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded. _(javascriptallonge.pdf (source-range-c98ab3e6-01004))_
- 64 It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. But this is not how JavaScript's built-in arrays work. _(javascriptallonge.pdf (source-range-c98ab3e6-01006))_
- Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend . _(javascriptallonge.pdf (source-range-c98ab3e6-01002))_
- Key Point : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded. _(javascriptallonge.pdf (source-range-c98ab3e6-01004))_
- 64 It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. _(javascriptallonge.pdf (source-range-c98ab3e6-01006))_

## Statements by subsection

### Garbage, Garbage Everywhere / summary

- Although we showed how to use tail calls to map and fold over arrays with [first, ...rest] , in reality this is not how it ought to be done. But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. _(javascriptallonge.pdf (source-range-c98ab3e6-01039))_
- But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. _(javascriptallonge.pdf (source-range-c98ab3e6-01039))_

## Technical atoms

### Technical frame 1: Garbage, Garbage Everywhere / some history

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01009))_

<a id="atom-technical-atom-e5250e23571ce1f5"></a>
```text
some history
Once upon a time, there was a programming language called Lisp 65 , an acronym for LISt Processing. 66 Lisp was one of the very first high-level languages, the very first implementation was written for the IBM 704 67 computer. (The very first FORTRAN implementation was also written for the 704).
The 704 had a 36-bit word, meaning that it was very fast to store and retrieve 36-bit values. The CPU's instruction set featured two important macros: CAR would fetch 15 bits representing the Contents of the Address part of the Register, while CDR would fetch the Contents of the Decrement part of the Register.
65 https://en.wikipedia.org/wiki/Lisp_
67 https://en.wikipedia.org/wiki/IBM_704
66 Lisp is still very much alive, and one of the most interesting and exciting programming languages in use today is Clojure, a Lisp dialect that runs on the JVM, along with its sibling ClojureScript, Clojure that transpiles to JavaScript.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 66 | Lisp was one of the very first high-level languages, the very first implementation was written for the IBM 704 |
| 67 | computer. (The very first FORTRAN implementation was also written for the 704). The 704 had a 36-bit word, meaning that it was very fast to store and retrieve 36-bit values. The CPU's instruction set featured two important macros: CAR would fetch 15 bits representing the Contents of the Address part of the Register, while CDR would fetch the Contents of the Decrement part of the Register. |
| 65 | https://en.wikipedia.org/wiki/Lisp_ |
| 67 | https://en.wikipedia.org/wiki/IBM_704 |
| 66 | Lisp is still very much alive, and one of the most interesting and exciting programming languages in use today is Clojure, a Lisp dialect that runs on the JVM, along with its sibling ClojureScript, Clojure that transpiles to JavaScript. |

</details>
