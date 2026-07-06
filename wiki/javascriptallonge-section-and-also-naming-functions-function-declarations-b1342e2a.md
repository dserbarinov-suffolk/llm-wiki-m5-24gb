---
page_id: javascriptallonge-section-and-also-naming-functions-function-declarations-b1342e2a
page_kind: source
summary: And also: / Naming Functions / function declarations: 15 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-naming-functions-function-declarations-b1342e2a@7fa419810cb1adb5f1763deea6fff046
---

# And also: / Naming Functions / function declarations

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-and-also-naming-functions-the-function-keyword-c5591d39]] - previous source section: And also: / Naming Functions / the function keyword
- [[javascriptallonge-section-and-also-naming-functions-function-declaration-caveats-34-4f93ce28]] - next source section: And also: / Naming Functions / function declaration caveats 34

### Source structure

- [[javascriptallonge-section-and-also-naming-functions-c9513a66]] - broader source section: And also: / Naming Functions

## Statements

- There is another syntax for naming and/or defining a function. It's called a function declaration statement , and it looks a lot like a named function expression, only we use it as a statement: _(javascriptallonge.pdf (source-range-c98ab3e6-00532))_
- In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-c98ab3e6-00535))_
- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently: _(javascriptallonge.pdf (source-range-c98ab3e6-00538))_
- The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code. _(javascriptallonge.pdf (source-range-c98ab3e6-00541))_
- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. _(javascriptallonge.pdf (source-range-c98ab3e6-00538))_

## Technical atoms

### Technical frame 1: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00535))_

> In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00533))_

<a id="atom-technical-atom-0ab51df09609c9a7"></a>
```
function someName () {
// ...
}
This behaves a little like:
const someName = function someName ()
// ...
}
```

### Technical frame 2: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00535))_

> In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00534))_

<a id="atom-technical-atom-6e5c8cf419fc735b"></a>
```
{
```

### Technical frame 3: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00541))_

> The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00539))_

<a id="atom-technical-atom-524f907061a9862d"></a>
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

### Technical frame 4: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00541))_

> The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00540))_

<a id="atom-technical-atom-48428010d2f136cf"></a>
```
const fizzbuzz = function fizzbuzz ()
return "Fizz" + "Buzz";
}
return fizzbuzz();
})()
```
