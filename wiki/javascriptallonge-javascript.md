---
page_id: javascriptallonge-javascript
page_kind: concept
summary: Javascript: 75 statement(s) and 62 atom(s) from raw/javascriptallonge.pdf.
page_family: broad-topic
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-javascript@d99a2e20789be3a89727387920cbd267
---

# Javascript

What [[javascriptallonge]] covers about javascript:

## Statements

### A Pull of the Lever: Prefaces / About JavaScript Allongé

- JavaScript Allongé is a first and foremost, a book about programming with functions . It's written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope. If those terms seem unfamiliar, don't worry: JavaScript Allongé takes great delight in explaining what they mean and why they matter. _(javascriptallonge.pdf (source-range-c98ab3e6-00016))_

- JavaScript Allongé begins at the beginning, with values and expressions, and builds from there to discuss types, identity, functions, closures, scopes, collections, iterators, and many more subjects up to working with classes and instances. _(javascriptallonge.pdf (source-range-c98ab3e6-00017))_

- It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or code-centric. JavaScript idioms like function combinators and decorators leverage JavaScript's power to make code easier to read, modify, debug and refactor. _(javascriptallonge.pdf (source-range-c98ab3e6-00018))_

### A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. For example, JavaScript did not include block-structured variables. Over time, programmers discovered ways to roll their own versions of important features. _(javascriptallonge.pdf (source-range-c98ab3e6-00022))_

- And the variable i is scoped locally to the code within the braces. Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write: _(javascriptallonge.pdf (source-range-c98ab3e6-00025))_

- Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like: _(javascriptallonge.pdf (source-range-c98ab3e6-00030))_

### A Pull of the Lever: Prefaces / About JavaScript Allongé / that's nice. is that the only reason?

- But there's more to it than that . The original JavaScript Allongé was not just written to teach JavaScript: It was written to describe certain ideas in programming: Working with small, independent entities that compose together to make bigger programs. Thus, the focus on things like writing decorators. _(javascriptallonge.pdf (source-range-c98ab3e6-00043))_

### A Pull of the Lever: Prefaces / What JavaScript Allongé is. And isn't.

- JavaScript Allongé is a book about programming with functions. From functions flow many ideas, from decorators to methods to delegation to mixins, and onwards in so many fruitful directions. _(javascriptallonge.pdf (source-range-c98ab3e6-00051))_

- But while JavaScript Allongé attempts to be provocative, it is not prescriptive . There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others. _(javascriptallonge.pdf (source-range-c98ab3e6-00053))_

- JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn't a book about practicing, it's a book about thinking. _(javascriptallonge.pdf (source-range-c98ab3e6-00062))_

### ECMAScript 6 has three major groups of features:

- With ECMAScript 6, JavaScript has become much larger as a language. JavaScript Allongé, the 'Six' Edition is both a comprehensive tour of its features and a rich collection of techniques for making better use of them. You will learn much about functional programming and object-oriented programming. And you'll do so via ES6 code, handed to you in small, easily digestible pieces. _(javascriptallonge.pdf (source-range-c98ab3e6-00078))_

### ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus

- As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. However, you'll not be beaten about the head and neck with dogma. Instead, every section is motivated by relevant dialog and fortified with compelling source examples. As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time. _(javascriptallonge.pdf (source-range-c98ab3e6-00086))_

### ECMAScript 6 has three major groups of features: / About The Sample PDF

- This sample edition of the book includes just a portion of the complete book. Buying the book in progress entitles you to free updates, so download it today 7 ! Besides, there's really no risk at all . If you read JavaScript Allongé, The 'six' edition and it doesn't blow your mind, your money will be cheerfully refunded. _(javascriptallonge.pdf (source-range-c98ab3e6-00092))_

### Prelude: Values and Expressions over Coffee / values are expressions

- First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types . For example, the string "2" is not the same thing as the number 2 . Strings and numbers are different types, so strings and numbers are never identical: _(javascriptallonge.pdf (source-range-c98ab3e6-00116))_

- Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 . _(javascriptallonge.pdf (source-range-c98ab3e6-00118))_

### A Rich Aroma: Basic Numbers

- For example, the largest integer JavaScript can safely 14 handle is 9007199254740991 , or 2 '53' - 1 . Like most programming languages, JavaScript does not allow us to use commas to separate groups of digits. _(javascriptallonge.pdf (source-range-c98ab3e6-00141))_

### A Rich Aroma: Basic Numbers / operations on numbers

- As we've seen, JavaScript has many common arithmetic operators. We can create expressions that look very much like mathematical expressions, for example we can write 1 + 1 or 2 * 3 or 42 34 or even 6 / 2 . These can be combined to make more complex expressions, like 2 * 5 + 1 . _(javascriptallonge.pdf (source-range-c98ab3e6-00153))_

- In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. So: _(javascriptallonge.pdf (source-range-c98ab3e6-00154))_

- JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2) , because the * operator has a higher precedence than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2 , this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the name plus , of course). _(javascriptallonge.pdf (source-range-c98ab3e6-00156))_

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less

- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represent computations to be performed. Like numbers, strings, and arrays, they have a representation. Let's start with the second simplest possible function. 16 In JavaScript, it looks like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00162))_

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

- The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words: _(javascriptallonge.pdf (source-range-c98ab3e6-00195))_

### Or even: / the simplest possible block / undefined

- In JavaScript, the absence of a value is written undefined , and it means there is no value. It will crop up again. undefined is its own type of value, and it acts like a value type: _(javascriptallonge.pdf (source-range-c98ab3e6-00211))_

- Like numbers, booleans and strings, JavaScript can print out the value undefined . _(javascriptallonge.pdf (source-range-c98ab3e6-00214))_

- 18 Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons. This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. We will not take advantage of this feature, but it's helpful to know it exists. _(javascriptallonge.pdf (source-range-c98ab3e6-00217))_

### And also: / call by sharing

- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. As you recall, value types like strings and numbers are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans as it wishes. _(javascriptallonge.pdf (source-range-c98ab3e6-00308))_

- Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-c98ab3e6-00310))_

### shadowy variables from a shadowy planet

- When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor. _(javascriptallonge.pdf (source-range-c98ab3e6-00360))_

### which came first, the chicken or the egg?

- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } . _(javascriptallonge.pdf (source-range-c98ab3e6-00365))_

### That Constant Coffee Craving / inside-out

- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated 'IIFE.' _(javascriptallonge.pdf (source-range-c98ab3e6-00389))_

### That Constant Coffee Craving / const

- JavaScript gives us a way to do that, the const keyword. We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const : _(javascriptallonge.pdf (source-range-c98ab3e6-00405))_

### That Constant Coffee Craving / rebinding

- JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-c98ab3e6-00481))_

### Naming Functions / the function keyword

- JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00488))_

### Naming Functions / function declaration caveats 34

- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-c98ab3e6-00533))_

### Combinators and Function Decorators / higher-order functions

- As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. _(javascriptallonge.pdf (source-range-c98ab3e6-00542))_

### Building Blocks

- When you look at functions within functions in JavaScript, there's a bit of a 'spaghetti code' look to it. The strength of JavaScript is that you can do anything. The weakness is that you will. There are ifs, fors, returns, everything thrown higgledy piggledy together. Although you needn't restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks. _(javascriptallonge.pdf (source-range-c98ab3e6-00565))_

### Summary / Functions

- JavaScript uses const to bind values to names within block scope. _(javascriptallonge.pdf (source-range-c98ab3e6-00630))_

- JavaScript uses function declarations to bind functions to names within function scope. Function declarations are 'hoisted.' _(javascriptallonge.pdf (source-range-c98ab3e6-00631))_


## Technical atoms

### Technical frame 1: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00116))_

> First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types . For example, the string "2" is not the same thing as the number 2 . Strings and numbers are different types, so strings and numbers are never identical:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00114))_

<a id="atom-technical-atom-40e0723bf66bd225"></a>
```
2 === 2
//=> true
'hello' !== 'goodbye'
//=> true
```

### Technical frame 2: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00118))_

> Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00117))_

<a id="atom-technical-atom-583a408c77323f15"></a>
```
2 === '2'
//=> false
true !== 'true'
//=> true
```

### Technical frame 3: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00118))_

> Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00119))_

<a id="atom-technical-atom-48e01153efd33d84"></a>
```
true === false
//=> false
2 !== 5
//=> true
'two' === 'five'
//=> false
```

### Technical frame 4: A Rich Aroma: Basic Numbers / operations on numbers

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00156))_

> JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2) , because the * operator has a higher precedence than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2 , this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the name plus , of course).

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00155))_

<a id="atom-technical-atom-9dfa7b23a97da046"></a>
```
2 * 5 + 1
//=> 11
1 + 5 * 2
//=> 11
```

### Technical frame 5: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00195))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00196))_

<a id="atom-technical-atom-f6e57dd43b3f2e06"></a>
```
//=> 2
(1 + 1, 2 + 2)
```

### Technical frame 6: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00195))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00200))_

<a id="atom-technical-atom-cba8be65cdd5c811"></a>
```
() =>
(1 + 1, 2 + 2)
```

### Technical frame 7: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00214))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00212))_

<a id="atom-technical-atom-62b489c3348a33a0"></a>
```
undefined
```

### Technical frame 8: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00214))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00213))_

<a id="atom-technical-atom-d7f4dab15ef86a18"></a>
```
//=> undefined
```

### Technical frame 9: shadowy variables from a shadowy planet

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00360))_

> When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00359))_

<a id="atom-technical-atom-c23519ba9922cace"></a>
```
(x) =>
(x, y) =>
(w, z) =>
(w) =>
x + y + z
```

### Technical frame 10: which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00365))_

> JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00366))_

<a id="atom-technical-atom-6cb62b7189b018dc"></a>
> If you don't want your code to operate directly within the global environment, what can you do?

### Technical frame 11: which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00365))_

> JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00367))_

<a id="atom-technical-atom-8cdbcf80542c25d7"></a>
```
// top of the file
(() => {
// ... lots of JavaScript ...
})();
// bottom of the file
```

### Technical frame 12: That Constant Coffee Craving / rebinding

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00481))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00478))_

<a id="atom-technical-atom-3fadc6bc95295bf5"></a>
```
const evenStevens = (n) => {
if (n === 0) {
return true;
}
else if (n == 1) {
return false;
}
else {
n = n - 2;
return evenStevens(n);
}
}
evenStevens(42)
//=> true
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-allong]] - shared statements and technical atoms: Allong shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé: JavaScript Allongé is a first and foremost, a book about programming with functions . It's written in JavaScript, because JavaScript hits the perfect sweet spot of b ... [truncated]; Allong shares technical record from JavaScript Allongé, the 'Six' Edition / Reg 'raganwald' Braithwaite: function foo (first, ...rest) { // ... } (10 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from Plain Old JavaScript Objects: In JavaScript, an object is a map from string keys to values.; Object shares technical record from Plain Old JavaScript Objects / literal object syntax: { year: 2012, month: 6, day: 14 } (3 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-bind]] - shared statements and technical atoms: Bind shares source evidence from And also: / call by sharing: We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to ... [truncated]; Bind shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching: const [what] = []; (2 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-ecmascript]] - shared statements and technical atoms: Ecmascript shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. For example, JavaScript did ... [truncated]; Ecmascript shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (4 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-array]] - shared statements and technical atoms: Array shares source evidence from Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals: JavaScript has a literal syntax for creating an array: The [ and ] characters. We can create an empty array:; Array shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals: [] //=> [] (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-decorator]] - shared statements and technical atoms: Decorator shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé: It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or ... [truncated]; Decorator shares technical record from Combinators and Function Decorators / function decorators: const compose = (a, b) => (c) => a(b(c)); const cookAndEat = compose(eat, cook); (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-edition]] - shared statements and technical atoms: Edition shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: JavaScript Allongé, The 'Six' Edition packs all the goodness of JavaScript Allongé into a new, updated package that is relevant for programmers working with (or plan ... [truncated]; Edition shares technical record from JavaScript Allongé, the 'Six' Edition / Reg 'raganwald' Braithwaite: Contents | A Pull of the Lever: Prefaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | i | | --- | --- | | About JavaScript Allongé . . . . ... [truncated] (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms: Element shares source evidence from Garbage, Garbage Everywhere / some history: Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of ar ... [truncated]; Element shares technical record from Garbage, Garbage Everywhere / some history: const cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d; (1 shared statement(s), 3 shared atom(s))

### Shared claims

- [[javascriptallonge-evaluate]] - shared statements: Evaluate shares source evidence from Picking the Bean: Choice and Truthiness / truthiness and the ternary operator: Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true . (2 shared statement(s))
- [[javascriptallonge-functional]] - shared statements: Functional shares source evidence from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated] (1 shared statement(s))
- [[javascriptallonge-quasi]] - shared statements: Quasi shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-quasi-literal]] - shared statements: Quasi Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-ternary-operator]] - shared statements: Ternary Operator shares source evidence from Picking the Bean: Choice and Truthiness / truthiness and the ternary operator: JavaScript inherited an operator from the C family of languages, the ternary operator. It's the only operator that takes three arguments. It looks like this: first ? ... [truncated] (1 shared statement(s))

### Topics

- [[javascriptallonge-javascript-allong]] - narrower topic: About JavaScript Allongé shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé: JavaScript Allongé is a first and foremost, a book about programming with functions . It's written in JavaScript, because JavaScript hits the perfect sweet spot of b ... [truncated]; About JavaScript Allongé shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (14 shared statement(s), 4 shared atom(s))

## Source

- [[javascriptallonge]]
