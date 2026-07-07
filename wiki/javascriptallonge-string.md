---
page_id: javascriptallonge-string
page_kind: concept
summary: String: 7 statement(s) and 6 atom(s) from raw/javascriptallonge.pdf.
page_family: broad-topic
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-string@11fa88aece5dbf122a1015bcb9f48cde
---

# String

What [[javascriptallonge]] covers about string:

## Statements

### Prelude: Values and Expressions over Coffee / values are expressions

- First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types . For example, the string "2" is not the same thing as the number 2 . Strings and numbers are different types, so strings and numbers are never identical: _(javascriptallonge.pdf (source-range-c98ab3e6-00116))_

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less

- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represent computations to be performed. Like numbers, strings, and arrays, they have a representation. Let's start with the second simplest possible function. 16 In JavaScript, it looks like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00162))_

### Or even: / the simplest possible block / undefined

- Like numbers, booleans and strings, JavaScript can print out the value undefined . _(javascriptallonge.pdf (source-range-c98ab3e6-00214))_

### And also: / call by sharing

- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. As you recall, value types like strings and numbers are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans as it wishes. _(javascriptallonge.pdf (source-range-c98ab3e6-00308))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments

- While we have mentioned arrays briefly, we haven't had a close look at them. Arrays are JavaScript's 'native' representation of lists. Strings are important because they represent writing. Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-c98ab3e6-00798))_

### A Warm Cup: Basic Strings and Quasi-Literals

- String manipulation is extremely common in programming. Writing is a big part of what makes us human, and strings are how JavaScript and most other languages represent writing. _(javascriptallonge.pdf (source-range-c98ab3e6-01475))_

### A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

- JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a string literal, but is actually an expression. Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-c98ab3e6-01477))_


## Technical atoms

### Technical frame 1: A Warm Cup: Basic Strings and Quasi-Literals

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01475))_

> String manipulation is extremely common in programming. Writing is a big part of what makes us human, and strings are how JavaScript and most other languages represent writing.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01474))_

<a id="atom-technical-atom-fcacbaa05ba382d2"></a>
```
'fu' + 'bar'
//=> 'fubar'
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Or even: / the simplest possible block / undefined: Like numbers, booleans and strings, JavaScript can print out the value undefined .; Javascript shares technical record from Prelude: Values and Expressions over Coffee / values are expressions: 2 === '2' //=> false true !== 'true' //=> true (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-type]] - shared statements and technical atoms: Type shares source evidence from And also: / call by sharing: We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to ... [truncated]; Type shares technical record from Prelude: Values and Expressions over Coffee / values are expressions / value types: 2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-literal]] - shared statements and technical atoms: Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a str ... [truncated]; Literal shares technical record from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-quasi]] - shared statements and technical atoms: Quasi shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a str ... [truncated]; Quasi shares technical record from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-quasi-literal]] - shared statements and technical atoms: Quasi Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a str ... [truncated]; Quasi Literal shares technical record from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (1 shared atom(s))

## Source

- [[javascriptallonge]]
