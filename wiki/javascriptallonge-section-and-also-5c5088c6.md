---
page_id: javascriptallonge-section-and-also-5c5088c6
page_kind: source
summary: And also:: 439 source-backed entries and 131 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-5c5088c6@775873ed55a14687aa9b8946c0801f91
---

# And also:

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-or-even-c90af7e2]] - previous source section: Or even:
- [[javascriptallonge-section-recipes-with-basic-functions-8e785fac]] - next source section: Recipes with Basic Functions

### Source structure

- [[javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-7c7543ef]] - narrower source section: And also: / Ah. I'd Like to Have an Argument, Please. 22
- [[javascriptallonge-section-and-also-building-blocks-59e935fc]] - narrower source section: And also: / Building Blocks
- [[javascriptallonge-section-and-also-call-by-sharing-483b119d]] - narrower source section: And also: / call by sharing
- [[javascriptallonge-section-and-also-closures-and-scope-b0169abc]] - narrower source section: And also: / Closures and Scope
- [[javascriptallonge-section-and-also-combinators-and-function-decorators-f08ca983]] - narrower source section: And also: / Combinators and Function Decorators
- [[javascriptallonge-section-and-also-functions-that-evaluate-to-functions-5d342922]] - narrower source section: And also: / functions that evaluate to functions
- [[javascriptallonge-section-and-also-magic-names-e1687356]] - narrower source section: And also: / Magic Names
- [[javascriptallonge-section-and-also-naming-functions-c9513a66]] - narrower source section: And also: / Naming Functions

## Statements

- Statements belong inside blocks and only inside blocks. _(javascriptallonge.pdf (source-range-c98ab3e6-00251))_

## Statements by subsection

### And also: / functions that evaluate to functions

- That's a function! It's a function that when applied, evaluates to a function that when applied, evaluates to 0 . So we have a function, that returns a function, that returns zero . Likewise: _(javascriptallonge.pdf (source-range-c98ab3e6-00256))_
- Well. We've been very clever, but so far this all seems very abstract. Diffraction of a crystal is beautiful and interesting in its own right, but you can't blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. So… In the next chapter, 'I'd Like to Have an Argument, Please,' we'll see how to make functions practical. _(javascriptallonge.pdf (source-range-c98ab3e6-00263))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22

- Up to now, we've looked at functions without arguments. We haven't even said what an argument is , only that our functions don't have any. _(javascriptallonge.pdf (source-range-c98ab3e6-00265))_
- Most programmers are perfectly familiar with arguments (often called 'parameters'). Secondary school mathematics discusses this. So you know what they are, and I know that you know what they are, but please be patient with the explanation! _(javascriptallonge.pdf (source-range-c98ab3e6-00266))_
- This function has one argument, room , and an empty body. Here's a function with two arguments and an empty body: _(javascriptallonge.pdf (source-range-c98ab3e6-00269))_
- I'm sure you are perfectly comfortable with the idea that this function has two arguments, room , and board . What does one do with the arguments? Use them in the body, of course. What do you think this is? _(javascriptallonge.pdf (source-range-c98ab3e6-00271))_
- It's a function for calculating the circumference of a circle given the diameter. I read that aloud as 'When applied to a value representing the diameter, this function returns the diameter times 3.14159265.' _(javascriptallonge.pdf (source-range-c98ab3e6-00273))_
- You won't be surprised to see how to write and apply a function to two arguments: _(javascriptallonge.pdf (source-range-c98ab3e6-00276))_
- We haven't even said what an argument is , only that our functions don't have any. _(javascriptallonge.pdf (source-range-c98ab3e6-00265))_
- To apply a function with an argument (or arguments), we put the argument (or arguments) within the parentheses, like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00274))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / a quick summary of functions and bodies

- How arguments are used in a body's expression is probably perfectly obvious to you from the examples, especially if you've used any programming language (except for the dialect of BASIC-which I recall from my secondary school-that didn't allow parameters when you called a procedure). _(javascriptallonge.pdf (source-range-c98ab3e6-00281))_
- Expressions consist either of representations of values (like 3.14159265 , true , and undefined ), operators that combine expressions (like 3 + 2 ), some special forms like [1, 2, 3] for creating arrays out of expressions, or function ( arguments ) { body-statements } for creating functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00282))_
- One of the important possible statements is a return statement. A return statement accepts any valid JavaScript expression. _(javascriptallonge.pdf (source-range-c98ab3e6-00283))_
- This loose definition is recursive, so we can intuit (or use our experience with other languages) that since a function can contain a return statement with an expression, we can write a function that returns a function, or an array that contains another array expression. Or a function that returns an array, an array of functions, a function that returns an array of functions, and so forth: _(javascriptallonge.pdf (source-range-c98ab3e6-00284))_
- How arguments are used in a body's expression is probably perfectly obvious to you from the examples, especially if you've used any programming language (except for the dialect of BASIC-which I recall from my secondary school-that didn't allow parameters when you called a procedure). _(javascriptallonge.pdf (source-range-c98ab3e6-00281))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by value

- Like most contemporary programming languages, JavaScript uses the 'call by value' evaluation strategy 23 . That means that when you write some code that appears to apply a function to an expression or expressions, JavaScript evaluates all of those expressions and applies the functions to the resulting value(s). _(javascriptallonge.pdf (source-range-c98ab3e6-00286))_
- What happened internally is that the expression 1 + 1 was evaluated first, resulting in 2 . Then our circumference function was applied to 2 . 24 _(javascriptallonge.pdf (source-range-c98ab3e6-00290))_
- That means that when you write some code that appears to apply a function to an expression or expressions, JavaScript evaluates all of those expressions and applies the functions to the resulting value(s). _(javascriptallonge.pdf (source-range-c98ab3e6-00286))_
- Then our circumference function was applied to 2 . _(javascriptallonge.pdf (source-range-c98ab3e6-00290))_

### And also: / variables and bindings

- Right now everything looks simple and straightforward, and we can move on to talk about arguments in more detail. And we're going to work our way up from (diameter) => diameter * 3.14159265 to functions like: _(javascriptallonge.pdf (source-range-c98ab3e6-00293))_
- (x) => (y) => x just looks crazy, as if we are learning English as a second language and the teacher promises us that soon we will be using words like antidisestablishmentarianism . Besides a desire to use long words to sound impressive, this is not going to seem attractive until we find ourselves wanting to discuss the role of the Church of England in 19th century British politics. _(javascriptallonge.pdf (source-range-c98ab3e6-00295))_
- But there's another reason for learning the word antidisestablishmentarianism : We might learn how prefixes and postfixes work in English grammar. It's the same thing with (x) => (y) => x . It has a certain important meaning in its own right, and it's also an excellent excuse to learn about functions that make functions, environments, variables, and more. _(javascriptallonge.pdf (source-range-c98ab3e6-00296))_
- In order to talk about how this works, we should agree on a few terms (you may already know them, but let's check-in together and 'synchronize our dictionaries'). The first x , the one in (x) => ... , is an argument . The y in function (y) ... is another argument. The second x , the one in => x , is not an argument, it's an expression referring to a variable . Arguments and variables work the same way whether we're talking about (x) => (y) => x or just plain (x) => x . _(javascriptallonge.pdf (source-range-c98ab3e6-00297))_
- Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. An environment is a (possibly empty) dictionary that maps variables to values by name. The x in the expression that we call a 'variable' is itself an expression that is evaluated by looking up the value in the environment. _(javascriptallonge.pdf (source-range-c98ab3e6-00298))_
- 24 We said that you can't apply a function to an expression. You can apply a function to one or more functions. Functions are values! This has interesting applications, and they will be explored much more thoroughly in Functions That Are Applied to Functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00299))_
- How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dictionary for each argument. So when we write: _(javascriptallonge.pdf (source-range-c98ab3e6-00300))_
- The value '2' is bound to the name 'x' in the environment. _(javascriptallonge.pdf (source-range-c98ab3e6-00309))_
- The expression 'x' (the right side of the function) is evaluated within the environment we just created. _(javascriptallonge.pdf (source-range-c98ab3e6-00310))_
- The value of a variable when evaluated in an environment is the value bound to the variable's name in that environment, which is '2' _(javascriptallonge.pdf (source-range-c98ab3e6-00311))_
- When we talk about environments, we'll use an unsurprising syntax 25 for showing their bindings: {x: 2, ...} . meaning, that the environment is a dictionary, and that the value 2 is bound to the name x , and that there might be other stuff in that dictionary we aren't discussing right now. _(javascriptallonge.pdf (source-range-c98ab3e6-00313))_
- Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. _(javascriptallonge.pdf (source-range-c98ab3e6-00298))_
- - The expression 'x' (the right side of the function) is evaluated within the environment we just created. _(javascriptallonge.pdf (source-range-c98ab3e6-00310))_

### And also: / call by sharing

- Earlier, we distinguished JavaScript's value types from its reference types . At that time, we looked at how JavaScript distinguishes objects that are identical from objects that are not. Now it is time to take another look at the distinction between value and reference types. _(javascriptallonge.pdf (source-range-c98ab3e6-00315))_
- There is a property that JavaScript strictly maintains: When a value-any value-is passed as an argument to a function, the value bound in the function's environment must be identical to the original. _(javascriptallonge.pdf (source-range-c98ab3e6-00316))_
- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. As you recall, value types like strings and numbers are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans as it wishes. _(javascriptallonge.pdf (source-range-c98ab3e6-00317))_
- Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-c98ab3e6-00319))_
- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement 'call by sharing' semantics. Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types. _(javascriptallonge.pdf (source-range-c98ab3e6-00320))_
- 26 Unless the argument is NaN , which isn't equal to anything, including itself . NaN in JavaScript behaves a lot like NULL in SQL. _(javascriptallonge.pdf (source-range-c98ab3e6-00323))_
- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. _(javascriptallonge.pdf (source-range-c98ab3e6-00317))_
- 26 Unless the argument is NaN , which isn't equal to anything, including itself . _(javascriptallonge.pdf (source-range-c98ab3e6-00323))_

### And also: / Closures and Scope

- The environment belonging to the function with signature (x) => ... becomes {x: 1, ...} , and the result of applying the function is another function value. It makes sense that the result value is a function, because the expression for (x) => ... 's body is: _(javascriptallonge.pdf (source-range-c98ab3e6-00329))_
- So now we have a value representing that function. Then we're going to take the value of that function and apply it to the argument 2 , something like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00331))_
- So we seem to get a new environment {y: 2, ...} . How is the expression x going to be evaluated in that function's environment? There is no x in its environment, it must come from somewhere else. _(javascriptallonge.pdf (source-range-c98ab3e6-00333))_
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from 'outside' of a function that are referenced inside a function. For example, here's the equivalent code in Ruby: _(javascriptallonge.pdf (source-range-c98ab3e6-00334))_
- It makes sense that the result value is a function, because the expression for (x) => ... _(javascriptallonge.pdf (source-range-c98ab3e6-00329))_
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from 'outside' of a function that are referenced inside a function. _(javascriptallonge.pdf (source-range-c98ab3e6-00334))_

### And also: / Closures and Scope / if functions without free variables are pure, are closures impure?

- The function (y) => x is interesting. It contains a free variable , x . 27 A free variable is one that is not bound within the function. Up to now, we've only seen one way to 'bind' a variable, namely by passing in an argument with the same name. Since the function (y) => x doesn't have an argument named x , the variable x isn't bound in this function, which makes it 'free.' _(javascriptallonge.pdf (source-range-c98ab3e6-00338))_
- Now that we know that variables used in a function are either bound or free, we can bifurcate functions into those with free variables and those without: _(javascriptallonge.pdf (source-range-c98ab3e6-00339))_
- Functions containing no free variables are called pure functions . _(javascriptallonge.pdf (source-range-c98ab3e6-00340))_
- Functions containing one or more free variables are called closures . _(javascriptallonge.pdf (source-range-c98ab3e6-00341))_
- Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we've already seen: _(javascriptallonge.pdf (source-range-c98ab3e6-00342))_
- The first function doesn't have any variables, therefore doesn't have any free variables. The second doesn't have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ... , and it doesn't have a free variable: The only variable anywhere in its body is x , which is certainly bound within (x) => ... . _(javascriptallonge.pdf (source-range-c98ab3e6-00343))_
- From this, we learn something: A pure function can contain a closure. _(javascriptallonge.pdf (source-range-c98ab3e6-00344))_
- If pure functions can contain closures, can a closure contain a pure function? Using only what we've learned so far, attempt to compose a closure that contains a pure function. If you can't, give your reasoning for why it's impossible. _(javascriptallonge.pdf (source-range-c98ab3e6-00346))_
- Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x . _(javascriptallonge.pdf (source-range-c98ab3e6-00347))_
- 27 You may also hear the term 'non-local variable.' Both are correct. _(javascriptallonge.pdf (source-range-c98ab3e6-00348))_
- 27 A free variable is one that is not bound within the function. _(javascriptallonge.pdf (source-range-c98ab3e6-00338))_
- , and it doesn't have a free variable: The only variable anywhere in its body is x , which is certainly bound within (x) => ... _(javascriptallonge.pdf (source-range-c98ab3e6-00343))_
- The second doesn't have any free variables, because its only variable is bound. _(javascriptallonge.pdf (source-range-c98ab3e6-00343))_
- The third one is actually two functions, one inside the other. _(javascriptallonge.pdf (source-range-c98ab3e6-00343))_
- The first function doesn't have any variables, therefore doesn't have any free variables. _(javascriptallonge.pdf (source-range-c98ab3e6-00343))_
- has a free variable, but the entire expression refers to (x) => ... _(javascriptallonge.pdf (source-range-c98ab3e6-00343))_
- Using only what we've learned so far, attempt to compose a closure that contains a pure function. _(javascriptallonge.pdf (source-range-c98ab3e6-00346))_

### And also: / Closures and Scope / it's always the environment

- To understand how closures are evaluated, we need to revisit environments. As we've said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...} ? Let's fill in the blanks! _(javascriptallonge.pdf (source-range-c98ab3e6-00350))_
- (x) => x is called the I Combinator, or the Identity Function . (x) => (y) => x is called the K Combinator, or Kestrel . Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. a http://www.amzn.com/0192801422?tag=raganwald001-20 _(javascriptallonge.pdf (source-range-c98ab3e6-00353))_
- Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) . _(javascriptallonge.pdf (source-range-c98ab3e6-00360))_
- The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-c98ab3e6-00361))_
- As we've said before, all functions are associated with an environment. _(javascriptallonge.pdf (source-range-c98ab3e6-00350))_
- (x) => x is called the I Combinator, or the Identity Function . _(javascriptallonge.pdf (source-range-c98ab3e6-00353))_
- (x) => (y) => x is called the K Combinator, or Kestrel . _(javascriptallonge.pdf (source-range-c98ab3e6-00353))_
- Only you call it with (1)(2)(3) instead of (1, 2, 3) . _(javascriptallonge.pdf (source-range-c98ab3e6-00360))_
- Calling a curried function with only some of its arguments is sometimes called partial application b . _(javascriptallonge.pdf (source-range-c98ab3e6-00361))_

### And also: / Closures and Scope / shadowy variables from a shadowy planet

- An interesting thing happens when a variable has the same name as an ancestor environment's variable. Consider: _(javascriptallonge.pdf (source-range-c98ab3e6-00366))_
- The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x , it is ignored when evaluating x + y . JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of: _(javascriptallonge.pdf (source-range-c98ab3e6-00368))_
- When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor. _(javascriptallonge.pdf (source-range-c98ab3e6-00370))_
- This is often a good thing. _(javascriptallonge.pdf (source-range-c98ab3e6-00371))_
- The function (x, y) => x + y is a pure function, because its x is defined within its own environment. _(javascriptallonge.pdf (source-range-c98ab3e6-00368))_
- JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. _(javascriptallonge.pdf (source-range-c98ab3e6-00368))_

### And also: / Closures and Scope / which came first, the chicken or the egg?

- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. We are going to explore them in some detail as well as look at some of the other mechanisms JavaScript provides for working with variables and mutable state. _(javascriptallonge.pdf (source-range-c98ab3e6-00373))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } . _(javascriptallonge.pdf (source-range-c98ab3e6-00375))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00375))_

### And also: / That Constant Coffee Craving

- Up to now, all we've really seen are anonymous functions , functions that don't have a name. This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. Naming things is a critical part of programming, but all we've seen so far is how to name arguments. _(javascriptallonge.pdf (source-range-c98ab3e6-00380))_
- In order to bind 3.14159265 to the name PI , we'll need a function with a parameter of PI applied to an argument of 3.14159265 . If we put our function expression in parentheses, we can apply it to the argument of 3.14159265 : _(javascriptallonge.pdf (source-range-c98ab3e6-00383))_
- This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 . _(javascriptallonge.pdf (source-range-c98ab3e6-00387))_

### And also: / That Constant Coffee Craving / inside-out

- There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. We can turn things inside-out by putting the binding inside our diameter calculating function, like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00393))_
- Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development. _(javascriptallonge.pdf (source-range-c98ab3e6-00397))_
- The third one is easiest for most people to read. It separates concerns nicely: The 'outer' function describes its parameters: _(javascriptallonge.pdf (source-range-c98ab3e6-00398))_
- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated 'IIFE.' _(javascriptallonge.pdf (source-range-c98ab3e6-00399))_
- Everything else is encapsulated in its body. That's how it should be, naming PI is its concern, not ours. The other formulation: _(javascriptallonge.pdf (source-range-c98ab3e6-00401))_
- Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. Every time we invoke the outer function, we'll invoke the inner function. We could get around this by writing _(javascriptallonge.pdf (source-range-c98ab3e6-00405))_
- But then we've obfuscated our code, and we don't want to do that unless we absolutely have to. _(javascriptallonge.pdf (source-range-c98ab3e6-00407))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. And JavaScript does. _(javascriptallonge.pdf (source-range-c98ab3e6-00408))_
- There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. _(javascriptallonge.pdf (source-range-c98ab3e6-00393))_
- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-c98ab3e6-00399))_
- But then we've obfuscated our code, and we don't want to do that unless we absolutely have to. _(javascriptallonge.pdf (source-range-c98ab3e6-00407))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. _(javascriptallonge.pdf (source-range-c98ab3e6-00408))_

### And also: / That Constant Coffee Craving / const

- Another way to write our 'circumference' function would be to pass PI along with the diameter argument, something like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00410))_
- This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name. _(javascriptallonge.pdf (source-range-c98ab3e6-00414))_
- JavaScript gives us a way to do that, the const keyword. We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const : _(javascriptallonge.pdf (source-range-c98ab3e6-00415))_
- The const keyword introduces one or more bindings in the block that encloses it. It doesn't incur the cost of a function invocation. That's great. Even better, it puts the symbol (like PI ) close to the value ( 3.14159265 ). That's much better than what we were writing. _(javascriptallonge.pdf (source-range-c98ab3e6-00417))_
- We use the const keyword in a const statement . const statements occur inside blocks, we can't use them when we write a fat arrow that has an expression as its body. _(javascriptallonge.pdf (source-range-c98ab3e6-00418))_
- We can bind any expression. Functions are expressions, so we can bind helper functions: _(javascriptallonge.pdf (source-range-c98ab3e6-00425))_
- Notice calc(d) ? This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () . A name that's bound to a function is a valid expression evaluating to a function. 30 _(javascriptallonge.pdf (source-range-c98ab3e6-00427))_
- Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as 'first class entities. ' Functions are values that can be bound to names like any other value, passed as arguments, returned from other functions, and so forth. _(javascriptallonge.pdf (source-range-c98ab3e6-00428))_
- 30 We're into the second chapter and we've finally named a function. Sheesh. _(javascriptallonge.pdf (source-range-c98ab3e6-00431))_
- This differs from our example above in that there is only one environment, rather than two. _(javascriptallonge.pdf (source-range-c98ab3e6-00414))_

### And also: / That Constant Coffee Craving / nested blocks

- Up to now, we've only ever seen blocks we use as the body of functions. But there are other kinds of blocks. One of the places you can find blocks is in an if statement. In JavaScript, an if statement looks like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00433))_
- The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like: _(javascriptallonge.pdf (source-range-c98ab3e6-00437))_
- We've used a block as the else clause, and since it's a block, we've placed a const statement inside it. _(javascriptallonge.pdf (source-range-c98ab3e6-00441))_
- Up to now, we've only ever seen blocks we use as the body of functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00433))_
- We've used a block as the else clause, and since it's a block, we've placed a const statement inside it. _(javascriptallonge.pdf (source-range-c98ab3e6-00441))_

### And also: / That Constant Coffee Craving / const and lexical scope

- This seems very straightforward, but alas, there are some semantics of binding names that we need to understand if we're to place const anywhere we like. The first thing to ask ourselves is, what happens if we use const to bind two different values to the 'same' name? _(javascriptallonge.pdf (source-range-c98ab3e6-00443))_
- It's more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we've elided. We can use any expression in there, and that expression can invoke diameter_fn . For example: _(javascriptallonge.pdf (source-range-c98ab3e6-00447))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn . _(javascriptallonge.pdf (source-range-c98ab3e6-00449))_
- This is called lexical scoping 31 , because we can discover where a name is bound by looking at the source code for the program. We can see that PI is bound in an environment surrounding (diameter) => diameter * PI , we don't need to know where diameter_fn is invoked. _(javascriptallonge.pdf (source-range-c98ab3e6-00450))_
- Although we have bound 3 to PI in the environment surrounding diameter_fn(2) , the value that counts is 3.14159265 , the value we bound to PI in the environment surrounding (diameter) ⇒ diameter * PI. _(javascriptallonge.pdf (source-range-c98ab3e6-00453))_
- That much we can carefully work out from the way closures work. Does const work the same way? Let's find out: _(javascriptallonge.pdf (source-range-c98ab3e6-00454))_
- Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-c98ab3e6-00457))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn . _(javascriptallonge.pdf (source-range-c98ab3e6-00449))_

### And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

- We just saw that values bound with const use lexical scope, just like values bound with parameters. They are looked up in the environment where they are declared. And we know that functions create environments. Parameters are declared when we create functions, so it makes sense that parameters are bound to environments created when we invoke functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00459))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. So where are const variables bound? In the function environment? Or in an environment corresponding to the block? _(javascriptallonge.pdf (source-range-c98ab3e6-00460))_
- We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-c98ab3e6-00461))_
- And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the 'outer' environment? Let's rewrite things slightly differently: _(javascriptallonge.pdf (source-range-c98ab3e6-00468))_
- Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . Does that binding 'overwrite' the outer one? Will our function return 6 or 6.2831853 ? This is a book, you've already scanned ahead, so you know that the answer is no , the inner binding does not overwrite the outer binding: _(javascriptallonge.pdf (source-range-c98ab3e6-00470))_
- We say that when we bind a variable using a parameter inside another binding, the inner binding shadows the outer binding. It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-c98ab3e6-00472))_
- Parameters are only bound when we invoke a function. That's why we made all these IIFEs. But const statements can appear inside blocks. What happens when we use a const inside of a block? We'll need a gratuitous block. We've seen if statements, what could be more gratuitous than: _(javascriptallonge.pdf (source-range-c98ab3e6-00476))_
- Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it. _(javascriptallonge.pdf (source-range-c98ab3e6-00484))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. _(javascriptallonge.pdf (source-range-c98ab3e6-00460))_
- Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . _(javascriptallonge.pdf (source-range-c98ab3e6-00470))_
- We say that when we bind a variable using a parameter inside another binding, the inner binding shadows the outer binding. _(javascriptallonge.pdf (source-range-c98ab3e6-00472))_
- It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-c98ab3e6-00472))_
- Parameters are only bound when we invoke a function. _(javascriptallonge.pdf (source-range-c98ab3e6-00476))_
- But const statements can appear inside blocks. _(javascriptallonge.pdf (source-range-c98ab3e6-00476))_
- Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it. _(javascriptallonge.pdf (source-range-c98ab3e6-00484))_
- This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. _(javascriptallonge.pdf (source-range-c98ab3e6-00484))_

### And also: / That Constant Coffee Craving / rebinding

- JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-c98ab3e6-00491))_
- This is valuable, as it greatly simplifies the analysis of programs to see at a glance that when something is bound with const , we need never worry that its value may change. _(javascriptallonge.pdf (source-range-c98ab3e6-00492))_

### And also: / Naming Functions

- It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 . This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous. _(javascriptallonge.pdf (source-range-c98ab3e6-00496))_

### And also: / Naming Functions / the function keyword

- JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00498))_
- Something else we're about to discuss is optional. _(javascriptallonge.pdf (source-range-c98ab3e6-00505))_
- We have arguments in parentheses, just like fat arrow functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00506))_
- We do not have a fat arrow, we go directly to the body. _(javascriptallonge.pdf (source-range-c98ab3e6-00507))_
- We always use a block, we cannot write function (str) str + str . This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-c98ab3e6-00508))_
- In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment. _(javascriptallonge.pdf (source-range-c98ab3e6-00518))_
- 33 'Yes of course?' Well, in chapter of a book dedicated to naming functions, it is not surprising that feature we mention has something to do with naming functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00522))_
- Now, the function's actual name has no effect on the environment in which it is used. To whit: _(javascriptallonge.pdf (source-range-c98ab3e6-00524))_
- So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines whether a positive integer is even or not. We'll use it in an IIFE so that we don't have to bind it to a name with const : _(javascriptallonge.pdf (source-range-c98ab3e6-00526))_
- Clearly, the name even is bound to the function within the function's body . Is it bound to the function outside of the function's body? _(javascriptallonge.pdf (source-range-c98ab3e6-00528))_
- even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere else, you needn't. _(javascriptallonge.pdf (source-range-c98ab3e6-00530))_
- This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-c98ab3e6-00508))_
- Clearly, the name even is bound to the function within the function's body . _(javascriptallonge.pdf (source-range-c98ab3e6-00528))_
- even is bound within the function itself, but not outside it. _(javascriptallonge.pdf (source-range-c98ab3e6-00530))_

### And also: / Naming Functions / function declarations

- There is another syntax for naming and/or defining a function. It's called a function declaration statement , and it looks a lot like a named function expression, only we use it as a statement: _(javascriptallonge.pdf (source-range-c98ab3e6-00532))_
- In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-c98ab3e6-00535))_
- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently: _(javascriptallonge.pdf (source-range-c98ab3e6-00538))_
- The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code. _(javascriptallonge.pdf (source-range-c98ab3e6-00541))_
- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. _(javascriptallonge.pdf (source-range-c98ab3e6-00538))_

### And also: / Naming Functions / function declaration caveats 34

- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-c98ab3e6-00543))_
- 34 A number of the caveats discussed here were described in Jyrly Zaytsev's excellent article Named function expressions demystified. _(javascriptallonge.pdf (source-range-c98ab3e6-00544))_
- Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization. _(javascriptallonge.pdf (source-range-c98ab3e6-00546))_
- Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. So this is a function declaration: _(javascriptallonge.pdf (source-range-c98ab3e6-00547))_
- The parentheses make this an expression, not a function declaration. _(javascriptallonge.pdf (source-range-c98ab3e6-00549))_
- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. _(javascriptallonge.pdf (source-range-c98ab3e6-00543))_
- Function declarations are not supposed to occur inside of blocks. _(javascriptallonge.pdf (source-range-c98ab3e6-00546))_
- Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. _(javascriptallonge.pdf (source-range-c98ab3e6-00547))_

### And also: / Combinators and Function Decorators / higher-order functions

- As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. _(javascriptallonge.pdf (source-range-c98ab3e6-00552))_
- But before we go on, we'll talk about some specific types of higher-order functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00555))_

### And also: / Combinators and Function Decorators / combinators

- In this book, we will be using a looser definition of 'combinator:' Higher-order pure functions that take only functions as arguments and return a function. We won't be strict about using only previously defined combinators in their construction. _(javascriptallonge.pdf (source-range-c98ab3e6-00558))_
- This is, of course, just one example of many. You'll find lots more perusing the recipes in this book. While some programmers believe 'There Should Only Be One Way To Do It,' having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously. _(javascriptallonge.pdf (source-range-c98ab3e6-00561))_
- We won't be strict about using only previously defined combinators in their construction. _(javascriptallonge.pdf (source-range-c98ab3e6-00558))_
- While some programmers believe 'There Should Only Be One Way To Do It,' having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously. _(javascriptallonge.pdf (source-range-c98ab3e6-00561))_

### And also: / Combinators and Function Decorators / a balanced statement about combinators

- Code that uses a lot of combinators tends to name the verbs and adverbs (like doubleOf , addOne , and compose ) while avoiding language keywords and the names of nouns (like number ). So one perspective is that combinators are useful when you want to emphasize what you're doing and how it fits together, and more explicit code is useful when you want to emphasize what you're working with. _(javascriptallonge.pdf (source-range-c98ab3e6-00563))_

### And also: / Combinators and Function Decorators / function decorators

- So instead of writing !someFunction(42) , we can write not(someFunction)(42) . Hardly progress. But like compose , we could write either: _(javascriptallonge.pdf (source-range-c98ab3e6-00567))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-c98ab3e6-00573))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. _(javascriptallonge.pdf (source-range-c98ab3e6-00573))_

### And also: / Building Blocks

- When you look at functions within functions in JavaScript, there's a bit of a 'spaghetti code' look to it. The strength of JavaScript is that you can do anything. The weakness is that you will. There are ifs, fors, returns, everything thrown higgledy piggledy together. Although you needn't restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks. _(javascriptallonge.pdf (source-range-c98ab3e6-00575))_
- When you look at functions within functions in JavaScript, there's a bit of a 'spaghetti code' look to it. _(javascriptallonge.pdf (source-range-c98ab3e6-00575))_

### And also: / Building Blocks / composition

- It's really that simple: Whenever you are chaining two or more functions together, you're composing them. You can compose them with explicit JavaScript code as we've just done. You can also generalize composition with the B Combinator or 'compose' that we saw in Combinators and Decorators: _(javascriptallonge.pdf (source-range-c98ab3e6-00579))_
- If that was all there was to it, composition wouldn't matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways. _(javascriptallonge.pdf (source-range-c98ab3e6-00581))_
- In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument. _(javascriptallonge.pdf (source-range-c98ab3e6-00582))_
- Of course, you needn't use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit: _(javascriptallonge.pdf (source-range-c98ab3e6-00583))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-c98ab3e6-00581))_
- In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. _(javascriptallonge.pdf (source-range-c98ab3e6-00582))_

### And also: / Building Blocks / partial application

- Another basic building block is partial application . When a function takes multiple arguments, we 'apply' the function to the arguments by evaluating it with all of the arguments, producing a value. But what if we only supply some of the arguments? In that case, we can't get the final value, but we can get a function that represents part of our application. _(javascriptallonge.pdf (source-range-c98ab3e6-00586))_
- Code is easier than words for this. The Underscore 39 library provides a higher-order function called map . 40 It applies another function to each element of an array, like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00587))_
- The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-c98ab3e6-00592))_
- We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely: _(javascriptallonge.pdf (source-range-c98ab3e6-00594))_
- Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe. _(javascriptallonge.pdf (source-range-c98ab3e6-00598))_

### And also: / Magic Names

- When a function is applied to arguments (or 'called'), JavaScript binds the values of arguments to the function's argument names in an environment created for the function's execution. What we haven't discussed so far is that JavaScript also binds values to some 'magic' names in addition to any you put in the argument list. 42 _(javascriptallonge.pdf (source-range-c98ab3e6-00600))_

### And also: / Magic Names / the function keyword

- There are two separate rules for these 'magic' names, one for when you invoke a function using the function keyword, and another for functions defined with 'fat arrows.' We'll begin with how things work for functions defined with the function keyword. _(javascriptallonge.pdf (source-range-c98ab3e6-00602))_
- The first magic name is this , and it is bound to something called the function's context. We will explore this in more detail when we start discussing objects and classes. The second magic name is very interesting, it's called arguments , and the most interesting thing about it is that it contains a list of arguments passed to a function: _(javascriptallonge.pdf (source-range-c98ab3e6-00603))_
- arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00607))_
- The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses. _(javascriptallonge.pdf (source-range-c98ab3e6-00612))_

### And also: / Magic Names / magic names and fat arrows

- The magic names this and arguments have a different behaviour when you invoke a function that was defined with a fat arrow: Instead of being bound when the function is invoked, the fat arrow function always acquires the bindings for this and arguments from its enclosing scope, just like any other binding. _(javascriptallonge.pdf (source-range-c98ab3e6-00614))_
- For example, when this expression's inner function is defined with function , arguments[0] refers to its only argument, "inner" : _(javascriptallonge.pdf (source-range-c98ab3e6-00615))_
- But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function . And thus arguments[0] will refer to "outer" , not to "inner" : _(javascriptallonge.pdf (source-range-c98ab3e6-00617))_
- Although it seems quixotic for the two syntaxes to have different semantics, it makes sense when you consider the design goal: Fat arrow functions are designed to be very lightweight and are often used with constructs like mapping or callbacks to emulate syntax. _(javascriptallonge.pdf (source-range-c98ab3e6-00619))_
- To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. It uses mapWith , which we discussed in Building Blocks. 44 We'll use arguments just to show the difference between using a fat arrow and the function keyword: _(javascriptallonge.pdf (source-range-c98ab3e6-00620))_
- This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind arguments when it's invoked. But if we rewrite row to use the function keyword, it stops working: _(javascriptallonge.pdf (source-range-c98ab3e6-00622))_
- 44 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. _(javascriptallonge.pdf (source-range-c98ab3e6-00623))_
- Although this example is clearly unrealistic, there is a general design principle that deserves attention. Sometimes, a function is meant to be used as a Big-F function. It has a name, it is called by different pieces of code, it's a first-class entity in the code. _(javascriptallonge.pdf (source-range-c98ab3e6-00626))_
- But sometimes, a function is a small-f function. It's a simple representation of an expression to be computed. In our example above, row is a Big-F function, but (column) => column * arguments[0] is a small-f function, it exists just to give mapWith something to apply. _(javascriptallonge.pdf (source-range-c98ab3e6-00627))_
- Having magic variables apply to Big-F functions but not to small-G functions makes it much easier to use small-F functions as syntax, treating them as expressions or blocks that can be passed to functions like mapWith . _(javascriptallonge.pdf (source-range-c98ab3e6-00628))_
- For example, when this expression's inner function is defined with function , arguments[0] refers to its only argument, "inner" : _(javascriptallonge.pdf (source-range-c98ab3e6-00615))_
- This works just fine, because arguments[0] refers to the 3 we passed to the function row . _(javascriptallonge.pdf (source-range-c98ab3e6-00622))_
- It's the same idea, after all. _(javascriptallonge.pdf (source-range-c98ab3e6-00623))_

### And also: / Summary / Functions

- Functions are values that can be part of expressions, returned from other functions, and so forth. _(javascriptallonge.pdf (source-range-c98ab3e6-00632))_
- Functions are reference values . _(javascriptallonge.pdf (source-range-c98ab3e6-00633))_
- Functions are applied to arguments. _(javascriptallonge.pdf (source-range-c98ab3e6-00634))_
- Fat arrow functions have expressions or blocks as their bodies. _(javascriptallonge.pdf (source-range-c98ab3e6-00636))_
- function keyword functions always have blocks as their bodies. _(javascriptallonge.pdf (source-range-c98ab3e6-00637))_
- Function bodies have zero or more statements. _(javascriptallonge.pdf (source-range-c98ab3e6-00638))_
- Block bodies evaluate to whatever is returned with the return keyword, or to undefined . _(javascriptallonge.pdf (source-range-c98ab3e6-00640))_
- JavaScript uses const to bind values to names within block scope. _(javascriptallonge.pdf (source-range-c98ab3e6-00641))_
- JavaScript uses function declarations to bind functions to names within function scope. Function declarations are 'hoisted.' _(javascriptallonge.pdf (source-range-c98ab3e6-00642))_
- Blocks also create scopes if const statements are within them. _(javascriptallonge.pdf (source-range-c98ab3e6-00644))_
- Scopes are nested and free variable references closed over. _(javascriptallonge.pdf (source-range-c98ab3e6-00645))_
- Variables can shadow variables in an enclosing scope. _(javascriptallonge.pdf (source-range-c98ab3e6-00646))_
- - JavaScript uses const to bind values to names within block scope. _(javascriptallonge.pdf (source-range-c98ab3e6-00641))_
- - JavaScript uses function declarations to bind functions to names within function scope. _(javascriptallonge.pdf (source-range-c98ab3e6-00642))_
- - Blocks also create scopes if const statements are within them. _(javascriptallonge.pdf (source-range-c98ab3e6-00644))_

## Technical atoms

### Technical frame 1: And also:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00248))_

<a id="atom-technical-atom-13dd89f3ac118210"></a>
```
(() => {
return 1 + 1;
2 + 2
})()
//=> 2
```

### Technical frame 2: And also:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00249))_

<a id="atom-technical-atom-a457a1b3175f6a8e"></a>
> The return statement is the first statement we've seen, and it behaves differently than an expression. For example, you can't use one as the expression in a simple function, because it isn't an expression:

### Technical frame 3: And also:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00250))_

<a id="atom-technical-atom-a667c22563532c5e"></a>
```
(() => return 0)()
//=> ERROR
```

### Technical frame 4: And also: / functions that evaluate to functions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00256))_

> That's a function! It's a function that when applied, evaluates to a function that when applied, evaluates to 0 . So we have a function, that returns a function, that returns zero . Likewise:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00253))_

<a id="atom-technical-atom-d4eb2fd6363b86b4"></a>
> If an expression that evaluates to a function is, well, an expression, and if a return statement can have any expression on its right side… Can we put an expression that evaluates to a function on the right side of a function expression?

### Technical frame 5: And also: / functions that evaluate to functions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00256))_

> That's a function! It's a function that when applied, evaluates to a function that when applied, evaluates to 0 . So we have a function, that returns a function, that returns zero . Likewise:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00255))_

<a id="atom-technical-atom-4b34b196e6fba444"></a>
```
() => () => 0
```

### Technical frame 6: And also: / functions that evaluate to functions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00263))_

> Well. We've been very clever, but so far this all seems very abstract. Diffraction of a crystal is beautiful and interesting in its own right, but you can't blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. So… In the next chapter, 'I'd Like to Have an Argument, Please,' we'll see how to make functions practical.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00257))_

<a id="atom-technical-atom-33d003f8c5230f90"></a>
```
() => () => true
```

### Technical frame 7: And also: / functions that evaluate to functions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00263))_

> Well. We've been very clever, but so far this all seems very abstract. Diffraction of a crystal is beautiful and interesting in its own right, but you can't blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. So… In the next chapter, 'I'd Like to Have an Argument, Please,' we'll see how to make functions practical.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00259))_

<a id="atom-technical-atom-7604c14ab1102181"></a>
```
(() => () => true)()()
//=> true
```

### Technical frame 8: And also: / functions that evaluate to functions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00263))_

> Well. We've been very clever, but so far this all seems very abstract. Diffraction of a crystal is beautiful and interesting in its own right, but you can't blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. So… In the next chapter, 'I'd Like to Have an Argument, Please,' we'll see how to make functions practical.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00261))_

<a id="atom-technical-atom-be15185d1d021d50"></a>
```
() => () => { return true; }
```

### Technical frame 9: And also: / Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00269))_

> This function has one argument, room , and an empty body. Here's a function with two arguments and an empty body:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00268))_

<a id="atom-technical-atom-378182b30d568639"></a>
```
(room) => {}
```

### Technical frame 10: And also: / Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00271))_

> I'm sure you are perfectly comfortable with the idea that this function has two arguments, room , and board . What does one do with the arguments? Use them in the body, of course. What do you think this is?

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00270))_

<a id="atom-technical-atom-b307aaeb37325856"></a>
```
(room, board) => {}
```

### Technical frame 11: And also: / Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00273))_

> It's a function for calculating the circumference of a circle given the diameter. I read that aloud as 'When applied to a value representing the diameter, this function returns the diameter times 3.14159265.'

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00272))_

<a id="atom-technical-atom-1df34609a129f999"></a>
```
(diameter) => diameter * 3.14159265
```

### Technical frame 12: And also: / Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00276))_

> You won't be surprised to see how to write and apply a function to two arguments:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00275))_

<a id="atom-technical-atom-0d3e28f9e8eb415f"></a>
```
((diameter) => diameter * 3.14159265)(2)
//=> 6.2831853
```

### Technical frame 13: And also: / Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00276))_

> You won't be surprised to see how to write and apply a function to two arguments:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00278))_

<a id="atom-technical-atom-765d5bcc7f305651"></a>
```
((room, board) => room + board)(800, 150)
//=> 950
```

### Technical frame 14: And also: / Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00276))_

> You won't be surprised to see how to write and apply a function to two arguments:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00279))_

<a id="atom-technical-atom-3cd5bc2727742709"></a>
> [Figure] (p.40)

### Technical frame 15: And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by value

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00290))_

> What happened internally is that the expression 1 + 1 was evaluated first, resulting in 2 . Then our circumference function was applied to 2 . 24

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00289))_

<a id="atom-technical-atom-a46e927ad3ebbe03"></a>
```
((diameter) => diameter * 3.14159265)(1 + 1)
//=> 6.2831853
```

### Technical frame 16: And also: / variables and bindings

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00295))_

> (x) => (y) => x just looks crazy, as if we are learning English as a second language and the teacher promises us that soon we will be using words like antidisestablishmentarianism . Besides a desire to use long words to sound impressive, this is not going to seem attractive until we find ourselves wanting to discuss the role of the Church of England in 19th century British politics.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00294))_

<a id="atom-technical-atom-3ef90bd4cce342bd"></a>
```
(x) => (y) => x
```

### Technical frame 17: And also: / variables and bindings

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00309))_

> The value '2' is bound to the name 'x' in the environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00301))_

<a id="atom-technical-atom-71caad9251a6dc1e"></a>
```
((x) => x)(2)
//=> 2
```

### Technical frame 18: And also: / variables and bindings

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00309))_

> The value '2' is bound to the name 'x' in the environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00305))_

<a id="atom-technical-atom-97705926f590cf82"></a>
> - One sub-expression, (x) => x evaluates to a function.

### Technical frame 19: And also: / call by sharing

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00319))_

> Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00317))_

<a id="atom-technical-atom-a0c1b297f3e92d72"></a>
> So JavaScript can make as many copies of strings, numbers, or booleans as it wishes.

### Technical frame 20: And also: / call by sharing

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00323))_

> 26 Unless the argument is NaN , which isn't equal to anything, including itself . NaN in JavaScript behaves a lot like NULL in SQL.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00322))_

<a id="atom-technical-atom-300f3bd87e349a64"></a>
```
(value) =>
((ref1, ref2) => ref1 === ref2)(value, value)
```

### Technical frame 21: And also: / Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00329))_

> The environment belonging to the function with signature (x) => ... becomes {x: 1, ...} , and the result of applying the function is another function value. It makes sense that the result value is a function, because the expression for (x) => ... 's body is:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00326))_

<a id="atom-technical-atom-914c69e7d0554d1d"></a>
```
((x) => (y) => x)(1)(2)
//=> 1
```

### Technical frame 22: And also: / Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00329))_

> The environment belonging to the function with signature (x) => ... becomes {x: 1, ...} , and the result of applying the function is another function value. It makes sense that the result value is a function, because the expression for (x) => ... 's body is:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00328))_

<a id="atom-technical-atom-4aea764a0d3a89b7"></a>
```
((x) => (y) => x)(1)
//=> [Function]
```

### Technical frame 23: And also: / Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00331))_

> So now we have a value representing that function. Then we're going to take the value of that function and apply it to the argument 2 , something like this:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00330))_

<a id="atom-technical-atom-57f43cc9744dbfe6"></a>
```
(y) => x
```

### Technical frame 24: And also: / Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00333))_

> So we seem to get a new environment {y: 2, ...} . How is the expression x going to be evaluated in that function's environment? There is no x in its environment, it must come from somewhere else.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00332))_

<a id="atom-technical-atom-f8c0ddd0951b9177"></a>
```
((y) => x)(2)
```

### Technical frame 25: And also: / Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00334))_

> This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from 'outside' of a function that are referenced inside a function. For example, here's the equivalent code in Ruby:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00335))_

<a id="atom-technical-atom-75800df132b3dc98"></a>
```
lambda { |x|
lambda { |y| x }
}[1][2]
#=> 1
```

### Technical frame 26: And also: / Closures and Scope / if functions without free variables are pure, are closures impure?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00346))_

> If pure functions can contain closures, can a closure contain a pure function? Using only what we've learned so far, attempt to compose a closure that contains a pure function. If you can't, give your reasoning for why it's impossible.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00345))_

<a id="atom-technical-atom-392b2329d2f738f0"></a>
> [Figure] (p.45)

### Technical frame 27: And also: / Closures and Scope / if functions without free variables are pure, are closures impure?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00347))_

> Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00346))_

<a id="atom-technical-atom-9b8745fb9ab701d4"></a>
> If pure functions can contain closures, can a closure contain a pure function?

### Technical frame 28: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00353))_

> (x) => x is called the I Combinator, or the Identity Function . (x) => (y) => x is called the K Combinator, or Kestrel . Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. a http://www.amzn.com/0192801422?tag=raganwald001-20

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00351))_

<a id="atom-technical-atom-296a8c7cbfbf3dd3"></a>
> So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

### Technical frame 29: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00360))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00355))_

<a id="atom-technical-atom-f0178d0a52be8520"></a>
```
bh
```

### Technical frame 30: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00360))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00357))_

<a id="atom-technical-atom-19cca9a511188b36"></a>
```
(x) =>
(y) =>
(z) => x + y + z
```

### Technical frame 31: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00360))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00359))_

<a id="atom-technical-atom-30a4e428ab8015d7"></a>
```
(x, y, z) => x + y + z
```

### Technical frame 32: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00361))_

> The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00362))_

<a id="atom-technical-atom-2b0e91b9cc610d80"></a>
```
ah
bh
```

### Technical frame 33: And also: / Closures and Scope / shadowy variables from a shadowy planet

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00368))_

> The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x , it is ignored when evaluating x + y . JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00367))_

<a id="atom-technical-atom-32164e0d6666462d"></a>
```
(x) =>
(x, y) => x + y
```

### Technical frame 34: And also: / Closures and Scope / shadowy variables from a shadowy planet

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00370))_

> When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00369))_

<a id="atom-technical-atom-a67da09f86e7c7b4"></a>
```
(x) =>
(x, y) =>
(w, z) =>
(w) =>
x + y + z
```

### Technical frame 35: And also: / Closures and Scope / which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00375))_

> JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00376))_

<a id="atom-technical-atom-88057ff31b65b082"></a>
> If you don't want your code to operate directly within the global environment, what can you do?

### Technical frame 36: And also: / Closures and Scope / which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00375))_

> JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00377))_

<a id="atom-technical-atom-0585f3d8f8df0d96"></a>
```
// top of the file
(() => {
// ... lots of JavaScript ...
})();
// bottom of the file
```

### Technical frame 37: And also: / That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00383))_

> In order to bind 3.14159265 to the name PI , we'll need a function with a parameter of PI applied to an argument of 3.14159265 . If we put our function expression in parentheses, we can apply it to the argument of 3.14159265 :

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00381))_

<a id="atom-technical-atom-01c8bab18bb52d95"></a>
> There are other ways to name things in JavaScript, but before we learn some of those, let's see how to use what we already have to name things. Let's revisit a very simple example:

### Technical frame 38: And also: / That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00387))_

> This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00384))_

<a id="atom-technical-atom-014d13752577ce6f"></a>
```
((PI) =>
// ????
)(3.14159265)
```

### Technical frame 39: And also: / That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00387))_

> This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00386))_

<a id="atom-technical-atom-91d57d223a0298ed"></a>
```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```

### Technical frame 40: And also: / That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00387))_

> This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00390))_

<a id="atom-technical-atom-e4aacf2a2db94ef5"></a>
```
((diameter) => diameter * 3.14159265)(2)
//=> 6.2831853
((PI) =>
(diameter) => diameter * PI
)(3.14159265)(2)
//=> 6.2831853
```

### Technical frame 41: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00397))_

> Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00394))_

<a id="atom-technical-atom-4395b77b43edc5c5"></a>
```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```

### Technical frame 42: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00397))_

> Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00396))_

<a id="atom-technical-atom-c63271963e8f9475"></a>
```
((diameter) => diameter * 3.14159265)(2)
//=> 6.2831853
((PI) =>
(diameter) => diameter * PI
)(3.14159265)(2)
//=> 6.2831853
((diameter) =>
((PI) =>
diameter * PI)(3.14159265))(2)
//=> 6.2831853
```

### Technical frame 43: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00401))_

> Everything else is encapsulated in its body. That's how it should be, naming PI is its concern, not ours. The other formulation:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00400))_

<a id="atom-technical-atom-175dcf62d9bcf771"></a>
```
(diameter) =>
// ...
```

### Technical frame 44: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00405))_

> Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. Every time we invoke the outer function, we'll invoke the inner function. We could get around this by writing

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00402))_

<a id="atom-technical-atom-bab824258ef59114"></a>
```
((PI) =>
// ...
)(3.14159265)
```

### Technical frame 45: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00405))_

> Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. Every time we invoke the outer function, we'll invoke the inner function. We could get around this by writing

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00404))_

<a id="atom-technical-atom-85f6749d8dfcade5"></a>
```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```

### Technical frame 46: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00407))_

> But then we've obfuscated our code, and we don't want to do that unless we absolutely have to.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00406))_

<a id="atom-technical-atom-1572f8b0441b9fa7"></a>
```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```

### Technical frame 47: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00414))_

> This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00411))_

<a id="atom-technical-atom-6916d39cc8564463"></a>
```
(diameter, PI) => diameter * PI
```

### Technical frame 48: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00414))_

> This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00413))_

<a id="atom-technical-atom-4334c5d0c389dcf1"></a>
```
((diameter, PI) => diameter * PI)(2, 3.14159265)
//=> 6.2831853
```

### Technical frame 49: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00417))_

> The const keyword introduces one or more bindings in the block that encloses it. It doesn't incur the cost of a function invocation. That's great. Even better, it puts the symbol (like PI ) close to the value ( 3.14159265 ). That's much better than what we were writing.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00416))_

<a id="atom-technical-atom-a482cf19ef0e144c"></a>
```
(diameter) => {
const PI = 3.14159265;
return diameter * PI
}
```

### Technical frame 50: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00425))_

> We can bind any expression. Functions are expressions, so we can bind helper functions:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00420))_

<a id="atom-technical-atom-cc841d8d4d9cc286"></a>
```
((diameter) =>
((PI) =>
```

### Technical frame 51: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00425))_

> We can bind any expression. Functions are expressions, so we can bind helper functions:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00421))_

<a id="atom-technical-atom-4ef438c5d6765359"></a>
```
diameter * PI)(3.14159265))(2)
Or:
((diameter, PI) => diameter * PI)(2, 3.14159265)
```

### Technical frame 52: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00425))_

> We can bind any expression. Functions are expressions, so we can bind helper functions:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00422))_

<a id="atom-technical-atom-575cc476e9cdf052"></a>
```
//=> 6.2831853
```

### Technical frame 53: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00425))_

> We can bind any expression. Functions are expressions, so we can bind helper functions:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00424))_

<a id="atom-technical-atom-14e81cd8609a9147"></a>
```
((diameter) => {
const PI = 3.14159265;
return diameter * PI
})(2)
//=> 6.2831853
```

### Technical frame 54: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00427))_

> Notice calc(d) ? This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () . A name that's bound to a function is a valid expression evaluating to a function. 30

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00426))_

<a id="atom-technical-atom-e03fc883e3aa964c"></a>
```
(d) => {
const calc = (diameter) => {
const PI = 3.14159265;
return diameter * PI
};
return "The circumference is " + calc(d)
}
```

### Technical frame 55: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00428))_

> Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as 'first class entities. ' Functions are values that can be bound to names like any other value, passed as arguments, returned from other functions, and so forth.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00427))_

<a id="atom-technical-atom-068b206236850b14"></a>
> This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () .

### Technical frame 56: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00431))_

> 30 We're into the second chapter and we've finally named a function. Sheesh.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00430))_

<a id="atom-technical-atom-ce6b11407d77f023"></a>
```
(d) => {
const PI
= 3.14159265,
calc = (diameter) => diameter * PI;
return "The circumference is " + calc(d)
}
```

### Technical frame 57: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00437))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00433))_

<a id="atom-technical-atom-ff213fd41fe9d935"></a>
> One of the places you can find blocks is in an if statement.

### Technical frame 58: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00437))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00434))_

<a id="atom-technical-atom-e67b820748ba0049"></a>
```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else
return !even(x - 1);
}
return even(n)
}
```

### Technical frame 59: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00437))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00436))_

<a id="atom-technical-atom-a52d039337b47d63"></a>
```
((n) => {
const even = (x) => {
if (x === 0)
return true;
else
return !even(x - 1);
}
return even(n)
})(13)
//=> false
```

### Technical frame 60: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00441))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00438))_

<a id="atom-technical-atom-0d9f08f18535239f"></a>
```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else {
const odd = (y) => !even(y);
return odd(x - 1);
}
```

### Technical frame 61: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00441))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00439))_

<a id="atom-technical-atom-8c9e193ceefd106f"></a>
```
}
return even(n)
}
And this also works:
((n) => {
const even = (x) => {
if (x === 0)
return true;
else {
const odd = (y) => !even(y);
return odd(x - 1);
}
}
return even(n)
})(42)
```

### Technical frame 62: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00441))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00440))_

<a id="atom-technical-atom-7606d2710d39fd29"></a>
```
//=> true
```

### Technical frame 63: And also: / That Constant Coffee Craving / const and lexical scope

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00447))_

> It's more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we've elided. We can use any expression in there, and that expression can invoke diameter_fn . For example:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00446))_

<a id="atom-technical-atom-0439a379681b59e7"></a>
```
((diameter_fn) =>
// ...
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
```

### Technical frame 64: And also: / That Constant Coffee Craving / const and lexical scope

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00449))_

> We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00448))_

<a id="atom-technical-atom-3aae9befa17f21cb"></a>
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

### Technical frame 65: And also: / That Constant Coffee Craving / const and lexical scope

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00453))_

> Although we have bound 3 to PI in the environment surrounding diameter_fn(2) , the value that counts is 3.14159265 , the value we bound to PI in the environment surrounding (diameter) ⇒ diameter * PI.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00452))_

<a id="atom-technical-atom-5a5cae3b129eb377"></a>
```
((diameter_fn) =>
((PI) =>
diameter_fn(2)
)(3)
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
//=> 6.2831853
```

### Technical frame 66: And also: / That Constant Coffee Craving / const and lexical scope

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00457))_

> Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00456))_

<a id="atom-technical-atom-ea7c217727207a4f"></a>
```
((diameter_fn) => {
const PI = 3;
return diameter_fn(2)
})(
(() => {
const PI = 3.14159265;
return (diameter) => diameter * PI
})()
)
//=> 6.2831853
```

### Technical frame 67: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00468))_

> And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the 'outer' environment? Let's rewrite things slightly differently:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00463))_

<a id="atom-technical-atom-6115afb4cc710ca8"></a>
```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```

### Technical frame 68: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00468))_

> And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the 'outer' environment? Let's rewrite things slightly differently:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00465))_

<a id="atom-technical-atom-5719038d877f3e6c"></a>
```
((PI) =>
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)(3)
```

### Technical frame 69: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00468))_

> And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the 'outer' environment? Let's rewrite things slightly differently:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00467))_

<a id="atom-technical-atom-5a3bc9b5d2ababaa"></a>
```
((PI) =>
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)(3)(2)
//=> 6.2831853
```

### Technical frame 70: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00470))_

> Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . Does that binding 'overwrite' the outer one? Will our function return 6 or 6.2831853 ? This is a book, you've already scanned ahead, so you know that the answer is no , the inner binding does not overwrite the outer binding:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00469))_

<a id="atom-technical-atom-81cc93279d65de76"></a>
```
((PI) => {
((PI) => {})(3);
return (diameter) => diameter * PI;
})(3.14159265)
```

### Technical frame 71: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00472))_

> We say that when we bind a variable using a parameter inside another binding, the inner binding shadows the outer binding. It has effect inside its own scope, but does not affect the binding in the enclosing scope.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00471))_

<a id="atom-technical-atom-e607cb51ca30f199"></a>
```
((PI) => {
((PI) => {})(3);
return (diameter) => diameter * PI;
})(3.14159265)(2)
//=> 6.2831853
```

### Technical frame 72: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00476))_

> Parameters are only bound when we invoke a function. That's why we made all these IIFEs. But const statements can appear inside blocks. What happens when we use a const inside of a block? We'll need a gratuitous block. We've seen if statements, what could be more gratuitous than:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00474))_

<a id="atom-technical-atom-f59577654195d7a7"></a>
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

### Technical frame 73: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00484))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00477))_

<a id="atom-technical-atom-0b9114a0af25f5dd"></a>
```
if (true) {
// an immediately invoked block statement (IIBS)
}
Let’s try it:
((diameter) => {
const PI = 3;
if (true) {
const PI = 3.14159265;
return diameter * PI;
}
})(2)
//=> 6.2831853
((diameter) => {
const PI = 3.14159265;
if (true) {
const PI = 3;
}
return diameter * PI;
```

### Technical frame 74: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00484))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00478))_

<a id="atom-technical-atom-ee49304565dd3e20"></a>
```
})(2)
//=> 6.2831853
```

### Technical frame 75: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00484))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00481))_

<a id="atom-technical-atom-c802e18aa1217e7c"></a>
```
((diameter) => {
const PI = 3.14159265;
if (true) {
const PI = 3;
}
return diameter * PI;
})(2)
//=> would return 6 if const had function scope
```

### Technical frame 76: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00484))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00482))_

<a id="atom-technical-atom-bbb1c4392555e4dc"></a>
> If const always bound its value to the name defined in the function's environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents.

### Technical frame 77: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00484))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00483))_

<a id="atom-technical-atom-1f302173cfb952ac"></a>
```
((diameter) => {
if (true) {
const PI = 3.14159265;
}
return diameter * PI;
})(2)
//=> would return 6.2831853 if const had function scope
```

### Technical frame 78: And also: / That Constant Coffee Craving / rebinding

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00491))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00488))_

<a id="atom-technical-atom-91190aee40557e7b"></a>
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

### Technical frame 79: And also: / That Constant Coffee Craving / rebinding

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00491))_

> JavaScript does not permit us to rebind a name that has been bound with const . We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00490))_

<a id="atom-technical-atom-fac32a47c5fd8469"></a>
```
evenStevens = (n) => {
if (n === 0) {
return true;
}
else if (n == 1) {
return false;
}
else {
return evenStevens(n - 2);
}
}
//=> ERROR, evenStevens is read-only
```

### Technical frame 80: And also: / Naming Functions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00496))_

> It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 . This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00495))_

<a id="atom-technical-atom-ef2dff219c6c6e7e"></a>
```
const repeat = (str) => str + str
```

### Technical frame 81: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00505))_

> Something else we're about to discuss is optional.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00500))_

<a id="atom-technical-atom-5e357060e1b06a1e"></a>
```
(str) => str + str
```

### Technical frame 82: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00505))_

> Something else we're about to discuss is optional.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00502))_

<a id="atom-technical-atom-cc7641804dc4b408"></a>
```
function (str) { return str + str }
```

### Technical frame 83: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00508))_

> We always use a block, we cannot write function (str) str + str . This means that if we want our functions to return a value, we always need to use the return keyword

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00509))_

<a id="atom-technical-atom-403ec4c29ac30a7d"></a>
> If we leave out the 'something optional' that comes after the function keyword, we can translate all of the fat arrow functions that we've seen into function keyword functions, e.g.

### Technical frame 84: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00518))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00510))_

<a id="atom-technical-atom-ca757f2ec4259859"></a>
```
(n) => (1.618**n - -1.618**-n) / 2.236
```

### Technical frame 85: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00518))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00512))_

<a id="atom-technical-atom-b893bf7c1c32203d"></a>
```
function (n) {
return (1.618**n - -1.618**-n) / 2.236;
}
```

### Technical frame 86: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00518))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00515))_

<a id="atom-technical-atom-b5f05fe8ccef523e"></a>
```
const repeat = function repeat (str) {
return str + str;
};
const fib = function fib (n) {
return (1.618**n - -1.618**-n) / 2.236;
};
```

### Technical frame 87: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00518))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00516))_

<a id="atom-technical-atom-0f8e3dc99df94b1b"></a>
> Placing a name between the function keyword and the argument list names the function. Confusingly, the name of the function is not exactly the same thing as the name we may choose to bind to the value of the function. For example, we can write:

### Technical frame 88: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00518))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00517))_

<a id="atom-technical-atom-92f9c606d28cd91a"></a>
```
const double = function repeat (str) {
return str + str;
}
```

### Technical frame 89: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00522))_

> 33 'Yes of course?' Well, in chapter of a book dedicated to naming functions, it is not surprising that feature we mention has something to do with naming functions.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00520))_

<a id="atom-technical-atom-329f1c0328539cfb"></a>
```
double.name
//=> 'repeat'
```

### Technical frame 90: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00524))_

> Now, the function's actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00523))_

<a id="atom-technical-atom-37edd8dd08e32d9a"></a>
```
someBackboneView.on('click', function clickHandler () {
//...
});
```

### Technical frame 91: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00526))_

> So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines whether a positive integer is even or not. We'll use it in an IIFE so that we don't have to bind it to a name with const :

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00525))_

<a id="atom-technical-atom-64e54ae8241a5d4a"></a>
```
const bindingName = function actualName () {
//...
};
bindingName
//=> [Function: actualName]
actualName
//=> ReferenceError: actualName is not defined
```

### Technical frame 92: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00528))_

> Clearly, the name even is bound to the function within the function's body . Is it bound to the function outside of the function's body?

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00527))_

<a id="atom-technical-atom-9bd9a3108ea28b7e"></a>
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

### Technical frame 93: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00530))_

> even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere else, you needn't.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00529))_

<a id="atom-technical-atom-245f6ccf936b3285"></a>
```
even
//=> Can't find variable: even
```

### Technical frame 94: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00535))_

> In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00533))_

<a id="atom-technical-atom-0ab51df09609c9a7"></a>
```
function someName () {
// ...
}
This behaves a little like:
const someName = function someName ()
// ...
}
```

### Technical frame 95: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00535))_

> In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00534))_

<a id="atom-technical-atom-6e5c8cf419fc735b"></a>
```
{
```

### Technical frame 96: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00538))_

> We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00536))_

<a id="atom-technical-atom-67646880ada400e3"></a>
> Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const :

### Technical frame 97: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00538))_

> We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00537))_

<a id="atom-technical-atom-bee66abec44ca7e0"></a>
```
(function () {
return fizzbuzz();
const fizzbuzz = function fizzbuzz () {
return "Fizz" + "Buzz";
}
})()
//=> undefined is not a function (evaluating 'fizzbuzz()')
```

### Technical frame 98: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00541))_

> The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00539))_

<a id="atom-technical-atom-524f907061a9862d"></a>
```
(function () {
return fizzbuzz();
function fizzbuzz () {
return "Fizz" + "Buzz";
}
})()
//=> 'FizzBuzz'
Although fizzbuzz is declared later in the function, JavaScript behaves as if we’d written:
(function () {
const fizzbuzz = function fizzbuzz () {
```

### Technical frame 99: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00541))_

> The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00540))_

<a id="atom-technical-atom-48428010d2f136cf"></a>
```
const fizzbuzz = function fizzbuzz ()
return "Fizz" + "Buzz";
}
return fizzbuzz();
})()
```

### Technical frame 100: And also: / Naming Functions / function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00546))_

> Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00545))_

<a id="atom-technical-atom-0a43a2ced43dfe34"></a>
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

### Technical frame 101: And also: / Naming Functions / function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00547))_

> Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. So this is a function declaration:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00546))_

<a id="atom-technical-atom-6dca4ba4c64161ea"></a>
> Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

### Technical frame 102: And also: / Naming Functions / function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00549))_

> The parentheses make this an expression, not a function declaration.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00548))_

<a id="atom-technical-atom-10f60b81014128d0"></a>
```
function trueDat () { return true }
But this is not:
(function trueDat () { return true })
```

### Technical frame 103: And also: / Combinators and Function Decorators / higher-order functions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00552))_

> As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00554))_

<a id="atom-technical-atom-efae692b221fbed3"></a>
```
const repeat = (num, fn) =>
(num > 0)
? (repeat(num - 1, fn), fn(num))
: undefined
repeat(3, function (n) {
console.log(`Hello ${n}`)
})
//=>
'Hello 1'
'Hello 2'
'Hello 3'
undefined
```

### Technical frame 104: And also: / Combinators and Function Decorators / combinators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00558))_

> In this book, we will be using a looser definition of 'combinator:' Higher-order pure functions that take only functions as arguments and return a function. We won't be strict about using only previously defined combinators in their construction.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00557))_

<a id="atom-technical-atom-34eed5cf99dd08a1"></a>
```text
combinators
The word 'combinator' has a precise technical meaning in mathematics:
'A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.'-Wikipedia 35
If we were learning Combinatorial Logic, we'd start with the most basic combinators like S , K , and I , and work up from there to practical combinators. We'd learn that the fundamental combinators are named after birds following the example of Raymond Smullyan's famous book To Mock a Mockingbird 36 .
35 https://en.wikipedia.org/wiki/Combinatory_logic
36 http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 35 | https://en.wikipedia.org/wiki/Combinatory_logic |
| 36 | http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20 |

</details>

### Technical frame 105: And also: / Combinators and Function Decorators / combinators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00561))_

> This is, of course, just one example of many. You'll find lots more perusing the recipes in this book. While some programmers believe 'There Should Only Be One Way To Do It,' having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00560))_

<a id="atom-technical-atom-be90997af459ed38"></a>
```
const compose = (a, b) =>
(c) => a(b(c))
Let’s say we have:
const addOne = (number) => number + 1;
const doubleOf = (number) => number * 2;
With compose, anywhere you would write
const doubleOfAddOne = (number) => doubleOf(addOne(number));
You could also write:
const doubleOfAddOne = compose(doubleOf, addOne);
```

### Technical frame 106: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00573))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00565))_

<a id="atom-technical-atom-ece2f4b7b92ce2c5"></a>
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

### Technical frame 107: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00567))_

> So instead of writing !someFunction(42) , we can write not(someFunction)(42) . Hardly progress. But like compose , we could write either:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00566))_

<a id="atom-technical-atom-412f451ef26f53cb"></a>
```
const not = (fn) => (x) => !fn(x)
```

### Technical frame 108: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00573))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00568))_

<a id="atom-technical-atom-053ba4103aaa6009"></a>
```
const something = (x) => x != null;
```

### Technical frame 109: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00573))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00570))_

<a id="atom-technical-atom-ffe2f38a07f2ab5e"></a>
```
const nothing = (x) => !something(x);
```

### Technical frame 110: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00573))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00572))_

<a id="atom-technical-atom-48b9732f10355b03"></a>
```
const nothing = not(something);
```

### Technical frame 111: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00579))_

> It's really that simple: Whenever you are chaining two or more functions together, you're composing them. You can compose them with explicit JavaScript code as we've just done. You can also generalize composition with the B Combinator or 'compose' that we saw in Combinators and Decorators:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00578))_

<a id="atom-technical-atom-cf1a312e4314a38c"></a>
```
const cookAndEat = (food) => eat(cook(food));
```

### Technical frame 112: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00581))_

> If that was all there was to it, composition wouldn't matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00580))_

<a id="atom-technical-atom-f640f6d4abf32482"></a>
```
const compose = (a, b) => (c) => a(b(c));
const cookAndEat = compose(eat, cook);
```

### Technical frame 113: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00582))_

> In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00581))_

<a id="atom-technical-atom-6409eab3891c8c8f"></a>
> The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

### Technical frame 114: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00582))_

> In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00583))_

<a id="atom-technical-atom-46149964d44fc22f"></a>
> Of course, you needn't use combinators to implement either of these ideas, you can use if statements.

### Technical frame 115: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00583))_

> Of course, you needn't use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00584))_

<a id="atom-technical-atom-105e5de730962e24"></a>
```
const actuallyTransfer= (from, to, amount) =>
// do something
const invokeTransfer = once(maybe(actuallyTransfer(...)));
```

### Technical frame 116: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00592))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00588))_

<a id="atom-technical-atom-f87dd909796a74eb"></a>
```
_.map([1, 2, 3], (n) => n * n)
//=> [1, 4, 9]
```

### Technical frame 117: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00592))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00591))_

<a id="atom-technical-atom-f2244ab0161c959e"></a>
```
const squareAll = (array) => map(array,
(n) => n * n);
```

### Technical frame 118: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00594))_

> We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00593))_

<a id="atom-technical-atom-a85967f9315d6b06"></a>
```
const mapWith = (fn) =>
(array) => map(array, fn);
const squareAll = mapWith((n) => n * n);
squareAll([1, 2, 3])
//=> [1, 4, 9]
```

### Technical frame 119: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00598))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00595))_

<a id="atom-technical-atom-d3f59d0607285f04"></a>
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

### Technical frame 120: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00598))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00596))_

<a id="atom-technical-atom-4d2674ca1763ddca"></a>
```
const safeSquareAll = mapWith(maybe((n) => n * n));
```

### Technical frame 121: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00598))_

> Wegeneralized composition with the compose combinator. Partial application also has a combinator, which we'll see in the partial recipe.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00597))_

<a id="atom-technical-atom-8abe24c81a2a8b98"></a>
```
safeSquareAll([1, null, 2, 3])
//=> [1, null, 4, 9]
```

### Technical frame 122: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00607))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00604))_

<a id="atom-technical-atom-d9d2432be6039e9c"></a>
```
const plus = function (a, b) {
return arguments[0] + arguments[1];
}
plus(2,3)
//=> 5
```

### Technical frame 123: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00607))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00606))_

<a id="atom-technical-atom-4460849cb173a0af"></a>
```
const args = function (a, b) {
return arguments;
}
args(2,3)
//=> { '0': 2, '1': 3 }
```

### Technical frame 124: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00612))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00608))_

<a id="atom-technical-atom-0cef432672ec2709"></a>
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

### Technical frame 125: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00612))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00609))_

<a id="atom-technical-atom-d291d8101b5b3742"></a>
```
const plus = function () {
return arguments[0] + arguments[1];
}
plus(2,3)
//=> 5
```

### Technical frame 126: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00612))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00611))_

<a id="atom-technical-atom-8e5c3dd900fd3230"></a>
```
const howMany = function () {
return arguments['length'];
}
howMany()
//=> 0
howMany('hello')
//=> 1
howMany('sharks', 'are', 'apex', 'predators')
//=> 4
```

### Technical frame 127: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00617))_

> But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function . And thus arguments[0] will refer to "outer" , not to "inner" :

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00616))_

<a id="atom-technical-atom-f767fed3ff61a679"></a>
```
(function () {
return (function () { return arguments[0]; })('inner');
})('outer')
//=> "inner"
```

### Technical frame 128: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00619))_

> Although it seems quixotic for the two syntaxes to have different semantics, it makes sense when you consider the design goal: Fat arrow functions are designed to be very lightweight and are often used with constructs like mapping or callbacks to emulate syntax.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00618))_

<a id="atom-technical-atom-36489576d7b26541"></a>
```
(function () {
return (() => arguments[0])('inner');
})('outer')
//=> "outer"
```

### Technical frame 129: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00622))_

> This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind arguments when it's invoked. But if we rewrite row to use the function keyword, it stops working:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00621))_

<a id="atom-technical-atom-bb9b8c1dc457608e"></a>
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

### Technical frame 130: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00626))_

> Although this example is clearly unrealistic, there is a general design principle that deserves attention. Sometimes, a function is meant to be used as a Big-F function. It has a name, it is called by different pieces of code, it's a first-class entity in the code.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00624))_

<a id="atom-technical-atom-8f017765a9af7337"></a>
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

### Technical frame 131: And also: / Summary

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00630))_

<a id="atom-technical-atom-31d2866301c01909"></a>
> [Figure] (p.78)
