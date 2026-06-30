---
page_id: javascriptallonge-section-and-also-naming-functions-cae91ee1
page_kind: source
summary: And also: / Naming Functions: 63 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-naming-functions-cae91ee1@720b6cf44ae4f0875a5a1540c67fc188
---

# And also: / Naming Functions

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-0e29dfba]] - broader source section: And also:
- [[javascriptallonge-section-and-also-naming-functions-the-function-keyword-443f109f]] - narrower source section: And also: / Naming Functions / the function keyword
- [[javascriptallonge-section-and-also-naming-functions-function-declarations-94e43325]] - narrower source section: And also: / Naming Functions / function declarations
- [[javascriptallonge-section-and-also-naming-functions-function-declaration-caveats-34-d724d0dc]] - narrower source section: And also: / Naming Functions / function declaration caveats 34
- [[javascriptallonge-section-and-also-that-constant-coffee-craving-ac9d9918]] - previous source section: And also: / That Constant Coffee Craving
- [[javascriptallonge-section-and-also-combinators-and-function-decorators-4a7771ac]] - next source section: And also: / Combinators and Function Decorators

## Statements

- It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 . This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous. _(javascriptallonge.pdf (source-range-0e12e052-00496))_

## Statements by subsection

### And also: / Naming Functions / the function keyword

- JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions. _(javascriptallonge.pdf (source-range-0e12e052-00498))_
- Something else we're about to discuss is optional. _(javascriptallonge.pdf (source-range-0e12e052-00505))_
- We have arguments in parentheses, just like fat arrow functions. _(javascriptallonge.pdf (source-range-0e12e052-00506))_
- We do not have a fat arrow, we go directly to the body. _(javascriptallonge.pdf (source-range-0e12e052-00507))_
- We always use a block, we cannot write function (str) str + str . This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-0e12e052-00508))_
- In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment. _(javascriptallonge.pdf (source-range-0e12e052-00518))_
- 33 'Yes of course?' Well, in chapter of a book dedicated to naming functions, it is not surprising that feature we mention has something to do with naming functions. _(javascriptallonge.pdf (source-range-0e12e052-00522))_
- Now, the function's actual name has no effect on the environment in which it is used. To whit: _(javascriptallonge.pdf (source-range-0e12e052-00524))_
- So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines whether a positive integer is even or not. We'll use it in an IIFE so that we don't have to bind it to a name with const : _(javascriptallonge.pdf (source-range-0e12e052-00526))_
- Clearly, the name even is bound to the function within the function's body . Is it bound to the function outside of the function's body? _(javascriptallonge.pdf (source-range-0e12e052-00528))_
- even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere else, you needn't. _(javascriptallonge.pdf (source-range-0e12e052-00530))_
- This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-0e12e052-00508))_
- Clearly, the name even is bound to the function within the function's body . _(javascriptallonge.pdf (source-range-0e12e052-00528))_
- even is bound within the function itself, but not outside it. _(javascriptallonge.pdf (source-range-0e12e052-00530))_

### And also: / Naming Functions / function declarations

- There is another syntax for naming and/or defining a function. It's called a function declaration statement , and it looks a lot like a named function expression, only we use it as a statement: _(javascriptallonge.pdf (source-range-0e12e052-00532))_
- In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-0e12e052-00535))_
- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently: _(javascriptallonge.pdf (source-range-0e12e052-00538))_
- The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code. _(javascriptallonge.pdf (source-range-0e12e052-00541))_
- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. _(javascriptallonge.pdf (source-range-0e12e052-00538))_

### And also: / Naming Functions / function declaration caveats 34

- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-0e12e052-00543))_
- 34 A number of the caveats discussed here were described in Jyrly Zaytsev's excellent article Named function expressions demystified. _(javascriptallonge.pdf (source-range-0e12e052-00544))_
- Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization. _(javascriptallonge.pdf (source-range-0e12e052-00546))_
- Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. So this is a function declaration: _(javascriptallonge.pdf (source-range-0e12e052-00547))_
- The parentheses make this an expression, not a function declaration. _(javascriptallonge.pdf (source-range-0e12e052-00549))_
- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. _(javascriptallonge.pdf (source-range-0e12e052-00543))_
- Function declarations are not supposed to occur inside of blocks. _(javascriptallonge.pdf (source-range-0e12e052-00546))_
- Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. _(javascriptallonge.pdf (source-range-0e12e052-00547))_

## Technical atoms

### Technical frame 1: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00524))_

> Now, the function's actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00523))_

```
someBackboneView.on('click', function clickHandler () {
//...
});
```

### Technical frame 2: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00535))_

> In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00533))_

```
function someName () {
// ...
}
This behaves a little like:
const someName = function someName ()
// ...
}
```

### Technical frame 3: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00535))_

> In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00534))_

```
{
```
