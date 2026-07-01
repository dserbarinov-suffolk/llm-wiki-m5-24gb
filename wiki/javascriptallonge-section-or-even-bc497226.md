---
page_id: javascriptallonge-section-or-even-bc497226
page_kind: source
summary: Or even:: 33 source-backed entries and 12 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-or-even-bc497226@163bd1c2b0a9be7ffbeaffca802265e6
---

# Or even:

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-or-even-the-simplest-possible-block-fbb6a26c]] - narrower source section: Or even: / the simplest possible block
- [[javascriptallonge-section-or-even-void-fe958725]] - narrower source section: Or even: / void
- [[javascriptallonge-section-or-even-back-on-the-block-b65a6ef3]] - narrower source section: Or even: / back on the block
- [[javascriptallonge-section-the-first-sip-basic-functions-e66ec551]] - previous source section: The first sip: Basic Functions
- [[javascriptallonge-section-and-also-0e29dfba]] - next source section: And also:

## Statements by subsection

### Or even: / the simplest possible block

- There's another thing we can put to the right of an arrow, a block . A block has zero or more statements , separated by semicolons. 18 _(javascriptallonge.pdf (source-range-0e12e052-00212))_
- It returns the result of evaluating a block that has no statements. What would that be? Let's try it: _(javascriptallonge.pdf (source-range-0e12e052-00215))_

### Or even: / the simplest possible block / undefined

- In JavaScript, the absence of a value is written undefined , and it means there is no value. It will crop up again. undefined is its own type of value, and it acts like a value type: _(javascriptallonge.pdf (source-range-0e12e052-00219))_
- Like numbers, booleans and strings, JavaScript can print out the value undefined . _(javascriptallonge.pdf (source-range-0e12e052-00222))_
- No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-) _(javascriptallonge.pdf (source-range-0e12e052-00224))_
- 18 Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons. This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. We will not take advantage of this feature, but it's helpful to know it exists. _(javascriptallonge.pdf (source-range-0e12e052-00225))_
- You might think that undefined in JavaScript is equivalent to NULL in SQL. No. In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can't be equal. In JavaScript, every undefined is identical to every other undefined . _(javascriptallonge.pdf (source-range-0e12e052-00226))_
- In JavaScript, the absence of a value is written undefined , and it means there is no value. _(javascriptallonge.pdf (source-range-0e12e052-00219))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-0e12e052-00225))_
- In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can't be equal. _(javascriptallonge.pdf (source-range-0e12e052-00226))_

### Or even: / void

- void is an operator that takes any value and evaluates to undefined , always. So, when we deliberately want an undefined value, should we use the first, second, or third form? 19 The answer is, use void . By convention, use void 0 . _(javascriptallonge.pdf (source-range-0e12e052-00233))_
- The first form works but it's cumbersome. The second form works most of the time, but it is possible to break it by reassigning undefined to a different value, something we'll discuss in Reassignment and Mutation. The third form is guaranteed to always work, so that's what we will use. 20 _(javascriptallonge.pdf (source-range-0e12e052-00234))_

### Or even: / back on the block

- We haven't discussed these statements . What's a statement? _(javascriptallonge.pdf (source-range-0e12e052-00240))_
- There are many kinds of JavaScript statements, but the first kind is one we've already met. An expression is a JavaScript statement. Although they aren't very practical, these are valid JavaScript functions, and they return undefined when applied: _(javascriptallonge.pdf (source-range-0e12e052-00241))_
- As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way: _(javascriptallonge.pdf (source-range-0e12e052-00243))_
- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined : _(javascriptallonge.pdf (source-range-0e12e052-00245))_

## Technical atoms

### Technical frame 1: Or even:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00210))_

```
() => (
1 + 1,
2 + 2
)
```

### Technical frame 2: Or even: / the simplest possible block

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00215))_

> It returns the result of evaluating a block that has no statements. What would that be? Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00214))_

```
() => {}
```

### Technical frame 3: Or even: / the simplest possible block

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00215))_

> It returns the result of evaluating a block that has no statements. What would that be? Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00216))_

```
(() => {})()
//=> undefined
```

### Technical frame 4: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00222))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00220))_

```
undefined
```

### Technical frame 5: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00222))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00221))_

```
//=> undefined
```

### Technical frame 6: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00224))_

> No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-)

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00223))_

```
undefined === undefined
//=> true
(() => {})() === (() => {})()
//=> true
(() => {})() === undefined
//=> true
```

### Technical frame 7: Or even: / void

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00233))_

> void is an operator that takes any value and evaluates to undefined , always. So, when we deliberately want an undefined value, should we use the first, second, or third form? 19 The answer is, use void . By convention, use void 0 .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00232))_

```
void 0
//=> undefined
void 1
//=> undefined
void (2 + 2)
//=> undefined
```

### Technical frame 8: Or even: / back on the block

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

### Technical frame 9: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00240))_

> We haven't discussed these statements . What's a statement?

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00237))_

```
(() => {})()
//=> undefined
```

### Technical frame 10: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00243))_

> As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00242))_

```
() => { 2 + 2 }
() => { 1 + 1; 2 + 2 }
```

### Technical frame 11: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00245))_

> But no matter how we arrange them, a block with one or more expressions still evaluates to undefined :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00244))_

```
() => {
1 + 1;
2 + 2
}
```

### Technical frame 12: Or even: / back on the block

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
