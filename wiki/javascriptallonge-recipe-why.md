---
page_id: javascriptallonge-recipe-why
page_kind: recipe
summary: Why?: reusable source-backed pattern with 6 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: why
projection_coverage: recipe-javascriptallonge-recipe-why@0f1d2c8d8be5ce69b060386d34103d8b
---

# Why?

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-data-why-3f8e67cf]].
- Evidence roles: decision, explanation, example.

## Applicability And Rationale

- It enables you to make recursive functions without needing to bind a function to a name in an environment. _(javascriptallonge.pdf (source-range-0e12e052-01484))_
- This has little practical utility in JavaScript, but in combinatory logic it's essential: With fixed-point combinators it's possible to compute everything computable without binding names. _(javascriptallonge.pdf (source-range-0e12e052-01484))_
- Well, besides all of the practical applications that combinators provide, there is this little thing called The joy of working things out. _(javascriptallonge.pdf (source-range-0e12e052-01485))_
- There are many explanations of the Y Combinator's mechanism on the internet, but resist the temptation to read any of them: Work it out for yourself. _(javascriptallonge.pdf (source-range-0e12e052-01486))_
- One tip is to use JavaScript to name things. _(javascriptallonge.pdf (source-range-0e12e052-01487))_
- Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-0e12e052-01489))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01482)_

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

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01483)_

```
return function (n) {
return (n == 0 ? 1
}
});
factorial(5)
//=> 120
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01488)_

```
const Y = (f) => {
const something = x => f(v => x(x)(v));
return something(something);
};
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-data-why-3f8e67cf]]
