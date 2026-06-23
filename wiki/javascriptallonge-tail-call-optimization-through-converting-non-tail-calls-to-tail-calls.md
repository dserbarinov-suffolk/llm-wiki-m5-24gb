---
page_id: javascriptallonge-tail-call-optimization-through-converting-non-tail-calls-to-tail-calls
page_kind: source
summary: tail-call optimization through converting non-tail-calls to tail-calls from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.119-119, raw/javascriptallonge.pdf p.120-121
updated: 2026-06-23
domain: javascriptallonge
category_path: source-sections
source_id: javascriptallonge.pdf
---

## Source record

Source record for [[javascriptallonge-tail-call-optimization-through-converting-non-tail-calls-to-tail-calls]]. (raw/javascriptallonge.pdf)

## Key supported claims

- A tail-call occurs when a function's last act is to invoke another function and return its result. (raw/javascriptallonge.pdf)
- The length function calls itself, but it is not a tail-call because it returns 1 + length(rest) instead of length(rest). (raw/javascriptallonge.pdf)
- Mapping over large arrays can avoid memory and performance overhead of non-tail-calls. (raw/javascriptallonge.pdf)
- Converting non-tail-calls to tail-calls is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization. (raw/javascriptallonge.pdf)
