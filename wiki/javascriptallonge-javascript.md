---
page_id: javascriptallonge-javascript
page_kind: concept
summary: Javascript: 75 statement(s) and 81 atom(s) from raw/javascriptallonge.pdf.
page_family: broad-topic
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-javascript@ddaa53c6d40a81fa0e1ab2be5b2e58ec
---

# Javascript

What [[javascriptallonge]] covers about javascript:

## Statements

### A Pull of the Lever: Prefaces / About JavaScript Allongé

- JavaScript Allongé is a first and foremost, a book about programming with functions . It's written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope. If those terms seem unfamiliar, don't worry: JavaScript Allongé takes great delight in explaining what they mean and why they matter. _(javascriptallonge.pdf (source-range-0e12e052-00018))_

- JavaScript Allongé begins at the beginning, with values and expressions, and builds from there to discuss types, identity, functions, closures, scopes, collections, iterators, and many more subjects up to working with classes and instances. _(javascriptallonge.pdf (source-range-0e12e052-00019))_

- It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or code-centric. JavaScript idioms like function combinators and decorators leverage JavaScript's power to make code easier to read, modify, debug and refactor. _(javascriptallonge.pdf (source-range-0e12e052-00020))_

### A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. For example, JavaScript did not include block-structured variables. Over time, programmers discovered ways to roll their own versions of important features. _(javascriptallonge.pdf (source-range-0e12e052-00024))_

- And the variable i is scoped locally to the code within the braces. Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write: _(javascriptallonge.pdf (source-range-0e12e052-00027))_

- Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like: _(javascriptallonge.pdf (source-range-0e12e052-00032))_

### A Pull of the Lever: Prefaces / About JavaScript Allongé / that's nice. is that the only reason?

- But there's more to it than that . The original JavaScript Allongé was not just written to teach JavaScript: It was written to describe certain ideas in programming: Working with small, independent entities that compose together to make bigger programs. Thus, the focus on things like writing decorators. _(javascriptallonge.pdf (source-range-0e12e052-00045))_

### A Pull of the Lever: Prefaces / What JavaScript Allongé is. And isn't.

- JavaScript Allongé is a book about programming with functions. From functions flow many ideas, from decorators to methods to delegation to mixins, and onwards in so many fruitful directions. _(javascriptallonge.pdf (source-range-0e12e052-00054))_

- But while JavaScript Allongé attempts to be provocative, it is not prescriptive . There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others. _(javascriptallonge.pdf (source-range-0e12e052-00056))_

- JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn't a book about practicing, it's a book about thinking. _(javascriptallonge.pdf (source-range-0e12e052-00065))_

### ECMAScript 6 has three major groups of features:

- With ECMAScript 6, JavaScript has become much larger as a language. JavaScript Allongé, the 'Six' Edition is both a comprehensive tour of its features and a rich collection of techniques for making better use of them. You will learn much about functional programming and object-oriented programming. And you'll do so via ES6 code, handed to you in small, easily digestible pieces. _(javascriptallonge.pdf (source-range-0e12e052-00081))_

### ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus

- As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. However, you'll not be beaten about the head and neck with dogma. Instead, every section is motivated by relevant dialog and fortified with compelling source examples. As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time. _(javascriptallonge.pdf (source-range-0e12e052-00089))_

### ECMAScript 6 has three major groups of features: / About The Sample PDF

- This sample edition of the book includes just a portion of the complete book. Buying the book in progress entitles you to free updates, so download it today 7 ! Besides, there's really no risk at all . If you read JavaScript Allongé, The 'six' edition and it doesn't blow your mind, your money will be cheerfully refunded. _(javascriptallonge.pdf (source-range-0e12e052-00095))_

### Prelude: Values and Expressions over Coffee / values are expressions

- First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types . For example, the string "2" is not the same thing as the number 2 . Strings and numbers are different types, so strings and numbers are never identical: _(javascriptallonge.pdf (source-range-0e12e052-00120))_

- Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 . _(javascriptallonge.pdf (source-range-0e12e052-00122))_

### A Rich Aroma: Basic Numbers

- For example, the largest integer JavaScript can safely 14 handle is 9007199254740991 , or 2 '53' - 1 . Like most programming languages, JavaScript does not allow us to use commas to separate groups of digits. _(javascriptallonge.pdf (source-range-0e12e052-00147))_

### A Rich Aroma: Basic Numbers / operations on numbers

- As we've seen, JavaScript has many common arithmetic operators. We can create expressions that look very much like mathematical expressions, for example we can write 1 + 1 or 2 * 3 or 42 34 or even 6 / 2 . These can be combined to make more complex expressions, like 2 * 5 + 1 . _(javascriptallonge.pdf (source-range-0e12e052-00159))_

- In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. So: _(javascriptallonge.pdf (source-range-0e12e052-00160))_

- JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2) , because the * operator has a higher precedence than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2 , this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the name plus , of course). _(javascriptallonge.pdf (source-range-0e12e052-00162))_

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less

- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represent computations to be performed. Like numbers, strings, and arrays, they have a representation. Let's start with the second simplest possible function. 16 In JavaScript, it looks like this: _(javascriptallonge.pdf (source-range-0e12e052-00170))_

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

- The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words: _(javascriptallonge.pdf (source-range-0e12e052-00203))_

### Or even: / the simplest possible block / undefined

- In JavaScript, the absence of a value is written undefined , and it means there is no value. It will crop up again. undefined is its own type of value, and it acts like a value type: _(javascriptallonge.pdf (source-range-0e12e052-00219))_

- Like numbers, booleans and strings, JavaScript can print out the value undefined . _(javascriptallonge.pdf (source-range-0e12e052-00222))_

- 18 Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons. This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. We will not take advantage of this feature, but it's helpful to know it exists. _(javascriptallonge.pdf (source-range-0e12e052-00225))_

### And also: / call by sharing

- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. As you recall, value types like strings and numbers are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans as it wishes. _(javascriptallonge.pdf (source-range-0e12e052-00317))_

- Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-0e12e052-00319))_

### And also: / Closures and Scope / shadowy variables from a shadowy planet

- When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor. _(javascriptallonge.pdf (source-range-0e12e052-00370))_

### And also: / Closures and Scope / which came first, the chicken or the egg?

- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } . _(javascriptallonge.pdf (source-range-0e12e052-00375))_

### And also: / That Constant Coffee Craving / inside-out

- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated 'IIFE.' _(javascriptallonge.pdf (source-range-0e12e052-00399))_

### And also: / That Constant Coffee Craving / const

- JavaScript gives us a way to do that, the const keyword. We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const : _(javascriptallonge.pdf (source-range-0e12e052-00415))_

### And also: / That Constant Coffee Craving / rebinding

- JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-0e12e052-00491))_

### And also: / Naming Functions / the function keyword

- JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions. _(javascriptallonge.pdf (source-range-0e12e052-00498))_

### And also: / Naming Functions / function declaration caveats 34

- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-0e12e052-00543))_

### And also: / Combinators and Function Decorators / higher-order functions

- As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. _(javascriptallonge.pdf (source-range-0e12e052-00552))_

### And also: / Building Blocks

- When you look at functions within functions in JavaScript, there's a bit of a 'spaghetti code' look to it. The strength of JavaScript is that you can do anything. The weakness is that you will. There are ifs, fors, returns, everything thrown higgledy piggledy together. Although you needn't restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks. _(javascriptallonge.pdf (source-range-0e12e052-00575))_

### And also: / Summary / Functions

- JavaScript uses const to bind values to names within block scope. _(javascriptallonge.pdf (source-range-0e12e052-00641))_

- JavaScript uses function declarations to bind functions to names within function scope. Function declarations are 'hoisted.' _(javascriptallonge.pdf (source-range-0e12e052-00642))_

- But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. _(javascriptallonge.pdf (source-range-0e12e052-00036))_
- JavaScript Allongé, The 'Six' Edition packs all the goodness of JavaScript Allongé into a new, updated package that is relevant for programmers working with (or planning to work with) the latest version of JavaScript. _(javascriptallonge.pdf (source-range-0e12e052-00041))_
- In JavaScript, every undefined is identical to every other undefined . _(javascriptallonge.pdf (source-range-0e12e052-00226))_
- JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. _(javascriptallonge.pdf (source-range-0e12e052-00664))_
- Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-0e12e052-00690))_
- In 'Ye Olde Days,' 53 JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice , or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. _(javascriptallonge.pdf (source-range-0e12e052-00720))_
- Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' . _(javascriptallonge.pdf (source-range-0e12e052-00761))_
- JavaScript inherited an operator from the C family of languages, the ternary operator. _(javascriptallonge.pdf (source-range-0e12e052-00763))_
- Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true . _(javascriptallonge.pdf (source-range-0e12e052-00769))_
- JavaScript has a literal syntax for creating an array: The [ and ] characters. _(javascriptallonge.pdf (source-range-0e12e052-00814))_
- JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. _(javascriptallonge.pdf (source-range-0e12e052-00859))_
- From its very inception, JavaScript has striven to avoid catastrophic errors. _(javascriptallonge.pdf (source-range-0e12e052-00863))_
- So we know that JavaScript is going to hang on to 1 . _(javascriptallonge.pdf (source-range-0e12e052-00954))_
- JavaScript cannot throw first away. _(javascriptallonge.pdf (source-range-0e12e052-00954))_
- Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . _(javascriptallonge.pdf (source-range-0e12e052-00955))_
- In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. _(javascriptallonge.pdf (source-range-0e12e052-01042))_
- JavaScript has dictionaries, and it calls them 'objects.' The word 'object' is loaded in programming circles, due to the widespread use of the term 'object-oriented programming' that was coined by Alan Kay but has since come to mean many, many things to many different people. _(javascriptallonge.pdf (source-range-0e12e052-01064))_
- In JavaScript, an object is a map from string keys to values. _(javascriptallonge.pdf (source-range-0e12e052-01065))_
- JavaScript has a literal syntax for creating objects. _(javascriptallonge.pdf (source-range-0e12e052-01068))_
- In JavaScript, almost every type of value can mutate . _(javascriptallonge.pdf (source-range-0e12e052-01116))_
- Like some imperative programming languages, JavaScript allows you to re-assign the value bound to parameters. _(javascriptallonge.pdf (source-range-0e12e052-01157))_
- JavaScript does not permit us to rebind a name that has been bound with const . _(javascriptallonge.pdf (source-range-0e12e052-01162))_
- JavaScript has one more way to bind a name to a value, var . _(javascriptallonge.pdf (source-range-0e12e052-01182))_
- JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. _(javascriptallonge.pdf (source-range-0e12e052-01281))_
- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. _(javascriptallonge.pdf (source-range-0e12e052-01311))_
- JavaScript would apply fn to every element. _(javascriptallonge.pdf (source-range-0e12e052-01316))_
- Practically speaking, languages like JavaScript already provide arrays with mapping and folding methods, choice operations, and other rich constructs. _(javascriptallonge.pdf (source-range-0e12e052-01399))_
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. _(javascriptallonge.pdf (source-range-0e12e052-01514))_
- Many objects in JavaScript can model collections of things. _(javascriptallonge.pdf (source-range-0e12e052-01523))_
- Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-0e12e052-01616))_
- But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next() , it runs until it returns, ends, or yields. _(javascriptallonge.pdf (source-range-0e12e052-01702))_
- We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call. _(javascriptallonge.pdf (source-range-0e12e052-01704))_
- When he's not shipping JavaScript, Ruby, CoffeeScript and Java applications scaling out to millions of users, Reg 'Raganwald' Braithwaite has authored libraries 221 for JavaScript, CoffeeScript, and Ruby programming such as Allong.es, Method Combinators, Katy, JQuery Combinators, YouAreDaChef, andand, and others. _(javascriptallonge.pdf (source-range-0e12e052-02055))_

## Technical atoms

### Technical frame 1: JavaScript Allongé, the 'Six' Edition / Reg 'raganwald' Braithwaite

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00009))_

| A Pull of the Lever: Prefaces................................... | i |
| --- | --- |
| About JavaScript Allongé................................... | ii |
| What JavaScript Allongé is. And isn’t............................. | v |
| Foreword to the “Six” edition................................. | viii |
| Forewords to the First Edition................................. | ix |
| About The Sample PDF.................................... | xi |
| Prelude: Values and Expressions over Coffee......................... | xiii |
| values are expressions..................................... | xiv |
| values and identity....................................... | xvi |
| A Rich Aroma: Basic Numbers.................................. | 1 |
| The first sip: Basic Functions................................... | 5 |
| As Little As Possible About Functions, But No Less..................... | 7 |
| Ah. I’d Like to Have an Argument, Please........................... | 16 |
| Closures and Scope...................................... | 21 |
| That Constant Coffee Craving................................ | 26 |
| Naming Functions....................................... | 39 |
| Combinators and Function Decorators............................ | 45 |
| Building Blocks........................................ | 48 |
| Magic Names.......................................... | 51 |
| Summary............................................ | 55 |
| Recipes with Basic Functions.................................. | 56 |
| Partial Application....................................... | 57 |
| Unary.............................................. | 59 |
| Tap............................................... | 61 |
| Maybe............................................. | 63 |
| Once.............................................. | 65 |
| Left-Variadic Functions.................................... | 66 |
| Picking the Bean: Choice and Truthiness............................ | 71 |

<details>
<summary>Raw table text</summary>

```text
Contents
| A Pull of the Lever: Prefaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | i |
| --- | --- |
| About JavaScript Allongé . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ii |
| What JavaScript Allongé is. And isn’t. . . . . . . . . . . . . . . . . . . . . . . . . . . . . | v |
| Foreword to the “Six” edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | viii |
| Forewords to the First Edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ix |
| About The Sample PDF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xi |
| Prelude: Values and Expressions over Coffee . . . . . . . . . . . . . . . . . . . . . . . . . | xiii |
| values are expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xiv |
| values and identity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xvi |
| A Rich Aroma: Basic Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 1 |
| The first sip: Basic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 5 |
| As Little As Possible About Functions, But No Less . . . . . . . . . . . . . . . . . . . . . | 7 |
| Ah. I’d Like to Have an Argument, Please. . . . . . . . . . . . . . . . . . . . . . . . . . . | 16 |
| Closures and Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 21 |
| That Constant Coffee Craving . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 26 |
| Naming Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 39 |
| Combinators and Function Decorators . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 45 |
| Building Blocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 48 |
| Magic Names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 51 |
| Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 55 |
| Recipes with Basic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 56 |
| Partial Application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 57 |
| Unary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 59 |
| Tap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 61 |
| Maybe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 63 |
| Once . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 65 |
| Left-Variadic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 66 |
| Picking the Bean: Choice and Truthiness . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 71 |
```

</details>

### Technical frame 2: JavaScript Allongé, the 'Six' Edition / Reg 'raganwald' Braithwaite

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00010))_

| Composing and Decomposing Data....... | ........................ | 77 |
| --- | --- | --- |
| Arrays and Destructuring Arguments.... | ........................ | 78 |
| Self-Similarity................. | ........................ | 86 |
| Tail Calls (and Default Arguments)...... | ........................ | 94 |
| Garbage, Garbage Everywhere........ | ........................ | 103 |
| Plain Old JavaScript Objects......... | ........................ | 109 |
| Mutation.................... | ........................ | 118 |
| Reassignment................. | ........................ | 125 |
| Copy on Write................. | ........................ | 135 |
| Tortoises, Hares, and Teleporting Turtles... | ........................ | 141 |
| Functional Iterators.............. | ........................ | 144 |
| Making Data Out Of Functions........ | ........................ | 154 |
| Recipes with Data................. | ........................ | 168 |
| mapWith.................... | ........................ | 170 |
| Flip....................... | ........................ | 172 |
| Object.assign.................. | ........................ | 175 |
| Why?...................... | ........................ | 178 |
| A Warm Cup: Basic Strings and Quasi-Literals | ........................ | 179 |
| Served by the Pot: Collections.......... | ........................ | 182 |
| Iteration and Iterables............. | ........................ | 183 |
| Generating Iterables.............. | ........................ | 201 |
| Lazy and Eager Collections.......... | ........................ | 223 |
| Interlude: The Carpenter Interviews for a Job | ........................ | 238 |
| Interactive Generators............. | ........................ | 250 |
| Basic Operations on Iterables......... | ........................ | 261 |
| The Golden Crema: Appendices and Afterwords | ....................... | 265 |
| How to run the examples........... | ........................ | 266 |
| Thanks!..................... | ........................ | 268 |
| Copyright Notice................ | ........................ | 270 |
| About The Author............... | ........................ | 274 |

<details>
<summary>Raw table text</summary>

```text
Contents
| Composing and Decomposing Data . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 77 |
| --- | --- | --- |
| Arrays and Destructuring Arguments . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 78 |
| Self-Similarity . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 86 |
| Tail Calls (and Default Arguments) . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 94 |
| Garbage, Garbage Everywhere . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 103 |
| Plain Old JavaScript Objects . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 109 |
| Mutation . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 118 |
| Reassignment . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 125 |
| Copy on Write . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 135 |
| Tortoises, Hares, and Teleporting Turtles . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 141 |
| Functional Iterators . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 144 |
| Making Data Out Of Functions . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 154 |
| Recipes with Data . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 168 |
| mapWith . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 170 |
| Flip . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 172 |
| Object.assign . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 175 |
| Why? . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 178 |
| A Warm Cup: Basic Strings and Quasi-Literals | . . . . . . . . . . . . . . . . . . . . . . . . | 179 |
| Served by the Pot: Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 182 |
| Iteration and Iterables . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 183 |
| Generating Iterables . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 201 |
| Lazy and Eager Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 223 |
| Interlude: The Carpenter Interviews for a Job | . . . . . . . . . . . . . . . . . . . . . . . . | 238 |
| Interactive Generators . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 250 |
| Basic Operations on Iterables . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 261 |
| The Golden Crema: Appendices and Afterwords | . . . . . . . . . . . . . . . . . . . . . . . | 265 |
| How to run the examples . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 266 |
| Thanks! . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 268 |
| Copyright Notice . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 270 |
| About The Author . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 274 |
```

</details>

### Technical frame 3: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00030))_

> Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Ruby, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00028))_

```
var i;
for (i = 0; i < array.length; ++i) {
(function (i) {
// ...
})(i)
}
```

### Technical frame 4: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00034))_

> The first edition of JavaScript Allongé explained these and many other patterns for writing flexible and composable programs in JavaScript, but the intention wasn't to explain how to work around JavaScript's missing features: The intention was to explain why the style of programming exemplified by the missing features is important.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00033))_

```
function foo () {
var first = arguments[0],
rest
= [].slice.call(arguments, 1);
// ...
}
```

### Technical frame 5: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00038))_

> And i is scoped to the for loop. We can also write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00037))_

```
for (let i = 0; i < array.length; ++i) {
// ...
}
```

### Technical frame 6: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00040))_

> And presto, rest collects the rest of the arguments without a lot of malarky involving slicing arguments . Not having to work around these kinds of missing features makes JavaScript Allongé a better book , because it can focus on the why to do something and when to do it, instead of on the how to make it work

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00039))_

```
function foo (first, ...rest) {
// ...
}
```

### Technical frame 7: ECMAScript 6 has three major groups of features:

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00081))_

> With ECMAScript 6, JavaScript has become much larger as a language. JavaScript Allongé, the 'Six' Edition is both a comprehensive tour of its features and a rich collection of techniques for making better use of them. You will learn much about functional programming and object-oriented programming. And you'll do so via ES6 code, handed to you in small, easily digestible pieces.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00083))_

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

### Technical frame 8: ECMAScript 6 has three major groups of features: / Forewords to the First Edition / matthew knox

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00093))_

```text
matthew knox
A different kind of language requires a different kind of book.
JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor strictly dynamic, and it supports procedural, object-oriented (in several flavors!), and functional programming. Many books try to hide most of those capabilities away, giving you recipes for writing JavaScript in a way that approximates class-centric programming in other languages. Not JavaScript Allongé. It starts with the fundamentals of values, functions, and objects, and then guides you through JavaScript from the inside with exploratory bits of code that illustrate scoping, combinators, context, state, prototypes, and constructors.
5 http://www.fogus.me
Like JavaScript itself, this book gives you a gentle start before showing you its full depth, and like a Cafe Allongé, it's over too soon. Enjoy!
-Matthew Knox, mattknox.com 6
6 http://mattknox.com
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 5 | http://www.fogus.me Like JavaScript itself, this book gives you a gentle start before showing you its full depth, and like a Cafe Allongé, it's over too soon. Enjoy! -Matthew Knox, mattknox.com 6 |
| 6 | http://mattknox.com |

</details>

### Technical frame 9: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00109))_

> All values are expressions. That's easy! Are there any other kinds of expressions? Sure! let's go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let's hand over some ground coffee plus some boiling water.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00108))_

```
42
//=> 42
```

### Technical frame 10: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00122))_

> Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00114))_

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

### Technical frame 11: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00122))_

> Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00116))_

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

### Technical frame 12: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00120))_

> First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types . For example, the string "2" is not the same thing as the number 2 . Strings and numbers are different types, so strings and numbers are never identical:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00118))_

```
2 === 2
//=> true
'hello' !== 'goodbye'
//=> true
```

### Technical frame 13: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00122))_

> Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00121))_

```
2 === '2'
//=> false
true !== 'true'
//=> true
```

### Technical frame 14: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00122))_

> Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00123))_

```
true === false
//=> false
2 !== 5
//=> true
'two' === 'five'
//=> false
```

### Technical frame 15: Prelude: Values and Expressions over Coffee / values are expressions / value types

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00128))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same 'content.' Strings, numbers, and booleans are examples of what JavaScript calls 'value' or 'primitive' types. We'll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00127))_

```
2 + 2 === 4
//=> true
(2 + 2 === 4) === (2 !== 5)
//=> true
```

### Technical frame 16: Prelude: Values and Expressions over Coffee / values are expressions / value types

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00131))_

> Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d'Italia

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00129))_

> So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them.

### Technical frame 17: A Rich Aroma: Basic Numbers / floating

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00157))_

> But as a rule, if you need to work with real numbers, you should have more than a nodding acquaintance with the IEEE Standard for Floating-Point Arithmetic 15 . Professional programmers almost never use floating point numbers to represent monetary amounts. For example, '$43.21' will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21 . In this book, we need not think about such details, but outside of this book, we must.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00154))_

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

### Technical frame 18: A Rich Aroma: Basic Numbers / floating

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00150))_

> It's tempting to think we now have everything we need to do things like handle amounts of money, but as the late John Belushi would say, 'Nooooooooooooooooooooo.' A computer's internal representation for a floating point number is binary, while our literal number was in base ten. This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00157))_

> Professional programmers almost never use floating point numbers to represent monetary amounts.

### Technical frame 19: A Rich Aroma: Basic Numbers / operations on numbers

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00162))_

> JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2) , because the * operator has a higher precedence than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2 , this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the name plus , of course).

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00161))_

```
2 * 5 + 1
//=> 11
1 + 5 * 2
//=> 11
```

### Technical frame 20: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00172))_

> This is a function that is applied to no values and returns 0 . Let's verify that our function is a value like all others:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00171))_

```
() => 0
```

### Technical frame 21: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00174))_

> What!? Why didn't it type back () => 0 for us? This seems to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What's going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a br

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00173))_

```
(() => 0)
//=> [Function]
```

### Technical frame 22: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00176))_

> I'd prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00175))_

> 16 The simplest possible function is () => {} , we'll see that later.

### Technical frame 23: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00181))_

> Like arrays, every time you evaluate an expression to produce a function, you get a new function that is not identical to any other function, even if you use the same expression to generate it. 'Function' is a reference type.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00180))_

```
(() => 0) === (() => 0)
//=> false
```

### Technical frame 24: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / applying functions

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00186))_

> Right now, we only know about one such expression: () => 0 , so let's use it. We'll put it in parentheses 17 to keep the parser happy, like we did above: (() => 0) . Since we aren't giving it any arguments, we'll simply write () after the expression. So we write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00185))_

```
fn_expr(args)
```

### Technical frame 25: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00203))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00204))_

```
//=> 2
(1 + 1, 2 + 2)
```

### Technical frame 26: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00203))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00208))_

```
() =>
(1 + 1, 2 + 2)
```

### Technical frame 27: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00222))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00220))_

```
undefined
```

### Technical frame 28: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00222))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00221))_

```
//=> undefined
```

### Technical frame 29: Or even: / back on the block

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00236))_

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

### Technical frame 30: Or even: / back on the block

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

### Technical frame 31: And also: / Closures and Scope / shadowy variables from a shadowy planet

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00368))_

> The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x , it is ignored when evaluating x + y . JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00367))_

```
(x) =>
(x, y) => x + y
```

### Technical frame 32: And also: / Closures and Scope / shadowy variables from a shadowy planet

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00370))_

> When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00369))_

```
(x) =>
(x, y) =>
(w, z) =>
(w) =>
x + y + z
```

### Technical frame 33: And also: / Closures and Scope / which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00375))_

> JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00376))_

> If you don't want your code to operate directly within the global environment, what can you do?

### Technical frame 34: And also: / Closures and Scope / which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00375))_

> JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00377))_

```
// top of the file
(() => {
// ... lots of JavaScript ...
})();
// bottom of the file
```

### Technical frame 35: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00401))_

> Everything else is encapsulated in its body. That's how it should be, naming PI is its concern, not ours. The other formulation:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00400))_

```
(diameter) =>
// ...
```

### Technical frame 36: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00417))_

> The const keyword introduces one or more bindings in the block that encloses it. It doesn't incur the cost of a function invocation. That's great. Even better, it puts the symbol (like PI ) close to the value ( 3.14159265 ). That's much better than what we were writing.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00416))_

```
(diameter) => {
const PI = 3.14159265;
return diameter * PI
}
```

### Technical frame 37: And also: / That Constant Coffee Craving / rebinding

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00491))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00488))_

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

### Technical frame 38: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00524))_

> Now, the function's actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00523))_

```
someBackboneView.on('click', function clickHandler () {
//...
});
```

### Technical frame 39: And also: / Combinators and Function Decorators / function decorators

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

### Technical frame 40: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00581))_

> If that was all there was to it, composition wouldn't matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00580))_

```
const compose = (a, b) => (c) => a(b(c));
const cookAndEat = compose(eat, cook);
```

### Technical frame 41: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00582))_

> In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00581))_

> The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

### Technical frame 42: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00598))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00595))_

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

### Technical frame 43: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00612))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00608))_

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

### Technical frame 44: Recipes with Basic Functions / Partial Application

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00655))_

> These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00654))_

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

### Technical frame 45: Recipes with Basic Functions / Partial Application

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00660))_

> We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00658))_

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

### Technical frame 46: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00669))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00665))_

```
['1', '2', '3'].map(parseFloat)
//=> [1, 2, 3]
```

### Technical frame 47: Recipes with Basic Functions / Left-Variadic Functions / a history lesson

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00726))_

> This is a right-variadic function , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00721))_

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

### Technical frame 48: Picking the Bean: Choice and Truthiness / truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00773))_

> Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00772))_

```
!5
//=> false
!undefined
//=> true
```

### Technical frame 49: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00822))_

> This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00815))_

```
[]
//=> []
```

### Technical frame 50: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00859))_

> That match would fail because the array doesn't have an element to assign to what . But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. Therefore:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00858))_

```
const [what] = [];
```

### Technical frame 51: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00863))_

> From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00860))_

```
const [what] = [];
what
//=> undefined
const [which, what,
who
//=> undefined
```

### Technical frame 52: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00863))_

> From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00861))_

```
const [...they] = [];
they
//=> []
const [which, what, .
they
//=> []
```

### Technical frame 53: Composing and Decomposing Data / Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00954))_

> Note that while evaluating mapWith(fn, rest) , JavaScript must retain the value first or fn(first) , plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result. JavaScript cannot throw first away. So we know that JavaScript is going to hang on to 1 .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00953))_

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

### Technical frame 54: Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00964))_

> There are three places it returns. The first two don't return anything, they don't matter. But the third is fn.apply(this, args) . This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. It isn't going to do any more work, so it can throw its existing stack frame away.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00963))_

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

### Technical frame 55: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00981))_

> Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00978))_

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

### Technical frame 56: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00981))_

> Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00979))_

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

### Technical frame 57: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00981))_

> Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00980))_

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

### Technical frame 58: Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01037))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01031))_

```
const cons = (a, d) => [a, d],
car
= ([a, d]) => a,
cdr
= ([a, d]) => d;
```

### Technical frame 59: Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01037))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01036))_

```
const node5 = [5,null],
node4 = [4, node5],
node3 = [3, node4],
node2 = [2, node3],
node1 = [1, node2];
const oneToFive = node1;
```

### Technical frame 60: Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01042))_

> Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is fas

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01041))_

```
cdr(oneToFive)
//=> [2,[3,[4,[5,null]]]]
```

### Technical frame 61: Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01070))_

> Two objects created with separate evaluations have differing identities, just like arrays:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01069))_

```
{ year: 2012, month: 6, day: 14 }
```

### Technical frame 62: Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01095))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01096))_

```
const description = ({name: { first }, occupation: { title } }) =>
`${first} is a ${title}`;
description(user)
//=> "Reginald is a Author"
And that same syntax works for literals:
const abbrev = ({name: { first, last }, occupation: { title } }) => {
```

### Technical frame 63: Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01095))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01097))_

```
const abbrev = ({name: { first, last }, occupation: { title } }) =>
return { first, last, title};
}
abbrev(user)
//=> {"first":"Reginald","last":"Braithwaite","title":"Author"}
```

### Technical frame 64: Mutation

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01122))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01117))_

```
const oneTwoThree = [1, 2, 3];
oneTwoThree[0] = 'one';
oneTwoThree
//=> [ 'one', 2, 3 ]
```

### Technical frame 65: Mutation

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01124))_

> Both halloween and allHallowsEve are bound to the same array value within the local environment. And also:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01123))_

```
const allHallowsEve = [2012, 10, 31]
const halloween = allHallowsEve;
```

### Technical frame 66: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01162))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01159))_

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

### Technical frame 67: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01165))_

> We took the time to carefully examine what happens with bindings in environments. Let's take the time to explore what happens with reassigning values to variables. The key is to understand that we are rebinding a different value to the same name in the same environment.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01164))_

```
let age = 52;
age = 53;
age
//=> 53
```

### Technical frame 68: Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01186))_

> But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01183))_

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

### Technical frame 69: Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01186))_

> But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01185))_

```
return n * factorial2(x);
}
}
factorial2(5)
//=> 120
```

### Technical frame 70: Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01195))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01190))_

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

### Technical frame 71: Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01195))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01192))_

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

### Technical frame 72: Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01195))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01194))_

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

### Technical frame 73: Reassignment / why const and let were invented

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01200))_

> Hopefully, you can think of a faster way to calculate this sum. 72 And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. But is this ever a problem?

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01199))_

```
var sum = 0;
for (var i = 1; i <= 100; i++) {
sum = sum + i
}
sum
#=> 5050
```

### Technical frame 74: Copy on Write / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01283))_

> Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01282))_

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

### Technical frame 75: Copy on Write / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01289))_

> Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01287))_

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

### Technical frame 76: Copy on Write / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01289))_

> Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01288))_

```
sum += eachIteration.value;
}
return sum;
}
iteratorSum(arrayIterator([1, 4, 9, 16, 25]))
//=> 55
```

### Technical frame 77: Copy on Write / Functional Iterators / bonus

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01314))_

> This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01313))_

```
const firstInIteration = (fn, iterator) =>
take(filterIteratorWith(fn, iterator), 1);
```

### Technical frame 78: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01590))_

> Every time we write for (const i of Evens) , JavaScript calls Evens[Symbol.iterator]() . That in turns means it executes const iterator = Numbers[Symbol.iterator](); every time we write for (const i of Evens) , and that means that iterator starts at the beginning of Numbers .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01589))_

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

### Technical frame 79: Served by the Pot: Collections / Iteration and Iterables / from

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01609))_

> We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ] . And if we assign a function to a property, we've created a method.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01608))_

```
Array.from(UpTo1000)
//=> [1,81,121,361,441,841,961]
```

### Technical frame 80: Served by the Pot: Collections / Generating Iterables / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01708))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01705))_

> If we call our generator function more than once, we get new iterators.

### Technical frame 81: Served by the Pot: Collections / Generating Iterables / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01710))_

> This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01709))_

```
const ThreeNumbers = {
*[Symbol.iterator] () {
yield 1;
yield 2;
yield 3
}
}
```


## Related pages

- [[javascriptallonge-javascript-allong]] - narrower topic: About JavaScript Allongé shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé: JavaScript Allongé is a first and foremost, a book about programming with functions . It's written in JavaScript, because JavaScript hits the perfect sweet spot of b ... [truncated]; About JavaScript Allongé shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (18 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-allong]] - shared statements and technical atoms: Allong shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé: JavaScript Allongé is a first and foremost, a book about programming with functions . It's written in JavaScript, because JavaScript hits the perfect sweet spot of b ... [truncated]; Allong shares technical record from JavaScript Allongé, the 'Six' Edition / Reg 'raganwald' Braithwaite: function foo (first, ...rest) { // ... } (10 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from Plain Old JavaScript Objects: In JavaScript, an object is a map from string keys to values.; Object shares technical record from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / matthew knox: { year: 2012, month: 6, day: 14 } (3 shared statement(s), 8 shared atom(s))
- [[javascriptallonge-bind]] - shared statements and technical atoms: Bind shares source evidence from And also: / call by sharing: We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to ... [truncated]; Bind shares technical record from And also: / Magic Names / the function keyword: const [what] = []; (2 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-ecmascript]] - shared statements and technical atoms: Ecmascript shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. For example, JavaScript did ... [truncated]; Ecmascript shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (4 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-copy-write]] - shared statements and technical atoms: Copy on Write shares source evidence from Copy on Write / Functional Iterators / iterating: JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. Summing the elements of an array can be accomplished with:; Copy on Write shares technical record from Copy on Write / Functional Iterators / iterating: const arraySum = (array) => { let sum = 0; for (let i = 0; i < array.length; ++i) { sum += array[i]; } return sum } arraySum([1, 4, 9, 16, 25]) //=> 55 (4 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-type]] - shared statements and technical atoms: Type shares source evidence from And also: / call by sharing: Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, ... [truncated]; Type shares technical record from Prelude: Values and Expressions over Coffee / values are expressions: 2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true (2 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-edition]] - shared statements and technical atoms: Edition shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: JavaScript Allongé, The 'Six' Edition packs all the goodness of JavaScript Allongé into a new, updated package that is relevant for programmers working with (or plan ... [truncated]; Edition shares technical record from JavaScript Allongé, the 'Six' Edition / Reg 'raganwald' Braithwaite: 2 http://www.2ality.com 4 http://exploringjs.com 3 http://ecmanauten.de (3 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-functional-iterator]] - shared statements and technical atoms: Functional Iterators shares source evidence from Copy on Write / Functional Iterators / iterating: JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. Summing the elements of an array can be accomplished with:; Functional Iterators shares technical record from Copy on Write / Functional Iterators / iterating: const arraySum = (array) => { let sum = 0; for (let i = 0; i < array.length; ++i) { sum += array[i]; } return sum } arraySum([1, 4, 9, 16, 25]) //=> 55 (3 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-string]] - shared statements and technical atoms: String shares source evidence from Or even: / the simplest possible block / undefined: Like numbers, booleans and strings, JavaScript can print out the value undefined .; String shares technical record from Prelude: Values and Expressions over Coffee / values are expressions: 2 === '2' //=> false true !== 'true' //=> true (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-array]] - shared statements and technical atoms: Array shares source evidence from Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals: JavaScript has a literal syntax for creating an array: The [ and ] characters. We can create an empty array:; Array shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals: [] //=> [] (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms: Element shares source evidence from Garbage, Garbage Everywhere / some history: Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of ar ... [truncated]; Element shares technical record from Garbage, Garbage Everywhere / some history: const cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d; (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from Served by the Pot: Collections / Generating Iterables / generators and iterables: Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of r ... [truncated]; Return shares technical record from Or even: / back on the block: !5 //=> false !undefined //=> true (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-scope]] - shared statements and technical atoms: Scope shares source evidence from And also: / Closures and Scope / shadowy variables from a shadowy planet: When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is igno ... [truncated]; Scope shares technical record from And also: / Closures and Scope / shadowy variables from a shadowy planet: (x) => (x, y) => x + y (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-decorator]] - shared statements and technical atoms: Decorator shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé: It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or ... [truncated]; Decorator shares technical record from And also: / Combinators and Function Decorators / function decorators: const compose = (a, b) => (c) => a(b(c)); const cookAndEat = compose(eat, cook); (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-functional]] - shared statements and technical atoms: Functional shares source evidence from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Functional shares technical record from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / matthew knox: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements and technical atoms: Iterator shares source evidence from Served by the Pot: Collections / Iteration and Iterables / summary: Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility ... [truncated]; Iterator shares technical record from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: const Evens = { [Symbol.iterator] () { const iterator = Numbers[Symbol.iterator](); return { next () { const {done, value} = iterator.next(); return ({done, value: d ... [truncated] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-write]] - shared statements and technical atoms: Write shares source evidence from Served by the Pot: Collections / Generating Iterables / generators and iterables: Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of r ... [truncated]; Write shares technical record from And also: / Building Blocks / partial application: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-programming]] - shared statements and technical atoms: Programming shares source evidence from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Programming shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-function-keyword]] - shared statements and technical atoms: the function keyword shares source evidence from And also: / Naming Functions / the function keyword: JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions.; the function keyword shares technical record from And also: / Naming Functions / the function keyword: someBackboneView.on('click', function clickHandler () { //... }); (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-reference]] - shared statements and technical atoms: Reference shares source evidence from And also: / call by sharing: Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, ... [truncated]; Reference shares technical record from Garbage, Garbage Everywhere / some history: const node5 = [5,null], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; const oneToFive = node1; (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-evaluate]] - shared statements and technical atoms: Evaluate shares source evidence from Picking the Bean: Choice and Truthiness / truthiness and the ternary operator: Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true .; Evaluate shares technical record from Or even: / back on the block: //=> undefined We said that the function returns the result of evaluating a block, and we said that a block is a (possibly empty) list of JavaScript statements separ ... [truncated] (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-literal]] - shared statements and technical atoms: Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated]; Literal shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals: [] //=> [] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-truthiness]] - shared statements and technical atoms: Truthiness shares source evidence from Picking the Bean: Choice and Truthiness / truthiness and the ternary operator: In JavaScript, there is a notion of 'truthiness.' Every value is either 'truthy' or 'falsy.' Obviously, false is falsy. So are null and undefined , values that seman ... [truncated]; Truthiness shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from Or even: / back on the block: !5 //=> false !undefined //=> true (6 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from Prelude: Values and Expressions over Coffee / values are expressions: 2 * 5 + 1 //=> 11 1 + 5 * 2 //=> 11 (5 shared atom(s))
- [[javascriptallonge-feature]] - shared technical atoms: Feature shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: for (let i = 0; i < array.length; ++i) { // ... } (4 shared atom(s))
- [[javascriptallonge-list]] - shared technical atoms: List shares technical record from Or even: / back on the block: const node5 = [5,null], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; const oneToFive = node1; (4 shared atom(s))
- [[javascriptallonge-partial-application]] - shared technical atoms: partial application shares technical record from And also: / Building Blocks / partial application: 39 http://underscorejs.org 41 If we don't want to sort out Underscore, we can also write the following: const map = (a, fn) => a.map(fn); , and trust that it works e ... [truncated] (3 shared atom(s))
- [[javascriptallonge-recipe]] - shared technical atoms: Recipe shares technical record from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / matthew knox: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (3 shared atom(s))
- [[javascriptallonge-coffee]] - shared technical atoms: Coffee shares technical record from Prelude: Values and Expressions over Coffee / values are expressions: 10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' ... [truncated] (2 shared atom(s))
- [[javascriptallonge-collection]] - shared technical atoms: Collection shares technical record from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: const Evens = { [Symbol.iterator] () { const iterator = Numbers[Symbol.iterator](); return { next () { const {done, value} = iterator.next(); return ({done, value: d ... [truncated] (2 shared atom(s))
- [[javascriptallonge-data]] - shared technical atoms: Data shares technical record from JavaScript Allongé, the 'Six' Edition / Reg 'raganwald' Braithwaite: converting non-tail-calls to tail-calls | 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 10, | 11, ... [truncated] (2 shared atom(s))
- [[javascriptallonge-declaration]] - shared technical atoms: Declaration shares technical record from Reassignment / mixing let and const / var: const factorial = (n) => { return innerFactorial(n, 1); function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } } fa ... [truncated] (2 shared atom(s))
- [[javascriptallonge-generator]] - shared technical atoms: Generator shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: If we call our generator function more than once, we get new iterators. (2 shared atom(s))
- [[javascriptallonge-iterable]] - shared technical atoms: Iterable shares technical record from Served by the Pot: Collections / Iteration and Iterables / from: Array.from(UpTo1000) //=> [1,81,121,361,441,841,961] (2 shared atom(s))
- [[javascriptallonge-iteration]] - shared technical atoms: Iteration shares technical record from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: const Evens = { [Symbol.iterator] () { const iterator = Numbers[Symbol.iterator](); return { next () { const {done, value} = iterator.next(); return ({done, value: d ... [truncated] (2 shared atom(s))
- [[javascriptallonge-method]] - shared technical atoms: Method shares technical record from And also: / Building Blocks / partial application: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (2 shared atom(s))
- [[javascriptallonge-pattern]] - shared technical atoms: Pattern shares technical record from And also: / That Constant Coffee Craving / inside-out: (diameter) => // ... (2 shared atom(s))
- [[javascriptallonge-binding]] - shared technical atoms: Binding shares technical record from And also: / Magic Names / the function keyword: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-copy]] - shared technical atoms: Copy shares technical record from Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared atom(s))
- [[javascriptallonge-identity]] - shared technical atoms: Identity shares technical record from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities: (() => 0) === (() => 0) //=> false (1 shared atom(s))
- [[javascriptallonge-operation]] - shared technical atoms: Operation shares technical record from Copy on Write / Functional Iterators / bonus: const firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1); (1 shared atom(s))
- [[javascriptallonge-operator]] - shared technical atoms: Operator shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-parameter]] - shared technical atoms: Parameter shares technical record from Recipes with Basic Functions / Left-Variadic Functions / a history lesson: var __slice = Array.prototype.slice; function rightVariadic (fn) { if (fn.length < 1) return fn; return function () { var ordinaryArgs = (1 <= arguments.length ? __s ... [truncated] (1 shared atom(s))
- [[javascriptallonge-statement]] - shared technical atoms: Statement shares technical record from Or even: / back on the block: //=> undefined We said that the function returns the result of evaluating a block, and we said that a block is a (possibly empty) list of JavaScript statements separ ... [truncated] (1 shared atom(s))
- [[javascriptallonge-structure]] - shared technical atoms: Structure shares technical record from Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared atom(s))
- [[javascriptallonge-quasi]] - shared statements: Quasi shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-quasi-literal]] - shared statements: Quasi Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-ternary-operator]] - shared statements: Ternary Operator shares source evidence from Picking the Bean: Choice and Truthiness / truthiness and the ternary operator: JavaScript inherited an operator from the C family of languages, the ternary operator. It's the only operator that takes three arguments. It looks like this: first ? ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
