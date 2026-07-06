---
page_id: javascriptallonge-section-copy-on-write-making-data-out-of-functions-the-kestrel-and-the-idiot-b97adf2c
page_kind: source
summary: Copy on Write / Making Data Out Of Functions / the kestrel and the idiot: 14 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-write-making-data-out-of-functions-the-kestrel-and-the-idiot-b97adf2c@9ba52b6eaa6aa59edadc937e78318135
---

# Copy on Write / Making Data Out Of Functions / the kestrel and the idiot

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-copy-on-write-making-data-out-of-functions-backwardness-2a64703a]] - next source section: Copy on Write / Making Data Out Of Functions / backwardness

### Source structure

- [[javascriptallonge-section-copy-on-write-making-data-out-of-functions-bbf4cfc0]] - broader source section: Copy on Write / Making Data Out Of Functions

## Statements

- A constant function is a function that always returns the same thing, no matter what you give it. For example, (x) => 42 is a constant function that always evaluates to 42. The kestrel, or K , is a function that makes constant functions. You give it a value, and it returns a constant function that gives that value. _(javascriptallonge.pdf (source-range-c98ab3e6-01333))_
- The identity function is a function that evaluates to whatever parameter you pass it. So I(42) => 42 . Very simple, but useful. Now we'll take it one more step forward: Passing a value to K gets a function back, and passing a value to that function gets us a value. _(javascriptallonge.pdf (source-range-c98ab3e6-01336))_
- This is very interesting. Given two values, we can say that K always returns the first value: K(x)(y) => x (that's not valid JavaScript, but it's essentially how it works). _(javascriptallonge.pdf (source-range-c98ab3e6-01339))_
- This is very interesting. Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value. _(javascriptallonge.pdf (source-range-c98ab3e6-01347))_
- For example, (x) => 42 is a constant function that always evaluates to 42. _(javascriptallonge.pdf (source-range-c98ab3e6-01333))_
