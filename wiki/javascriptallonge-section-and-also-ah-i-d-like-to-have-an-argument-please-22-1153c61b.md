---
page_id: javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-1153c61b
page_kind: source
summary: And also: / Ah. I'd Like to Have an Argument, Please. 22: 27 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-1153c61b@056346e850bb38f29aa3c86e8ffa538d
---

# And also: / Ah. I'd Like to Have an Argument, Please. 22

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-0e29dfba]] - broader source section: And also:
- [[javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-a-quick-summary-of-functions-and-bodies-5cc0f029]] - narrower source section: And also: / Ah. I'd Like to Have an Argument, Please. 22 / a quick summary of functions and bodies
- [[javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-call-by-value-2ee5c091]] - narrower source section: And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by value
- [[javascriptallonge-section-and-also-functions-that-evaluate-to-functions-354b2284]] - previous source section: And also: / functions that evaluate to functions
- [[javascriptallonge-section-and-also-variables-and-bindings-baf19230]] - next source section: And also: / variables and bindings

## Statements

- Up to now, we've looked at functions without arguments. We haven't even said what an argument is , only that our functions don't have any. _(javascriptallonge.pdf (source-range-0e12e052-00265))_
- Most programmers are perfectly familiar with arguments (often called 'parameters'). Secondary school mathematics discusses this. So you know what they are, and I know that you know what they are, but please be patient with the explanation! _(javascriptallonge.pdf (source-range-0e12e052-00266))_
- This function has one argument, room , and an empty body. Here's a function with two arguments and an empty body: _(javascriptallonge.pdf (source-range-0e12e052-00269))_
- I'm sure you are perfectly comfortable with the idea that this function has two arguments, room , and board . What does one do with the arguments? Use them in the body, of course. What do you think this is? _(javascriptallonge.pdf (source-range-0e12e052-00271))_
- It's a function for calculating the circumference of a circle given the diameter. I read that aloud as 'When applied to a value representing the diameter, this function returns the diameter times 3.14159265.' _(javascriptallonge.pdf (source-range-0e12e052-00273))_
- You won't be surprised to see how to write and apply a function to two arguments: _(javascriptallonge.pdf (source-range-0e12e052-00276))_
- We haven't even said what an argument is , only that our functions don't have any. _(javascriptallonge.pdf (source-range-0e12e052-00265))_
- To apply a function with an argument (or arguments), we put the argument (or arguments) within the parentheses, like this: _(javascriptallonge.pdf (source-range-0e12e052-00274))_

## Statements by subsection

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / a quick summary of functions and bodies

- How arguments are used in a body's expression is probably perfectly obvious to you from the examples, especially if you've used any programming language (except for the dialect of BASIC-which I recall from my secondary school-that didn't allow parameters when you called a procedure). _(javascriptallonge.pdf (source-range-0e12e052-00281))_
- Expressions consist either of representations of values (like 3.14159265 , true , and undefined ), operators that combine expressions (like 3 + 2 ), some special forms like [1, 2, 3] for creating arrays out of expressions, or function ( arguments ) { body-statements } for creating functions. _(javascriptallonge.pdf (source-range-0e12e052-00282))_
- One of the important possible statements is a return statement. A return statement accepts any valid JavaScript expression. _(javascriptallonge.pdf (source-range-0e12e052-00283))_
- This loose definition is recursive, so we can intuit (or use our experience with other languages) that since a function can contain a return statement with an expression, we can write a function that returns a function, or an array that contains another array expression. Or a function that returns an array, an array of functions, a function that returns an array of functions, and so forth: _(javascriptallonge.pdf (source-range-0e12e052-00284))_
- How arguments are used in a body's expression is probably perfectly obvious to you from the examples, especially if you've used any programming language (except for the dialect of BASIC-which I recall from my secondary school-that didn't allow parameters when you called a procedure). _(javascriptallonge.pdf (source-range-0e12e052-00281))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by value

- Like most contemporary programming languages, JavaScript uses the 'call by value' evaluation strategy 23 . That means that when you write some code that appears to apply a function to an expression or expressions, JavaScript evaluates all of those expressions and applies the functions to the resulting value(s). _(javascriptallonge.pdf (source-range-0e12e052-00286))_
- What happened internally is that the expression 1 + 1 was evaluated first, resulting in 2 . Then our circumference function was applied to 2 . 24 _(javascriptallonge.pdf (source-range-0e12e052-00290))_
- That means that when you write some code that appears to apply a function to an expression or expressions, JavaScript evaluates all of those expressions and applies the functions to the resulting value(s). _(javascriptallonge.pdf (source-range-0e12e052-00286))_
- Then our circumference function was applied to 2 . _(javascriptallonge.pdf (source-range-0e12e052-00290))_
