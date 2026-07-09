---
page_id: javascriptallonge-truthiness
page_kind: concept
summary: Truthiness: 4 statement(s) and 9 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-truthiness@0e851df96fe07fe5657f778eed867092
---

# Truthiness

What [[javascriptallonge]] covers about truthiness:

## Statements

### Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

- In JavaScript, there is a notion of 'truthiness.' Every value is either 'truthy' or 'falsy.' Obviously, false is falsy. So are null and undefined , values that semantically represent 'no value.' NaN is falsy, a value representing the result of a calculation that is not a number. 54 And there are more: 0 is falsy, a value representing 'none of something.' The empty string, '' is falsy, a value representing having no characters. _(javascriptallonge.pdf (source-range-c98ab3e6-00747))_

- Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' . (Many other languages that have a notion of truthiness consider zero and the empty string to be truthy, not falsy, so beware of blindly transliterating code from one language to another!) _(javascriptallonge.pdf (source-range-c98ab3e6-00748))_

- The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on truthiness , not on boolean values. This affects the way the ! , && , and || operators work. We'll look at them in a moment, but first, we'll look at one more operator. _(javascriptallonge.pdf (source-range-c98ab3e6-00749))_

### Picking the Bean: Choice and Truthiness / summary

- Logical operators are based on truthiness and falsiness, not the strict values true and false . _(javascriptallonge.pdf (source-range-c98ab3e6-00789))_


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

### Technical frame 3: Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

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

### Technical frame 4: Picking the Bean: Choice and Truthiness / truthiness and operators

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

### Technical frame 5: Picking the Bean: Choice and Truthiness / truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00771))_

> In JavaScript, && and || aren't boolean logical operators in the logical sense. They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00769))_

<a id="atom-technical-atom-77ca1ad65a2fc56a"></a>
> But when we pass other values, we no longer get true or false :

### Technical frame 6: Picking the Bean: Choice and Truthiness / truthiness and operators

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

### Technical frame 7: Picking the Bean: Choice and Truthiness / truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00780))_

> This is more than just an optimization. It's best to think of || and && as control-flow operators. The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00776))_

<a id="atom-technical-atom-b9e8ea4f1abe6f81"></a>
```
const even = (n) =>
n === 0 || (n !== 1 && even(n - 2))
even(42)
//=> true
```

### Technical frame 8: Picking the Bean: Choice and Truthiness / function parameters are eager

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00785))_

> If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don't need anything like this for or and and , but to demonstrate the technique:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00783))_

<a id="atom-technical-atom-d46d0adcfad1d7bc"></a>
```
const or = (a, b) => a || b
const and = (a, b) => a && b
const even = (n) =>
or(n === 0, and(n !== 1, even(n - 2)))
even(42)
//=> Maximum call stack size exceeded.
```

### Technical frame 9: Picking the Bean: Choice and Truthiness / function parameters are eager

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00787))_

> Here we've passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00786))_

<a id="atom-technical-atom-598249ac5d84dd27"></a>
```
const or = (a, b) => a() || b()
const and = (a, b) => a() && b()
const even = (n) =>
or(() => n === 0, () => and(() => n !== 1, () => even(n - 2)))
even(7)
//=> false
```


## Related pages

### Source structure

- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-d2a76f30]] - source section: Picking the Bean: Choice and Truthiness
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-function-parameters-are-eager-699c4c1b]] - source section: Picking the Bean: Choice and Truthiness / function parameters are eager
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-operators-44549e80]] - source section: Picking the Bean: Choice and Truthiness / truthiness and operators
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-the-ternary-operator-b715a907]] - source section: Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

### Shared technical atoms

- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Picking the Bean: Choice and Truthiness / truthiness and the ternary operator: In JavaScript, there is a notion of 'truthiness.' Every value is either 'truthy' or 'falsy.' Obviously, false is falsy. So are null and undefined , values that seman ... [truncated]; Javascript shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-operator]] - shared technical atoms: Operator shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-ternary-operator]] - shared technical atoms: Ternary Operator shares technical record from Picking the Bean: Choice and Truthiness / truthiness and the ternary operator: true ? 'Hello' : 'Good bye' //=> 'Hello' 0 ? 'Hello' : 'Good bye' //=> 'Good bye' [1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal' //=> 'Pentatonic' (1 shared atom(s))

### Shared claims

- [[javascriptallonge-reason]] - shared statements: Reason shares source evidence from Picking the Bean: Choice and Truthiness / truthiness and the ternary operator: The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on truthiness , not on boolean values. This af ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
