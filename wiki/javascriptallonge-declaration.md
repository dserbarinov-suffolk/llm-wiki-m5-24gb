---
page_id: javascriptallonge-declaration
page_kind: concept
summary: Declaration: 4 statement(s) and 5 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-declaration@919632582706727320f13a161e260074
---

# Declaration

What [[javascriptallonge]] covers about declaration:

## Statements

### Naming Functions / function declarations

- In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-c98ab3e6-00525))_

### Naming Functions / function declaration caveats 34

- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-c98ab3e6-00533))_

- Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization. _(javascriptallonge.pdf (source-range-c98ab3e6-00536))_

### Reassignment / mixing let and const / var

- But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. Note this example of a function that uses a helper: _(javascriptallonge.pdf (source-range-c98ab3e6-01170))_


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

### Technical frame 3: Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01169))_

> Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All var declarations behave as if they were hoisted to the top of the function, a little like function declarations.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01168))_

<a id="atom-technical-atom-bd739848728b2b19"></a>
```
(() => {
var age = 49;
if (true) {
var age = 50;
}
return age;
})()
//=> 50
```

### Technical frame 4: Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01176))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01171))_

<a id="atom-technical-atom-f129162fe850f018"></a>
```
const factorial = (n) => {
return innerFactorial(n, 1);
function innerFactorial (x, y) {
if (x == 1) {
return y;
}
else {
return innerFactorial(x-1, x * y);
}
}
}
factorial(4)
//=> 24
```

### Technical frame 5: Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01176))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01175))_

<a id="atom-technical-atom-c2ee219ff9d71c86"></a>
```
const factorial = (n) => {
let innerFactorial = undefined;
return innerFactorial(n, 1);
innerFactorial = function innerFactorial (x, y) {
if (x == 1) {
return y;
}
else {
return innerFactorial(x-1, x * y);
}
}
}
factorial(4)
//=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```


## Related pages

### Source structure

- [[javascriptallonge-section-naming-functions-function-declaration-caveats-34-2bc8359c]] - source section: Naming Functions / function declaration caveats 34
- [[javascriptallonge-section-naming-functions-function-declarations-8c0a2df7]] - source section: Naming Functions / function declarations

### Shared technical atoms

- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Reassignment / mixing let and const / var: const factorial = (n) => { return innerFactorial(n, 1); function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } } fa ... [truncated] (2 shared atom(s))
- [[javascriptallonge-bind]] - shared technical atoms: Bind shares technical record from Naming Functions / function declarations: { (1 shared atom(s))

## Source

- [[javascriptallonge]]
