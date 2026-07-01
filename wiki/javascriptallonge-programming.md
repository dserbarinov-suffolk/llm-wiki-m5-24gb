---
page_id: javascriptallonge-programming
page_kind: concept
summary: Programming: 9 statement(s) and 7 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-programming@3f6bc6b53f7325dfc199728b02beea27
---

# Programming

What [[javascriptallonge]] covers about programming:

## Statements

### A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

- Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Ruby, we can write: _(javascriptallonge.pdf (source-range-0e12e052-00030))_

### ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus

- As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. However, you'll not be beaten about the head and neck with dogma. Instead, every section is motivated by relevant dialog and fortified with compelling source examples. As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time. _(javascriptallonge.pdf (source-range-0e12e052-00089))_

### A Rich Aroma: Basic Numbers

- In computer science, a literal is a notation for representing a fixed value in source code. Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. An anonymous function is a literal for the function type.Wikipedia 12 _(javascriptallonge.pdf (source-range-0e12e052-00143))_

### And also: / Closures and Scope / it's always the environment

- The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-0e12e052-00361))_

### And also: / That Constant Coffee Craving

- Up to now, all we've really seen are anonymous functions , functions that don't have a name. This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. Naming things is a critical part of programming, but all we've seen so far is how to name arguments. _(javascriptallonge.pdf (source-range-0e12e052-00380))_

### Recipes with Basic Functions / Maybe

- A common problem in programming is checking for null or undefined (hereafter called 'nothing,' while all other values including 0 , [] and false will be called 'something'). Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-0e12e052-00690))_

### Reassignment

- Like some imperative programming languages, JavaScript allows you to re-assign the value bound to parameters. We saw this earlier in rebinding: _(javascriptallonge.pdf (source-range-0e12e052-01157))_


## Technical atoms

### Technical frame 1: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

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

### Technical frame 2: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00032))_

> Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00031))_

```
def foo (first, *rest)
# ...
end
```

### Technical frame 3: ECMAScript 6 has three major groups of features: / Forewords to the First Edition / matthew knox

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

### Technical frame 4: A Rich Aroma: Basic Numbers

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00147))_

> For example, the largest integer JavaScript can safely 14 handle is 9007199254740991 , or 2 '53' - 1 . Like most programming languages, JavaScript does not allow us to use commas to separate groups of digits.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00146))_

> The machine's representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the computer's behaviour surprises us if we don't know a little about what it's doing 'under the hood.'

### Technical frame 5: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00360))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00359))_

```
(x, y, z) => x + y + z
```

### Technical frame 6: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00695))_

> Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00697))_

```text
50 https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad
51 https://github.com/raganwald/andand
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 50 | https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad |
| 51 | https://github.com/raganwald/andand |

</details>

### Technical frame 7: Garbage, Garbage Everywhere / some history

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01025))_

```text
some history
Once upon a time, there was a programming language called Lisp 65 , an acronym for LISt Processing. 66 Lisp was one of the very first high-level languages, the very first implementation was written for the IBM 704 67 computer. (The very first FORTRAN implementation was also written for the 704).
The 704 had a 36-bit word, meaning that it was very fast to store and retrieve 36-bit values. The CPU's instruction set featured two important macros: CAR would fetch 15 bits representing the Contents of the Address part of the Register, while CDR would fetch the Contents of the Decrement part of the Register.
65 https://en.wikipedia.org/wiki/Lisp_
67 https://en.wikipedia.org/wiki/IBM_704
66 Lisp is still very much alive, and one of the most interesting and exciting programming languages in use today is Clojure, a Lisp dialect that runs on the JVM, along with its sibling ClojureScript, Clojure that transpiles to JavaScript.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 66 | Lisp was one of the very first high-level languages, the very first implementation was written for the IBM 704 |
| 67 | computer. (The very first FORTRAN implementation was also written for the 704). The 704 had a 36-bit word, meaning that it was very fast to store and retrieve 36-bit values. The CPU's instruction set featured two important macros: CAR would fetch 15 bits representing the Contents of the Address part of the Register, while CDR would fetch the Contents of the Decrement part of the Register. |
| 65 | https://en.wikipedia.org/wiki/Lisp_ |
| 67 | https://en.wikipedia.org/wiki/IBM_704 |
| 66 | Lisp is still very much alive, and one of the most interesting and exciting programming languages in use today is Clojure, a Lisp dialect that runs on the JVM, along with its sibling ClojureScript, Clojure that transpiles to JavaScript. |

</details>


## Related pages

- [[javascriptallonge-javascript-allong]] - shared statements and technical atoms: About JavaScript Allongé shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Rub ... [truncated]; About JavaScript Allongé shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-functional]] - shared statements and technical atoms: Functional shares source evidence from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Functional shares technical record from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / matthew knox: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Javascript shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-allong]] - shared statements and technical atoms: Allong shares source evidence from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus: As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript ... [truncated]; Allong shares technical record from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / matthew knox: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-evaluate]] - shared statements and technical atoms: Evaluate shares source evidence from And also: / Closures and Scope / it's always the environment: The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial applicatio ... [truncated]; Evaluate shares technical record from And also: / Closures and Scope / it's always the environment: (x, y, z) => x + y + z (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-ecmascript]] - shared technical atoms: Ecmascript shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (2 shared atom(s))
- [[javascriptallonge-recipe]] - shared technical atoms: Recipe shares technical record from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / matthew knox: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (2 shared atom(s))
- [[javascriptallonge-decorator]] - shared technical atoms: Decorator shares technical record from Recipes with Basic Functions / Maybe: 50 https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad 51 https://github.com/raganwald/andand (1 shared atom(s))
- [[javascriptallonge-edition]] - shared technical atoms: Edition shares technical record from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / matthew knox: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-feature]] - shared technical atoms: Feature shares technical record from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / matthew knox: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-list]] - shared technical atoms: List shares technical record from Garbage, Garbage Everywhere / some history: some history Once upon a time, there was a programming language called Lisp 65 , an acronym for LISt Processing. 66 Lisp was one of the very first high-level languag ... [truncated] (1 shared atom(s))
- [[javascriptallonge-literal]] - shared technical atoms: Literal shares technical record from A Rich Aroma: Basic Numbers: The machine's representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the comp ... [truncated] (1 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms: Object shares technical record from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / matthew knox: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))
- [[javascriptallonge-scope]] - shared technical atoms: Scope shares technical record from And also: / Closures and Scope / it's always the environment: (x, y, z) => x + y + z (1 shared atom(s))

## Source

- [[javascriptallonge]]
