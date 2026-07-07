---
page_id: javascriptallonge-section-and-also-building-blocks-fdb3fcfb
page_kind: source
summary: And also: / Building Blocks: 5 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-building-blocks-fdb3fcfb@2a54624a2adeea55e871111c18414b43
---

# And also: / Building Blocks

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-and-also-combinators-and-function-decorators-901f172c]] - previous source section: And also: / Combinators and Function Decorators
- [[javascriptallonge-section-and-also-magic-names-0c5d7af9]] - next source section: And also: / Magic Names

### Source structure

- [[javascriptallonge-section-and-also-building-blocks-composition-ed84a096]] - narrower source section: And also: / Building Blocks / composition
- [[javascriptallonge-section-and-also-building-blocks-partial-application-68c16436]] - narrower source section: And also: / Building Blocks / partial application

## Statements

- When you look at functions within functions in JavaScript, there's a bit of a 'spaghetti code' look to it. The strength of JavaScript is that you can do anything. The weakness is that you will. There are ifs, fors, returns, everything thrown higgledy piggledy together. Although you needn't restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks. _(javascriptallonge.pdf (source-range-c98ab3e6-00565))_
- When you look at functions within functions in JavaScript, there's a bit of a 'spaghetti code' look to it. _(javascriptallonge.pdf (source-range-c98ab3e6-00565))_

## Technical atoms

### Technical frame 1: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00588))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00585))_

<a id="atom-technical-atom-8f517a4c4e32b9dc"></a>
```text
39 http://underscorejs.org
41 If we don't want to sort out Underscore, we can also write the following: const map = (a, fn) => a.map(fn); , and trust that it works even though we haven't discussed methods yet.
40 Modern JavaScript implementations provide a map method for arrays, but Underscore's implementation also works with older browsers if you are working with that headache.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 39 | http://underscorejs.org |
| 41 | If we don't want to sort out Underscore, we can also write the following: const map = (a, fn) => a.map(fn);, and trust that it works even though we haven't discussed methods yet. |
| 40 | Modern JavaScript implementations provide a map method for arrays, but Underscore's implementation also works with older browsers if you are working with that headache. |

</details>
