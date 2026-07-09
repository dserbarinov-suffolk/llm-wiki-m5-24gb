---
page_id: javascriptallonge-garbage-garbage-everywhere
page_kind: concept
summary: Garbage, Garbage Everywhere: 12 accepted assertion(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_28efab9fc56ea941@c9a4c13f15808f460c3bde5c5b1675bb
---

# Garbage, Garbage Everywhere

Source: [[javascriptallonge]]

## Statements

- We have now seen how to use Tail Calls to execute mapWith in constant space:. (javascriptallonge.pdf p.126)
- The right tool to discover why it's still slow is a memory profiler, but a simple inspection of the program will reveal the following:. (javascriptallonge.pdf p.126)
- But when we try it on very large arrays, we discover that it is still very slow. (javascriptallonge.pdf p.126)
- To do that, we take the array in prepend and push fn(first) onto the end, creating a new array that will be passed to the next invocation of mapWith . (javascriptallonge.pdf p.126)
- The array we had in prepend is no longer used. (javascriptallonge.pdf p.127)
- In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. (javascriptallonge.pdf p.127)
- Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend . (javascriptallonge.pdf p.127)
- Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another. (javascriptallonge.pdf p.127)
- We may not be creating 3,000 stack frames, but we are creating three thousand new arrays and copying elements into each and every one of them. (javascriptallonge.pdf p.127)
- Key Point : Our [first, ..rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded. (javascriptallonge.pdf p.127)
- 64 It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. (javascriptallonge.pdf p.127)
- But this is not how JavaScript's built-in arrays work. (javascriptallonge.pdf p.127)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const mapWith = (fn, [first, ...rest], prepend = []) =>
first === undefined
? prepend
: mapWith(fn, rest, [...prepend, fn(first)]);
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```
