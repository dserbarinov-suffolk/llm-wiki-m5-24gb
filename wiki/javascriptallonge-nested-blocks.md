---
page_id: javascriptallonge-nested-blocks
page_kind: concept
summary: topic-concept: 12 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_8cbcda443d94c70c@1991f2aaf3374ca4488e998c7b46f357
---

# nested blocks

Source: [[javascriptallonge]]

## Statements

- Up to now, we've only ever seen blocks we use as the body of functions. (javascriptallonge.pdf p.54)
- But there are other kinds of blocks. (javascriptallonge.pdf p.54)
- The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. (javascriptallonge.pdf p.54)
- We've used a block as the else clause, and since it's a block, we've placed a const statement inside it. (javascriptallonge.pdf p.55)

## Technical atoms

<a id="atom-1"></a>
**Atom:** rule

```
One of the places you can find blocks is in an if statement.
```

<a id="atom-2"></a>
**Atom:** code block

```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else
return !even(x - 1);
}
return even(n)
}
```

<a id="atom-3"></a>
**Atom:** code block

```
((n) => {
const even = (x) => {
if (x === 0)
return true;
else
return !even(x - 1);
}
return even(n)
})(13)
//=> false
```

<a id="atom-4"></a>
**Atom:** code block

```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else {
const odd = (y) => !even(y);
return odd(x - 1);
}
```

<a id="atom-5"></a>
**Atom:** code block

```
}
return even(n)
}
And this also works:
((n) => {
const even = (x) => {
if (x === 0)
return true;
else {
const odd = (y) => !even(y);
return odd(x - 1);
}
}
return even(n)
})(42)
```

<a id="atom-6"></a>
**Atom:** code block

```
//=> true
```


## Related pages

- [[javascriptallonge-const]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-const-and-lexical-scope]] - contextualizes: source-supported topic dependency
