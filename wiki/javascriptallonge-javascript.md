---
page_id: javascriptallonge-javascript
page_kind: concept
summary: Javascript: 75 statement(s) and 80 atom(s) from raw/javascriptallonge.pdf.
page_family: broad-topic
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-javascript@1f18d82b31a663b873b7b326a1bed658
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

### And also: / Closures and Scope / shadowy variables from a shadowy planet

- When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor. _(javascriptallonge.pdf (source-range-c98ab3e6-00360))_

### And also: / Closures and Scope / which came first, the chicken or the egg?

- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } . _(javascriptallonge.pdf (source-range-c98ab3e6-00365))_

### And also: / That Constant Coffee Craving / inside-out

- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated 'IIFE.' _(javascriptallonge.pdf (source-range-c98ab3e6-00389))_

### And also: / That Constant Coffee Craving / const

- JavaScript gives us a way to do that, the const keyword. We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const : _(javascriptallonge.pdf (source-range-c98ab3e6-00405))_

### And also: / That Constant Coffee Craving / rebinding

- JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-c98ab3e6-00481))_

### And also: / Naming Functions / the function keyword

- JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00488))_

### And also: / Naming Functions / function declaration caveats 34

- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-c98ab3e6-00533))_

### And also: / Combinators and Function Decorators / higher-order functions

- As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. _(javascriptallonge.pdf (source-range-c98ab3e6-00542))_

### And also: / Building Blocks

- When you look at functions within functions in JavaScript, there's a bit of a 'spaghetti code' look to it. The strength of JavaScript is that you can do anything. The weakness is that you will. There are ifs, fors, returns, everything thrown higgledy piggledy together. Although you needn't restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks. _(javascriptallonge.pdf (source-range-c98ab3e6-00565))_

### And also: / Summary / Functions

- JavaScript uses const to bind values to names within block scope. _(javascriptallonge.pdf (source-range-c98ab3e6-00630))_

- JavaScript uses function declarations to bind functions to names within function scope. Function declarations are 'hoisted.' _(javascriptallonge.pdf (source-range-c98ab3e6-00631))_

- But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. _(javascriptallonge.pdf (source-range-c98ab3e6-00034))_
- JavaScript Allongé, The 'Six' Edition packs all the goodness of JavaScript Allongé into a new, updated package that is relevant for programmers working with (or planning to work with) the latest version of JavaScript. _(javascriptallonge.pdf (source-range-c98ab3e6-00039))_
- In JavaScript, every undefined is identical to every other undefined . _(javascriptallonge.pdf (source-range-c98ab3e6-00218))_
- JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. _(javascriptallonge.pdf (source-range-c98ab3e6-00652))_
- Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-c98ab3e6-00678))_
- In 'Ye Olde Days,' 53 JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice , or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. _(javascriptallonge.pdf (source-range-c98ab3e6-00708))_
- Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' . _(javascriptallonge.pdf (source-range-c98ab3e6-00748))_
- JavaScript inherited an operator from the C family of languages, the ternary operator. _(javascriptallonge.pdf (source-range-c98ab3e6-00750))_
- Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true . _(javascriptallonge.pdf (source-range-c98ab3e6-00756))_
- JavaScript has a literal syntax for creating an array: The [ and ] characters. _(javascriptallonge.pdf (source-range-c98ab3e6-00800))_
- JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. _(javascriptallonge.pdf (source-range-c98ab3e6-00845))_
- From its very inception, JavaScript has striven to avoid catastrophic errors. _(javascriptallonge.pdf (source-range-c98ab3e6-00849))_
- JavaScript cannot throw first away. _(javascriptallonge.pdf (source-range-c98ab3e6-00940))_
- So we know that JavaScript is going to hang on to 1 . _(javascriptallonge.pdf (source-range-c98ab3e6-00940))_
- Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . _(javascriptallonge.pdf (source-range-c98ab3e6-00941))_
- In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. _(javascriptallonge.pdf (source-range-c98ab3e6-01026))_
- JavaScript has dictionaries, and it calls them 'objects.' The word 'object' is loaded in programming circles, due to the widespread use of the term 'object-oriented programming' that was coined by Alan Kay but has since come to mean many, many things to many different people. _(javascriptallonge.pdf (source-range-c98ab3e6-01048))_
- In JavaScript, an object is a map from string keys to values. _(javascriptallonge.pdf (source-range-c98ab3e6-01049))_
- JavaScript has a literal syntax for creating objects. _(javascriptallonge.pdf (source-range-c98ab3e6-01052))_
- In JavaScript, almost every type of value can mutate . _(javascriptallonge.pdf (source-range-c98ab3e6-01099))_
- Like some imperative programming languages, JavaScript allows you to re-assign the value bound to parameters. _(javascriptallonge.pdf (source-range-c98ab3e6-01138))_
- JavaScript does not permit us to rebind a name that has been bound with const . _(javascriptallonge.pdf (source-range-c98ab3e6-01143))_
- JavaScript has one more way to bind a name to a value, var . _(javascriptallonge.pdf (source-range-c98ab3e6-01163))_
- JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. _(javascriptallonge.pdf (source-range-c98ab3e6-01261))_
- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. _(javascriptallonge.pdf (source-range-c98ab3e6-01291))_
- JavaScript would apply fn to every element. _(javascriptallonge.pdf (source-range-c98ab3e6-01296))_
- Practically speaking, languages like JavaScript already provide arrays with mapping and folding methods, choice operations, and other rich constructs. _(javascriptallonge.pdf (source-range-c98ab3e6-01378))_
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. _(javascriptallonge.pdf (source-range-c98ab3e6-01491))_
- Many objects in JavaScript can model collections of things. _(javascriptallonge.pdf (source-range-c98ab3e6-01498))_
- Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-c98ab3e6-01591))_
- But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next() , it runs until it returns, ends, or yields. _(javascriptallonge.pdf (source-range-c98ab3e6-01676))_
- We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call. _(javascriptallonge.pdf (source-range-c98ab3e6-01678))_
- When he's not shipping JavaScript, Ruby, CoffeeScript and Java applications scaling out to millions of users, Reg 'Raganwald' Braithwaite has authored libraries 221 for JavaScript, CoffeeScript, and Ruby programming such as Allong.es, Method Combinators, Katy, JQuery Combinators, YouAreDaChef, andand, and others. _(javascriptallonge.pdf (source-range-c98ab3e6-02007))_

## Technical atoms

### Technical frame 1: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00028))_

> Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Ruby, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00026))_

<a id="atom-technical-atom-4d5b8dc98853c3bb"></a>
```
var i;
for (i = 0; i < array.length; ++i) {
(function (i) {
// ...
})(i)
}
```

### Technical frame 2: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00032))_

> The first edition of JavaScript Allongé explained these and many other patterns for writing flexible and composable programs in JavaScript, but the intention wasn't to explain how to work around JavaScript's missing features: The intention was to explain why the style of programming exemplified by the missing features is important.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00031))_

<a id="atom-technical-atom-84f4e345e4c1dec2"></a>
```
function foo () {
var first = arguments[0],
rest
= [].slice.call(arguments, 1);
// ...
}
```

### Technical frame 3: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00036))_

> And i is scoped to the for loop. We can also write:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00035))_

<a id="atom-technical-atom-339e65417e2add1c"></a>
```
for (let i = 0; i < array.length; ++i) {
// ...
}
```

### Technical frame 4: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00038))_

> And presto, rest collects the rest of the arguments without a lot of malarky involving slicing arguments . Not having to work around these kinds of missing features makes JavaScript Allongé a better book , because it can focus on the why to do something and when to do it, instead of on the how to make it work

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00037))_

<a id="atom-technical-atom-ad49ef49c0ac5fcf"></a>
```
function foo (first, ...rest) {
// ...
}
```

### Technical frame 5: ECMAScript 6 has three major groups of features:

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00078))_

> With ECMAScript 6, JavaScript has become much larger as a language. JavaScript Allongé, the 'Six' Edition is both a comprehensive tour of its features and a rich collection of techniques for making better use of them. You will learn much about functional programming and object-oriented programming. And you'll do so via ES6 code, handed to you in small, easily digestible pieces.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00080))_

<a id="atom-technical-atom-24432d50b19465df"></a>
```text
2 http://www.2ality.com
4 http://exploringjs.com
3 http://ecmanauten.de
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 2 | http://www.2ality.com |
| 4 | http://exploringjs.com |
| 3 | http://ecmanauten.de |

</details>

### Technical frame 6: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00105))_

> All values are expressions. That's easy! Are there any other kinds of expressions? Sure! let's go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let's hand over some ground coffee plus some boiling water.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00104))_

<a id="atom-technical-atom-b864e01d2b117c1e"></a>
```
42
//=> 42
```

### Technical frame 7: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00118))_

> Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00110))_

<a id="atom-technical-atom-c64bb3ece0d1ebd3"></a>
```text
10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' and so does the computer.
11 In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 10 | Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' and so does the computer. |
| 11 | In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values. |

</details>

### Technical frame 8: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00118))_

> Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00112))_

<a id="atom-technical-atom-2ce83e0abe51f9aa"></a>
```text
2 In JavaScript, we test whether two values are identical with the operator, and whether they are === not identical with the operator: !== 2 === 2 //=> true 'hello' !== 'goodbye' //=> true How does work, exactly? Imagine that you’re shown a cup of coffee. And then you’re shown === another cup of coffee. Are the two cups “identical?” In JavaScript, there are four possibilities: First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types. For example, the string "2" is not the same thing as the number 2. Strings and numbers are different types, so strings and numbers are never identical:
2 === '2' //=> false true !== 'true' //=> true Second, sometimes, the cups are of the same type–perhaps two espresso cups–but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2. true === false //=> false
2 !== 5 //=> true 'two' === 'five' //=> false What if the cups are of the same type and the contents are the same? Well, JavaScript’s third and fourth possibilities cover that. Prelude: Values and Expressions over Coffee xvii value types Third, some types of cups have no distinguishing marks on them. If they are the same kind of cup, and they hold the same contents, we have no way to tell the difference between them. This is the case with the strings, numbers, and booleans we have seen so far.
2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably. We haven’t encountered the fourth possibility yet. Stretching the metaphor somewhat, some types of cups have a serial number on the bottom. So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them. Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d’Italia reference types So what kinds of values might be the same type and have the same contents, but not be considered identical to JavaScript? Let’s meet a data structure that is very common in contemporary programming languages, the Array (other languages sometimes call it a List or a Vector). Prelude: Values and Expressions over Coffee xviii An array looks like this: [1, 2, 3]. This is an expression, and you can combine [] with other expressions. Go wild with things like: [2-1, 2, 2+1] [1, 1+1, 1+1+1] Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of is identical to every other value of 42? Try these for yourself: 42 [2-1, 2, 2+1] === [1,2,3] [1,2,3] === [1, 2, 3] [1, 2, 3] === [1, 2, 3] How about that! When you type or any of its variations, you are typing an expression [1, 2, 3] that generates its own unique array that is not identical to any other array, even if that other array also looks like 3]. It’s as if JavaScript is generating new cups of coffee with serial numbers [1, 2, on the bottom. They look the same, but if you examine them with ===, you see that they are different. Every time you evaluate an expression (including typing something in) to create an array, you’re creating a new, distinct value even if it appears to be the same as some other array value. As we’ll see, this is true of many other kinds of values, including functions, the main subject of this book.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 2 | In JavaScript, we test whether two values are identical with the operator, and whether they are === not identical with the operator:!== 2 === 2 //=> true 'hello'!== 'goodbye' //=> true How does work, exactly? Imagine that you’re shown a cup of coffee. And then you’re shown === another cup of coffee. Are the two cups “identical?” In JavaScript, there are four possibilities: First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types. For example, the string "2" is not the same thing as the number 2. Strings and numbers are different types, so strings and numbers are never identical: |
| 2 | === '2' //=> false true!== 'true' //=> true Second, sometimes, the cups are of the same type–perhaps two espresso cups–but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2. true === false //=> false 2!== 5 //=> true 'two' === 'five' //=> false What if the cups are of the same type and the contents are the same? Well, JavaScript’s third and fourth possibilities cover that. Prelude: Values and Expressions over Coffee xvii value types Third, some types of cups have no distinguishing marks on them. If they are the same kind of cup, and they hold the same contents, we have no way to tell the difference between them. This is the case with the strings, numbers, and booleans we have seen so far. |
| 2 | + 2 === 4 //=> true (2 + 2 === 4) === (2!== 5) //=> true Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably. We haven’t encountered the fourth possibility yet. Stretching the metaphor somewhat, some types of cups have a serial number on the bottom. So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them. Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d’Italia reference types So what kinds of values might be the same type and have the same contents, but not be considered identical to JavaScript? Let’s meet a data structure that is very common in contemporary programming languages, the Array (other languages sometimes call it a List or a Vector). Prelude: Values and Expressions over Coffee xviii An array looks like this: [1, 2, 3]. This is an expression, and you can combine [] with other expressions. Go wild with things like: [2-1, 2, 2+1] [1, 1+1, 1+1+1] Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of is identical to every other value of 42? Try these for yourself: 42 [2-1, 2, 2+1] === [1,2,3] [1,2,3] === [1, 2, 3] [1, 2, 3] === [1, 2, 3] How about that! When you type or any of its variations, you are typing an expression [1, 2, 3] that generates its own unique array that is not identical to any other array, even if that other array also looks like 3]. It’s as if JavaScript is generating new cups of coffee with serial numbers [1, 2, on the bottom. They look the same, but if you examine them with ===, you see that they are different. Every time you evaluate an expression (including typing something in) to create an array, you’re creating a new, distinct value even if it appears to be the same as some other array value. As we’ll see, this is true of many other kinds of values, including functions, the main subject of this book. |

</details>

### Technical frame 9: Prelude: Values and Expressions over Coffee / values are expressions

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

### Technical frame 10: Prelude: Values and Expressions over Coffee / values are expressions

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

### Technical frame 11: Prelude: Values and Expressions over Coffee / values are expressions

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

### Technical frame 12: Prelude: Values and Expressions over Coffee / values are expressions / value types

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00124))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same 'content.' Strings, numbers, and booleans are examples of what JavaScript calls 'value' or 'primitive' types. We'll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00123))_

<a id="atom-technical-atom-1e1cd89b82275076"></a>
```
2 + 2 === 4
//=> true
(2 + 2 === 4) === (2 !== 5)
//=> true
```

### Technical frame 13: Prelude: Values and Expressions over Coffee / values are expressions / value types

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00126))_

> Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d'Italia

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00125))_

<a id="atom-technical-atom-63d3491cbf82f2a9"></a>
> So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them.

### Technical frame 14: A Rich Aroma: Basic Numbers / floating

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00151))_

> But as a rule, if you need to work with real numbers, you should have more than a nodding acquaintance with the IEEE Standard for Floating-Point Arithmetic 15 . Professional programmers almost never use floating point numbers to represent monetary amounts. For example, '$43.21' will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21 . In this book, we need not think about such details, but outside of this book, we must.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00148))_

<a id="atom-technical-atom-aee77d48a5615cc7"></a>
```text
13 http://en.wikipedia.org/wiki/Double-precision_floating-point_format
14 Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js , it will happily report that the answer is 18014398509481982 . But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 13 | http://en.wikipedia.org/wiki/Double-precision_floating-point_format |
| 14 | Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations. |

</details>

### Technical frame 15: A Rich Aroma: Basic Numbers / floating

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00144))_

> It's tempting to think we now have everything we need to do things like handle amounts of money, but as the late John Belushi would say, 'Nooooooooooooooooooooo.' A computer's internal representation for a floating point number is binary, while our literal number was in base ten. This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00151))_

<a id="atom-technical-atom-dc77c060fb9232f3"></a>
> Professional programmers almost never use floating point numbers to represent monetary amounts.

### Technical frame 16: A Rich Aroma: Basic Numbers / operations on numbers

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

### Technical frame 17: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00164))_

> This is a function that is applied to no values and returns 0 . Let's verify that our function is a value like all others:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00163))_

<a id="atom-technical-atom-55063c246fc08fa6"></a>
```
() => 0
```

### Technical frame 18: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00166))_

> What!? Why didn't it type back () => 0 for us? This seems to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What's going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a br

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00165))_

<a id="atom-technical-atom-a6c1f98f651551c3"></a>
```
(() => 0)
//=> [Function]
```

### Technical frame 19: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00173))_

> Like arrays, every time you evaluate an expression to produce a function, you get a new function that is not identical to any other function, even if you use the same expression to generate it. 'Function' is a reference type.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00172))_

<a id="atom-technical-atom-1bdec14274efa197"></a>
```
(() => 0) === (() => 0)
//=> false
```

### Technical frame 20: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / applying functions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00178))_

> Right now, we only know about one such expression: () => 0 , so let's use it. We'll put it in parentheses 17 to keep the parser happy, like we did above: (() => 0) . Since we aren't giving it any arguments, we'll simply write () after the expression. So we write:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00177))_

<a id="atom-technical-atom-049e0946eb2ab91d"></a>
```
fn_expr(args)
```

### Technical frame 21: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00195))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00196))_

<a id="atom-technical-atom-f6e57dd43b3f2e06"></a>
```
//=> 2
(1 + 1, 2 + 2)
```

### Technical frame 22: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00195))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00200))_

<a id="atom-technical-atom-cba8be65cdd5c811"></a>
```
() =>
(1 + 1, 2 + 2)
```

### Technical frame 23: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00214))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00212))_

<a id="atom-technical-atom-62b489c3348a33a0"></a>
```
undefined
```

### Technical frame 24: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00214))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00213))_

<a id="atom-technical-atom-d7f4dab15ef86a18"></a>
```
//=> undefined
```

### Technical frame 25: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00237))_

> But no matter how we arrange them, a block with one or more expressions still evaluates to undefined :

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00238))_

<a id="atom-technical-atom-bb398f7a1ecce0a5"></a>
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

### Technical frame 26: And also: / Closures and Scope / shadowy variables from a shadowy planet

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00358))_

> The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x , it is ignored when evaluating x + y . JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00357))_

<a id="atom-technical-atom-b47eb83b86d8ebfa"></a>
```
(x) =>
(x, y) => x + y
```

### Technical frame 27: And also: / Closures and Scope / shadowy variables from a shadowy planet

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

### Technical frame 28: And also: / Closures and Scope / which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00365))_

> JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00366))_

<a id="atom-technical-atom-6cb62b7189b018dc"></a>
> If you don't want your code to operate directly within the global environment, what can you do?

### Technical frame 29: And also: / Closures and Scope / which came first, the chicken or the egg?

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

### Technical frame 30: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00391))_

> Everything else is encapsulated in its body. That's how it should be, naming PI is its concern, not ours. The other formulation:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00390))_

<a id="atom-technical-atom-c7f7381982c5437e"></a>
```
(diameter) =>
// ...
```

### Technical frame 31: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00407))_

> The const keyword introduces one or more bindings in the block that encloses it. It doesn't incur the cost of a function invocation. That's great. Even better, it puts the symbol (like PI ) close to the value ( 3.14159265 ). That's much better than what we were writing.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00406))_

<a id="atom-technical-atom-0589efc09f36452c"></a>
```
(diameter) => {
const PI = 3.14159265;
return diameter * PI
}
```

### Technical frame 32: And also: / That Constant Coffee Craving / rebinding

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

### Technical frame 33: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00514))_

> Now, the function's actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00513))_

<a id="atom-technical-atom-41934a4235867742"></a>
```
someBackboneView.on('click', function clickHandler () {
//...
});
```

### Technical frame 34: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00563))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00555))_

<a id="atom-technical-atom-73d86f3bb2def087"></a>
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

### Technical frame 35: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00571))_

> If that was all there was to it, composition wouldn't matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00570))_

<a id="atom-technical-atom-70f9079dd32050af"></a>
```
const compose = (a, b) => (c) => a(b(c));
const cookAndEat = compose(eat, cook);
```

### Technical frame 36: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00572))_

> In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00571))_

<a id="atom-technical-atom-cfaa3155b7ac1dea"></a>
> The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

### Technical frame 37: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00588))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00585))_

<a id="atom-technical-atom-8f517a4c4e32b9dc"></a>
```text
39 http://underscorejs.org
41 If we don't want to sort out Underscore, we can also write the following: const map = (a, fn) => a.map(fn); , and trust that it works even though we haven't discussed methods yet.
40 Modern JavaScript implementations provide a map method for arrays, but Underscore's implementation also works with older browsers if you are working with that headache.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 39 | http://underscorejs.org |
| 41 | If we don't want to sort out Underscore, we can also write the following: const map = (a, fn) => a.map(fn);, and trust that it works even though we haven't discussed methods yet. |
| 40 | Modern JavaScript implementations provide a map method for arrays, but Underscore's implementation also works with older browsers if you are working with that headache. |

</details>

### Technical frame 38: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00602))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00598))_

<a id="atom-technical-atom-5bb18c52a0c78571"></a>
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

### Technical frame 39: Recipes with Basic Functions / Partial Application

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00643))_

> These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00642))_

<a id="atom-technical-atom-83e28a0f45b81408"></a>
```text
Partial Application
In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libraries provide some form of partial application. You'll find examples in Lemonad 45 from Michael Fogus, Functional JavaScript 46 from Oliver Steele and the terse but handy node-ap 47 from James Halliday.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 45 | from Michael Fogus, Functional JavaScript |
| 46 | from Oliver Steele and the terse but handy node-ap |
| 47 | from James Halliday. |

</details>

### Technical frame 40: Recipes with Basic Functions / Partial Application

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00648))_

> We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00646))_

<a id="atom-technical-atom-695bbaa3f7cd2b31"></a>
```text
45 https://github.com/fogus/lemonad 46 http://osteele.com/sources/javascript/functional/ 47 https://github.com/substack/node-ap 48
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 45 | https://github.com/fogus/lemonad |
| 46 | http://osteele.com/sources/javascript/functional/ |
| 47 | https://github.com/substack/node-ap 48 |

</details>

### Technical frame 41: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00657))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00653))_

<a id="atom-technical-atom-05445cf32d19c6d1"></a>
```
['1', '2', '3'].map(parseFloat)
//=> [1, 2, 3]
```

### Technical frame 42: Recipes with Basic Functions / Left-Variadic Functions / a history lesson

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00714))_

> This is a right-variadic function , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00709))_

<a id="atom-technical-atom-185649a0505afc33"></a>
```
var __slice = Array.prototype.slice;
function rightVariadic (fn) {
if (fn.length < 1) return fn;
return function () {
var ordinaryArgs = (1 <= arguments.length ?
__slice.call(arguments, 0, fn.length - 1) : []),
restOfTheArgsList = __slice.call(arguments, fn.length - 1),
args = (fn.length <= arguments.length ?
ordinaryArgs.concat([restOfTheArgsList]) : []);
return fn.apply(this, args);
}
};
var firstAndButFirst = rightVariadic(function test (first, butFirst) {
return [first, butFirst]
});
firstAndButFirst('why', 'hello', 'there', 'little', 'droid')
//=> ["why",["hello","there","little","droid"]]
```

### Technical frame 43: Picking the Bean: Choice and Truthiness / truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00760))_

> Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00759))_

<a id="atom-technical-atom-cb98425a31f8e87a"></a>
```
!5
//=> false
!undefined
//=> true
```

### Technical frame 44: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00808))_

> This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00801))_

<a id="atom-technical-atom-abf332c98aac0fdf"></a>
```
[]
//=> []
```

### Technical frame 45: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00845))_

> That match would fail because the array doesn't have an element to assign to what . But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. Therefore:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00844))_

<a id="atom-technical-atom-31853146d3cd854e"></a>
```
const [what] = [];
```

### Technical frame 46: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

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

### Technical frame 47: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

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

### Technical frame 48: Composing and Decomposing Data / Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00940))_

> Note that while evaluating mapWith(fn, rest) , JavaScript must retain the value first or fn(first) , plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result. JavaScript cannot throw first away. So we know that JavaScript is going to hang on to 1 .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00939))_

<a id="atom-technical-atom-f0b470702aeddcd8"></a>
```
const mapWith = function (fn, [first, ...rest]) {
if (first === undefined) {
return [];
}
else {
const _temp1 = fn(first),
_temp2 = mapWith(fn, rest),
_temp3 = [_temp1, ..._temp2];
return _temp3;
}
}
```

### Technical frame 49: Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00950))_

> There are three places it returns. The first two don't return anything, they don't matter. But the third is fn.apply(this, args) . This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. It isn't going to do any more work, so it can throw its existing stack frame away.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00949))_

<a id="atom-technical-atom-8b535f2755dca7fd"></a>
```
const maybe = (fn) =>
function (...args) {
if (args.length === 0) {
return;
}
else {
for (let arg of args) {
if (arg == null) return;
}
return fn.apply(this, args);
}
}
```

### Technical frame 50: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00967))_

> Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00964))_

<a id="atom-technical-atom-09b3f51b7d0928fc"></a>
```
const mapWithDelaysWork = (fn, [first, ...rest], prepend) =>
first === undefined
? prepend
: mapWithDelaysWork(fn, rest, [...prepend, fn(first)]);
const mapWith = callLast(mapWithDelaysWork, []);
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
We can use it with ridiculously large arrays:
```

### Technical frame 51: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00967))_

> Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00965))_

<a id="atom-technical-atom-a5e35321dc80423c"></a>
```
mapWith((x) => x * x, [
0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10,
11,
12,
13,
14,
15,
16,
17,
18,
19,
20,
21,
22,
23,
24,
25,
26,
27,
28,
29,
30,
31,
32,
33,
34,
35,
36,
37,
38,
39,
40,
41,
42,
43,
44,
45,
46,
47,
48,
49,
50,
51,
52,
53,
54,
55,
56,
57,
58,
59,
60,
61,
62,
63,
64,
65,
66,
67,
68,
69,
70,
71,
72,
73,
74,
75,
76,
77,
78,
79,
80,
81,
82,
83,
84,
85,
86,
87,
88,
89,
90,
91,
92,
93,
94,
95,
96,
97,
98,
99,
// ...
2980, 2981, 2982, 2983, 2984, 2985, 2986, 2987, 2988, 2989,
2990, 2991, 2992, 2993, 2994, 2995, 2996, 2997, 2998, 2999 ])
//=> [0,1,4,9,16,25,36,49,64,81,100,121,144,169,196, ...
```

### Technical frame 52: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00967))_

> Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00966))_

<a id="atom-technical-atom-3439b2237aced771"></a>
| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |

<details>
<summary>Raw table text</summary>

```text
converting non-tail-calls to tail-calls
| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |
```

</details>

### Technical frame 53: Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01021))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01015))_

<a id="atom-technical-atom-5f9b1798e734d975"></a>
```
const cons = (a, d) => [a, d],
car
= ([a, d]) => a,
cdr
= ([a, d]) => d;
```

### Technical frame 54: Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01021))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01020))_

<a id="atom-technical-atom-53c810020d4e78ef"></a>
```
const node5 = [5,null],
node4 = [4, node5],
node3 = [3, node4],
node2 = [2, node3],
node1 = [1, node2];
const oneToFive = node1;
```

### Technical frame 55: Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01026))_

> Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is fas

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01025))_

<a id="atom-technical-atom-26303fe469ee0e47"></a>
```
cdr(oneToFive)
//=> [2,[3,[4,[5,null]]]]
```

### Technical frame 56: Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01054))_

> Two objects created with separate evaluations have differing identities, just like arrays:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01053))_

<a id="atom-technical-atom-86ff9c88f6398559"></a>
```
{ year: 2012, month: 6, day: 14 }
```

### Technical frame 57: Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01079))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01080))_

<a id="atom-technical-atom-154953666ca27427"></a>
```
const description = ({name: { first }, occupation: { title } }) =>
`${first} is a ${title}`;
description(user)
//=> "Reginald is a Author"
And that same syntax works for literals:
const abbrev = ({name: { first, last }, occupation: { title } }) => {
```

### Technical frame 58: Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01079))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01081))_

<a id="atom-technical-atom-33b47d4af6a385f1"></a>
```
const abbrev = ({name: { first, last }, occupation: { title } }) =>
return { first, last, title};
}
abbrev(user)
//=> {"first":"Reginald","last":"Braithwaite","title":"Author"}
```

### Technical frame 59: Mutation

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01105))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01100))_

<a id="atom-technical-atom-4843398da358010b"></a>
```
const oneTwoThree = [1, 2, 3];
oneTwoThree[0] = 'one';
oneTwoThree
//=> [ 'one', 2, 3 ]
```

### Technical frame 60: Mutation

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01107))_

> Both halloween and allHallowsEve are bound to the same array value within the local environment. And also:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01106))_

<a id="atom-technical-atom-7b9965fb0f436cd7"></a>
```
const allHallowsEve = [2012, 10, 31]
const halloween = allHallowsEve;
```

### Technical frame 61: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01143))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01140))_

<a id="atom-technical-atom-dd47fb0868c56680"></a>
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

### Technical frame 62: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01146))_

> We took the time to carefully examine what happens with bindings in environments. Let's take the time to explore what happens with reassigning values to variables. The key is to understand that we are rebinding a different value to the same name in the same environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01145))_

<a id="atom-technical-atom-d1224ba9068cb7b9"></a>
```
let age = 52;
age = 53;
age
//=> 53
```

### Technical frame 63: Reassignment / mixing let and const / var

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

### Technical frame 64: Reassignment / mixing let and const / var

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

### Technical frame 65: Reassignment / mixing let and const / var

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

### Technical frame 66: Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01176))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01173))_

<a id="atom-technical-atom-e7a670d4286bc042"></a>
```
const factorial = (n) => {
let innerFactorial = function innerFactorial (x, y) {
if (x == 1) {
return y;
}
else {
return innerFactorial(x-1, x * y);
}
}
return innerFactorial(n, 1);
}
JavaScript hoists the let and the assignment. But not so with var:
const factorial = (n) => {
return innerFactorial(n, 1);
var innerFactorial = function innerFactorial (x, y) {
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

### Technical frame 67: Reassignment / mixing let and const / var

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

### Technical frame 68: Reassignment / why const and let were invented

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01181))_

> Hopefully, you can think of a faster way to calculate this sum. 72 And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. But is this ever a problem?

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01180))_

<a id="atom-technical-atom-29d2242892772137"></a>
```
var sum = 0;
for (var i = 1; i <= 100; i++) {
sum = sum + i
}
sum
#=> 5050
```

### Technical frame 69: Copy on Write / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01263))_

> Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01262))_

<a id="atom-technical-atom-c0033c3f5acdc292"></a>
```
const arraySum = (array) => {
let sum = 0;
for (let i = 0; i < array.length; ++i) {
sum += array[i];
}
return sum
}
arraySum([1, 4, 9, 16, 25])
//=> 55
```

### Technical frame 70: Copy on Write / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01269))_

> Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01267))_

<a id="atom-technical-atom-e2eebf14a262e5cb"></a>
```
const arraySum = (array) => {
let iter,
sum = 0,
index = 0;
while (
(eachIteration = {
done: index === array.length,
value: index < array.length ? array[index] : undefined
},
++index,
!eachIteration.done)
) {
sum += eachIteration.value;
}
return sum;
}
arraySum([1, 4, 9, 16, 25])
//=> 55
With this code, we make a POJO that has done and value keys. All the summing code needs to know
is to add eachIteration.value. Now we can extract the ickiness into a separate function:
const arrayIterator = (array) => {
let i = 0;
return () => {
const done = i === array.length;
return {
done,
value: done ? undefined : array[i++]
}
}
}
const iteratorSum = (iterator) => {
let eachIteration,
sum = 0;
while ((eachIteration = iterator(), !eachIteration.done)) {
```

### Technical frame 71: Copy on Write / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01269))_

> Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01268))_

<a id="atom-technical-atom-e53a3a370658b356"></a>
```
sum += eachIteration.value;
}
return sum;
}
iteratorSum(arrayIterator([1, 4, 9, 16, 25]))
//=> 55
```

### Technical frame 72: Copy on Write / Functional Iterators / bonus

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01294))_

> This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01293))_

<a id="atom-technical-atom-da3ef04aced8adf4"></a>
```
const firstInIteration = (fn, iterator) =>
take(filterIteratorWith(fn, iterator), 1);
```

### Technical frame 73: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01565))_

> Every time we write for (const i of Evens) , JavaScript calls Evens[Symbol.iterator]() . That in turns means it executes const iterator = Numbers[Symbol.iterator](); every time we write for (const i of Evens) , and that means that iterator starts at the beginning of Numbers .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01564))_

<a id="atom-technical-atom-b4aac75a2c3d116b"></a>
```
const Evens =
{
[Symbol.iterator] () {
const iterator = Numbers[Symbol.iterator]();
return {
next () {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : 2 *value});
}
}
}
};
```

### Technical frame 74: Served by the Pot: Collections / Iteration and Iterables / from

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01584))_

> We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ] . And if we assign a function to a property, we've created a method.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01583))_

<a id="atom-technical-atom-492f235f0cd82891"></a>
```
Array.from(UpTo1000)
//=> [1,81,121,361,441,841,961]
```

### Technical frame 75: Served by the Pot: Collections / Generating Iterables / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01682))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01679))_

<a id="atom-technical-atom-7ca2d5da0f09f056"></a>
> If we call our generator function more than once, we get new iterators.

### Technical frame 76: Served by the Pot: Collections / Generating Iterables / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01684))_

> This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01683))_

<a id="atom-technical-atom-54530c82c657b597"></a>
```
const ThreeNumbers = {
*[Symbol.iterator] () {
yield 1;
yield 2;
yield 3
}
}
```

### Technical atom 77

<a id="atom-technical-atom-83f43abc1781eefe"></a>

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00230))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00228))_

```text
back on the block
Back to our function. We evaluated this:
19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This was actually the preferred mechanism until void became commonplace.
20 As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined . We have no idea.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 19 | Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This was actually the preferred mechanism until void became commonplace. |
| 20 | As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined. We have no idea. |

</details>


## Related pages

### Shared technical atoms

- [[javascriptallonge-allong]] - shared statements and technical atoms: Allong shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé: JavaScript Allongé is a first and foremost, a book about programming with functions . It's written in JavaScript, because JavaScript hits the perfect sweet spot of b ... [truncated]; Allong shares technical record from JavaScript Allongé, the 'Six' Edition / Reg 'raganwald' Braithwaite: function foo (first, ...rest) { // ... } (10 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from Plain Old JavaScript Objects: In JavaScript, an object is a map from string keys to values.; Object shares technical record from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / matthew knox: { year: 2012, month: 6, day: 14 } (3 shared statement(s), 8 shared atom(s))
- [[javascriptallonge-bind]] - shared statements and technical atoms: Bind shares source evidence from And also: / call by sharing: We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to ... [truncated]; Bind shares technical record from And also: / Magic Names / the function keyword: const [what] = []; (2 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-ecmascript]] - shared statements and technical atoms: Ecmascript shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. For example, JavaScript did ... [truncated]; Ecmascript shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (4 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from Or even: / back on the block: !5 //=> false !undefined //=> true (6 shared atom(s))
- [[javascriptallonge-copy-write]] - shared statements and technical atoms: Copy on Write shares source evidence from Copy on Write / Functional Iterators / iterating: JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. Summing the elements of an array can be accomplished with:; Copy on Write shares technical record from Copy on Write / Functional Iterators / iterating: const arraySum = (array) => { let sum = 0; for (let i = 0; i < array.length; ++i) { sum += array[i]; } return sum } arraySum([1, 4, 9, 16, 25]) //=> 55 (4 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-type]] - shared statements and technical atoms: Type shares source evidence from And also: / call by sharing: Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, ... [truncated]; Type shares technical record from Prelude: Values and Expressions over Coffee / values are expressions: 2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true (2 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-edition]] - shared statements and technical atoms: Edition shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: JavaScript Allongé, The 'Six' Edition packs all the goodness of JavaScript Allongé into a new, updated package that is relevant for programmers working with (or plan ... [truncated]; Edition shares technical record from JavaScript Allongé, the 'Six' Edition / Reg 'raganwald' Braithwaite: 2 http://www.2ality.com 4 http://exploringjs.com 3 http://ecmanauten.de (3 shared statement(s), 4 shared atom(s))

### Shared claims

- [[javascriptallonge-quasi]] - shared statements: Quasi shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-quasi-literal]] - shared statements: Quasi Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-ternary-operator]] - shared statements: Ternary Operator shares source evidence from Picking the Bean: Choice and Truthiness / truthiness and the ternary operator: JavaScript inherited an operator from the C family of languages, the ternary operator. It's the only operator that takes three arguments. It looks like this: first ? ... [truncated] (1 shared statement(s))

### Topics

- [[javascriptallonge-javascript-allong]] - narrower topic: About JavaScript Allongé shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé: JavaScript Allongé is a first and foremost, a book about programming with functions . It's written in JavaScript, because JavaScript hits the perfect sweet spot of b ... [truncated]; About JavaScript Allongé shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (18 shared statement(s), 4 shared atom(s))

## Source

- [[javascriptallonge]]
