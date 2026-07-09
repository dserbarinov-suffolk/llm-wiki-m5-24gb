---
page_id: javascriptallonge-section-naming-functions-function-declarations-8c0a2df7
page_kind: source
summary: Naming Functions / function declarations: 13 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-naming-functions-function-declarations-8c0a2df7@a1579794c7127faa5a37a28d49935bd0
---

# Naming Functions / function declarations

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-naming-functions-the-function-keyword-46a79cb6]] - previous source section: Naming Functions / the function keyword
- [[javascriptallonge-section-naming-functions-function-declaration-caveats-34-2bc8359c]] - next source section: Naming Functions / function declaration caveats 34

### Source structure

- [[javascriptallonge-section-naming-functions-c49aef83]] - broader source section: Naming Functions

### Recipes

- [[javascriptallonge-recipe-function-declarations]] - recipe pattern: function declarations

## Statements

- There is another syntax for naming and/or defining a function. It's called a function declaration statement , and it looks a lot like a named function expression, only we use it as a statement: _(javascriptallonge.pdf (source-range-c98ab3e6-00522))_
- In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-c98ab3e6-00525))_
- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently: _(javascriptallonge.pdf (source-range-c98ab3e6-00528))_
- The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code. _(javascriptallonge.pdf (source-range-c98ab3e6-00531))_
- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. _(javascriptallonge.pdf (source-range-c98ab3e6-00528))_

## Technical atoms

### Technical frame 1: Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00525))_

> In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00524))_

<a id="atom-technical-atom-1edc2159fdc08db8"></a>
```
{
```

### Technical frame 2: Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00531))_

> The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00530))_

<a id="atom-technical-atom-b5a022c45e0a8b3d"></a>
```
const fizzbuzz = function fizzbuzz ()
return "Fizz" + "Buzz";
}
return fizzbuzz();
})()
```
