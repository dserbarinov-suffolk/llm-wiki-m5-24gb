---
page_id: javascriptallonge-reference-types
page_kind: concept
summary: topic-concept: 10 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_58bff99adfc9c2c6@48a6c4ff60e42b62b8e24d508e113c25
---

# reference types

Source: [[javascriptallonge]]

## Statements

- This is an expression, and you can combine [] with other expressions. (javascriptallonge.pdf p.23)
- Notice that you are always generating arrays with the same contents. (javascriptallonge.pdf p.23)
- When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own unique array that is not identical to any other array, even if that other array also looks like [1, 2, 3] . (javascriptallonge.pdf p.23)
- Every time you evaluate an expression (including typing something in) to create an array, you're creating a new, distinct value even if it appears to be the same as some other array value. (javascriptallonge.pdf p.23)
- As we'll see, this is true of many other kinds of values, including functions , the main subject of this book. (javascriptallonge.pdf p.23)
- They look the same, but if you examine them with === , you see that they are different. (javascriptallonge.pdf p.23)

## Rules

- This is an expression, and you can combine [] with other expressions. (javascriptallonge.pdf p.23)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
[2-1, 2, 2+1]
[1, 1+1, 1+1+1]
```

<a id="atom-2"></a>
**Atom:** code block

```
[2-1, 2, 2+1] === [1,2,3]
[1,2,3] === [1, 2, 3]
[1, 2, 3] === [1, 2, 3]
```


## Related pages

- [[javascriptallonge-value-types]] - contextualizes: source-supported topic dependency
