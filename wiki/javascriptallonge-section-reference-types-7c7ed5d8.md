---
page_id: javascriptallonge-section-reference-types-7c7ed5d8
page_kind: source
summary: reference types: 8 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-reference-types-7c7ed5d8@8dba09e8f293ae7fe3e9a984e4449074
---

# reference types

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-value-types-67ccb447]] - previous source section: value types
- [[javascriptallonge-section-a-rich-aroma-basic-numbers-7443c717]] - next source section: A Rich Aroma: Basic Numbers

## Statements

- An array looks like this: [1, 2, 3] . This is an expression, and you can combine [] with other expressions. Go wild with things like: _(javascriptallonge.pdf (source-range-c98ab3e6-00129))_
- Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of 42 is identical to every other value of 42 ? Try these for yourself: _(javascriptallonge.pdf (source-range-c98ab3e6-00131))_
- How about that! When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own unique array that is not identical to any other array, even if that other array also looks like [1, 2, 3] . It's as if JavaScript is generating new cups of coffee with serial numbers on the bottom. _(javascriptallonge.pdf (source-range-c98ab3e6-00133))_
- They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to create an array, you're creating a new, distinct value even if it appears to be the same as some other array value. As we'll see, this is true of many other kinds of values, including functions , the main subject of this book. _(javascriptallonge.pdf (source-range-c98ab3e6-00134))_
