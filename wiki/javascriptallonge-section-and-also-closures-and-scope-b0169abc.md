---
page_id: javascriptallonge-section-and-also-closures-and-scope-b0169abc
page_kind: source
summary: And also: / Closures and Scope: 74 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-closures-and-scope-b0169abc@d418567f8823a1146240c39ac50540ba
---

# And also: / Closures and Scope

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-and-also-call-by-sharing-483b119d]] - previous source section: And also: / call by sharing
- [[javascriptallonge-section-and-also-that-constant-coffee-craving-149774f4]] - next source section: And also: / That Constant Coffee Craving

### Source structure

- [[javascriptallonge-section-and-also-5c5088c6]] - broader source section: And also:
- [[javascriptallonge-section-and-also-closures-and-scope-if-functions-without-free-variables-are-pure-are-closures-impure-7b2f0444]] - narrower source section: And also: / Closures and Scope / if functions without free variables are pure, are closures impure?
- [[javascriptallonge-section-and-also-closures-and-scope-it-s-always-the-environment-3f11c3df]] - narrower source section: And also: / Closures and Scope / it's always the environment
- [[javascriptallonge-section-and-also-closures-and-scope-shadowy-variables-from-a-shadowy-planet-7ccc05d7]] - narrower source section: And also: / Closures and Scope / shadowy variables from a shadowy planet
- [[javascriptallonge-section-and-also-closures-and-scope-which-came-first-the-chicken-or-the-egg-85167dcf]] - narrower source section: And also: / Closures and Scope / which came first, the chicken or the egg?

## Statements

- The environment belonging to the function with signature (x) => ... becomes {x: 1, ...} , and the result of applying the function is another function value. It makes sense that the result value is a function, because the expression for (x) => ... 's body is: _(javascriptallonge.pdf (source-range-c98ab3e6-00329))_
- So now we have a value representing that function. Then we're going to take the value of that function and apply it to the argument 2 , something like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00331))_
- So we seem to get a new environment {y: 2, ...} . How is the expression x going to be evaluated in that function's environment? There is no x in its environment, it must come from somewhere else. _(javascriptallonge.pdf (source-range-c98ab3e6-00333))_
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from 'outside' of a function that are referenced inside a function. For example, here's the equivalent code in Ruby: _(javascriptallonge.pdf (source-range-c98ab3e6-00334))_
- It makes sense that the result value is a function, because the expression for (x) => ... _(javascriptallonge.pdf (source-range-c98ab3e6-00329))_
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from 'outside' of a function that are referenced inside a function. _(javascriptallonge.pdf (source-range-c98ab3e6-00334))_

## Statements by subsection

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
