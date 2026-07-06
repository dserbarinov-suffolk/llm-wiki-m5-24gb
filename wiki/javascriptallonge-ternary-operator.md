---
page_id: javascriptallonge-ternary-operator
page_kind: concept
summary: Ternary Operator: 1 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-ternary-operator@7ce69aa88169df2709be57c61b94eaa4
---

# Ternary Operator

What [[javascriptallonge]] covers about ternary operator:

## Statements

### Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

- JavaScript inherited an operator from the C family of languages, the ternary operator. It's the only operator that takes three arguments. It looks like this: first ? second : third . It evaluates first , and if first is 'truthy', it evaluates second and that is its value. If first is not truthy, it evaluates third and that is its value. _(javascriptallonge.pdf (source-range-c98ab3e6-00763))_


## Technical atoms

### Technical frame 1: Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00769))_

> Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00767))_

<a id="atom-technical-atom-850cbf42a14e0910"></a>
```
true ? 'Hello' : 'Good bye'
//=> 'Hello'
0 ? 'Hello' : 'Good bye'
//=> 'Good bye'
[1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal'
//=> 'Pentatonic'
```

### Technical frame 2: Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00763))_

> JavaScript inherited an operator from the C family of languages, the ternary operator. It's the only operator that takes three arguments. It looks like this: first ? second : third . It evaluates first , and if first is 'truthy', it evaluates second and that is its value. If first is not truthy, it evaluates third and that is its value.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00768))_

<a id="atom-technical-atom-9f2f063732907792"></a>
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


## Related pages

### Shared technical atoms

- [[javascriptallonge-truthiness]] - shared technical atoms: Truthiness shares technical record from Picking the Bean: Choice and Truthiness / truthiness and the ternary operator: true ? 'Hello' : 'Good bye' //=> 'Hello' 0 ? 'Hello' : 'Good bye' //=> 'Good bye' [1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal' //=> 'Pentatonic' (2 shared atom(s))

### Shared claims

- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from Picking the Bean: Choice and Truthiness / truthiness and the ternary operator: JavaScript inherited an operator from the C family of languages, the ternary operator. It's the only operator that takes three arguments. It looks like this: first ? ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
