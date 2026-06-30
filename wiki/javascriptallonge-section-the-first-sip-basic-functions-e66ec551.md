---
page_id: javascriptallonge-section-the-first-sip-basic-functions-e66ec551
page_kind: source
summary: The first sip: Basic Functions: 41 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-first-sip-basic-functions-e66ec551@b45b821a3a96cccb11d362864897c967
---

# The first sip: Basic Functions

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-40f8e29e]] - narrower source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less
- [[javascriptallonge-section-a-rich-aroma-basic-numbers-ef9b6d69]] - previous source section: A Rich Aroma: Basic Numbers
- [[javascriptallonge-section-or-even-bc497226]] - next source section: Or even:

## Statements by subsection

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less

- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represent computations to be performed. Like numbers, strings, and arrays, they have a representation. Let's start with the second simplest possible function. 16 In JavaScript, it looks like this: _(javascriptallonge.pdf (source-range-0e12e052-00170))_
- This is a function that is applied to no values and returns 0 . Let's verify that our function is a value like all others: _(javascriptallonge.pdf (source-range-0e12e052-00172))_
- What!? Why didn't it type back () => 0 for us? This seems to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What's going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a browser, you may see something else. _(javascriptallonge.pdf (source-range-0e12e052-00174))_
- I'd prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function. _(javascriptallonge.pdf (source-range-0e12e052-00176))_

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities

- You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same contents. Reference types do not. _(javascriptallonge.pdf (source-range-0e12e052-00178))_
- Like arrays, every time you evaluate an expression to produce a function, you get a new function that is not identical to any other function, even if you use the same expression to generate it. 'Function' is a reference type. _(javascriptallonge.pdf (source-range-0e12e052-00181))_

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / applying functions

- Let's put functions to work. The way we use functions is to apply them to zero or more values called arguments . Just as 2 + 2 produces a value (in this case 4 ), applying a function to zero or more arguments produces a value as well. _(javascriptallonge.pdf (source-range-0e12e052-00183))_
- Right now, we only know about one such expression: () => 0 , so let's use it. We'll put it in parentheses 17 to keep the parser happy, like we did above: (() => 0) . Since we aren't giving it any arguments, we'll simply write () after the expression. So we write: _(javascriptallonge.pdf (source-range-0e12e052-00186))_
- 17 If you're used to other programming languages, you've probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. If not… Welcome to the ALGOL family of programming languages! _(javascriptallonge.pdf (source-range-0e12e052-00188))_
- Since we aren't giving it any arguments, we'll simply write () after the expression. _(javascriptallonge.pdf (source-range-0e12e052-00186))_

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

- We've seen () => 0 . We know that (() => 0)() returns 0 , and this is unsurprising. Likewise, the following all ought to be obvious: _(javascriptallonge.pdf (source-range-0e12e052-00190))_
- In the prelude, we looked at expressions. Values like 0 are expressions, as are things like 40 + 2 . Can we put an expression to the right of the arrow? _(javascriptallonge.pdf (source-range-0e12e052-00193))_
- Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)() ? _(javascriptallonge.pdf (source-range-0e12e052-00195))_
- Yes we can! Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-0e12e052-00198))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-0e12e052-00195))_

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

- The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words: _(javascriptallonge.pdf (source-range-0e12e052-00203))_
