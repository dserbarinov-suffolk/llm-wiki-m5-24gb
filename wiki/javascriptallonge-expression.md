---
page_id: javascriptallonge-expression
page_kind: concept
summary: Expression: 19 statement(s) and 30 atom(s) from raw/javascriptallonge.pdf.
page_family: broad-topic
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-expression@3fde5c977d2c452cf432ffe217ecf361
---

# Expression

What [[javascriptallonge]] covers about expression:

## Statements

### Prelude: Values and Expressions over Coffee / reference types

- They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to create an array, you're creating a new, distinct value even if it appears to be the same as some other array value. As we'll see, this is true of many other kinds of values, including functions , the main subject of this book. _(javascriptallonge.pdf (source-range-c98ab3e6-00134))_

### A Rich Aroma: Basic Numbers

- JavaScript, like most languages, has a collection of literals. We saw that an expression consisting solely of numbers, like 42 , is a literal. It represents the number forty-two, which is 42 base 10. Not all numbers are base ten. If we start a literal with a zero, it is an octal literal. So the literal 042 is 42 base 8, which is actually 34 base 10. _(javascriptallonge.pdf (source-range-c98ab3e6-00138))_

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities

- Like arrays, every time you evaluate an expression to produce a function, you get a new function that is not identical to any other function, even if you use the same expression to generate it. 'Function' is a reference type. _(javascriptallonge.pdf (source-range-c98ab3e6-00173))_

### Or even: / back on the block

- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined : _(javascriptallonge.pdf (source-range-c98ab3e6-00237))_

### And also: / variables and bindings

- The expression 'x' (the right side of the function) is evaluated within the environment we just created. _(javascriptallonge.pdf (source-range-c98ab3e6-00301))_

### That Constant Coffee Craving

- This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 . _(javascriptallonge.pdf (source-range-c98ab3e6-00377))_

### Naming Functions / the function keyword

- In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment. _(javascriptallonge.pdf (source-range-c98ab3e6-00508))_

### Naming Functions / function declaration caveats 34

- Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization. _(javascriptallonge.pdf (source-range-c98ab3e6-00536))_

### Magic Names / magic names and fat arrows

- For example, when this expression's inner function is defined with function , arguments[0] refers to its only argument, "inner" : _(javascriptallonge.pdf (source-range-c98ab3e6-00605))_

- But sometimes, a function is a small-f function. It's a simple representation of an expression to be computed. In our example above, row is a Big-F function, but (column) => column * arguments[0] is a small-f function, it exists just to give mapWith something to apply. _(javascriptallonge.pdf (source-range-c98ab3e6-00617))_

### Picking the Bean: Choice and Truthiness / truthiness and operators

- This is more than just an optimization. It's best to think of || and && as control-flow operators. The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. _(javascriptallonge.pdf (source-range-c98ab3e6-00780))_

### Composing and Decomposing Data / Self-Similarity

- We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-c98ab3e6-00865))_

### Plain Old JavaScript Objects / literal object syntax

- Expressions can be used for keys as well. The syntax is to enclose the key's expression in [ and ] : _(javascriptallonge.pdf (source-range-c98ab3e6-01062))_

### A Warm Cup: Basic Strings and Quasi-Literals

- Coffee and a Book An expression is any valid unit of code that resolves to a value.-Mozilla Development Network: Expressions and operators 87 _(javascriptallonge.pdf (source-range-c98ab3e6-01471))_

### A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

- Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-c98ab3e6-01479))_

### A Warm Cup: Basic Strings and Quasi-Literals / evaluation time

- Like any other expression, quasi-literals are evaluated late , when that line or lines of code is evaluated. _(javascriptallonge.pdf (source-range-c98ab3e6-01488))_

### Served by the Pot: Collections / Iteration and Iterables / iterables

- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-c98ab3e6-01527))_

### Lazy and Eager Collections / lazy collection operations

- This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array. _(javascriptallonge.pdf (source-range-c98ab3e6-01761))_

### The Golden Crema: Appendices and Afterwords / How to run the examples

- Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser. _(javascriptallonge.pdf (source-range-c98ab3e6-01926))_


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

### Technical frame 2: Naming Functions / function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00536))_

> Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00535))_

<a id="atom-technical-atom-68d5663ef5a9981c"></a>
```
(function (camelCase) {
return fizzbuzz();
if (camelCase) {
function fizzbuzz () {
return "Fizz" + "Buzz";
}
}
else {
function fizzbuzz () {
return "Fizz" + "Buzz";
}
}
})(true)
//=> 'FizzBuzz'? Or ERROR: Can't find variable: fizzbuzz?
```

### Technical frame 3: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01479))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01478))_

<a id="atom-technical-atom-852bc8ae09d13507"></a>
```
`foobar`
//=> 'foobar'
`fizz` + `buzz`
//=> 'fizzbuzz'
```

### Technical frame 4: Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01761))_

> This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01758))_

<a id="atom-technical-atom-6ea07f1c4e64cc03"></a>
> When working with very large collections and many operations, this can be important.

### Technical frame 5: Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01761))_

> This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01759))_

<a id="atom-technical-atom-9ab381ac2559bb31"></a>
> The effect is even more pronounced when we use methods like first , until , or take :

### Technical frame 6: The Golden Crema: Appendices and Afterwords / How to run the examples

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01926))_

> Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01924))_

<a id="atom-technical-atom-408b209e7e2247a3"></a>
```
100https://github.com
101http://babeljs.io/
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-bind]] - shared technical atoms: Bind shares technical record from That Constant Coffee Craving: ((PI) => // ???? )(3.14159265) (8 shared atom(s))
- [[javascriptallonge-literal]] - shared statements and technical atoms: Literal shares source evidence from Composing and Decomposing Data / Self-Similarity: We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment.; Literal shares technical record from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-quasi]] - shared statements and technical atoms: Quasi shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / evaluation time: Like any other expression, quasi-literals are evaluated late , when that line or lines of code is evaluated.; Quasi shares technical record from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-quasi-literal]] - shared statements and technical atoms: Quasi Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / evaluation time: Like any other expression, quasi-literals are evaluated late , when that line or lines of code is evaluated.; Quasi Literal shares technical record from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-function-keyword]] - shared statements and technical atoms: the function keyword shares source evidence from Naming Functions / the function keyword: In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, b ... [truncated]; the function keyword shares technical record from Naming Functions / the function keyword: (function even (n) { if (n === 0) { return true } else return !even(n - 1) })(5) //=> false (function even (n) { if (n === 0) { return true } else return !even(n - 1 ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.; Object shares technical record from Plain Old JavaScript Objects / literal object syntax: const SecretDecoderRing = { encode (plaintext) { return plaintext .split('') .map( char => char.charCodeAt() ) .map( code => code + 1 ) .map( code => String.fromChar ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-binding]] - shared technical atoms: Binding shares technical record from That Constant Coffee Craving / are consts also from a shadowy planet?: ((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265) (2 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from A Rich Aroma: Basic Numbers / operations on numbers: 2 * 5 + 1 //=> 11 1 + 5 * 2 //=> 11 (2 shared atom(s))

### Shared claims

- [[javascriptallonge-evaluate]] - shared statements: Evaluate shares source evidence from Prelude: Values and Expressions over Coffee / reference types: They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to crea ... [truncated] (4 shared statement(s))
- [[javascriptallonge-coffee]] - shared statements: Coffee shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: Coffee and a Book An expression is any valid unit of code that resolves to a value.-Mozilla Development Network: Expressions and operators 87 (1 shared statement(s))

## Source

- [[javascriptallonge]]
