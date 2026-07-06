---
page_id: javascriptallonge-section-and-also-combinators-and-function-decorators-combinators-21ded55c
page_kind: source
summary: And also: / Combinators and Function Decorators / combinators: 7 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-combinators-and-function-decorators-combinators-21ded55c@d1ba4a81abe22df97d17d67e0cb05774
---

# And also: / Combinators and Function Decorators / combinators

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-and-also-combinators-and-function-decorators-higher-order-functions-b21997ec]] - previous source section: And also: / Combinators and Function Decorators / higher-order functions
- [[javascriptallonge-section-and-also-combinators-and-function-decorators-a-balanced-statement-about-combinators-3591f357]] - next source section: And also: / Combinators and Function Decorators / a balanced statement about combinators

### Source structure

- [[javascriptallonge-section-and-also-combinators-and-function-decorators-f08ca983]] - broader source section: And also: / Combinators and Function Decorators

### Topics

- [[javascriptallonge-combinator]] - topic hub: opens the topic page for Combinator

## Statements

- In this book, we will be using a looser definition of 'combinator:' Higher-order pure functions that take only functions as arguments and return a function. We won't be strict about using only previously defined combinators in their construction. _(javascriptallonge.pdf (source-range-c98ab3e6-00558))_
- This is, of course, just one example of many. You'll find lots more perusing the recipes in this book. While some programmers believe 'There Should Only Be One Way To Do It,' having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously. _(javascriptallonge.pdf (source-range-c98ab3e6-00561))_
- We won't be strict about using only previously defined combinators in their construction. _(javascriptallonge.pdf (source-range-c98ab3e6-00558))_
- While some programmers believe 'There Should Only Be One Way To Do It,' having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously. _(javascriptallonge.pdf (source-range-c98ab3e6-00561))_

## Technical atoms

### Technical frame 1: And also: / Combinators and Function Decorators / combinators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00558))_

> In this book, we will be using a looser definition of 'combinator:' Higher-order pure functions that take only functions as arguments and return a function. We won't be strict about using only previously defined combinators in their construction.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00557))_

<a id="atom-technical-atom-34eed5cf99dd08a1"></a>
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

### Technical frame 2: And also: / Combinators and Function Decorators / combinators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00561))_

> This is, of course, just one example of many. You'll find lots more perusing the recipes in this book. While some programmers believe 'There Should Only Be One Way To Do It,' having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00560))_

<a id="atom-technical-atom-be90997af459ed38"></a>
```
const compose = (a, b) =>
(c) => a(b(c))
Let’s say we have:
const addOne = (number) => number + 1;
const doubleOf = (number) => number * 2;
With compose, anywhere you would write
const doubleOfAddOne = (number) => doubleOf(addOne(number));
You could also write:
const doubleOfAddOne = compose(doubleOf, addOne);
```
