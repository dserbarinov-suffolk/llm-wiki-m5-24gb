---
page_id: javascriptallonge-feature
page_kind: concept
summary: Feature: 4 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-feature@78746a54fcba9990a225746ac22be0dd
---

# Feature

What [[javascriptallonge]] covers about feature:

## Statements

### A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

- ECMAScript 2015 (formerly called ECMAScript 6 or 'ES6'), is ushering in a very large number of improvements to the way programmers can write small, powerful components and combine them into larger, fully featured programs. Features like destructuring, block-structured variables, iterables, generators, and the class keyword are poised to make JavaScript programming more expressive. _(javascriptallonge.pdf (source-range-0e12e052-00023))_

- Working around the missing features was a necessary evil. _(javascriptallonge.pdf (source-range-0e12e052-00035))_

- And presto, rest collects the rest of the arguments without a lot of malarky involving slicing arguments . Not having to work around these kinds of missing features makes JavaScript Allongé a better book , because it can focus on the why to do something and when to do it, instead of on the how to make it work _(javascriptallonge.pdf (source-range-0e12e052-00040))_

### A Pull of the Lever: Prefaces / Foreword to the 'Six' edition

- A larger upgrade would substantially improve JavaScript, but without being as radical as ECMAScript 4. This upgrade became ECMAScript 6 (some features that were initially discussed will show up later, in upcoming ECMAScript versions). _(javascriptallonge.pdf (source-range-0e12e052-00073))_


## Technical atoms

### Technical frame 1: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00038))_

> And i is scoped to the for loop. We can also write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00037))_

```
for (let i = 0; i < array.length; ++i) {
// ...
}
```

### Technical frame 2: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00040))_

> And presto, rest collects the rest of the arguments without a lot of malarky involving slicing arguments . Not having to work around these kinds of missing features makes JavaScript Allongé a better book , because it can focus on the why to do something and when to do it, instead of on the how to make it work

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00039))_

```
function foo (first, ...rest) {
// ...
}
```

### Technical frame 3: ECMAScript 6 has three major groups of features:

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00081))_

> With ECMAScript 6, JavaScript has become much larger as a language. JavaScript Allongé, the 'Six' Edition is both a comprehensive tour of its features and a rich collection of techniques for making better use of them. You will learn much about functional programming and object-oriented programming. And you'll do so via ES6 code, handed to you in small, easily digestible pieces.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00083))_

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

### Technical frame 4: ECMAScript 6 has three major groups of features: / Forewords to the First Edition / matthew knox

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00093))_

```text
matthew knox
A different kind of language requires a different kind of book.
JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor strictly dynamic, and it supports procedural, object-oriented (in several flavors!), and functional programming. Many books try to hide most of those capabilities away, giving you recipes for writing JavaScript in a way that approximates class-centric programming in other languages. Not JavaScript Allongé. It starts with the fundamentals of values, functions, and objects, and then guides you through JavaScript from the inside with exploratory bits of code that illustrate scoping, combinators, context, state, prototypes, and constructors.
5 http://www.fogus.me
Like JavaScript itself, this book gives you a gentle start before showing you its full depth, and like a Cafe Allongé, it's over too soon. Enjoy!
-Matthew Knox, mattknox.com 6
6 http://mattknox.com
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 5 | http://www.fogus.me Like JavaScript itself, this book gives you a gentle start before showing you its full depth, and like a Cafe Allongé, it's over too soon. Enjoy! -Matthew Knox, mattknox.com 6 |
| 6 | http://mattknox.com |

</details>


## Related pages

- [[javascriptallonge-ecmascript]] - shared statements and technical atoms: Ecmascript shares source evidence from A Pull of the Lever: Prefaces / Foreword to the 'Six' edition: A larger upgrade would substantially improve JavaScript, but without being as radical as ECMAScript 4. This upgrade became ECMAScript 6 (some features that were init ... [truncated]; Ecmascript shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: for (let i = 0; i < array.length; ++i) { // ... } (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-javascript-allong]] - shared statements and technical atoms: About JavaScript Allongé shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: ECMAScript 2015 (formerly called ECMAScript 6 or 'ES6'), is ushering in a very large number of improvements to the way programmers can write small, powerful componen ... [truncated]; About JavaScript Allongé shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: for (let i = 0; i < array.length; ++i) { // ... } (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: for (let i = 0; i < array.length; ++i) { // ... } (4 shared atom(s))
- [[javascriptallonge-allong]] - shared technical atoms: Allong shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: function foo (first, ...rest) { // ... } (3 shared atom(s))
- [[javascriptallonge-edition]] - shared technical atoms: Edition shares technical record from ECMAScript 6 has three major groups of features:: 2 http://www.2ality.com 4 http://exploringjs.com 3 http://ecmanauten.de (2 shared atom(s))
- [[javascriptallonge-functional]] - shared technical atoms: Functional shares technical record from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / matthew knox: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms: Object shares technical record from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / matthew knox: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-programming]] - shared technical atoms: Programming shares technical record from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / matthew knox: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-recipe]] - shared technical atoms: Recipe shares technical record from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / matthew knox: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
