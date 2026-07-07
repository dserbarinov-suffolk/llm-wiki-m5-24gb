---
page_id: javascriptallonge-recipe-function-declarations
page_kind: recipe
summary: function declarations: reusable source-backed pattern with 8 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: function-declarations
projection_coverage: recipe-javascriptallonge-recipe-function-declarations@d64d11ad1300ab8c26f604030a1ec327
---

# function declarations

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-function-declarations-c6aff434]].
- Evidence roles: decision, explanation, example.

## Applicability And Rationale

- There is another syntax for naming and/or defining a function. _(javascriptallonge.pdf (source-range-c98ab3e6-00522))_
- In that it binds a name in the environment to a named function. _(javascriptallonge.pdf (source-range-c98ab3e6-00525))_
- First, function declarations are hoisted to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-c98ab3e6-00525))_
- However, there are two important differences. _(javascriptallonge.pdf (source-range-c98ab3e6-00525))_
- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. _(javascriptallonge.pdf (source-range-c98ab3e6-00528))_
- The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). _(javascriptallonge.pdf (source-range-c98ab3e6-00531))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00523)_

```
function someName () {
// ...
}
This behaves a little like:
const someName = function someName ()
// ...
}
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00524)_

```
{
```

### Atom 3: `worked-example`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00526)_

```
Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const :
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00527)_

```
(function () {
return fizzbuzz();
const fizzbuzz = function fizzbuzz () {
return "Fizz" + "Buzz";
}
})()
//=> undefined is not a function (evaluating 'fizzbuzz()')
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00529)_

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

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00530)_

```
const fizzbuzz = function fizzbuzz ()
return "Fizz" + "Buzz";
}
return fizzbuzz();
})()
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-function-declarations-c6aff434]]
