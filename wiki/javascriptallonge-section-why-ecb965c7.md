---
page_id: javascriptallonge-section-why-ecb965c7
page_kind: source
summary: Why?: 10 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-why-ecb965c7@3be0b0d3a9ee5ec13cfdfc724a73fa96
---

# Why?

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-object-assign-f644e66b]] - previous source section: Object.assign
- [[javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-519b0d4d]] - next source section: A Warm Cup: Basic Strings and Quasi-Literals

## Statements

- Why? It enables you to make recursive functions without needing to bind a function to a name in an environment. This has little practical utility in JavaScript, but in combinatory logic it's essential: With fixed-point combinators it's possible to compute everything computable without binding names. _(javascriptallonge.pdf (source-range-c98ab3e6-01462))_
- So again, why include the recipe? Well, besides all of the practical applications that combinators provide, there is this little thing called The joy of working things out. _(javascriptallonge.pdf (source-range-c98ab3e6-01463))_
- There are many explanations of the Y Combinator's mechanism on the internet, but resist the temptation to read any of them: Work it out for yourself. Use it as an excuse to get familiar with your environment's debugging facility. _(javascriptallonge.pdf (source-range-c98ab3e6-01464))_
- One tip is to use JavaScript to name things. For example, you could start by writing: _(javascriptallonge.pdf (source-range-c98ab3e6-01465))_
- What is this something and how does it work? Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-c98ab3e6-01467))_
- Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-c98ab3e6-01467))_

## Technical atoms

### Technical frame 1: Why?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01462))_

> Why? It enables you to make recursive functions without needing to bind a function to a name in an environment. This has little practical utility in JavaScript, but in combinatory logic it's essential: With fixed-point combinators it's possible to compute everything computable without binding names.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01460))_

<a id="atom-technical-atom-5ec18a86e09e6108"></a>
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

### Technical frame 2: Why?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01462))_

> Why? It enables you to make recursive functions without needing to bind a function to a name in an environment. This has little practical utility in JavaScript, but in combinatory logic it's essential: With fixed-point combinators it's possible to compute everything computable without binding names.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01461))_

<a id="atom-technical-atom-daf10204b41b1c02"></a>
```
return function (n) {
return (n == 0 ? 1
}
});
factorial(5)
//=> 120
```

### Technical frame 3: Why?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01467))_

> What is this something and how does it work? Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01466))_

<a id="atom-technical-atom-6b3db8e543679bd4"></a>
```
const Y = (f) => {
const something = x => f(v => x(x)(v));
return something(something);
};
```
