---
page_id: javascriptallonge-argument
page_kind: concept
summary: Argument: 15 statement(s) and 27 atom(s) from raw/javascriptallonge.pdf.
page_family: broad-topic
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-argument@96fe66c29a393d0ee54b4488b242cdc2
---

# Argument

What [[javascriptallonge]] covers about argument:

## Statements

### And also: / Ah. I'd Like to Have an Argument, Please. 22

- Up to now, we've looked at functions without arguments. We haven't even said what an argument is , only that our functions don't have any. _(javascriptallonge.pdf (source-range-c98ab3e6-00257))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / a quick summary of functions and bodies

- How arguments are used in a body's expression is probably perfectly obvious to you from the examples, especially if you've used any programming language (except for the dialect of BASIC-which I recall from my secondary school-that didn't allow parameters when you called a procedure). _(javascriptallonge.pdf (source-range-c98ab3e6-00272))_

### And also: / variables and bindings

- How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dictionary for each argument. So when we write: _(javascriptallonge.pdf (source-range-c98ab3e6-00291))_

### And also: / call by sharing

- 26 Unless the argument is NaN , which isn't equal to anything, including itself . NaN in JavaScript behaves a lot like NULL in SQL. _(javascriptallonge.pdf (source-range-c98ab3e6-00314))_

### And also: / Combinators and Function Decorators / higher-order functions

- As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. _(javascriptallonge.pdf (source-range-c98ab3e6-00542))_

### And also: / Building Blocks / partial application

- The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-c98ab3e6-00582))_

### And also: / Magic Names / the function keyword

- arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00597))_

### And also: / Magic Names / magic names and fat arrows

- This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind arguments when it's invoked. But if we rewrite row to use the function keyword, it stops working: _(javascriptallonge.pdf (source-range-c98ab3e6-00612))_

### Recipes with Basic Functions / Partial Application

- These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic. _(javascriptallonge.pdf (source-range-c98ab3e6-00643))_

### Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

- Gathering arguments for functions is one of the ways JavaScript can destructure arrays. Another way is when assigning variables, like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00724))_

### Picking the Bean: Choice and Truthiness / truthiness and operators

- Our logical operators ! , && , and || are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-c98ab3e6-00758))_

### Composing and Decomposing Data / Self-Similarity

- In Arrays and Destructuring Arguments, we worked with the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-c98ab3e6-00864))_

### Composing and Decomposing Data / default arguments

- Now we don't need to use two functions. A default argument is concise and readable. _(javascriptallonge.pdf (source-range-c98ab3e6-00990))_


## Technical atoms

### Technical frame 1: And also: / call by sharing

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00314))_

> 26 Unless the argument is NaN , which isn't equal to anything, including itself . NaN in JavaScript behaves a lot like NULL in SQL.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00313))_

<a id="atom-technical-atom-9f47eb757bacdc28"></a>
```
(value) =>
((ref1, ref2) => ref1 === ref2)(value, value)
```

### Technical frame 2: And also: / Combinators and Function Decorators / higher-order functions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00542))_

> As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00544))_

<a id="atom-technical-atom-4fc3e2e77a3ff1bc"></a>
```
const repeat = (num, fn) =>
(num > 0)
? (repeat(num - 1, fn), fn(num))
: undefined
repeat(3, function (n) {
console.log(`Hello ${n}`)
})
//=>
'Hello 1'
'Hello 2'
'Hello 3'
undefined
```

### Technical frame 3: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00582))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00578))_

<a id="atom-technical-atom-bbed966728159c94"></a>
```
_.map([1, 2, 3], (n) => n * n)
//=> [1, 4, 9]
```

### Technical frame 4: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00582))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00581))_

<a id="atom-technical-atom-2d776dba8a34bc3d"></a>
```
const squareAll = (array) => map(array,
(n) => n * n);
```

### Technical frame 5: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00597))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00594))_

<a id="atom-technical-atom-c8785b9ba7a50297"></a>
```
const plus = function (a, b) {
return arguments[0] + arguments[1];
}
plus(2,3)
//=> 5
```

### Technical frame 6: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00597))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00596))_

<a id="atom-technical-atom-9046e00b2e52a6e1"></a>
```
const args = function (a, b) {
return arguments;
}
args(2,3)
//=> { '0': 2, '1': 3 }
```

### Technical frame 7: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00612))_

> This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind arguments when it's invoked. But if we rewrite row to use the function keyword, it stops working:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00611))_

<a id="atom-technical-atom-29d9d9b76cf52a40"></a>
```
const row = function () {
return mapWith(
(column) => column * arguments[0],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
)
}
row(3)
//=> [3,6,9,12,15,18,21,24,27,30,33,36]
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-partial-application]] - shared statements and technical atoms: partial application shares source evidence from And also: / Building Blocks / partial application: The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one funct ... [truncated]; partial application shares technical record from And also: / Building Blocks / partial application: _.map([1, 2, 3], (n) => n * n) //=> [1, 4, 9] (2 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-function-keyword]] - shared statements and technical atoms: the function keyword shares source evidence from And also: / Magic Names / the function keyword: arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:; the function keyword shares technical record from And also: / Magic Names / the function keyword: const plus = function (a, b) { return arguments[0] + arguments[1]; } plus(2,3) //=> 5 (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from And also: / Combinators and Function Decorators / higher-order functions: As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as argume ... [truncated]; Return shares technical record from And also: / Combinators and Function Decorators / function decorators: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (3 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-bind]] - shared statements and technical atoms: Bind shares source evidence from And also: / Magic Names / magic names and fat arrows: This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind ar ... [truncated]; Bind shares technical record from And also: / Magic Names / magic names and fat arrows: const row = function () { return mapWith( (column) => column * arguments[0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [3,6,9,12,15,18,21,24,27,30,33,36] (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-fat-arrow]] - shared statements and technical atoms: Fat Arrow shares source evidence from And also: / Magic Names / magic names and fat arrows: This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind ar ... [truncated]; Fat Arrow shares technical record from And also: / Magic Names / magic names and fat arrows: (function () { return (() => arguments[0])('inner'); })('outer') //=> "outer" (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from And also: / Combinators and Function Decorators / function decorators: !5 //=> false !undefined //=> true (2 shared atom(s))
- [[javascriptallonge-variable]] - shared technical atoms: Variable shares technical record from And also: / variables and bindings: (x) => (y) => x (2 shared atom(s))
- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from Recipes with Basic Functions / Partial Application: These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want ... [truncated]; List shares technical record from Recipes with Basic Functions / Partial Application: const callFirst = (fn, larg) => function (...rest) { return fn.call(this, larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call(this, ... [truncated] (1 shared statement(s), 1 shared atom(s))

### Topics

- [[javascriptallonge-works-just-fine-because-arguments]] - narrower topic: Works Just Fine, Because Arguments[0 shares source evidence from And also: / Magic Names / magic names and fat arrows: This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind ar ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
