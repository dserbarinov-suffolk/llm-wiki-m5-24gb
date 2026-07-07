---
page_id: javascriptallonge-section-and-also-combinators-and-function-decorators-901f172c
page_kind: source
summary: And also: / Combinators and Function Decorators: 2 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-combinators-and-function-decorators-901f172c@5cb63265a5ed29faef956b6d7d96fca0
---

# And also: / Combinators and Function Decorators

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-and-also-naming-functions-c49aef83]] - previous source section: And also: / Naming Functions
- [[javascriptallonge-section-and-also-building-blocks-fdb3fcfb]] - next source section: And also: / Building Blocks

### Source structure

- [[javascriptallonge-section-and-also-combinators-and-function-decorators-combinators-96e491bc]] - narrower source section: And also: / Combinators and Function Decorators / combinators
- [[javascriptallonge-section-and-also-combinators-and-function-decorators-function-decorators-9d6990ae]] - narrower source section: And also: / Combinators and Function Decorators / function decorators
- [[javascriptallonge-section-and-also-combinators-and-function-decorators-higher-order-functions-c07c644e]] - narrower source section: And also: / Combinators and Function Decorators / higher-order functions

## Statements by subsection

### And also: / Combinators and Function Decorators / a balanced statement about combinators

- Code that uses a lot of combinators tends to name the verbs and adverbs (like doubleOf , addOne , and compose ) while avoiding language keywords and the names of nouns (like number ). So one perspective is that combinators are useful when you want to emphasize what you're doing and how it fits together, and more explicit code is useful when you want to emphasize what you're working with. _(javascriptallonge.pdf (source-range-c98ab3e6-00553))_

## Technical atoms

### Technical frame 1: And also: / Combinators and Function Decorators / combinators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00548))_

> In this book, we will be using a looser definition of 'combinator:' Higher-order pure functions that take only functions as arguments and return a function. We won't be strict about using only previously defined combinators in their construction.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00547))_

<a id="atom-technical-atom-2dd842e1a4d4096e"></a>
```text
combinators
The word 'combinator' has a precise technical meaning in mathematics:
'A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.'-Wikipedia 35
If we were learning Combinatorial Logic, we'd start with the most basic combinators like S , K , and I , and work up from there to practical combinators. We'd learn that the fundamental combinators are named after birds following the example of Raymond Smullyan's famous book To Mock a Mockingbird 36 .
35 https://en.wikipedia.org/wiki/Combinatory_logic
36 http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 35 | https://en.wikipedia.org/wiki/Combinatory_logic |
| 36 | http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20 |

</details>

### Technical frame 2: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00563))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00555))_

<a id="atom-technical-atom-73d86f3bb2def087"></a>
```text
function decorators
A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. Here's a ridiculously simple decorator: 38
37 As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context.
38 We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args)
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 37 | As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. |
| 38 | We'll see later why an even more useful version would be written (fn) => (...args) =>!fn(...args) |

</details>
