---
page_id: javascriptallonge-return
page_kind: concept
summary: Return: 18 statement(s) and 20 atom(s) from raw/javascriptallonge.pdf.
page_family: broad-topic
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-return@612a4d7695fc8d933621ba8bfdd2e7a5
---

# Return

What [[javascriptallonge]] covers about return:

## Statements

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

- We've seen () => 0 . We know that (() => 0)() returns 0 , and this is unsurprising. Likewise, the following all ought to be obvious: _(javascriptallonge.pdf (source-range-0e12e052-00190))_

### Or even: / the simplest possible block

- It returns the result of evaluating a block that has no statements. What would that be? Let's try it: _(javascriptallonge.pdf (source-range-0e12e052-00215))_

### And also: / Combinators and Function Decorators / higher-order functions

- As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. _(javascriptallonge.pdf (source-range-0e12e052-00552))_

### And also: / Building Blocks / partial application

- The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-0e12e052-00592))_

### Picking the Bean: Choice and Truthiness / truthiness and operators

- Our logical operators ! , && , and || are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-0e12e052-00771))_

### Composing and Decomposing Data / Self-Similarity / folding

- And to return to our first example, our version of length can be written as a fold: _(javascriptallonge.pdf (source-range-0e12e052-00943))_

### Copy on Write / Functional Iterators / iterating

- Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } . _(javascriptallonge.pdf (source-range-0e12e052-01289))_

### Copy on Write / Making Data Out Of Functions / the vireo

- Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data. For arrays, we'd write cons = (first, second) => [first, second] . For objects we'd write: cons = (first, second) => {first, second} . In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-0e12e052-01359))_

### Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

- For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest] : _(javascriptallonge.pdf (source-range-0e12e052-01602))_

### Served by the Pot: Collections / Generating Iterables / javascript's generators

- Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-0e12e052-01667))_

### Served by the Pot: Collections / Generating Iterables / generators are coroutines

- The body of our generator runs until it returns, ends, or encounters a yield statement, which is yield 1; . _(javascriptallonge.pdf (source-range-0e12e052-01679))_

- The body of our generator runs until it returns, ends, or encounters the next yield statement, which is yield 2; . _(javascriptallonge.pdf (source-range-0e12e052-01684))_

- The body of our generator runs until it returns, ends, or encounters the next yield statement, which is yield 3; . _(javascriptallonge.pdf (source-range-0e12e052-01689))_

### Served by the Pot: Collections / Generating Iterables / generators and iterables

- Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call. _(javascriptallonge.pdf (source-range-0e12e052-01704))_

### Served by the Pot: Collections / Generating Iterables / more generators

- We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own. _(javascriptallonge.pdf (source-range-0e12e052-01721))_

### Served by the Pot: Collections / Generating Iterables / yielding iterables

- We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93 _(javascriptallonge.pdf (source-range-0e12e052-01727))_

### Lazy and Eager Collections / lazy collection operations

- This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array. _(javascriptallonge.pdf (source-range-0e12e052-01787))_

- The body of our generator runs until it returns, ends, or encounters the next yield statement. _(javascriptallonge.pdf (source-range-0e12e052-01694))_

## Technical atoms

### Technical frame 1: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00193))_

> In the prelude, we looked at expressions. Values like 0 are expressions, as are things like 40 + 2 . Can we put an expression to the right of the arrow?

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00191))_

```
(() => 1)()
//=> 1
(() => "Hello, JavaScript")()
//=> "Hello, JavaScript"
(() => Infinity)()
//=> Infinity
```

### Technical frame 2: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00195))_

> Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)() ?

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00194))_

```
(() => 1 + 1)()
//=> 2
(() => "Hello, " + "JavaScript")()
//=> "Hello, JavaScript"
(() => Infinity * Infinity)()
//=> Infinity
```

### Technical frame 3: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00198))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00199))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.

### Technical frame 4: Or even: / the simplest possible block

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00215))_

> It returns the result of evaluating a block that has no statements. What would that be? Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00214))_

```
() => {}
```

### Technical frame 5: Or even: / the simplest possible block

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00215))_

> It returns the result of evaluating a block that has no statements. What would that be? Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00216))_

```
(() => {})()
//=> undefined
```

### Technical frame 6: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00245))_

> But no matter how we arrange them, a block with one or more expressions still evaluates to undefined :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00246))_

```text
//=> undefined
We said that the function returns the result of evaluating a block, and we said that a block is a
(possibly empty) list of JavaScript statements separated by semicolons.21
Something like: { statement1; statement2; statement3; ... ; statementn }
We haven’t discussed these statements. What’s a statement?
There are many kinds of JavaScript statements, but the first kind is one we’ve already met. An
expression is a JavaScript statement. Although they aren’t very practical, these are valid JavaScript
functions, and they return undefined when applied:
() => { 2 + 2 }
() => { 1 + 1; 2 + 2 }
As we saw with commas above, we can rearrange these functions onto multiple lines when we feel
its more readable that way:
() => {
1 + 1;
2 + 2
}
But no matter how we arrange them, a block with one or more expressions still evaluates to
undefined:
(() => { 2 + 2 })()
//=> undefined
(() => { 1 + 1; 2 + 2 })()
//=> undefined
(() => {
1 + 1;
2 + 2
})()
//=> undefined
As you can see, a block with one expression does not behave like an expression, and a block with
more than one expression does not behave like an expression constructed with the comma operator:
21You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semi-
colon insertion. Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in
should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it’s part of
the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them.
The first sip: Basic Functions
14
(() => 2 + 2)()
//=> 4
(() => { 2 + 2 })()
//=> undefined
(() => (1 + 1, 2 + 2))()
//=> 4
(() => { 1 + 1; 2 + 2 })()
//=> undefined
So how do we get a function that evaluates a block to return a value when applied? With the return
keyword and any expression:
(() => { return 0 })()
//=> 0
(() => { return 1 })()
//=> 1
(() => { return 'Hello ' + 'World' })()
// 'Hello World'
The return keyword creates a return statement that immediately terminates the function application
and returns the result of evaluating its expression. For example:
(() => {
1 + 1;
return 2 + 2
})()
//=> 4
And also:
(() => {
return 1 + 1;
2 + 2
})()
//=> 2
The return statement is the first statement we’ve seen, and it behaves differently than an expression.
For example, you can’t use one as the expression in a simple function, because it isn’t an expression:
The first sip: Basic Functions
15
(() => return 0)()
//=> ERROR
Statements belong inside blocks and only inside blocks. Some languages simplify this by making
everything an expression, but JavaScript maintains this distinction, so when learning JavaScript we
also learn about statements like function declarations, for loops, if statements, and so forth. We’ll
see a few more of these later.
functions that evaluate to functions
If an expression that evaluates to a function is, well, an expression, and if a return statement can
have any expression on its right side… Can we put an expression that evaluates to a function on the
right side of a function expression?
Yes:
() => () => 0
That’s a function! It’s a function that when applied, evaluates to a function that when applied,
evaluates to 0. So we have a function, that returns a function, that returns zero. Likewise:
() => () => true
That’s a function, that returns a function, that returns true:
(() => () => true)()()
//=> true
We could, of course, do the same thing with a block if we wanted:
() => () => { return true; }
But we generally don’t.
Well. We’ve been very clever, but so far this all seems very abstract. Diffraction of a crystal is
beautiful and interesting in its own right, but you can’t blame us for wanting to be shown a practical
use for it, like being able to determine the composition of a star millions of light years away. So… In
the next chapter, “I’d Like to Have an Argument, Please,” we’ll see how to make functions practical.
The first sip: Basic Functions
16
Ah. I’d Like to Have an Argument, Please.22
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 1 | + 1; |
| 2 | + 2 But no matter how we arrange them, a block with one or more expressions still evaluates to undefined: (() => {2 + 2})() //=> undefined (() => {1 + 1; 2 + 2})() //=> undefined |
| 1 | + 1; |
| 2 | + 2 //=> undefined As you can see, a block with one expression does not behave like an expression, and a block with more than one expression does not behave like an expression constructed with the comma operator: 21You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semi- colon insertion. Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. |
| 14 | The first sip: Basic Functions (() => 2 + 2)() //=> 4 (() => {2 + 2})() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => {1 + 1; 2 + 2})() //=> undefined So how do we get a function that evaluates a block to return a value when applied? With the return keyword and any expression: (() => {return 0})() //=> 0 (() => {return 1})() //=> 1 (() => {return 'Hello ' + 'World'})() // 'Hello World' The return keyword creates a return statement that immediately terminates the function application and returns the result of evaluating its expression. For example: |
| 1 | + 1; return 2 + 2 //=> 4 return 1 + 1; |
| 2 | And also: + 2 //=> 2 The return statement is the first statement we’ve seen, and it behaves differently than an expression. For example, you can’t use one as the expression in a simple function, because it isn’t an expression: |
| 15 | The first sip: Basic Functions (() => return 0)() //=> ERROR Statements belong inside blocks and only inside blocks. Some languages simplify this by making everything an expression, but JavaScript maintains this distinction, so when learning JavaScript we also learn about statements like function declarations, for loops, if statements, and so forth. We’ll see a few more of these later. functions that evaluate to functions If an expression that evaluates to a function is, well, an expression, and if a return statement can have any expression on its right side… Can we put an expression that evaluates to a function on the right side of a function expression? Yes: () => () => 0 That’s a function! It’s a function that when applied, evaluates to a function that when applied, evaluates to 0. So we have a function, that returns a function, that returns zero. Likewise: () => () => true That’s a function, that returns a function, that returns true: (() => () => true)()() //=> true We could, of course, do the same thing with a block if we wanted: () => () => {return true;} But we generally don’t. Well. We’ve been very clever, but so far this all seems very abstract. Diffraction of a crystal is beautiful and interesting in its own right, but you can’t blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. So… In the next chapter, “I’d Like to Have an Argument, Please,” we’ll see how to make functions practical. |
| 16 | The first sip: Basic Functions Ah. I’d Like to Have an Argument, Please.22 |

</details>

### Technical frame 7: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00573))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00565))_

```text
function decorators
A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. Here's a ridiculously simple decorator: 38
37 As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context.
38 We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args)
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 37 | As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. |
| 38 | We'll see later why an even more useful version would be written (fn) => (...args) =>!fn(...args) |

</details>

### Technical frame 8: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00594))_

> We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00593))_

```
const mapWith = (fn) =>
(array) => map(array, fn);
const squareAll = mapWith((n) => n * n);
squareAll([1, 2, 3])
//=> [1, 4, 9]
```

### Technical frame 9: Picking the Bean: Choice and Truthiness / truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00773))_

> Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00772))_

```
!5
//=> false
!undefined
//=> true
```

### Technical frame 10: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00943))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00944))_

```
const length = (array) => foldWith((first, rest) => 1 + rest, 0, array);
length([1, 2, 3, 4, 5])
//=> 5
```

### Technical frame 11: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01585))_

> This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01584))_

```
const mapWith = (fn, collection) =>
({
[Symbol.iterator] () {
const iterator = collection[Symbol.iterator]();
return {
next () {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : fn(value)});
}
}
}
});
```

### Technical frame 12: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01588))_

> Numbers is an ordered collection. We invoke mapWith((x) => 2 * x, Numbers) and get Evens . Evens works just as if we'd written this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01587))_

```
const Evens = mapWith((x) => 2 * x, Numbers);
for (const i of Evens) {
console.log(i)
}
//=>
0
2
4
...
for (const i of Evens) {
console.log(i)
}
//=>
0
2
4
...
```

### Technical frame 13: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01604))_

> like our other operations, rest preserves the ordered collection semantics of its argument.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01603))_

```
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
const rest = (iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
iterator.next();
return iterator;
}
});
```

### Technical frame 14: Served by the Pot: Collections / Generating Iterables / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01663))_

> When we invoke empty , we get an iterator with no elements. This makes sense, because empty never yields anything. We call its .next() method, but it's done immediately.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01662))_

```
function * empty () {};
empty().next()
//=>
{"done":true}
```

### Technical frame 15: Served by the Pot: Collections / Generating Iterables / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01664))_

> Generator functions can take an argument. Let's use that to illustrate yield :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01663))_

> When we invoke empty , we get an iterator with no elements.

### Technical frame 16: Served by the Pot: Collections / Generating Iterables / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01667))_

> Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01668))_

```
only("you").next()
//=>
{"done":false, value: "you"}
only("the lonely").next()
//=>
{"done":false, value: "the lonely"}
```

### Technical frame 17: Served by the Pot: Collections / Generating Iterables / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01708))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01705))_

> If we call our generator function more than once, we get new iterators.

### Technical frame 18: Served by the Pot: Collections / Generating Iterables / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01727))_

> We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01726))_

```
const isIterable = (something) =>
!!something[Symbol.iterator];
const TreeIterable = (iterable) =>
({
[Symbol.iterator]: function * () {
for (const e of iterable) {
if (isIterable(e)) {
for (const ee of TreeIterable(e)) {
yield ee;
}
}
else {
yield e;
}
}
}
})
for (const i of TreeIterable([1, [2, [3, 4], 5]])) {
console.log(i);
}
//=>
1
2
3
4
5
```

### Technical frame 19: Served by the Pot: Collections / Generating Iterables / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01731))_

> Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01728))_

> But if you can write it as a simple generator, write it as a simple generator.

### Technical frame 20: Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01787))_

> This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01786))_

```
Stack.from([ 0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.first()
```


## Related pages

- [[javascriptallonge-function-return-value]] - narrower topic: Function Return Value shares technical record from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity)() //=> Infinity (2 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements and technical atoms: Iterator shares source evidence from Served by the Pot: Collections / Generating Iterables / javascript's generators: Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:; Iterator shares technical record from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-argument]] - shared statements and technical atoms: Argument shares source evidence from And also: / Combinators and Function Decorators / higher-order functions: As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as argume ... [truncated]; Argument shares technical record from And also: / Combinators and Function Decorators / function decorators: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (3 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Served by the Pot: Collections / Generating Iterables / generators and iterables: Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of r ... [truncated]; Javascript shares technical record from Or even: / back on the block: !5 //=> false !undefined //=> true (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from Served by the Pot: Collections / Generating Iterables / generators and iterables: Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of r ... [truncated]; Object shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms: Element shares source evidence from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that itera ... [truncated]; Element shares technical record from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: const first = (iterable) => iterable[Symbol.iterator]().next().value; const rest = (iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator] ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-iterable]] - shared statements and technical atoms: Iterable shares source evidence from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that itera ... [truncated]; Iterable shares technical record from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: const first = (iterable) => iterable[Symbol.iterator]().next().value; const rest = (iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator] ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-partial-application]] - shared statements and technical atoms: partial application shares source evidence from And also: / Building Blocks / partial application: The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one funct ... [truncated]; partial application shares technical record from And also: / Building Blocks / partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-write]] - shared statements and technical atoms: Write shares source evidence from Served by the Pot: Collections / Generating Iterables / generators and iterables: Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of r ... [truncated]; Write shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-iteration]] - shared technical atoms: Iteration shares technical record from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (3 shared atom(s))
- [[javascriptallonge-method]] - shared technical atoms: Method shares technical record from Served by the Pot: Collections / Generating Iterables / javascript's generators: function * empty () {}; empty().next() //=> {"done":true} (3 shared atom(s))
- [[javascriptallonge-collection]] - shared technical atoms: Collection shares technical record from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared atom(s))
- [[javascriptallonge-operation]] - shared technical atoms: Operation shares technical record from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared atom(s))
- [[javascriptallonge-decorator]] - shared technical atoms: Decorator shares technical record from And also: / Combinators and Function Decorators / function decorators: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))
- [[javascriptallonge-evaluate]] - shared technical atoms: Evaluate shares technical record from Or even: / back on the block: //=> undefined We said that the function returns the result of evaluating a block, and we said that a block is a (possibly empty) list of JavaScript statements separ ... [truncated] (1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from Or even: / back on the block: //=> undefined We said that the function returns the result of evaluating a block, and we said that a block is a (possibly empty) list of JavaScript statements separ ... [truncated] (1 shared atom(s))
- [[javascriptallonge-generator]] - shared technical atoms: Generator shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared atom(s))
- [[javascriptallonge-list]] - shared technical atoms: List shares technical record from Or even: / back on the block: //=> undefined We said that the function returns the result of evaluating a block, and we said that a block is a (possibly empty) list of JavaScript statements separ ... [truncated] (1 shared atom(s))
- [[javascriptallonge-operator]] - shared technical atoms: Operator shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-statement]] - shared technical atoms: Statement shares technical record from Or even: / back on the block: //=> undefined We said that the function returns the result of evaluating a block, and we said that a block is a (possibly empty) list of JavaScript statements separ ... [truncated] (1 shared atom(s))
- [[javascriptallonge-truthiness]] - shared technical atoms: Truthiness shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-body]] - shared statements: Body shares source evidence from Served by the Pot: Collections / Generating Iterables / generators are coroutines: The body of our generator runs until it returns, ends, or encounters a yield statement, which is yield 1; . (4 shared statement(s))
- [[javascriptallonge-copy-write]] - shared statements: Copy on Write shares source evidence from Copy on Write / Functional Iterators / iterating: Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iterator ... [truncated] (2 shared statement(s))
- [[javascriptallonge-functional-iterator]] - shared statements: Functional Iterators shares source evidence from Copy on Write / Functional Iterators / iterating: Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iterator ... [truncated] (1 shared statement(s))
- [[javascriptallonge-parameter]] - shared statements: Parameter shares source evidence from Copy on Write / Making Data Out Of Functions / the vireo: Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data. ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
