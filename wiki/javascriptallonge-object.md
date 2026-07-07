---
page_id: javascriptallonge-object
page_kind: concept
summary: Object: 19 statement(s) and 28 atom(s) from raw/javascriptallonge.pdf.
page_family: broad-topic
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-object@fb175edecaac9f97b10f178b7b8eba9e
---

# Object

What [[javascriptallonge]] covers about object:

## Statements

### Plain Old JavaScript Objects

- In JavaScript, an object is a map from string keys to values. _(javascriptallonge.pdf (source-range-c98ab3e6-01049))_

### Plain Old JavaScript Objects / literal object syntax

- Two objects created with separate evaluations have differing identities, just like arrays: _(javascriptallonge.pdf (source-range-c98ab3e6-01054))_

### Mutation

- In JavaScript, almost every type of value can mutate . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using [] . You can reassign a value using [] = : _(javascriptallonge.pdf (source-range-c98ab3e6-01099))_

- JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects. Mutating existing objects has special implications when two bindings are aliases of the same value. _(javascriptallonge.pdf (source-range-c98ab3e6-01115))_

### Served by the Pot: Collections / Iteration and Iterables

- Many objects in JavaScript can model collections of things. A collection is like a box containing stuff. Sometimes you just want to move the box around. But sometimes you want to open it up and do things with its contents. _(javascriptallonge.pdf (source-range-c98ab3e6-01498))_

### Served by the Pot: Collections / Iteration and Iterables / iterator objects

- Iteration for functions and objects has been around for many, many decades. For simple linear collections like arrays, linked lists, stacks, and queues, functional iterators are the simplest and easiest way to implement iterators. _(javascriptallonge.pdf (source-range-c98ab3e6-01516))_

- In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-c98ab3e6-01517))_

- Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object with a .next() method. _(javascriptallonge.pdf (source-range-c98ab3e6-01518))_

### Served by the Pot: Collections / Iteration and Iterables / iterator objects / Like this:

- Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object's scaffolding. _(javascriptallonge.pdf (source-range-c98ab3e6-01522))_

### Served by the Pot: Collections / Iteration and Iterables / iterables

- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-c98ab3e6-01527))_

- The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable: _(javascriptallonge.pdf (source-range-c98ab3e6-01532))_

### Served by the Pot: Collections / Generating Iterables

- Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done. _(javascriptallonge.pdf (source-range-c98ab3e6-01595))_

### Served by the Pot: Collections / Generating Iterables / generators and iterables

- Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call. _(javascriptallonge.pdf (source-range-c98ab3e6-01678))_

- This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-c98ab3e6-01684))_

### Served by the Pot: Collections / Summary

- A generator is a function that is defined with function * and uses yield (or yield * ) to generate values. Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns. And we don't need to worry about wrapping our values in an object with .done and .value properties. _(javascriptallonge.pdf (source-range-c98ab3e6-01729))_

### Lazy and Eager Collections

- in the older style of object-oriented programming, we built 'fat' objects. Each collection knew how to map itself ( .map ), how to fold itself ( .reduce ), how to filter itself ( .filter ) and how to find one element within itself ( .find ). If we wanted to flatten collections to arrays, we wrote a .toArray method for each type of collection. _(javascriptallonge.pdf (source-range-c98ab3e6-01734))_

- This 'fat object' style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don't need for the collection to handle every single detail. That would be like saying that when we ask a bank teller for some cash, they personally print every bank note. _(javascriptallonge.pdf (source-range-c98ab3e6-01737))_

### Lazy and Eager Collections / implementing methods with iteration

- Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. And they should know how to accomplish the desired result, but they should do so by delegating as much of the work as possible to operations like mapWith . _(javascriptallonge.pdf (source-range-c98ab3e6-01739))_

### Lazy and Eager Collections / lazy collection operations

- Whereas the .map and .filter methods on Pair work with iterators. They produce small iterable objects that refer back to the original iteration. This reduces the memory footprint. When working with very large collections and many operations, this can be important. _(javascriptallonge.pdf (source-range-c98ab3e6-01758))_


## Technical atoms

### Technical frame 1: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00602))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00598))_

<a id="atom-technical-atom-5bb18c52a0c78571"></a>
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

### Technical frame 2: Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01054))_

> Two objects created with separate evaluations have differing identities, just like arrays:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01053))_

<a id="atom-technical-atom-86ff9c88f6398559"></a>
```
{ year: 2012, month: 6, day: 14 }
```

### Technical frame 3: Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01056))_

> Values contained within an object work just like values contained within an array, we access them by reference to the original:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01055))_

<a id="atom-technical-atom-658448541f1bab12"></a>
```
{ year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 }
//=> false
Objects use [] to access the values by name, using a string:
{ year: 2012, month: 6, day: 14 }['day']
//=> 14
```

### Technical frame 4: Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01058))_

> Names needn't be alphanumeric strings. For anything else, enclose the label in quotes:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01057))_

<a id="atom-technical-atom-a85edef3979aa27f"></a>
```
const unique = () => [],
x = unique(),
y = unique(),
z = unique(),
o = { a: x, b: y, c: z };
o['a'] === x && o['b'] === y && o['c'] === z
//=> true
```

### Technical frame 5: Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01072))_

> (There are some other technical differences between binding a named function expression and using compact method syntax, but they are not relevant here. We will generally prefer compact method syntax whenever we can.)

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01071))_

<a id="atom-technical-atom-5fc0450b87f8fabc"></a>
```
const SecretDecoderRing = {
encode (plaintext) {
return plaintext
.split('')
.map( char => char.charCodeAt() )
.map( code => code + 1 )
.map( code => String.fromCharCode(code) )
.join('');
},
decode (cyphertext) {
return cyphertext
.split('')
.map( char => char.charCodeAt() )
.map( code => code - 1 )
.map( code => String.fromCharCode(code) )
.join('');
}
}
```

### Technical frame 6: Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01079))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01075))_

<a id="atom-technical-atom-7e6f1f63a68d677c"></a>
```
const user = {
name: { first: "Reginald",
last: "Braithwaite"
},
occupation: { title: "Author",
responsibilities: [ "JavaScript Allongé",
"JavaScript Spessore",
"CoffeeScript Ristretto"
]
}
};
user.name.last
//=> "Braithwaite"
user.occupation.title
//=> "Author"
And we can also write:
const {name: { first: given, last: surname}, occupation: { title: title }
er;
surname
//=> "Braithwaite"
title
//=> "Author"
```

### Technical frame 7: Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01079))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01080))_

<a id="atom-technical-atom-154953666ca27427"></a>
```
const description = ({name: { first }, occupation: { title } }) =>
`${first} is a ${title}`;
description(user)
//=> "Reginald is a Author"
And that same syntax works for literals:
const abbrev = ({name: { first, last }, occupation: { title } }) => {
```

### Technical frame 8: Plain Old JavaScript Objects / destructuring objects

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01079))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01081))_

<a id="atom-technical-atom-33b47d4af6a385f1"></a>
```
const abbrev = ({name: { first, last }, occupation: { title } }) =>
return { first, last, title};
}
abbrev(user)
//=> {"first":"Reginald","last":"Braithwaite","title":"Author"}
```

### Technical frame 9: Plain Old JavaScript Objects / revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01088))_

> What about mapping? Well, let's start with the simplest possible thing, making a copy of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn't fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01086))_

<a id="atom-technical-atom-d9b8b52b15508a2f"></a>
```
In that case, a linked list of the numbers 1, 2, and 3 will look like this: { first: 1, rest: { first:
2, rest: { first: 3, rest: EMPTY } } }.
We can then perform the equivalent of [first, ...rest] with direct property accessors:
```

### Technical frame 10: Plain Old JavaScript Objects / revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01088))_

> What about mapping? Well, let's start with the simplest possible thing, making a copy of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn't fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01087))_

<a id="atom-technical-atom-047a1c592c0a9923"></a>
```
const EMPTY = {};
const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \
} } };
OneTwoThree.first
//=> 1
OneTwoThree.rest
//=> {"first":2,"rest":{"first":3,"rest":{}}}
OneTwoThree.rest.rest.first
//=> 3
Taking the length of a linked list is easy:
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
length(OneTwoThree)
//=> 3
```

### Technical frame 11: Mutation

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01105))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01100))_

<a id="atom-technical-atom-4843398da358010b"></a>
```
const oneTwoThree = [1, 2, 3];
oneTwoThree[0] = 'one';
oneTwoThree
//=> [ 'one', 2, 3 ]
```

### Technical frame 12: Mutation

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01105))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01104))_

<a id="atom-technical-atom-c0b0e6add0f87a0e"></a>
```
const name = {firstName: 'Leonard', lastName: 'Braithwaite'};
name.middleName = 'Austin'
name
//=> { firstName: 'Leonard',
#
lastName: 'Braithwaite',
#
middleName: 'Austin' }
```

### Technical frame 13: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01511))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01503))_

<a id="atom-technical-atom-8042d9524ba796e4"></a>
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

### Technical frame 14: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01511))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01504))_

<a id="atom-technical-atom-e056a601168332ef"></a>
```
const iter = stack.iterator();
iter().value
//=> "you!"
iter().value
//=> "to"
```

### Technical frame 15: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01513))_

> If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01512))_

<a id="atom-technical-atom-10e1bb48509f0931"></a>
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

### Technical frame 16: Served by the Pot: Collections / Iteration and Iterables / iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01532))_

> The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01530))_

<a id="atom-technical-atom-9f69b9dd89759b90"></a>
```
const Stack3 = () =>
({
array: [],
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
[Symbol.iterator] () {
let iterationIndex = this.index;
return {
next () {
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
}
});
const stack = Stack3();
```

### Technical frame 17: Served by the Pot: Collections / Iteration and Iterables / iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01532))_

> The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01531))_

<a id="atom-technical-atom-16d5c5eff09bed36"></a>
```
stack.push(2000);
stack.push(10);
stack.push(5)
const collectionSum = (collection) => {
const iterator = collection[Symbol.iterator]();
let eachIteration,
sum = 0;
while ((eachIteration = iterator.next(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
collectionSum(stack)
//=> 2015
Using [Symbol.iterator] instead of .iterator seems like adding an extra moving part for nothing.
Do we get anything in return?
Indeed we do. Behold the for...of loop:
const iterableSum = (iterable) => {
let sum = 0;
for (const num of iterable) {
sum += num;
}
return sum
}
iterableSum(stack)
//=> 2015
```

### Technical frame 18: Served by the Pot: Collections / Iteration and Iterables / iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01534))_

> As we can see, we can use for...of with linked lists just as easily as with stacks. And there's one more thing: You recall that the spread operator ( ... ) can spread the elements of an array in an array literal or as parameters in a function invocation.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01533))_

<a id="atom-technical-atom-20470d41caf14e2c"></a>
```
const EMPTY = {
isEmpty: () => true
};
const isEmpty = (node) => node === EMPTY;
const Pair1 = (first, rest = EMPTY) =>
({
first,
rest,
isEmpty () { return false },
[Symbol.iterator] () {
let currentPair = this;
return {
next () {
if (currentPair.isEmpty()) {
return {done: true}
}
else {
const value = currentPair.first;
currentPair = currentPair.rest;
return {done: false, value}
}
}
}
}
});
const list = (...elements) => {
const [first, ...rest] = elements;
return elements.length === 0
? EMPTY
: Pair1(first, list(...rest))
}
const someSquares = list(1, 4, 9, 16, 25);
iterableSum(someSquares)
//=> 55
```

### Technical frame 19: Served by the Pot: Collections / Generating Iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01599))_

> Well, we've written our iterator as a server . It waits until given a request, and then it returns exactly one item. Then it waits for the next request. There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01596))_

<a id="atom-technical-atom-8ca85058badf52a7"></a>
> Iterators have to arrange its own state such that when you call them, they compute and return the next item.

### Technical frame 20: Served by the Pot: Collections / Generating Iterables / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01682))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01679))_

<a id="atom-technical-atom-7ca2d5da0f09f056"></a>
> If we call our generator function more than once, we get new iterators.

### Technical frame 21: Served by the Pot: Collections / Generating Iterables / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01684))_

> This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01683))_

<a id="atom-technical-atom-54530c82c657b597"></a>
```
const ThreeNumbers = {
*[Symbol.iterator] () {
yield 1;
yield 2;
yield 3
}
}
```

### Technical frame 22: Served by the Pot: Collections / Generating Iterables / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01701))_

> We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01700))_

<a id="atom-technical-atom-7f2d6c66b42c90d1"></a>
```
const isIterable = (something) =>
!!something[Symbol.iterator];
const TreeIterable = (iterable) =>
({
[Symbol.iterator]: function * () {
for (const e of iterable) {
if (isIterable(e)) {
for (const ee of TreeIterable(e)) {
yield ee;
}
}
else {
yield e;
}
}
}
})
for (const i of TreeIterable([1, [2, [3, 4], 5]])) {
console.log(i);
}
//=>
1
2
3
4
5
```

### Technical frame 23: Served by the Pot: Collections / Generating Iterables / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01705))_

> Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01702))_

<a id="atom-technical-atom-56d4d47f5e80ca55"></a>
> But if you can write it as a simple generator, write it as a simple generator.

### Technical frame 24: Served by the Pot: Collections / Generating Iterables / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01705))_

> Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01703))_

<a id="atom-technical-atom-d42f8425096b903b"></a>
```
function * tree (iterable) {
for (const e of iterable) {
if (isIterable(e)) {
for (const ee of tree(e)) {
yield ee;
}
}
else {
yield e;
}
}
};
for (const i of tree([1, [2, [3, 4], 5]])) {
console.log(i);
}
//=>
1
2
3
4
5
```

### Technical frame 25: Lazy and Eager Collections / implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01746))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01747))_

<a id="atom-technical-atom-795d0e64583e2f8f"></a>
```
const Numbers = Object.assign({
[Symbol.iterator]: () => {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
}, LazyCollection);
// Pair, a/k/a linked lists
const EMPTY = {
isEmpty: () => true
```

### Technical frame 26: Lazy and Eager Collections / implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01746))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01748))_

<a id="atom-technical-atom-d27d5907dbf68de0"></a>
```
};
const isEmpty = (node) => node === EMPTY;
const Pair = (car, cdr = EMPTY) =>
Object.assign({
car,
cdr,
isEmpty: () => false,
[Symbol.iterator]: function () {
let currentPair = this;
return {
next: () => {
if (currentPair.isEmpty()) {
return {done: true}
}
else {
const value = currentPair.car;
currentPair = currentPair.cdr;
return {done: false, value}
}
}
}
}
}, LazyCollection);
Pair.from = (iterable) =>
(function iterationToList (iteration) {
const {done, value} = iteration.next();
return done ? EMPTY : Pair(value, iterationToList(iteration));
})(iterable[Symbol.iterator]());
// Stack
const Stack = () =>
Object.assign({
array: [],
index: -1,
push: function (value) {
```

### Technical frame 27: Lazy and Eager Collections / implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01746))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01749))_

<a id="atom-technical-atom-078d32271e5067fb"></a>
```
return this.array[this.index += 1] = value;
},
pop: function () {
const value = this.array[this.index];
this.array[this.index] = undefined;
if (this.index >= 0) {
this.index -= 1
}
return value
},
isEmpty: function () {
return this.index < 0
},
[Symbol.iterator]: function () {
let iterationIndex = this.index;
return {
next: () => {
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
}
}, LazyCollection);
Stack.from = function (iterable) {
const stack = this();
for (let element of iterable) {
stack.push(element);
}
return stack;
}
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Plain Old JavaScript Objects: In JavaScript, an object is a map from string keys to values.; Javascript shares technical record from ECMAScript 6 has three major groups of features: / Forewords to the First Edition / matthew knox: { year: 2012, month: 6, day: 14 } (3 shared statement(s), 8 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements and technical atoms: Iterator shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterator objects: Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object w ... [truncated]; Iterator shares technical record from Served by the Pot: Collections / Iteration and Iterables / iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array ... [truncated] (5 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-method]] - shared statements and technical atoms: Method shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.; Method shares technical record from Served by the Pot: Collections / Iteration and Iterables / iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array ... [truncated] (2 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-iteration]] - shared statements and technical atoms: Iteration shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterator objects: Iteration for functions and objects has been around for many, many decades. For simple linear collections like arrays, linked lists, stacks, and queues, functional i ... [truncated]; Iteration shares technical record from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: const Stack1 = () => ({ array:[], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array[ ... [truncated] (1 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms: Expression shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.; Expression shares technical record from Plain Old JavaScript Objects / literal object syntax: const SecretDecoderRing = { encode (plaintext) { return plaintext .split('') .map( char => char.charCodeAt() ) .map( code => code + 1 ) .map( code => String.fromChar ... [truncated] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-functional-iterator]] - shared statements and technical atoms: Functional Iterators shares source evidence from Served by the Pot: Collections / Generating Iterables: Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly unt ... [truncated]; Functional Iterators shares technical record from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: const Stack1 = () => ({ array:[], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array[ ... [truncated] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from Served by the Pot: Collections / Generating Iterables / generators and iterables: Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of r ... [truncated]; Return shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-iterable]] - shared statements and technical atoms: Iterable shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterables: The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterato ... [truncated]; Iterable shares technical record from Served by the Pot: Collections / Iteration and Iterables / iterables: const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair1 = (first, rest = EMPTY) => ({ first, rest, isEmpty () { return false }, ... [truncated] (2 shared statement(s), 2 shared atom(s))

### Shared claims

- [[javascriptallonge-collection]] - shared statements: Collection shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterator objects: In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be ... [truncated] (2 shared statement(s))
- [[javascriptallonge-evaluate]] - shared statements: Evaluate shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. (1 shared statement(s))

## Source

- [[javascriptallonge]]
