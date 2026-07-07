---
page_id: javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-b4311a56
page_kind: source
summary: Composing and Decomposing Data / Tail Calls (and Default Arguments): 19 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-b4311a56@7113e74f9ecce38a27b9e76a81221c16
---

# Composing and Decomposing Data / Tail Calls (and Default Arguments)

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-ea23a471]] - previous source section: Composing and Decomposing Data / Self-Similarity
- [[javascriptallonge-section-composing-and-decomposing-data-factorials-4b205fe1]] - next source section: Composing and Decomposing Data / factorials

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-99b4771a]] - broader source section: Composing and Decomposing Data
- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-converting-non-tail-calls-to-tai-22a8069d]] - narrower source section: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls
- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-tail-call-optimization-52c04968]] - narrower source section: Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization

## Statements

- The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustrating the basic principles behind using recursion to work with self-similar data structures, but they are not 'production-ready' implementations. One of the reasons they are not production-ready is that they consume memory proportional to the size of the array being folded. _(javascriptallonge.pdf (source-range-c98ab3e6-00934))_
- Let's step through its execution. First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked. first is not undefined , so it evaluates [fn(first), …mapWith(fn, rest)]. To do that, it has to evaluate fn(first) and mapWith(fn, rest) , then evaluate [fn(first), ...mapWith(fn, rest)] . _(javascriptallonge.pdf (source-range-c98ab3e6-00937))_
- Note that while evaluating mapWith(fn, rest) , JavaScript must retain the value first or fn(first) , plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result. JavaScript cannot throw first away. So we know that JavaScript is going to hang on to 1 . _(javascriptallonge.pdf (source-range-c98ab3e6-00940))_
- Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . And the same thing happens: JavaScript has to hang on to 2 (or 4 , or both, depending on the implementation), plus some housekeeping information so it remembers what to do with that value, while it calls the equivalent of mapWith((x) => x * x, [3, 4, 5]) . _(javascriptallonge.pdf (source-range-c98ab3e6-00941))_
- This keeps on happening, so that JavaScript collects the values 1 , 2 , 3 , 4 , and 5 plus housekeeping information by the time it calls mapWith((x) => x * x, []) . It can start assembling the resulting array and start discarding the information it is saving. _(javascriptallonge.pdf (source-range-c98ab3e6-00942))_
- That information is saved on a call stack , and it is quite expensive. Furthermore, doubling the length of an array will double the amount of space we need on the stack, plus double all the work required to set up and tear down the housekeeping data for each call (these are called call frames , and they include the place where the function was called, an environment, and so on). _(javascriptallonge.pdf (source-range-c98ab3e6-00943))_
- In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error. _(javascriptallonge.pdf (source-range-c98ab3e6-00944))_
- Is there a better way? Yes. In fact, there are several better ways. Making algorithms faster is a very highly studied field of computer science. The one we're going to look at here is called tail-call optimization , or 'TCO.' _(javascriptallonge.pdf (source-range-c98ab3e6-00946))_
- To do that, it has to evaluate fn(first) and mapWith(fn, rest) , then evaluate [fn(first), ...mapWith(fn, rest)] . _(javascriptallonge.pdf (source-range-c98ab3e6-00937))_
