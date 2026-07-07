---
page_id: javascriptallonge-bind
page_kind: concept
summary: Bind: 10 statement(s) and 28 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-bind@dc61152af90088e8830fffa0212d3ab0
---

# Bind

What [[javascriptallonge]] covers about bind:

## Statements

### And also: / call by sharing

- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. As you recall, value types like strings and numbers are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans as it wishes. _(javascriptallonge.pdf (source-range-c98ab3e6-00308))_

### That Constant Coffee Craving

- In order to bind 3.14159265 to the name PI , we'll need a function with a parameter of PI applied to an argument of 3.14159265 . If we put our function expression in parentheses, we can apply it to the argument of 3.14159265 : _(javascriptallonge.pdf (source-range-c98ab3e6-00373))_

### That Constant Coffee Craving / are consts also from a shadowy planet?

- We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-c98ab3e6-00451))_

- Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it. _(javascriptallonge.pdf (source-range-c98ab3e6-00474))_

### Naming Functions

- It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 . This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous. _(javascriptallonge.pdf (source-range-c98ab3e6-00486))_

### Naming Functions / function declarations

- In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-c98ab3e6-00525))_

### Magic Names / magic names and fat arrows

- This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind arguments when it's invoked. But if we rewrite row to use the function keyword, it stops working: _(javascriptallonge.pdf (source-range-c98ab3e6-00612))_

### Recipes with Basic Functions / Partial Application

- These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic. _(javascriptallonge.pdf (source-range-c98ab3e6-00643))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

- That match would fail because the array doesn't have an element to assign to what . But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. Therefore: _(javascriptallonge.pdf (source-range-c98ab3e6-00845))_

### Reassignment

- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . We go from: _(javascriptallonge.pdf (source-range-c98ab3e6-01149))_


## Technical atoms

### Technical frame 1: That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00377))_

> This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00374))_

<a id="atom-technical-atom-4965aaf1d272bf3d"></a>
```
((PI) =>
// ????
)(3.14159265)
```

### Technical frame 2: That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00377))_

> This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00376))_

<a id="atom-technical-atom-c718309328e9dc79"></a>
```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```

### Technical frame 3: That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00387))_

> Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00384))_

<a id="atom-technical-atom-777993b745dde7ca"></a>
```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```

### Technical frame 4: That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00404))_

> This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00403))_

<a id="atom-technical-atom-9657cc29ab75266e"></a>
```
((diameter, PI) => diameter * PI)(2, 3.14159265)
//=> 6.2831853
```

### Technical frame 5: That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00417))_

> Notice calc(d) ? This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () . A name that's bound to a function is a valid expression evaluating to a function. 30

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00416))_

<a id="atom-technical-atom-14186183cf49b96a"></a>
```
(d) => {
const calc = (diameter) => {
const PI = 3.14159265;
return diameter * PI
};
return "The circumference is " + calc(d)
}
```

### Technical frame 6: That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00418))_

> Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as 'first class entities. ' Functions are values that can be bound to names like any other value, passed as arguments, returned from other functions, and so forth.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00417))_

<a id="atom-technical-atom-cb81c053d3442170"></a>
> This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () .

### Technical frame 7: That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00421))_

> 30 We're into the second chapter and we've finally named a function. Sheesh.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00420))_

<a id="atom-technical-atom-c2488f56337063b8"></a>
```
(d) => {
const PI
= 3.14159265,
calc = (diameter) => diameter * PI;
return "The circumference is " + calc(d)
}
```

### Technical frame 8: That Constant Coffee Craving / const and lexical scope

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00439))_

> We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00438))_

<a id="atom-technical-atom-8992af7dadf29da4"></a>
```
((diameter_fn) =>
diameter_fn(2)
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
//=> 6.2831853
```

### Technical frame 9: That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00458))_

> And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the 'outer' environment? Let's rewrite things slightly differently:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00455))_

<a id="atom-technical-atom-19d68b629cb34a7c"></a>
```
((PI) =>
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)(3)
```

### Technical frame 10: That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00460))_

> Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . Does that binding 'overwrite' the outer one? Will our function return 6 or 6.2831853 ? This is a book, you've already scanned ahead, so you know that the answer is no , the inner binding does not overwrite the outer binding:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00459))_

<a id="atom-technical-atom-7f4ba1b3dfbe5b5c"></a>
```
((PI) => {
((PI) => {})(3);
return (diameter) => diameter * PI;
})(3.14159265)
```

### Technical frame 11: That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00462))_

> We say that when we bind a variable using a parameter inside another binding, the inner binding shadows the outer binding. It has effect inside its own scope, but does not affect the binding in the enclosing scope.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00461))_

<a id="atom-technical-atom-4878f2e3a529b233"></a>
```
((PI) => {
((PI) => {})(3);
return (diameter) => diameter * PI;
})(3.14159265)(2)
//=> 6.2831853
```

### Technical frame 12: That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00466))_

> Parameters are only bound when we invoke a function. That's why we made all these IIFEs. But const statements can appear inside blocks. What happens when we use a const inside of a block? We'll need a gratuitous block. We've seen if statements, what could be more gratuitous than:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00464))_

<a id="atom-technical-atom-b2847d0a5b987159"></a>
```
((diameter) => {
const PI = 3.14159265;
(() => {
const PI = 3;
})();
return diameter * PI;
})(2)
//=> 6.2831853
```

### Technical frame 13: Naming Functions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00486))_

> It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 . This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00485))_

<a id="atom-technical-atom-f80a5e9c7417dd42"></a>
```
const repeat = (str) => str + str
```

### Technical frame 14: Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00508))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00507))_

<a id="atom-technical-atom-99130ddccdd26a72"></a>
```
const double = function repeat (str) {
return str + str;
}
```

### Technical frame 15: Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00518))_

> Clearly, the name even is bound to the function within the function's body . Is it bound to the function outside of the function's body?

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00517))_

<a id="atom-technical-atom-44be2641185165b4"></a>
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

### Technical frame 16: Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00520))_

> even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere else, you needn't.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00519))_

<a id="atom-technical-atom-3c3941f3152f01e3"></a>
```
even
//=> Can't find variable: even
```

### Technical frame 17: Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00525))_

> In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00524))_

<a id="atom-technical-atom-1edc2159fdc08db8"></a>
```
{
```

### Technical frame 18: Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00528))_

> We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00527))_

<a id="atom-technical-atom-4aedf6b59c8b52d0"></a>
```
(function () {
return fizzbuzz();
const fizzbuzz = function fizzbuzz () {
return "Fizz" + "Buzz";
}
})()
//=> undefined is not a function (evaluating 'fizzbuzz()')
```

### Technical frame 19: Magic Names / magic names and fat arrows

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

### Technical frame 20: Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00616))_

> Although this example is clearly unrealistic, there is a general design principle that deserves attention. Sometimes, a function is meant to be used as a Big-F function. It has a name, it is called by different pieces of code, it's a first-class entity in the code.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00614))_

<a id="atom-technical-atom-21c69ed12ae99029"></a>
```
const row = function () {
return mapWith(
function (column) { return column * arguments[0] },
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
)
}
row(3)
//=> [1,4,9,16,25,36,49,64,81,100,121,144]
```

### Technical frame 21: Recipes with Basic Functions / Partial Application

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00645))_

> As noted above, our partial recipe allows us to create functions that are partial applications of functions that are context aware. We'd need a different recipe if we wish to create partial applications of object methods.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00644))_

<a id="atom-technical-atom-bf9a96eab0c8c00a"></a>
```
const callFirst = (fn, larg) =>
function (...rest) {
return fn.call(this, larg, ...rest);
}
const callLast = (fn, rarg) =>
function (...rest) {
return fn.call(this, ...rest, rarg);
}
const greet = (me, you) =>
`Hello, ${you}, my name is ${me}`;
const heliosSaysHello = callFirst(greet, 'Helios');
heliosSaysHello('Eartha')
//=> 'Hello, Eartha, my name is Helios'
const sayHelloToCeline = callLast(greet, 'Celine');
sayHelloToCeline('Eartha')
//=> 'Hello, Celine, my name is Eartha'
```

### Technical frame 22: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00845))_

> That match would fail because the array doesn't have an element to assign to what . But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. Therefore:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00844))_

<a id="atom-technical-atom-31853146d3cd854e"></a>
```
const [what] = [];
```

### Technical frame 23: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00849))_

> From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00846))_

<a id="atom-technical-atom-8c41382b03eaba41"></a>
```
const [what] = [];
what
//=> undefined
const [which, what,
who
//=> undefined
```

### Technical frame 24: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00849))_

> From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00847))_

<a id="atom-technical-atom-d46f63fabe2b492d"></a>
```
const [...they] = [];
they
//=> []
const [which, what, .
they
//=> []
```

### Technical frame 25: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01149))_

> Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . We go from:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01148))_

<a id="atom-technical-atom-113c47faa991f857"></a>
```
(() => {
let age = 49;
if (true) {
let age = 50;
}
return age;
})()
//=> 49
```

### Technical frame 26: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01154))_

> Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01151))_

<a id="atom-technical-atom-4e14a82a74557b9f"></a>
```
{age: 49, '..': global-environment}
```

### Technical frame 27: Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01167))_

> But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01164))_

<a id="atom-technical-atom-ce362bfbb51880b9"></a>
```
const factorial = (n) => {
let x = n;
if (x === 1) {
return 1;
}
else {
--x;
return n * factorial(x);
}
}
factorial(5)
//=> 120
const factorial2 = (n) => {
var x = n;
if (x === 1) {
return 1;
}
else {
--x;
```

### Technical frame 28: Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01167))_

> But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01166))_

<a id="atom-technical-atom-ee34a34b88967961"></a>
```
return n * factorial2(x);
}
}
factorial2(5)
//=> 120
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from That Constant Coffee Craving: ((PI) => // ???? )(3.14159265) (8 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from And also: / call by sharing: We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to ... [truncated]; Javascript shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching: const [what] = []; (2 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-binding]] - shared statements and technical atoms: Binding shares source evidence from That Constant Coffee Craving / are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated]; Binding shares technical record from That Constant Coffee Craving / are consts also from a shadowy planet?: ((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265) (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-argument]] - shared statements and technical atoms: Argument shares source evidence from Magic Names / magic names and fat arrows: This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind ar ... [truncated]; Argument shares technical record from Magic Names / magic names and fat arrows: const row = function () { return mapWith( (column) => column * arguments[0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [3,6,9,12,15,18,21,24,27,30,33,36] (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-array]] - shared technical atoms: Array shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching: const [what] = []; (3 shared atom(s))
- [[javascriptallonge-function-keyword]] - shared technical atoms: the function keyword shares technical record from Naming Functions / the function keyword: const double = function repeat (str) { return str + str; } (3 shared atom(s))
- [[javascriptallonge-fat-arrow]] - shared statements and technical atoms: Fat Arrow shares source evidence from Magic Names / magic names and fat arrows: This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind ar ... [truncated]; Fat Arrow shares technical record from Magic Names / magic names and fat arrows: const row = function () { return mapWith( (column) => column * arguments[0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) //=> [3,6,9,12,15,18,21,24,27,30,33,36] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from Recipes with Basic Functions / Partial Application: These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want ... [truncated]; List shares technical record from Recipes with Basic Functions / Partial Application: const callFirst = (fn, larg) => function (...rest) { return fn.call(this, larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call(this, ... [truncated] (1 shared statement(s), 1 shared atom(s))

## Source

- [[javascriptallonge]]
