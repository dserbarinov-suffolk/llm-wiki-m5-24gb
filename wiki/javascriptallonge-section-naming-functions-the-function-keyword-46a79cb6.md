---
page_id: javascriptallonge-section-naming-functions-the-function-keyword-46a79cb6
page_kind: source
summary: Naming Functions / the function keyword: 33 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-naming-functions-the-function-keyword-46a79cb6@e847fe9ac9329d5753d5dfff3f3bf90d
---

# Naming Functions / the function keyword

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-naming-functions-function-declarations-8c0a2df7]] - next source section: Naming Functions / function declarations

### Source structure

- [[javascriptallonge-section-naming-functions-c49aef83]] - broader source section: Naming Functions

### Topics

- [[javascriptallonge-function-keyword]] - topic hub: opens the topic page for Function Keyword

## Statements

- JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00488))_
- Something else we're about to discuss is optional. _(javascriptallonge.pdf (source-range-c98ab3e6-00495))_
- We have arguments in parentheses, just like fat arrow functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00496))_
- We do not have a fat arrow, we go directly to the body. _(javascriptallonge.pdf (source-range-c98ab3e6-00497))_
- We always use a block, we cannot write function (str) str + str . This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-c98ab3e6-00498))_
- In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment. _(javascriptallonge.pdf (source-range-c98ab3e6-00508))_
- 33 'Yes of course?' Well, in chapter of a book dedicated to naming functions, it is not surprising that feature we mention has something to do with naming functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00512))_
- Now, the function's actual name has no effect on the environment in which it is used. To whit: _(javascriptallonge.pdf (source-range-c98ab3e6-00514))_
- So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines whether a positive integer is even or not. We'll use it in an IIFE so that we don't have to bind it to a name with const : _(javascriptallonge.pdf (source-range-c98ab3e6-00516))_
- Clearly, the name even is bound to the function within the function's body . Is it bound to the function outside of the function's body? _(javascriptallonge.pdf (source-range-c98ab3e6-00518))_
- even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere else, you needn't. _(javascriptallonge.pdf (source-range-c98ab3e6-00520))_
- This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-c98ab3e6-00498))_
- Clearly, the name even is bound to the function within the function's body . _(javascriptallonge.pdf (source-range-c98ab3e6-00518))_
- even is bound within the function itself, but not outside it. _(javascriptallonge.pdf (source-range-c98ab3e6-00520))_

## Technical atoms

### Technical frame 1: Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00495))_

> Something else we're about to discuss is optional.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00492))_

<a id="atom-technical-atom-4e6d1d42a8beb35b"></a>
```
function (str) { return str + str }
```

### Technical frame 2: Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00498))_

> We always use a block, we cannot write function (str) str + str . This means that if we want our functions to return a value, we always need to use the return keyword

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00499))_

<a id="atom-technical-atom-83da4ba3abe81f7f"></a>
> If we leave out the 'something optional' that comes after the function keyword, we can translate all of the fat arrow functions that we've seen into function keyword functions, e.g.

### Technical frame 3: Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00508))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00500))_

<a id="atom-technical-atom-c22d055dbc6bf1f2"></a>
```
(n) => (1.618**n - -1.618**-n) / 2.236
```

### Technical frame 4: Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00508))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00502))_

<a id="atom-technical-atom-59d7d99068f8242c"></a>
```
function (n) {
return (1.618**n - -1.618**-n) / 2.236;
}
```

### Technical frame 5: Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00508))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00507))_

<a id="atom-technical-atom-99130ddccdd26a72"></a>
```
const double = function repeat (str) {
return str + str;
}
```
