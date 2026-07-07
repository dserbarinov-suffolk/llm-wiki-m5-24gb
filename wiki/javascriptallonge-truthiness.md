---
page_id: javascriptallonge-truthiness
page_kind: concept
summary: Truthiness: 3 statement(s) and 7 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-truthiness@408df2423bccfda5dd2729736b384226
---

# Truthiness

What [[javascriptallonge]] covers about truthiness:

## Statements

### truthiness and the ternary operator

- In JavaScript, there is a notion of 'truthiness.' Every value is either 'truthy' or 'falsy.' Obviously, false is falsy. So are null and undefined , values that semantically represent 'no value.' NaN is falsy, a value representing the result of a calculation that is not a number. 54 And there are more: 0 is falsy, a value representing 'none of something.' The empty string, '' is falsy, a value representing having no characters. _(javascriptallonge.pdf (source-range-c98ab3e6-00747))_

- Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' . (Many other languages that have a notion of truthiness consider zero and the empty string to be truthy, not falsy, so beware of blindly transliterating code from one language to another!) _(javascriptallonge.pdf (source-range-c98ab3e6-00748))_

- The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on truthiness , not on boolean values. This affects the way the ! , && , and || operators work. We'll look at them in a moment, but first, we'll look at one more operator. _(javascriptallonge.pdf (source-range-c98ab3e6-00749))_


## Technical atoms

### Technical frame 1: Picking the Bean: Choice and Truthiness

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00745))_

> Now, note well: We have said what happens if you pass boolean values to ! , && , and || , but we've said nothing about expressions or about passing other values. We'll look at those presently.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00742))_

<a id="atom-technical-atom-47fabdabc176dc83"></a>
```
!true
//=> false
!false
//=> true
```

### Technical frame 2: Picking the Bean: Choice and Truthiness

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00745))_

> Now, note well: We have said what happens if you pass boolean values to ! , && , and || , but we've said nothing about expressions or about passing other values. We'll look at those presently.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00744))_

<a id="atom-technical-atom-feba25c09474dcd7"></a>
```
false && false //=> false
false && true
//=> false
true
&& false //=> false
true
&& true
//=> true
false || false //=> false
false || true
//=> true
true
|| false //=> true
true
|| true
//=> true
```

### Technical frame 3: truthiness and the ternary operator

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00756))_

> Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00754))_

<a id="atom-technical-atom-f9b7fc7f4a1c8300"></a>
```
true ? 'Hello' : 'Good bye'
//=> 'Hello'
0 ? 'Hello' : 'Good bye'
//=> 'Good bye'
[1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal'
//=> 'Pentatonic'
```

### Technical frame 4: truthiness and the ternary operator

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00750))_

> JavaScript inherited an operator from the C family of languages, the ternary operator. It's the only operator that takes three arguments. It looks like this: first ? second : third . It evaluates first , and if first is 'truthy', it evaluates second and that is its value. If first is not truthy, it evaluates third and that is its value.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00755))_

<a id="atom-technical-atom-3a87fa2a0a8bf88b"></a>
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

### Technical frame 5: truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00760))_

> Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00759))_

<a id="atom-technical-atom-cb98425a31f8e87a"></a>
```
!5
//=> false
!undefined
//=> true
```

### Technical frame 6: truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00771))_

> In JavaScript, && and || aren't boolean logical operators in the logical sense. They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00769))_

<a id="atom-technical-atom-77ca1ad65a2fc56a"></a>
> But when we pass other values, we no longer get true or false :

### Technical frame 7: truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00771))_

> In JavaScript, && and || aren't boolean logical operators in the logical sense. They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00770))_

<a id="atom-technical-atom-b51f5057f226a696"></a>
```
1 || 2
//=> 1
null && undefined
//=> null
undefined && null
//=> undefined
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-ternary-operator]] - shared technical atoms: Ternary Operator shares technical record from truthiness and the ternary operator: true ? 'Hello' : 'Good bye' //=> 'Hello' 0 ? 'Hello' : 'Good bye' //=> 'Good bye' [1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal' //=> 'Pentatonic' (2 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from truthiness and the ternary operator: In JavaScript, there is a notion of 'truthiness.' Every value is either 'truthy' or 'falsy.' Obviously, false is falsy. So are null and undefined , values that seman ... [truncated]; Javascript shares technical record from truthiness and operators: !5 //=> false !undefined //=> true (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-operator]] - shared technical atoms: Operator shares technical record from truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))

### Shared claims

- [[javascriptallonge-reason]] - shared statements: Reason shares source evidence from truthiness and the ternary operator: The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on truthiness , not on boolean values. This af ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
