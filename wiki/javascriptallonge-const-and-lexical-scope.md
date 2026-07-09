---
page_id: javascriptallonge-const-and-lexical-scope
page_kind: concept
summary: topic-concept: 17 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_0428b653ab99e33a@1b9ab8ee61294615cf6d0ca56ff405b1
---

# const and lexical scope

Source: [[javascriptallonge]]

## Statements

- This seems very straightforward, but alas, there are some semantics of binding names that we need to understand if we're to place const anywhere we like. (javascriptallonge.pdf p.55)
- It's more than a bit convoluted , but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we've elided. (javascriptallonge.pdf p.55)
- We can use any expression in there, and that expression can invoke diameter_fn . (javascriptallonge.pdf p.55)
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn . (javascriptallonge.pdf p.56)
- We can see that PI is bound in an environment surrounding (diameter) => diameter * PI , we don't need to know where diameter_fn is invoked. (javascriptallonge.pdf p.56)
- Although we have bound 3 to PI in the environment surrounding diameter_fn(2) , the value that counts is 3.14159265 , the value we bound to PI in the environment surrounding (diameter) ⇒ diameter * PI. (javascriptallonge.pdf p.56)
- That much we can carefully work out from the way closures work. (javascriptallonge.pdf p.56)
- Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. (javascriptallonge.pdf p.57)

## Rules

- We can use any expression in there, and that expression can invoke diameter_fn . (javascriptallonge.pdf p.55)
- We can see that PI is bound in an environment surrounding (diameter) => diameter * PI , we don't need to know where diameter_fn is invoked. (javascriptallonge.pdf p.56)
- That much we can carefully work out from the way closures work. (javascriptallonge.pdf p.56)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
((diameter_fn) =>
// ...
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
```

<a id="atom-2"></a>
**Atom:** code block

```
((diameter_fn) =>
diameter_fn(2)
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
//=> 6.2831853
```

<a id="atom-3"></a>
**Atom:** code block

```
((diameter_fn) =>
((PI) =>
diameter_fn(2)
)(3)
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
//=> 6.2831853
```

<a id="atom-4"></a>
**Atom:** code block

```
((diameter_fn) => {
const PI = 3;
return diameter_fn(2)
})(
(() => {
const PI = 3.14159265;
return (diameter) => diameter * PI
})()
)
//=> 6.2831853
```


## Related pages

- [[javascriptallonge-nested-blocks]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-are-consts-also-from-a-shadowy-planet]] - contextualizes: source-supported topic dependency
