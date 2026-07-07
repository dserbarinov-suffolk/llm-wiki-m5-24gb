---
page_id: javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-tail-call-optimization-52c04968
page_kind: source
summary: Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization: 18 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-tail-call-optimization-52c04968@90ce41e6fad17dee6081692a79e577df
---

# Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-converting-non-tail-calls-to-tai-22a8069d]] - next source section: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-b4311a56]] - broader source section: Composing and Decomposing Data / Tail Calls (and Default Arguments)

### Recipes

- [[javascriptallonge-recipe-tail-call-optimization]] - recipe pattern: tail-call optimization

## Statements

- A'tail-call' occurs when a function's last act is to invoke another function, and then return whatever the other function returns. For example, consider the maybe function decorator: _(javascriptallonge.pdf (source-range-c98ab3e6-00948))_
- There are three places it returns. The first two don't return anything, they don't matter. But the third is fn.apply(this, args) . This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. It isn't going to do any more work, so it can throw its existing stack frame away. _(javascriptallonge.pdf (source-range-c98ab3e6-00950))_
- And in fact, it does exactly that: It throws the stack frame away, and does not consume extra memory when making a maybe -wrapped call. This is a very important characteristic of JavaScript: If a function makes a call in tail position, JavaScript optimizes away the function call overhead and stack space. _(javascriptallonge.pdf (source-range-c98ab3e6-00951))_
- That is excellent, but one wrapping is not a big deal. When would we really care? Consider this implementation of length : _(javascriptallonge.pdf (source-range-c98ab3e6-00952))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) . _(javascriptallonge.pdf (source-range-c98ab3e6-00954))_
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length , the other happens after the recursive call. _(javascriptallonge.pdf (source-range-c98ab3e6-00955))_
- A'tail-call' occurs when a function's last act is to invoke another function, and then return whatever the other function returns. _(javascriptallonge.pdf (source-range-c98ab3e6-00948))_
- This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. _(javascriptallonge.pdf (source-range-c98ab3e6-00950))_
- This is a tail-call, because it invokes another function and returns its result. _(javascriptallonge.pdf (source-range-c98ab3e6-00950))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) . _(javascriptallonge.pdf (source-range-c98ab3e6-00954))_
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length , the other happens after the recursive call. _(javascriptallonge.pdf (source-range-c98ab3e6-00955))_
