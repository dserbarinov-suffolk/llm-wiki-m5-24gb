---
page_id: javascriptallonge-overcoming-limitations
page_kind: concept
summary: topic-concept: 7 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_8924535f6806c8f6@4983922148306392648bec5fade665ef
---

# overcoming limitations

Source: [[javascriptallonge]]

## Statements

- All left-variadic functions have one or more fixed arguments, and the rest are gathered into the leftmost argument. (javascriptallonge.pdf p.91)
- Our leftVariadic function is a decorator that turns any function into a function that gathers parameters from the left , instead of from the right. (javascriptallonge.pdf p.92)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const butLastAndLast = (...butLast, last) =>
[butLast, last];
```

<a id="atom-2"></a>
**Atom:** code block

```
const leftVariadic = (fn) => {
if (fn.length < 1) {
return fn;
}
else {
return function (...args) {
const gathered = args.slice(0, args.length - fn.length + 1),
spread
= args.slice(args.length - fn.length + 1);
return fn.apply(
this, [gathered].concat(spread)
```

<a id="atom-3"></a>
**Atom:** code block

```
);
}
}
};
const butLastAndLast = leftVariadic((butLast, last) => [butLast, last]);
butLastAndLast('why', 'hello', 'there', 'little', 'droid')
//=> [["why","hello","there","little"],"droid"]
```


## Related pages

- [[javascriptallonge-history-lesson]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-left-variadic-destructuring]] - contextualizes: source-supported topic dependency
