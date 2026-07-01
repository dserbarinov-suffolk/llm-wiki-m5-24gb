---
page_id: javascriptallonge-section-picking-the-bean-choice-and-truthiness-851a6e13
page_kind: source
summary: Picking the Bean: Choice and Truthiness: 48 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-picking-the-bean-choice-and-truthiness-851a6e13@f8eaffeca972b186b7306e9fc6704032
---

# Picking the Bean: Choice and Truthiness

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-the-ternary-operator-9ad8528f]] - narrower source section: Picking the Bean: Choice and Truthiness / truthiness and the ternary operator
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-operators-e7aa9191]] - narrower source section: Picking the Bean: Choice and Truthiness / truthiness and operators
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-and-are-control-flow-operators-e907a1ef]] - narrower source section: Picking the Bean: Choice and Truthiness / || and && are control-flow operators
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-function-parameters-are-eager-fbbf2d6a]] - narrower source section: Picking the Bean: Choice and Truthiness / function parameters are eager
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-summary-cb659264]] - narrower source section: Picking the Bean: Choice and Truthiness / summary
- [[javascriptallonge-section-recipes-with-basic-functions-58df4c63]] - previous source section: Recipes with Basic Functions
- [[javascriptallonge-section-composing-and-decomposing-data-58c1e32b]] - next source section: Composing and Decomposing Data

## Statements

- We've seen operators that act on numeric values, like + and % . In addition to numbers, we often need to represent a much more basic idea of truth or falsehood. Is this array empty? Does this person have a middle name? Is this user logged in? _(javascriptallonge.pdf (source-range-0e12e052-00748))_
- true and false are value types. All values of true are === all other values of true. We can see that is the case by looking at some operators we can perform on boolean values, ! , && , and || . To being with, ! is a unary prefix operator that negates its argument. So: _(javascriptallonge.pdf (source-range-0e12e052-00754))_
- Now, note well: We have said what happens if you pass boolean values to ! , && , and || , but we've said nothing about expressions or about passing other values. We'll look at those presently. _(javascriptallonge.pdf (source-range-0e12e052-00758))_

## Statements by subsection

### Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

- In JavaScript, there is a notion of 'truthiness.' Every value is either 'truthy' or 'falsy.' Obviously, false is falsy. So are null and undefined , values that semantically represent 'no value.' NaN is falsy, a value representing the result of a calculation that is not a number. 54 And there are more: 0 is falsy, a value representing 'none of something.' The empty string, '' is falsy, a value representing having no characters. _(javascriptallonge.pdf (source-range-0e12e052-00760))_
- Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' . (Many other languages that have a notion of truthiness consider zero and the empty string to be truthy, not falsy, so beware of blindly transliterating code from one language to another!) _(javascriptallonge.pdf (source-range-0e12e052-00761))_
- The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on truthiness , not on boolean values. This affects the way the ! , && , and || operators work. We'll look at them in a moment, but first, we'll look at one more operator. _(javascriptallonge.pdf (source-range-0e12e052-00762))_
- JavaScript inherited an operator from the C family of languages, the ternary operator. It's the only operator that takes three arguments. It looks like this: first ? second : third . It evaluates first , and if first is 'truthy', it evaluates second and that is its value. If first is not truthy, it evaluates third and that is its value. _(javascriptallonge.pdf (source-range-0e12e052-00763))_
- This is a lot like the if statement, however it is an expression , not a statement, and that can be very valuable. It also doesn't introduce braces, and that can be a help or a hindrance if we want to introduce a new scope or use statements. _(javascriptallonge.pdf (source-range-0e12e052-00765))_
- Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true . _(javascriptallonge.pdf (source-range-0e12e052-00769))_
- Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' . _(javascriptallonge.pdf (source-range-0e12e052-00761))_
- It's the only operator that takes three arguments. _(javascriptallonge.pdf (source-range-0e12e052-00763))_
- Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true . _(javascriptallonge.pdf (source-range-0e12e052-00769))_

### Picking the Bean: Choice and Truthiness / truthiness and operators

- Our logical operators ! , && , and || are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-0e12e052-00771))_
- Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user. _(javascriptallonge.pdf (source-range-0e12e052-00773))_
- First, and unlike ! , && and || do not necessarily evaluate to true or false . To be precise: _(javascriptallonge.pdf (source-range-0e12e052-00775))_
- If we look at our examples above, we see that when we pass true and false to && and || , we do indeed get true or false as a result. But when we pass other values, we no longer get true or false : _(javascriptallonge.pdf (source-range-0e12e052-00782))_
- In JavaScript, && and || aren't boolean logical operators in the logical sense. They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && . _(javascriptallonge.pdf (source-range-0e12e052-00784))_
- This is not a subtle distinction. _(javascriptallonge.pdf (source-range-0e12e052-00785))_
- So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user. _(javascriptallonge.pdf (source-range-0e12e052-00773))_

### Picking the Bean: Choice and Truthiness / || and && are control-flow operators

- We've seen the ternary operator: It is a control-flow operator, not a logical operator. The same is true of && and || . Consider this tail-recursive function that determines whether a positive integer is even: _(javascriptallonge.pdf (source-range-0e12e052-00787))_
- This is more than just an optimization. It's best to think of || and && as control-flow operators. The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. _(javascriptallonge.pdf (source-range-0e12e052-00793))_

### Picking the Bean: Choice and Truthiness / function parameters are eager

- If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don't need anything like this for or and and , but to demonstrate the technique: _(javascriptallonge.pdf (source-range-0e12e052-00798))_
- Here we've passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation. _(javascriptallonge.pdf (source-range-0e12e052-00800))_
- This leads to the infinite recursion we fear. _(javascriptallonge.pdf (source-range-0e12e052-00797))_

### Picking the Bean: Choice and Truthiness / summary

- Logical operators are based on truthiness and falsiness, not the strict values true and false . _(javascriptallonge.pdf (source-range-0e12e052-00802))_
- The ternary operator ( ?: ), || , and && are control flow operators, they do not always return true or false , and they have short-cut semantics. _(javascriptallonge.pdf (source-range-0e12e052-00804))_
- Function invocation uses eager evaluation, so if we need to roll our own control-flow semantics, we pass it functions, not expressions. _(javascriptallonge.pdf (source-range-0e12e052-00805))_

## Technical atoms

### Technical frame 1: Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00763))_

> JavaScript inherited an operator from the C family of languages, the ternary operator. It's the only operator that takes three arguments. It looks like this: first ? second : third . It evaluates first , and if first is 'truthy', it evaluates second and that is its value. If first is not truthy, it evaluates third and that is its value.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00768))_

```text
//=> 'Hello'
0 ? 'Hello' : 'Good bye'
//=> 'Good bye'
[1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal'
//=> 'Pentatonic'
The fact that either the second or the third (but not both) expressions are evaluated can have
important repercussions. Consider this hypothetical example:
const status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\
den';
We certainly don’t want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAutho-
rized(currentUser) returns true.
truthiness and operators
Our logical operators !, &&, and || are a little more subtle than our examples above implied. ! is the
simplest. It always returns false if its argument is truthy, and true is its argument is not truthy:
!5
//=> false
!undefined
//=> true
Programmers often take advantage of this behaviour to observe that !!(someExpression) will
always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript
(and other languages with similar semantics), when you see something like !!currentUser(), this
Picking the Bean: Choice and Truthiness
74
is an idiom that means “true if currentUser is truthy.” Thus, a function like currentUser() is free to
return null, or undefined, or false if there is no current user.
Thus, !! is the way we write “is truthy” in JavaScript. How about && and ||? What haven’t we
discussed?
First, and unlike !, && and || do not necessarily evaluate to true or false. To be precise:
• && evaluates its left-hand expression.
– If its left-hand expression evaluates to something falsy, && returns the value of its left-
hand expression without evaluating its right-hand expression.
– If its left-hand expression evaluates to something truthy, && evaluates its right-hand
expression and returns the value of the right-hand expression.
• || evaluates its left-hand expression.
– If its left-hand expression evaluates to something truthy, || returns the value of its left-
hand expression without evaluating its right-hand expression.
– If its left-hand expression evaluates to something false, || evaluates its right-hand
expression and returns the value of the right-hand expression.
If we look at our examples above, we see that when we pass true and false to && and ||, we do
indeed get true or false as a result. But when we pass other values, we no longer get true or false:
1 || 2
//=> 1
null && undefined
//=> null
undefined && null
//=> undefined
In JavaScript, && and || aren’t boolean logical operators in the logical sense. They don’t operate
strictly on logical values, and they don’t commute: a || b is not always equal to b || a, and the
same goes for &&.
This is not a subtle distinction.
|| and && are control-flow operators
We’ve seen the ternary operator: It is a control-flow operator, not a logical operator. The same is
true of && and ||. Consider this tail-recursive function that determines whether a positive integer
is even:
For example:
Picking the Bean: Choice and Truthiness
75
const even = (n) =>
n === 0 || (n !== 1 && even(n - 2))
even(42)
//=> true
If n === 0, JavaScript does not evaluate (n !== 1 && even(n - 2)). This is very important!
Imagine that JavaScript evaluated both sides of the || operator before determining its value. n ===
0 would be true. What about (n !== 1 && even(n - 2))? Well, it would evaluate even(n - 2), or
even(-2)
This leads us to evaluate n === 0 || (n !== 1 && even(n - 2)) all over again, and this time we
end up evaluating even(-4). And then even(-6). and so on and so forth until JavaScript throws up
its hands and runs out of stack space.
But that’s not what happens. || and && have short-cut semantics. In this case, if n === 0, JavaScript
does not evaluate (n !== 1 && even(n - 2)). Likewise, if n === 1, JavaScript evaluates n !== 1
&& even(n - 2) as false without ever evaluating even(n - 2).
This is more than just an optimization. It’s best to think of || and && as control-flow operators. The
expression on the left is always evaluated, and its value determines whether the expression on the
right is evaluated or not.
function parameters are eager
In contrast to the behaviour of the ternary operator, ||, and &&, function parameters are always
eagerly evaluated:
const or = (a, b) => a || b
const and = (a, b) => a && b
const even = (n) =>
or(n === 0, and(n !== 1, even(n - 2)))
even(42)
//=> Maximum call stack size exceeded.
Now our expression or(n === 0, and(n !== 1, even(n - 2))) is calling functions, and JavaScript
always evaluates the expressions for parameters before passing the values to a function to invoke.
This leads to the infinite recursion we fear.
If we need to have functions with control-flow semantics, we can pass anonymous functions. We
obviously don’t need anything like this for or and and, but to demonstrate the technique:
Picking the Bean: Choice and Truthiness
76
const or = (a, b) => a() || b()
const and = (a, b) => a() && b()
const even = (n) =>
or(() => n === 0, () => and(() => n !== 1, () => even(n - 2)))
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 74 | is an idiom that means “true if currentUser is truthy.” Thus, a function like currentUser() is free to return null, or undefined, or false if there is no current user. Thus,!! is the way we write “is truthy” in JavaScript. How about && and \|\|? What haven’t we discussed? First, and unlike!, && and \|\| do not necessarily evaluate to true or false. To be precise: • && evaluates its left-hand expression. – If its left-hand expression evaluates to something falsy, && returns the value of its left- hand expression without evaluating its right-hand expression. – If its left-hand expression evaluates to something truthy, && evaluates its right-hand expression and returns the value of the right-hand expression. • \|\| evaluates its left-hand expression. – If its left-hand expression evaluates to something truthy, \|\| returns the value of its left- hand expression without evaluating its right-hand expression. – If its left-hand expression evaluates to something false, \|\| evaluates its right-hand expression and returns the value of the right-hand expression. If we look at our examples above, we see that when we pass true and false to && and \|\|, we do indeed get true or false as a result. But when we pass other values, we no longer get true or false: |
| 1 | \|\| 2 //=> 1 null && undefined //=> null undefined && null //=> undefined In JavaScript, && and \|\| aren’t boolean logical operators in the logical sense. They don’t operate strictly on logical values, and they don’t commute: a \|\| b is not always equal to b \|\| a, and the same goes for &&. This is not a subtle distinction. \|\| and && are control-flow operators We’ve seen the ternary operator: It is a control-flow operator, not a logical operator. The same is true of && and \|\|. Consider this tail-recursive function that determines whether a positive integer is even: |
| 75 | For example: Picking the Bean: Choice and Truthiness const even = (n) => n === 0 \|\| (n!== 1 && even(n - 2)) even(42) //=> true If n === 0, JavaScript does not evaluate (n!== 1 && even(n - 2)). This is very important! Imagine that JavaScript evaluated both sides of the \|\| operator before determining its value. n === |
| 0 | would be true. What about (n!== 1 && even(n - 2))? Well, it would evaluate even(n - 2), or even(-2) This leads us to evaluate n === 0 \|\| (n!== 1 && even(n - 2)) all over again, and this time we end up evaluating even(-4). And then even(-6). and so on and so forth until JavaScript throws up its hands and runs out of stack space. But that’s not what happens. \|\| and && have short-cut semantics. In this case, if n === 0, JavaScript does not evaluate (n!== 1 && even(n - 2)). Likewise, if n === 1, JavaScript evaluates n!== 1 && even(n - 2) as false without ever evaluating even(n - 2). This is more than just an optimization. It’s best to think of \|\| and && as control-flow operators. The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. function parameters are eager In contrast to the behaviour of the ternary operator, \|\|, and &&, function parameters are always eagerly evaluated: const or = (a, b) => a \|\| b const and = (a, b) => a && b const even = (n) => or(n === 0, and(n!== 1, even(n - 2))) even(42) //=> Maximum call stack size exceeded. Now our expression or(n === 0, and(n!== 1, even(n - 2))) is calling functions, and JavaScript always evaluates the expressions for parameters before passing the values to a function to invoke. This leads to the infinite recursion we fear. If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don’t need anything like this for or and and, but to demonstrate the technique: |
| 76 | Picking the Bean: Choice and Truthiness const or = (a, b) => a() \|\| b() const and = (a, b) => a() && b() const even = (n) => or(() => n === 0, () => and(() => n!== 1, () => even(n - 2))) |

</details>
