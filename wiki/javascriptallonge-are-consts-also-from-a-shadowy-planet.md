---
page_id: javascriptallonge-are-consts-also-from-a-shadowy-planet
page_kind: concept
summary: are consts also from a shadowy planet?: 13 accepted assertion(s) and 11 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_14b9124315d0ad37@e0be1c15090ba959d6c584d9a8d10c7a
---

# are consts also from a shadowy planet?

Source: [[javascriptallonge]]

## Statements

- Parameters are declared when we create functions, so it makes sense that parameters are bound to environments created when we invoke functions. (javascriptallonge.pdf p.57)
- We just saw that values bound with const use lexical scope, just like values bound with parameters. (javascriptallonge.pdf p.57)
- They are looked up in the environment where they are declared. (javascriptallonge.pdf p.57)
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. (javascriptallonge.pdf p.57)
- But instead of binding two different variables to the same name in two different places, we'll bind two different values to the same name, but one environment will be completely enclosed by the other. (javascriptallonge.pdf p.57)
- And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. (javascriptallonge.pdf p.58)
- This is a book, you've already scanned ahead, so you know that the answer is no , the inner binding does not overwrite the outer binding:. (javascriptallonge.pdf p.58)
- It has effect inside its own scope, but does not affect the binding in the enclosing scope. (javascriptallonge.pdf p.58)
- Parameters are only bound when we invoke a function. (javascriptallonge.pdf p.59)
- We'll need a gratuitous block. (javascriptallonge.pdf p.59)
- But const statements can appear inside blocks. (javascriptallonge.pdf p.59)
- This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. (javascriptallonge.pdf p.60)
- Typically, we want to bind our names as close to where we need them as possible. (javascriptallonge.pdf p.60)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```

<a id="atom-2"></a>
**Atom:** code block

```
((PI) =>
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)(3)
```

<a id="atom-3"></a>
**Atom:** code block

```
((PI) =>
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)(3)(2)
//=> 6.2831853
```

<a id="atom-4"></a>
**Atom:** code block

```
((PI) => {
((PI) => {})(3);
return (diameter) => diameter * PI;
})(3.14159265)
```

<a id="atom-5"></a>
**Atom:** code block

```
((PI) => {
((PI) => {})(3);
return (diameter) => diameter * PI;
})(3.14159265)(2)
//=> 6.2831853
```

<a id="atom-6"></a>
**Atom:** code block

```
((diameter) => {
const PI = 3.14159265;
(() => {
const PI = 3;
})();
return diameter * PI;
})(2)
//=> 6.2831853
```

<a id="atom-7"></a>
**Atom:** code block

```
if (true) {
// an immediately invoked block statement (IIBS)
}
Let’s try it:
((diameter) => {
const PI = 3;
if (true) {
const PI = 3.14159265;
return diameter * PI;
}
})(2)
//=> 6.2831853
((diameter) => {
const PI = 3.14159265;
if (true) {
const PI = 3;
}
return diameter * PI;
```

<a id="atom-8"></a>
**Atom:** code block

```
})(2)
//=> 6.2831853
```

<a id="atom-9"></a>
**Atom:** code block

```
((diameter) => {
const PI = 3.14159265;
if (true) {
const PI = 3;
}
return diameter * PI;
})(2)
//=> would return 6 if const had function scope
```

<a id="atom-10"></a>
**Atom:** rule

```
If const always bound its value to the name defined in the function's environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents.
```

<a id="atom-11"></a>
**Atom:** code block

```
((diameter) => {
if (true) {
const PI = 3.14159265;
}
return diameter * PI;
})(2)
//=> would return 6.2831853 if const had function scope
```
