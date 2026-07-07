---
page_id: javascriptallonge-feature
page_kind: concept
summary: Feature: 4 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-feature@b2d1381b633036544569b53547886de3
---

# Feature

What [[javascriptallonge]] covers about feature:

## Statements

### why the 'six' edition?

- ECMAScript 2015 (formerly called ECMAScript 6 or 'ES6'), is ushering in a very large number of improvements to the way programmers can write small, powerful components and combine them into larger, fully featured programs. Features like destructuring, block-structured variables, iterables, generators, and the class keyword are poised to make JavaScript programming more expressive. _(javascriptallonge.pdf (source-range-c98ab3e6-00021))_

- Working around the missing features was a necessary evil. _(javascriptallonge.pdf (source-range-c98ab3e6-00033))_

- And presto, rest collects the rest of the arguments without a lot of malarky involving slicing arguments . Not having to work around these kinds of missing features makes JavaScript Allongé a better book , because it can focus on the why to do something and when to do it, instead of on the how to make it work _(javascriptallonge.pdf (source-range-c98ab3e6-00038))_

### Foreword to the 'Six' edition

- A larger upgrade would substantially improve JavaScript, but without being as radical as ECMAScript 4. This upgrade became ECMAScript 6 (some features that were initially discussed will show up later, in upcoming ECMAScript versions). _(javascriptallonge.pdf (source-range-c98ab3e6-00070))_


## Technical atoms

### Technical frame 1: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00036))_

> And i is scoped to the for loop. We can also write:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00035))_

<a id="atom-technical-atom-339e65417e2add1c"></a>
```
for (let i = 0; i < array.length; ++i) {
// ...
}
```

### Technical frame 2: why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00038))_

> And presto, rest collects the rest of the arguments without a lot of malarky involving slicing arguments . Not having to work around these kinds of missing features makes JavaScript Allongé a better book , because it can focus on the why to do something and when to do it, instead of on the how to make it work

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00037))_

<a id="atom-technical-atom-ad49ef49c0ac5fcf"></a>
```
function foo (first, ...rest) {
// ...
}
```

### Technical frame 3: ECMAScript 6 has three major groups of features:

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00078))_

> With ECMAScript 6, JavaScript has become much larger as a language. JavaScript Allongé, the 'Six' Edition is both a comprehensive tour of its features and a rich collection of techniques for making better use of them. You will learn much about functional programming and object-oriented programming. And you'll do so via ES6 code, handed to you in small, easily digestible pieces.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00080))_

<a id="atom-technical-atom-24432d50b19465df"></a>
```text
2 http://www.2ality.com
4 http://exploringjs.com
3 http://ecmanauten.de
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 2 | http://www.2ality.com |
| 4 | http://exploringjs.com |
| 3 | http://ecmanauten.de |

</details>


## Related pages

### Shared technical atoms

- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from why the 'six' edition?: for (let i = 0; i < array.length; ++i) { // ... } (3 shared atom(s))
- [[javascriptallonge-ecmascript]] - shared statements and technical atoms: Ecmascript shares source evidence from Foreword to the 'Six' edition: A larger upgrade would substantially improve JavaScript, but without being as radical as ECMAScript 4. This upgrade became ECMAScript 6 (some features that were init ... [truncated]; Ecmascript shares technical record from why the 'six' edition?: for (let i = 0; i < array.length; ++i) { // ... } (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-allong]] - shared technical atoms: Allong shares technical record from why the 'six' edition?: function foo (first, ...rest) { // ... } (2 shared atom(s))
- [[javascriptallonge-edition]] - shared technical atoms: Edition shares technical record from ECMAScript 6 has three major groups of features:: 2 http://www.2ality.com 4 http://exploringjs.com 3 http://ecmanauten.de (1 shared atom(s))

### Shared claims

- [[javascriptallonge-javascript-allong]] - shared statements: About JavaScript Allongé shares source evidence from why the 'six' edition?: And presto, rest collects the rest of the arguments without a lot of malarky involving slicing arguments . Not having to work around these kinds of missing features ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
