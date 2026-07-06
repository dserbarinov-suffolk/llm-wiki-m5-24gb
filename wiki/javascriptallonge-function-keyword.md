---
page_id: javascriptallonge-function-keyword
page_kind: concept
summary: the function keyword: 25 statement(s) and 16 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-function-keyword@06831e1ba2f0e9886aaf15ce1c5342c9
---

# the function keyword

What [[javascriptallonge]] covers about the function keyword:

## Statements

### And also: / Naming Functions / the function keyword

- JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00498))_

- Something else we're about to discuss is optional. _(javascriptallonge.pdf (source-range-c98ab3e6-00505))_

- We have arguments in parentheses, just like fat arrow functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00506))_

- We do not have a fat arrow, we go directly to the body. _(javascriptallonge.pdf (source-range-c98ab3e6-00507))_

- We always use a block, we cannot write function (str) str + str . This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-c98ab3e6-00508))_

- In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment. _(javascriptallonge.pdf (source-range-c98ab3e6-00518))_

- 33 'Yes of course?' Well, in chapter of a book dedicated to naming functions, it is not surprising that feature we mention has something to do with naming functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00522))_

- Now, the function's actual name has no effect on the environment in which it is used. To whit: _(javascriptallonge.pdf (source-range-c98ab3e6-00524))_

- So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines whether a positive integer is even or not. We'll use it in an IIFE so that we don't have to bind it to a name with const : _(javascriptallonge.pdf (source-range-c98ab3e6-00526))_

- Clearly, the name even is bound to the function within the function's body . Is it bound to the function outside of the function's body? _(javascriptallonge.pdf (source-range-c98ab3e6-00528))_

- even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere else, you needn't. _(javascriptallonge.pdf (source-range-c98ab3e6-00530))_

### And also: / Magic Names / the function keyword

- There are two separate rules for these 'magic' names, one for when you invoke a function using the function keyword, and another for functions defined with 'fat arrows.' We'll begin with how things work for functions defined with the function keyword. _(javascriptallonge.pdf (source-range-c98ab3e6-00602))_

- The first magic name is this , and it is bound to something called the function's context. We will explore this in more detail when we start discussing objects and classes. The second magic name is very interesting, it's called arguments , and the most interesting thing about it is that it contains a list of arguments passed to a function: _(javascriptallonge.pdf (source-range-c98ab3e6-00603))_

- arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00607))_

- The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses. _(javascriptallonge.pdf (source-range-c98ab3e6-00612))_

### And also: / Summary / Functions

- function keyword functions always have blocks as their bodies. _(javascriptallonge.pdf (source-range-c98ab3e6-00637))_

### Plain Old JavaScript Objects / literal object syntax

- It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords: _(javascriptallonge.pdf (source-range-c98ab3e6-01086))_


## Technical atoms

### Technical frame 1: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00505))_

> Something else we're about to discuss is optional.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00500))_

<a id="atom-technical-atom-5e357060e1b06a1e"></a>
```
(str) => str + str
```

### Technical frame 2: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00505))_

> Something else we're about to discuss is optional.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00502))_

<a id="atom-technical-atom-cc7641804dc4b408"></a>
```
function (str) { return str + str }
```

### Technical frame 3: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00518))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00510))_

<a id="atom-technical-atom-ca757f2ec4259859"></a>
```
(n) => (1.618**n - -1.618**-n) / 2.236
```

### Technical frame 4: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00518))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00512))_

<a id="atom-technical-atom-b893bf7c1c32203d"></a>
```
function (n) {
return (1.618**n - -1.618**-n) / 2.236;
}
```

### Technical frame 5: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00518))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00515))_

<a id="atom-technical-atom-b5f05fe8ccef523e"></a>
```
const repeat = function repeat (str) {
return str + str;
};
const fib = function fib (n) {
return (1.618**n - -1.618**-n) / 2.236;
};
```

### Technical frame 6: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00518))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00517))_

<a id="atom-technical-atom-92f9c606d28cd91a"></a>
```
const double = function repeat (str) {
return str + str;
}
```

### Technical frame 7: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00522))_

> 33 'Yes of course?' Well, in chapter of a book dedicated to naming functions, it is not surprising that feature we mention has something to do with naming functions.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00520))_

<a id="atom-technical-atom-329f1c0328539cfb"></a>
```
double.name
//=> 'repeat'
```

### Technical frame 8: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00524))_

> Now, the function's actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00523))_

<a id="atom-technical-atom-37edd8dd08e32d9a"></a>
```
someBackboneView.on('click', function clickHandler () {
//...
});
```

### Technical frame 9: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00526))_

> So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines whether a positive integer is even or not. We'll use it in an IIFE so that we don't have to bind it to a name with const :

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00525))_

<a id="atom-technical-atom-64e54ae8241a5d4a"></a>
```
const bindingName = function actualName () {
//...
};
bindingName
//=> [Function: actualName]
actualName
//=> ReferenceError: actualName is not defined
```

### Technical frame 10: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00528))_

> Clearly, the name even is bound to the function within the function's body . Is it bound to the function outside of the function's body?

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00527))_

<a id="atom-technical-atom-9bd9a3108ea28b7e"></a>
```
(function even (n) {
if (n === 0) {
return true
}
else return !even(n - 1)
})(5)
//=> false
(function even (n) {
if (n === 0) {
return true
}
else return !even(n - 1)
})(2)
//=> true
```

### Technical frame 11: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00530))_

> even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere else, you needn't.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00529))_

<a id="atom-technical-atom-245f6ccf936b3285"></a>
```
even
//=> Can't find variable: even
```

### Technical frame 12: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00607))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00604))_

<a id="atom-technical-atom-d9d2432be6039e9c"></a>
```
const plus = function (a, b) {
return arguments[0] + arguments[1];
}
plus(2,3)
//=> 5
```

### Technical frame 13: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00607))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00606))_

<a id="atom-technical-atom-4460849cb173a0af"></a>
```
const args = function (a, b) {
return arguments;
}
args(2,3)
//=> { '0': 2, '1': 3 }
```

### Technical frame 14: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00612))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00608))_

<a id="atom-technical-atom-0cef432672ec2709"></a>
```text
42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times.
43 We'll look at arrays and plain old javascript objects in depth later.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 42 | You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. |
| 43 | We'll look at arrays and plain old javascript objects in depth later. |

</details>

### Technical frame 15: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00612))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00609))_

<a id="atom-technical-atom-d291d8101b5b3742"></a>
```
const plus = function () {
return arguments[0] + arguments[1];
}
plus(2,3)
//=> 5
```

### Technical frame 16: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00612))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00611))_

<a id="atom-technical-atom-8e5c3dd900fd3230"></a>
```
const howMany = function () {
return arguments['length'];
}
howMany()
//=> 0
howMany('hello')
//=> 1
howMany('sharks', 'are', 'apex', 'predators')
//=> 4
```


## Related pages

### Source structure

- [[javascriptallonge-section-and-also-naming-functions-the-function-keyword-c5591d39]] - source section: And also: / Naming Functions / the function keyword shares source evidence from And also: / Naming Functions / the function keyword: JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions.; And also: / Naming Functions / the function keyword shares technical record from And also: / Naming Functions / the function keyword: (str) => str + str (17 shared statement(s), 11 shared atom(s))
- [[javascriptallonge-section-and-also-magic-names-the-function-keyword-d04ee81a]] - source section: And also: / Magic Names / the function keyword shares source evidence from And also: / Magic Names / the function keyword: There are two separate rules for these 'magic' names, one for when you invoke a function using the function keyword, and another for functions defined with 'fat arro ... [truncated]; And also: / Magic Names / the function keyword shares technical record from And also: / Magic Names / the function keyword: const plus = function (a, b) { return arguments[0] + arguments[1]; } plus(2,3) //=> 5 (6 shared statement(s), 5 shared atom(s))

### Shared technical atoms

- [[javascriptallonge-argument]] - shared statements and technical atoms: Argument shares source evidence from And also: / Magic Names / the function keyword: arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:; Argument shares technical record from And also: / Magic Names / the function keyword: const plus = function (a, b) { return arguments[0] + arguments[1]; } plus(2,3) //=> 5 (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-bind]] - shared technical atoms: Bind shares technical record from And also: / Naming Functions / the function keyword: const double = function repeat (str) { return str + str; } (4 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms: Expression shares source evidence from And also: / Naming Functions / the function keyword: In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, b ... [truncated]; Expression shares technical record from And also: / Naming Functions / the function keyword: (function even (n) { if (n === 0) { return true } else return !even(n - 1) })(5) //=> false (function even (n) { if (n === 0) { return true } else return !even(n - 1 ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from And also: / Naming Functions / the function keyword: JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions.; Javascript shares technical record from And also: / Naming Functions / the function keyword: someBackboneView.on('click', function clickHandler () { //... }); (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-binding]] - shared technical atoms: Binding shares technical record from And also: / Magic Names / the function keyword: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms: Object shares technical record from And also: / Magic Names / the function keyword: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))

### Shared claims

- [[javascriptallonge-ecmascript]] - shared statements: Ecmascript shares source evidence from And also: / Naming Functions / the function keyword: JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions. (1 shared statement(s))
- [[javascriptallonge-partial-application]] - shared statements: partial application shares source evidence from And also: / Magic Names / the function keyword: The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting o ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
