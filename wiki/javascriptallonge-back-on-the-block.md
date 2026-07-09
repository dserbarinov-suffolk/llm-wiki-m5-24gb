---
page_id: javascriptallonge-back-on-the-block
page_kind: concept
summary: back on the block: 5 accepted assertion(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_a882ccdf17ba322d@e695abb7a1850d86a933879fb91cf6e1
---

# back on the block

Source: [[javascriptallonge]]

## Statements

- We haven't discussed these statements . (javascriptallonge.pdf p.36)
- Although they aren't very practical, these are valid JavaScript functions, and they return undefined when applied:. (javascriptallonge.pdf p.36)
- There are many kinds of JavaScript statements, but the first kind is one we've already met. (javascriptallonge.pdf p.36)
- As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:. (javascriptallonge.pdf p.36)
- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined :. (javascriptallonge.pdf p.36)

## Technical atoms

<a id="atom-1"></a>
**Atom:** table

```text
back on the block
Back to our function. We evaluated this:
19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This was actually the preferred mechanism until void became commonplace.
20 As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined . We have no idea.
```

<a id="atom-2"></a>
**Atom:** code block

```
(() => {})()
//=> undefined
```

<a id="atom-3"></a>
**Atom:** code block

```
() => { 2 + 2 }
() => { 1 + 1; 2 + 2 }
```

<a id="atom-4"></a>
**Atom:** code block

```
() => {
1 + 1;
2 + 2
}
```

<a id="atom-5"></a>
**Atom:** table

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
