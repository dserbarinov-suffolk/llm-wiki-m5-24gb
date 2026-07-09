---
page_id: javascriptallonge-function-declarations
page_kind: concept
summary: topic-concept: 16 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_d378ab294c1078ed@0b4c45af3869f899778c47d6cf943be7
---

# function declarations

Source: [[javascriptallonge]]

## Statements

- There is another syntax for naming and/or defining a function. (javascriptallonge.pdf p.65)
- In that it binds a name in the environment to a named function. (javascriptallonge.pdf p.65)
- First, function declarations are hoisted to the top of the function in which they occur. (javascriptallonge.pdf p.65)
- However, there are two important differences. (javascriptallonge.pdf p.65)
- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. (javascriptallonge.pdf p.65)
- The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). (javascriptallonge.pdf p.66)
- This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. (javascriptallonge.pdf p.66)
- It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code. (javascriptallonge.pdf p.66)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
function someName () {
// ...
}
This behaves a little like:
const someName = function someName ()
// ...
}
```

<a id="atom-2"></a>
**Atom:** code block

```
{
```

<a id="atom-3"></a>
**Atom:** example

```
Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const :
```

<a id="atom-4"></a>
**Atom:** code block

```
(function () {
return fizzbuzz();
const fizzbuzz = function fizzbuzz () {
return "Fizz" + "Buzz";
}
})()
//=> undefined is not a function (evaluating 'fizzbuzz()')
```

<a id="atom-5"></a>
**Atom:** code block

```
(function () {
return fizzbuzz();
function fizzbuzz () {
return "Fizz" + "Buzz";
}
})()
//=> 'FizzBuzz'
Although fizzbuzz is declared later in the function, JavaScript behaves as if we’d written:
(function () {
const fizzbuzz = function fizzbuzz () {
```

<a id="atom-6"></a>
**Atom:** code block

```
const fizzbuzz = function fizzbuzz ()
return "Fizz" + "Buzz";
}
return fizzbuzz();
})()
```


## Related pages

- [[javascriptallonge-function-keyword]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-function-declaration-caveats-34]] - contextualizes: source-supported topic dependency
