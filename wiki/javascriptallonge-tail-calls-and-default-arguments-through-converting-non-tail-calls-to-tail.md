---
page_id: javascriptallonge-tail-calls-and-default-arguments-through-converting-non-tail-calls-to-tail
page_kind: source
summary: Tail Calls (and Default Arguments) through converting non-tail-calls to tail-calls from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.117-118, raw/javascriptallonge.pdf p.119-119, raw/javascriptallonge.pdf p.120-121
updated: 2026-06-20
domain: javascriptallonge
category_path: source-sections
source_id: javascriptallonge.pdf
---

## Source record

Source record for [[javascriptallonge-tail-calls-and-default-arguments-through-converting-non-tail-calls-to-tail]]. (raw/javascriptallonge.pdf)

## Key supported claims

- Tail calls occur when a function's last act is to invoke another function and return its result, enabling stack frame optimization. (raw/javascriptallonge.pdf)
- Non-tail calls, like in the length function, incur memory overhead due to the need to retain intermediate values. (raw/javascriptallonge.pdf)
- By converting non-tail calls to tail calls, memory and performance overhead can be avoided when working with large arrays. (raw/javascriptallonge.pdf)
- Recursive functions like mapWith can consume memory proportional to the array size due to the need to retain intermediate results. (raw/javascriptallonge.pdf)
