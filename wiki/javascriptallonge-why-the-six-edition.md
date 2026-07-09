---
page_id: javascriptallonge-why-the-six-edition
page_kind: concept
summary: topic-concept: 23 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_bd4a19e254d357ed@5d1d76b33fdf867c5cd25882ad067ff2
---

# why the 'six' edition?

Source: [[javascriptallonge]]

## Statements

- Features like destructuring, block- structured variables, iterables, generators, and the class keyword are poised to make JavaScript programming more expressive. (javascriptallonge.pdf p.7)
- ECMAScript 2015 (formerly called ECMAScript 6 or 'ES6'), is ushering in a very large number of improvements to the way programmers can write small, powerful components and combine them into larger, fully featured programs. (javascriptallonge.pdf p.7)
- For example, JavaScript did not include block-structured variables. (javascriptallonge.pdf p.7)
- Over time, programmers discovered ways to roll their own versions of important features. (javascriptallonge.pdf p.7)
- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. (javascriptallonge.pdf p.7)
- And the variable i is scoped locally to the code within the braces. (javascriptallonge.pdf p.7)
- Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write:. (javascriptallonge.pdf p.7)
- Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. (javascriptallonge.pdf p.8)
- Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like:. (javascriptallonge.pdf p.8)
- The first edition of JavaScript Allongé explained these and many other patterns for writing flexible and composable programs in JavaScript, but the intention wasn't to explain how to work around JavaScript's missing features: The intention was to explain why the style of programming exemplified by the missing features is important. (javascriptallonge.pdf p.8)
- Working around the missing features was a necessary evil. (javascriptallonge.pdf p.8)
- But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. (javascriptallonge.pdf p.8)
- And i is scoped to the for loop. (javascriptallonge.pdf p.8)
- Not having to work around these kinds of missing features makes JavaScript Allongé a better book , because it can focus on the why to do something and when to do it, instead of on the how to make it work. (javascriptallonge.pdf p.9)
- JavaScript Allongé, The 'Six' Edition packs all the goodness of JavaScript Allongé into a new, updated package that is relevant for programmers working with (or planning to work with) the latest version of JavaScript. (javascriptallonge.pdf p.9)

## Rules

- Not having to work around these kinds of missing features makes JavaScript Allongé a better book , because it can focus on the why to do something and when to do it, instead of on the how to make it work. (javascriptallonge.pdf p.9)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
for (int i = 0; i < array.length; ++i) {
// ...
}
```

<a id="atom-2"></a>
**Atom:** code block

```
var i;
for (i = 0; i < array.length; ++i) {
(function (i) {
// ...
})(i)
}
```

<a id="atom-3"></a>
**Atom:** code block

```
def foo (first, *rest)
# ...
end
```

<a id="atom-4"></a>
**Atom:** code block

```
function foo () {
var first = arguments[0],
rest
= [].slice.call(arguments, 1);
// ...
}
```

<a id="atom-5"></a>
**Atom:** code block

```
for (let i = 0; i < array.length; ++i) {
// ...
}
```

<a id="atom-6"></a>
**Atom:** code block

```
function foo (first, ...rest) {
// ...
}
```


## Related pages

- [[javascriptallonge-that-s-nice-is-that-the-only-reason]] - contextualizes: source-supported topic dependency
