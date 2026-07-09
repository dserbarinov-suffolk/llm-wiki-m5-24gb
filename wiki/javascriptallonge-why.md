---
page_id: javascriptallonge-why
page_kind: concept
summary: topic-concept: 10 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_a73a2afe6fe6df63@4650be390d96467ef50ef924582d19bb
---

# Why?

Source: [[javascriptallonge]]

## Statements

- It enables you to make recursive functions without needing to bind a function to a name in an environment. (javascriptallonge.pdf p.201)
- This has little practical utility in JavaScript, but in combinatory logic it's essential: With fixed-point combinators it's possible to compute everything computable without binding names. (javascriptallonge.pdf p.201)
- Well, besides all of the practical applications that combinators provide , there is this little thing called The joy of working things out. (javascriptallonge.pdf p.201)
- There are many explanations of the Y Combinator's mechanism on the internet, but resist the temptation to read any of them: Work it out for yourself. (javascriptallonge.pdf p.201)
- One tip is to use JavaScript to name things. (javascriptallonge.pdf p.201)
- Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. (javascriptallonge.pdf p.201)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
This is the canonical Y Combinator86:
const Y = (f) =>
( x => f(v => x(x)(v)) )(
x => f(v => x(x)(v))
);
You use it like this:
const factorial = Y(function (fac) {
return function (n) {
return (n == 0 ? 1 : n * fac(n - 1));
```

<a id="atom-2"></a>
**Atom:** code block

```
return function (n) {
return (n == 0 ? 1
}
});
factorial(5)
//=> 120
```

<a id="atom-3"></a>
**Atom:** code block

```
const Y = (f) => {
const something = x => f(v => x(x)(v));
return something(something);
};
```


## Related pages

- [[javascriptallonge-mapwith]] - contextualizes: source-supported topic dependency
