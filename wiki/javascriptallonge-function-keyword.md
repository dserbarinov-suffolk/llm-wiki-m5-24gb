---
page_id: javascriptallonge-function-keyword
page_kind: concept
summary: topic-concept: 26 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_eedd1d29548876ba@187b3fd86c82043fcdb65938c05bb201
---

# the function keyword

Source: [[javascriptallonge]]

## Procedure

- JavaScript does have a syntax for naming a function, we use the function keyword. (javascriptallonge.pdf p.62)
- Until ECMAScript 2015 was created, function was the usual syntax for writing functions. (javascriptallonge.pdf p.62)
- Something else we're about to discuss is optional. (javascriptallonge.pdf p.62)
- We have arguments in parentheses, just like fat arrow functions. (javascriptallonge.pdf p.62)
- We do not have a fat arrow, we go directly to the body. (javascriptallonge.pdf p.62)
- This means that if we want our functions to return a value, we always need to use the return keyword. (javascriptallonge.pdf p.62)
- In this expression, double is the name in the environment, but repeat is the function's actual name. (javascriptallonge.pdf p.63)
- While the name of the function is a property of the function, not of the environment. (javascriptallonge.pdf p.63)
- That may seem confusing, but think of the binding names as properties of the environment, not of the function. (javascriptallonge.pdf p.63)
- 33 'Yes of course?' Well, in chapter of a book dedicated to naming functions, it is not surprising that feature we mention has something to do with naming functions. (javascriptallonge.pdf p.63)
- Now, the function's actual name has no effect on the environment in which it is used. (javascriptallonge.pdf p.64)
- Here's a function that determines whether a positive integer is even or not. (javascriptallonge.pdf p.64)
- So 'actualName' isn't bound in the environment where we use the named function expression. (javascriptallonge.pdf p.64)
- Clearly, the name even is bound to the function within the function's body . (javascriptallonge.pdf p.64)
- This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere else, you needn't. (javascriptallonge.pdf p.65)
- even is bound within the function itself, but not outside it. (javascriptallonge.pdf p.65)
- There are two separate rules for these 'magic' names, one for when you invoke a function using the function keyword, and another for functions defined with 'fat arrows.' We'll begin with how things work for functions defined with the function keyword. (javascriptallonge.pdf p.74)
- The second magic name is very interesting, it's called arguments , and the most interesting thing about it is that it contains a list of arguments passed to a function:. (javascriptallonge.pdf p.74)
- The first magic name is this , and it is bound to something called the function's context. (javascriptallonge.pdf p.74)
- arguments always contains all of the arguments passed to a function, regardless of how many are declared. (javascriptallonge.pdf p.74)
- We'll see it used in many of the recipes, starting off with partial application and ellipses. (javascriptallonge.pdf p.75)
- The most common use of the arguments binding is to build functions that can take a variable number of arguments. (javascriptallonge.pdf p.75)

## Required tables and formulas

<a id="atom-1"></a>
**Atom:** table

```text
42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times.
43 We'll look at arrays and plain old javascript objects in depth later.
```


## Rules and exceptions

- That may seem confusing, but think of the binding names as properties of the environment, not of the function. (javascriptallonge.pdf p.63)
- The most common use of the arguments binding is to build functions that can take a variable number of arguments. (javascriptallonge.pdf p.75)

## Related pages

- [[javascriptallonge-function-declarations]] - contextualizes: source-supported topic dependency
