---
page_id: javascriptallonge-mapping
page_kind: concept
summary: topic-concept: 10 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_4e5e5498a1f2c9ce@f8131f961736f03f1b3da3cbef9b03c0
---

# mapping

Source: [[javascriptallonge]]

## Statements

- Another common problem is applying a function to every element of an array. (javascriptallonge.pdf p.113)
- This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again. (javascriptallonge.pdf p.114)
- Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution. (javascriptallonge.pdf p.114)

## Rules

- Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution. (javascriptallonge.pdf p.114)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const squareAll = ([first, ...rest]) => first === undefined
? []
: [first * first, ...squareAll(rest)\
];
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

<a id="atom-2"></a>
**Atom:** code block

```
const truthyAll = ([first, ...rest]) => first === undefined
? []
: [!!first, ...truthyAll(rest)];
truthyAll([null, true, 25, false, "foo"])
//=> [false,true,true,false,true]
```

<a id="atom-3"></a>
**Atom:** code block

```
const mapWith = (fn, array) => // ...
```

<a id="atom-4"></a>
**Atom:** code block

```
const mapWith = (fn, [first, ...rest]) =>
first === undefined
? []
: [fn(first), ...mapWith(fn, rest)];
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
mapWith((x) => !!x, [null, true, 25, false, "foo"])
//=> [false,true,true,false,true]
```


## Related pages

- [[javascriptallonge-linear-recursion]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-folding]] - contextualizes: source-supported topic dependency
