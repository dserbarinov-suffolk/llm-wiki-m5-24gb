---
page_id: javascriptallonge-section-yes-consider-this-variation-3b6cfc71
page_kind: source
summary: Yes. Consider this variation:: 16 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-yes-consider-this-variation-3b6cfc71@ce75bded5de8d0c55064296fd5d5e2a4
---

# Yes. Consider this variation:

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-reassignment-66d414a1]] - previous source section: Reassignment
- [[javascriptallonge-section-copy-on-write-5c8d94ae]] - next source section: Copy on Write

## Statements

- What went wrong? Why didn't it give us 'Hello, Raganwald, my name is Friedrich'? The answer is that pesky var i . Remember that i is bound in the surrounding environment, so it's as if we wrote: _(javascriptallonge.pdf (source-range-c98ab3e6-01208))_
- Now, at the time we created each function, i had a sensible value, like 0 , 1 , or 2 . But at the time we call one of the functions, i has the value 3 , which is why the loop terminated. So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3 . That's not what we want at all. _(javascriptallonge.pdf (source-range-c98ab3e6-01210))_
- This small error was a frequent cause of confusion, and in the days when there was no block-scoped let , programmers would need to know how to fake it, usually with an IIFE: _(javascriptallonge.pdf (source-range-c98ab3e6-01213))_
- Now we're creating a new inner parameter, i and binding it to the value of the outer i . This works, but let is so much simpler and cleaner that it was added to the language in the ECMAScript 2015 specification. _(javascriptallonge.pdf (source-range-c98ab3e6-01215))_
- In this book, we will use function declarations sparingly, and not use var at all. That does not mean that you should follow the exact same practice in your own code: The purpose of this book is to illustrate certain principles of programming. The purpose of your own code is to get things done. The two goals are often, but not always, aligned. _(javascriptallonge.pdf (source-range-c98ab3e6-01216))_
- So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3 . _(javascriptallonge.pdf (source-range-c98ab3e6-01210))_
