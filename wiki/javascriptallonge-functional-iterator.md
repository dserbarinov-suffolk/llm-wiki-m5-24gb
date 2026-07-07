---
page_id: javascriptallonge-functional-iterator
page_kind: concept
summary: Functional Iterators: 39 statement(s) and 27 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-functional-iterator@7dea1439e3850531df075463a3473bdc
---

# Functional Iterators

What [[javascriptallonge]] covers about functional iterators:

## Statements

### Copy on Write / Functional Iterators

- The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays. _(javascriptallonge.pdf (source-range-c98ab3e6-01251))_

- Well, we call arraySum with an array, and it has baked into it a method for traversing the array. Perhaps we could extract both of those things. Let's rearrange our code a bit: _(javascriptallonge.pdf (source-range-c98ab3e6-01253))_

- What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable. _(javascriptallonge.pdf (source-range-c98ab3e6-01255))_

### Copy on Write / Functional Iterators / iterating

- Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. Nevertheless, there is some value in being able to express some algorithms as iteration. _(javascriptallonge.pdf (source-range-c98ab3e6-01260))_

- JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. Summing the elements of an array can be accomplished with: _(javascriptallonge.pdf (source-range-c98ab3e6-01261))_

- Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 . _(javascriptallonge.pdf (source-range-c98ab3e6-01263))_

- Notice that buried inside our loop, we have bound the names done and value . We can put those into a POJO (a Plain Old JavaScript Object). It'll be a little awkward, but we'll be patient: _(javascriptallonge.pdf (source-range-c98ab3e6-01266))_

- Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } . _(javascriptallonge.pdf (source-range-c98ab3e6-01269))_

- We can write a different iterator for a different data structure. Here's one for linked lists: _(javascriptallonge.pdf (source-range-c98ab3e6-01270))_

### Copy on Write / Functional Iterators / unfolding and laziness

- Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let's consider the simplest example: _(javascriptallonge.pdf (source-range-c98ab3e6-01274))_

- A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators. _(javascriptallonge.pdf (source-range-c98ab3e6-01278))_

- This business of going on forever has some drawbacks. Let's introduce an idea: A function that takes an iterator and returns another iterator. We can start with take , an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-c98ab3e6-01282))_

- How about the squares of the first five odd numbers? We'll need an iterator that produces odd numbers. We can write that directly: _(javascriptallonge.pdf (source-range-c98ab3e6-01284))_

- Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions. _(javascriptallonge.pdf (source-range-c98ab3e6-01289))_

### Copy on Write / Functional Iterators / bonus

- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-c98ab3e6-01291))_

- This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like: _(javascriptallonge.pdf (source-range-c98ab3e6-01294))_

- JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy. _(javascriptallonge.pdf (source-range-c98ab3e6-01296))_

### Copy on Write / Functional Iterators / caveat

- Please note that unlike most of the other functions discussed in this book, iterators are stateful . There are some important implications of stateful functions. One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. So as you traverse the new decorator, you're changing the state of the original! _(javascriptallonge.pdf (source-range-c98ab3e6-01298))_

- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-c98ab3e6-01299))_

### Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

- When discussing functions, we looked at the benefits of writing Functional Iterators. We can do the same thing for objects. Here's a stack that has its own functional iterator method: _(javascriptallonge.pdf (source-range-c98ab3e6-01502))_

- We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method: _(javascriptallonge.pdf (source-range-c98ab3e6-01511))_

- If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-c98ab3e6-01513))_

### Served by the Pot: Collections / Iteration and Iterables / iterator objects

- Iteration for functions and objects has been around for many, many decades. For simple linear collections like arrays, linked lists, stacks, and queues, functional iterators are the simplest and easiest way to implement iterators. _(javascriptallonge.pdf (source-range-c98ab3e6-01516))_

### Served by the Pot: Collections / Iteration and Iterables / iterables

- People have been writing iterators since JavaScript was first released in the late 1990s. Since there was no particular standard way to do it, people used all sorts of methods, and their methods returned all sorts of things: Objects with various interfaces, functional iterators, you name it. _(javascriptallonge.pdf (source-range-c98ab3e6-01524))_

### Served by the Pot: Collections / Generating Iterables

- Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done. _(javascriptallonge.pdf (source-range-c98ab3e6-01595))_

### Served by the Pot: Collections / Generating Iterables / state machines

- The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 : _(javascriptallonge.pdf (source-range-c98ab3e6-01623))_


## Technical atoms

### Technical frame 1: Copy on Write / Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01251))_

> The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01248))_

<a id="atom-technical-atom-ee8aba9a9f143b13"></a>
```
const arraySum = ([first, ...rest], accumulator = 0) =>
first === undefined
? accumulator
: arraySum(rest, first + accumulator)
arraySum([1, 4, 9, 16, 25])
//=> 55
```

### Technical frame 2: Copy on Write / Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01251))_

> The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01250))_

<a id="atom-technical-atom-e688aea0db4b817d"></a>
```
const callLeft = (fn, ...args) =>
(...remainingArgs) =>
fn(...args, ...remainingArgs);
const foldArrayWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: fn(first, foldArrayWith(fn, terminalValue, rest));
const arraySum = callLeft(foldArrayWith, (a, b) => a + b, 0);
arraySum([1, 4, 9, 16, 25])
//=> 55
```

### Technical frame 3: Copy on Write / Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01255))_

> What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01254))_

<a id="atom-technical-atom-cfc50b6861f2e3ea"></a>
```
const callRight = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
const foldArrayWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: fn(first, foldArrayWith(fn, terminalValue, rest));
const foldArray = (array) => callRight(foldArrayWith, array);
const sumFoldable = (folder) => folder((a, b) => a + b, 0);
sumFoldable(foldArray([1, 4, 9, 16, 25]))
//=> 55
```

### Technical frame 4: Copy on Write / Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01258))_

> We've found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we've completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really).

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01257))_

<a id="atom-technical-atom-af9a4e86283834fb"></a>
```
const callRight = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
const foldTreeWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: Array.isArray(first)
? fn(foldTreeWith(fn, terminalValue, first), foldTreeWith(fn, terminalValu\
e, rest))
: fn(first, foldTreeWith(fn, terminalValue, rest));
const foldTree = (tree) => callRight(foldTreeWith, tree);
const sumFoldable = (folder) => folder((a, b) => a + b, 0);
sumFoldable(foldTree([1, [4, [9, 16]], 25]))
//=> 55
```

### Technical frame 5: Copy on Write / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01263))_

> Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01262))_

<a id="atom-technical-atom-c0033c3f5acdc292"></a>
```
const arraySum = (array) => {
let sum = 0;
for (let i = 0; i < array.length; ++i) {
sum += array[i];
}
return sum
}
arraySum([1, 4, 9, 16, 25])
//=> 55
```

### Technical frame 6: Copy on Write / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01266))_

> Notice that buried inside our loop, we have bound the names done and value . We can put those into a POJO (a Plain Old JavaScript Object). It'll be a little awkward, but we'll be patient:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01265))_

<a id="atom-technical-atom-d92615e150d7762f"></a>
```
const arraySum = (array) => {
let done,
sum = 0,
i = 0;
while ((done = i == array.length, !done)) {
const value = array[i++];
sum += value;
}
return sum
}
arraySum([1, 4, 9, 16, 25])
//=> 55
```

### Technical frame 7: Copy on Write / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01269))_

> Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01267))_

<a id="atom-technical-atom-e2eebf14a262e5cb"></a>
```
const arraySum = (array) => {
let iter,
sum = 0,
index = 0;
while (
(eachIteration = {
done: index === array.length,
value: index < array.length ? array[index] : undefined
},
++index,
!eachIteration.done)
) {
sum += eachIteration.value;
}
return sum;
}
arraySum([1, 4, 9, 16, 25])
//=> 55
With this code, we make a POJO that has done and value keys. All the summing code needs to know
is to add eachIteration.value. Now we can extract the ickiness into a separate function:
const arrayIterator = (array) => {
let i = 0;
return () => {
const done = i === array.length;
return {
done,
value: done ? undefined : array[i++]
}
}
}
const iteratorSum = (iterator) => {
let eachIteration,
sum = 0;
while ((eachIteration = iterator(), !eachIteration.done)) {
```

### Technical frame 8: Copy on Write / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01269))_

> Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01268))_

<a id="atom-technical-atom-e53a3a370658b356"></a>
```
sum += eachIteration.value;
}
return sum;
}
iteratorSum(arrayIterator([1, 4, 9, 16, 25]))
//=> 55
```

### Technical frame 9: Copy on Write / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01270))_

> We can write a different iterator for a different data structure. Here's one for linked lists:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01271))_

<a id="atom-technical-atom-a62bacb3265ebbff"></a>
```
const EMPTY = null;
const isEmpty = (node) => node === EMPTY;
const pair = (first, rest = EMPTY) => ({first, rest});
const list = (...elements) => {
const [first, ...rest] = elements;
return elements.length === 0
? EMPTY
: pair(first, list(...rest))
}
const print = (aPair) =>
isEmpty(aPair)
? ""
: `${aPair.first} ${print(aPair.rest)}`
const listIterator = (aPair) =>
() => {
const done = isEmpty(aPair);
if (done) {
return {done};
}
else {
const {first, rest} = aPair;
aPair = aPair.rest;
```

### Technical frame 10: Copy on Write / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01270))_

> We can write a different iterator for a different data structure. Here's one for linked lists:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01272))_

<a id="atom-technical-atom-dfff18cf80552c25"></a>
```
return { done, value: first }
}
}
const iteratorSum = (iterator) => {
let eachIteration,
sum = 0;;
while ((eachIteration = iterator(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
const aListIterator = listIterator(list(1, 4, 9, 16, 25));
iteratorSum(aListIterator)
//=> 55
```

### Technical frame 11: Copy on Write / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01278))_

> A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01275))_

<a id="atom-technical-atom-673ce6b311a6792f"></a>
```
const NumberIterator = (number = 0) =>
() => ({ done: false, value: number++ })
fromOne = NumberIterator(1);
fromOne().value;
//=> 1
fromOne().value;
//=> 2
fromOne().value;
//=> 3
fromOne().value;
//=> 4
fromOne().value;
//=> 5
```

### Technical frame 12: Copy on Write / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01278))_

> A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01277))_

<a id="atom-technical-atom-951a817b8bdbc79d"></a>
```
const FibonacciIterator
= () => {
let previous = 0,
current = 1;
return () => {
const value = current;
[previous, current] = [current, current + previous];
return {done: false, value};
};
};
const fib = FibonacciIterator()
fib().value
//=> 1
fib().value
//=> 1
fib().value
//=> 2
fib().value
//=> 3
fib().value
//=> 5
```

### Technical frame 13: Copy on Write / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01282))_

> This business of going on forever has some drawbacks. Let's introduce an idea: A function that takes an iterator and returns another iterator. We can start with take , an easy function that returns an iterator that only returns a fixed number of elements:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01280))_

<a id="atom-technical-atom-313ccf3036ff0bee"></a>
```
const mapIteratorWith = (fn, iterator) =>
() => {
const {done, value} = iterator();
return ({done, value: done ? undefined : fn(value)});
}
const squares = mapIteratorWith((x) => x * x, NumberIterator(1));
squares().value
//=> 1
squares().value
```

### Technical frame 14: Copy on Write / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01282))_

> This business of going on forever has some drawbacks. Let's introduce an idea: A function that takes an iterator and returns another iterator. We can start with take , an easy function that returns an iterator that only returns a fixed number of elements:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01281))_

<a id="atom-technical-atom-b8970c6b291f5037"></a>
```
//=> 4
squares().value
//=> 9
```

### Technical frame 15: Copy on Write / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01284))_

> How about the squares of the first five odd numbers? We'll need an iterator that produces odd numbers. We can write that directly:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01283))_

<a id="atom-technical-atom-08b7194d0deda5eb"></a>
```
const take = (iterator, numberToTake) => {
let count = 0;
return () => {
if (++count <= numberToTake) {
return iterator();
} else {
return {done: true};
}
};
};
const toArray = (iterator) => {
let eachIteration,
array = [];
while ((eachIteration = iterator(), !eachIteration.done)) {
array.push(eachIteration.value);
}
return array;
}
toArray(take(FibonacciIterator(), 5))
//=> [1, 1, 2, 3, 5]
toArray(take(squares, 5))
//=> [1, 4, 9, 16, 25]
```

### Technical frame 16: Copy on Write / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01289))_

> Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01285))_

<a id="atom-technical-atom-3cbb0179c9f157ad"></a>
```
const odds = () => {
```

### Technical frame 17: Copy on Write / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01289))_

> Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01286))_

<a id="atom-technical-atom-c80140cd0040b3b4"></a>
```
let number = 1;
return () => {
const value = number;
number += 2;
return {done: false, value};
}
}
const squareOf = callLeft(mapIteratorWith, (x) => x * x)
toArray(take(squareOf(odds()), 5))
//=> [1, 9, 25, 49, 81]
```

### Technical frame 18: Copy on Write / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01289))_

> Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01288))_

<a id="atom-technical-atom-276e586089a73115"></a>
```
const filterIteratorWith = (fn, iterator) =>
() => {
do {
const {done, value} = iterator();
} while (!done && !fn(value));
return {done, value};
}
const oddsOf = callLeft(filterIteratorWith, (n) => n % 2 === 1);
toArray(take(squareOf(oddsOf(NumberIterator(1))), 5))
//=> [1, 9, 25, 49, 81]
```

### Technical frame 19: Copy on Write / Functional Iterators / bonus

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01294))_

> This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01293))_

<a id="atom-technical-atom-da3ef04aced8adf4"></a>
```
const firstInIteration = (fn, iterator) =>
take(filterIteratorWith(fn, iterator), 1);
```

### Technical frame 20: Copy on Write / Functional Iterators / bonus

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01296))_

> JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01295))_

<a id="atom-technical-atom-305b589bdbaf0a36"></a>
```
const firstInArray = (fn, array) =>
array.filter(fn)[0];
```

### Technical frame 21: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

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

### Technical frame 22: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

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

### Technical frame 23: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01511))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01506))_

<a id="atom-technical-atom-3d2ca956d4a0d0e8"></a>
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

### Technical frame 24: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01511))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01508))_

<a id="atom-technical-atom-ef9b2ba6e355fbac"></a>
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

### Technical frame 25: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01511))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01510))_

<a id="atom-technical-atom-5ce3bb3e004e87ba"></a>
```
const stack = Stack1();
stack.push(1);
stack.push(2);
stack.push(3);
iteratorSum(stack.iterator())
//=> 6
```

### Technical frame 26: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

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

### Technical frame 27: Served by the Pot: Collections / Generating Iterables / state machines

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01623))_

> The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 :

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01622))_

<a id="atom-technical-atom-59b85769c4575211"></a>
```text
while (true) {
[a, b] = [b, a + b];
console.log(b);
}
}
fibonacci()
//=>
0
1
1
2
3
5
8
13
21
34
Served by the Pot: Collections
206
55
89
144
...
The thing to note here is that our fibonacci generator has three states: generating 0, generating
1, and generating everything after that. This isn’t a good fit for an iterator, because iterators have
one functional entry point and therefore, we’d have to represent our three states explicitly, perhaps
using a state pattern90:
We’ll keep it simple:
// Iteration
let a, b, state = 0;
const fibonacci = () => {
switch (state) {
case 0:
state = 1;
return a = 0;
case 1:
state = 2;
return b = 1;
case 2:
[a, b] = [b, a + b];
return b
}
};
while (true) {
console.log(fibonacci());
}
//=>
0
1
1
2
3
5
8
13
90https://en.wikipedia.org/wiki/State_pattern
Served by the Pot: Collections
207
21
34
55
89
144
...
Again, this is not particularly horrendous, but like the recursive example, we’re explicitly greenspun-
ning the natural linear state. In a generator, we write “do this, then this, then this.” In an iterator,
we have to wrap that up and explicitly keep track of what step we’re on.
So we see the same thing: The generation version has state, but it’s implicit in JavaScript’s linear
control flow. Whereas the iteration version must make that state explicit.
javascript’s generators
It would be very nice if we could sometimes write iterators as a .next() method that gets called, and
sometimes write out a generator. Given the title of this chapter, it is not a surprise that JavaScript
makes this possible.
We can write an iterator, but use a generation style of programming. An iterator written in a
generation style is called a generator. To write a generator, we write a function, but we make two
changes:
1. We declare the function using the function * syntax. Not a fat arrow. Not a plain function.
2. We don’t return values or output them to console.log. We “yield” values using the yield
keyword.
When we invoke the function, we get an iterator object back. Let’s start with the degenerate example,
the empty iterator:91
function * empty () {};
empty().next()
//=>
{"done":true}
When we invoke empty, we get an iterator with no elements. This makes sense, because empty never
yields anything. We call its .next() method, but it’s done immediately.
Generator functions can take an argument. Let’s use that to illustrate yield:
91We wrote a generator declaration. We can also write const empty = function * () {} to bind an anonymous generator to the empty keyword,
but we don’t need to do that here.
Served by the Pot: Collections
208
function * only (something) {
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 34 | Served by the Pot: Collections |
| 144 | The thing to note here is that our fibonacci generator has three states: generating 0, generating 1, and generating everything after that. This isn’t a good fit for an iterator, because iterators have one functional entry point and therefore, we’d have to represent our three states explicitly, perhaps using a state pattern90: We’ll keep it simple: // Iteration let a, b, state = 0; const fibonacci = () => { switch (state) { case 0: state = 1; return a = 0; case 1: state = 2; return b = 1; case 2: [a, b] = [b, a + b]; return b while (true) { console.log(fibonacci()); |
| 13 | 90https://en.wikipedia.org/wiki/State_pattern |
| 207 | Served by the Pot: Collections |
| 144 | Again, this is not particularly horrendous, but like the recursive example, we’re explicitly greenspun- ning the natural linear state. In a generator, we write “do this, then this, then this.” In an iterator, we have to wrap that up and explicitly keep track of what step we’re on. So we see the same thing: The generation version has state, but it’s implicit in JavaScript’s linear control flow. Whereas the iteration version must make that state explicit. javascript’s generators It would be very nice if we could sometimes write iterators as a.next() method that gets called, and sometimes write out a generator. Given the title of this chapter, it is not a surprise that JavaScript makes this possible. We can write an iterator, but use a generation style of programming. An iterator written in a generation style is called a generator. To write a generator, we write a function, but we make two changes: |
| 1 | We declare the function using the function * syntax. Not a fat arrow. Not a plain function. |
| 2 | We don’t return values or output them to console.log. We “yield” values using the yield keyword. When we invoke the function, we get an iterator object back. Let’s start with the degenerate example, the empty iterator:91 function * empty () {}; empty().next() {"done":true} When we invoke empty, we get an iterator with no elements. This makes sense, because empty never yields anything. We call its.next() method, but it’s done immediately. 91We wrote a generator declaration. We can also write const empty = function * () {} to bind an anonymous generator to the empty keyword, but we don’t need to do that here. |
| 208 | Generator functions can take an argument. Let’s use that to illustrate yield: Served by the Pot: Collections function * only (something) { |

</details>


## Related pages

### Source structure

- [[javascriptallonge-section-copy-on-write-functional-iterators-74724e0a]] - source section: Copy on Write / Functional Iterators shares source evidence from Copy on Write / Functional Iterators: The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still re ... [truncated]; Copy on Write / Functional Iterators shares technical record from Copy on Write / Functional Iterators: const arraySum = ([first, ...rest], accumulator = 0) => first === undefined ? accumulator : arraySum(rest, first + accumulator) arraySum([1, 4, 9, 16, 25]) //=> 55 (31 shared statement(s), 20 shared atom(s))
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-a-look-back-at-functional-iterators-57a76f01]] - source section: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators shares source evidence from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: When discussing functions, we looked at the benefits of writing Functional Iterators. We can do the same thing for objects. Here's a stack that has its own functiona ... [truncated]; Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators shares technical record from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: const Stack1 = () => ({ array:[], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array[ ... [truncated] (4 shared statement(s), 6 shared atom(s))

### Shared technical atoms

- [[javascriptallonge-copy-write]] - shared statements and technical atoms: Copy on Write shares source evidence from Copy on Write / Functional Iterators: The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still re ... [truncated]; Copy on Write shares technical record from Copy on Write / Functional Iterators: const arraySum = ([first, ...rest], accumulator = 0) => first === undefined ? accumulator : arraySum(rest, first + accumulator) arraySum([1, 4, 9, 16, 25]) //=> 55 (31 shared statement(s), 20 shared atom(s))
- [[javascriptallonge-iteration]] - shared statements and technical atoms: Iteration shares source evidence from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an ... [truncated]; Iteration shares technical record from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: const Stack1 = () => ({ array:[], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array[ ... [truncated] (1 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms: Element shares source evidence from Copy on Write / Functional Iterators / iterating: Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like ... [truncated]; Element shares technical record from Copy on Write / Functional Iterators: const arraySum = ([first, ...rest], accumulator = 0) => first === undefined ? accumulator : arraySum(rest, first + accumulator) arraySum([1, 4, 9, 16, 25]) //=> 55 (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Copy on Write / Functional Iterators / iterating: JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. Summing the elements of an array can be accomplished with:; Javascript shares technical record from Copy on Write / Functional Iterators / iterating: const arraySum = (array) => { let sum = 0; for (let i = 0; i < array.length; ++i) { sum += array[i]; } return sum } arraySum([1, 4, 9, 16, 25]) //=> 55 (3 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-data]] - shared statements and technical atoms: Data shares source evidence from Copy on Write / Functional Iterators: What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function do ... [truncated]; Data shares technical record from Copy on Write / Functional Iterators / iterating: const EMPTY = null; const isEmpty = (node) => node === EMPTY; const pair = (first, rest = EMPTY) => ({first, rest}); const list = (...elements) => { const [first, .. ... [truncated] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from Served by the Pot: Collections / Generating Iterables: Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly unt ... [truncated]; Object shares technical record from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: const Stack1 = () => ({ array:[], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array[ ... [truncated] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-list]] - shared technical atoms: List shares technical record from Copy on Write / Functional Iterators / iterating: const EMPTY = null; const isEmpty = (node) => node === EMPTY; const pair = (first, rest = EMPTY) => ({first, rest}); const list = (...elements) => { const [first, .. ... [truncated] (3 shared atom(s))
- [[javascriptallonge-structure]] - shared statements and technical atoms: Structure shares source evidence from Copy on Write / Functional Iterators: What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function do ... [truncated]; Structure shares technical record from Copy on Write / Functional Iterators / iterating: const EMPTY = null; const isEmpty = (node) => node === EMPTY; const pair = (first, rest = EMPTY) => ({first, rest}); const list = (...elements) => { const [first, .. ... [truncated] (1 shared statement(s), 2 shared atom(s))

### Shared claims

- [[javascriptallonge-method]] - shared statements: Method shares source evidence from Served by the Pot: Collections / Generating Iterables: Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly unt ... [truncated] (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements: Return shares source evidence from Copy on Write / Functional Iterators / iterating: Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iterator ... [truncated] (1 shared statement(s))

### Topics

- [[javascriptallonge-iterator]] - broader topic: Iterator shares source evidence from Copy on Write / Functional Iterators / unfolding and laziness: Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions.; Iterator shares technical record from Copy on Write / Functional Iterators / unfolding and laziness: const NumberIterator = (number = 0) => () => ({ done: false, value: number++ }) fromOne = NumberIterator(1); fromOne().value; //=> 1 fromOne().value; //=> 2 fromOne( ... [truncated] (4 shared statement(s), 8 shared atom(s))
- [[javascriptallonge-functional]] - broader topic: Functional shares source evidence from Served by the Pot: Collections / Generating Iterables: Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly unt ... [truncated]; Functional shares technical record from Served by the Pot: Collections / Generating Iterables / state machines: while (true) { [a, b] = [b, a + b]; console.log(b); } } fibonacci() //=> 0 1 1 2 3 5 8 13 21 34 Served by the Pot: Collections 206 55 89 144 ... The thing to note he ... [truncated] (1 shared statement(s), 1 shared atom(s))

## Source

- [[javascriptallonge]]
