---
page_id: javascriptallonge-look-back-at-functional-iterators
page_kind: concept
summary: a look back at functional iterators: 4 accepted assertion(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_66626f425176d876@06c29fa42124efc0fdae927ef1191316
---

# a look back at functional iterators

Source: [[javascriptallonge]]

## Statements

- We can do the same thing for objects. (javascriptallonge.pdf p.206)
- We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:. (javascriptallonge.pdf p.209)
- If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. (javascriptallonge.pdf p.209)
- Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. (javascriptallonge.pdf p.209)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const Stack1 = () =>
({
array:[],
index: -1,
push (value) {
return this.array[this.index += 1] = value;
},
pop () {
const value = this.array[this.index];
this.array[this.index] = undefined;
if (this.index >= 0) {
this.index -= 1
}
return value
},
isEmpty () {
return this.index < 0
},
iterator () {
let iterationIndex = this.index;
return () => {
if (iterationIndex > this.index) {
iterationIndex = this.index;
}
if (iterationIndex < 0) {
return {done: true};
}
else {
return {done: false, value: this.array[iterationIndex--]}
}
}
}
});
const stack = Stack1();
stack.push("Greetings");
stack.push("to");
stack.push("you!")
```

<a id="atom-2"></a>
**Atom:** code block

```
const iter = stack.iterator();
iter().value
//=> "you!"
iter().value
//=> "to"
```

<a id="atom-3"></a>
**Atom:** code block

```
The .iterator() method is defined with shorthand equivalent to iterator: function iterator()
{ ... }. Note that it uses the function keyword, so when we invoke it with stack.iterator(),
JavaScript sets this to the value of stack. But what about the function .iterator() returns? It is
defined with a fat arrow () => { ... }. What is the value of this within that function?
Since JavaScript doesn’t bind this within a fat arrow function, we follow the same rules of variable
scoping as any other variable name: We check in the environment enclosing the function. Although
the .iterator() method has returned, its environment is the one that encloses our () => { ...
} function, and that’s where this is bound to the value of stack.
Therefore, the iterator function returned by the .iterator() method has this bound to the stack
object, even though we call it with iter().
```

<a id="atom-4"></a>
**Atom:** code block

```
const iteratorSum = (iterator) => {
let eachIteration,
sum = 0;
while ((eachIteration = iterator(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
```

<a id="atom-5"></a>
**Atom:** code block

```
const stack = Stack1();
stack.push(1);
stack.push(2);
stack.push(3);
iteratorSum(stack.iterator())
//=> 6
```

<a id="atom-6"></a>
**Atom:** code block

```
const collectionSum = (collection) => {
const iterator = collection.iterator();
let eachIteration,
sum = 0;
while ((eachIteration = iterator(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
collectionSum(stack)
//=> 6
```
