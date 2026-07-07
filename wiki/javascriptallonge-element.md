---
page_id: javascriptallonge-element
page_kind: concept
summary: Element: 21 statement(s) and 23 atom(s) from raw/javascriptallonge.pdf.
page_family: broad-topic
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-element@62a901d1fac350a895845772c397b4a3
---

# Element

What [[javascriptallonge]] covers about element:

## Statements

### Composing and Decomposing Data / Arrays and Destructuring Arguments / element references

- Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract: _(javascriptallonge.pdf (source-range-c98ab3e6-00814))_

### Composing and Decomposing Data / Self-Similarity

- Let's convert our rules to array literals. The first rule is simple: [] is a list. How about the second rule? We can express that using a spread. Given an element e and a list list , [e, ...list] is a list. We can test this manually by building up a list: _(javascriptallonge.pdf (source-range-c98ab3e6-00870))_

### Composing and Decomposing Data / Self-Similarity / linear recursion

- The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. Our solutions are a little simpler in that we don't really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. _(javascriptallonge.pdf (source-range-c98ab3e6-00895))_

- The usual 'terminal case' will be that flattening an empty array will produce an empty array. The next terminal case is that if an element isn't an array, we don't flatten it, and can put it together with the rest of our solution directly. Whereas if an element is an array, we'll flatten it and put it together with the rest of our solution. _(javascriptallonge.pdf (source-range-c98ab3e6-00899))_

- Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions. _(javascriptallonge.pdf (source-range-c98ab3e6-00903))_

### Garbage, Garbage Everywhere

- The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend . _(javascriptallonge.pdf (source-range-c98ab3e6-01002))_

### Garbage, Garbage Everywhere / some history

- Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is faster than copying a bunch of elements. _(javascriptallonge.pdf (source-range-c98ab3e6-01026))_

### Garbage, Garbage Everywhere / so why arrays

- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-c98ab3e6-01036))_

### Copy on Write

- This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection. _(javascriptallonge.pdf (source-range-c98ab3e6-01207))_

### Copy on Write / Functional Iterators / iterating

- Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 . _(javascriptallonge.pdf (source-range-c98ab3e6-01263))_

### Served by the Pot: Collections / Iteration and Iterables

- All of these actions involve going through the contents one by one. Acting on the elements of a collection one at a time is called iterating over the contents , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-c98ab3e6-01500))_

### Served by the Pot: Collections / Iteration and Iterables / iterator objects

- Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object with a .next() method. _(javascriptallonge.pdf (source-range-c98ab3e6-01518))_

### Served by the Pot: Collections / Iteration and Iterables / iterables

- One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-c98ab3e6-01540))_

### Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

- For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest] : _(javascriptallonge.pdf (source-range-c98ab3e6-01577))_

### Served by the Pot: Collections / Generating Iterables / recursive iterators

- For example, iterating over a tree. Given an array that might contain arrays, let's say we want to generate all the 'leaf' elements, i.e. elements that are not, themselves, iterable. _(javascriptallonge.pdf (source-range-c98ab3e6-01607))_

### Served by the Pot: Collections / Generating Iterables / state machines

- The first element of the fibonacci sequence is zero. _(javascriptallonge.pdf (source-range-c98ab3e6-01617))_

- The second element of the fibonacci sequence is one. _(javascriptallonge.pdf (source-range-c98ab3e6-01618))_

- Every subsequent element of the fibonacci sequence is the sum of the previous two elements. _(javascriptallonge.pdf (source-range-c98ab3e6-01619))_

### Served by the Pot: Collections / Generating Iterables / yielding iterables

- Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e . _(javascriptallonge.pdf (source-range-c98ab3e6-01705))_

### Lazy and Eager Collections / lazy collection operations

- Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack's elements, and it only needs to square two of those elements, 29 and 28 , to return the answer. _(javascriptallonge.pdf (source-range-c98ab3e6-01762))_


## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Arrays and Destructuring Arguments / element references

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00816))_

> As we can see, JavaScript Arrays are zero-based 56 .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00815))_

<a id="atom-technical-atom-fd4ca2610d355e62"></a>
```
const oneTwoThree = ["one", "two", "three"];
oneTwoThree[0]
//=> 'one'
oneTwoThree[1]
//=> 'two'
oneTwoThree[2]
//=> 'three'
```

### Technical frame 2: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00872))_

> Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00871))_

<a id="atom-technical-atom-51aa4003a2265bab"></a>
```
[]
//=> []
["baz", ...[]]
//=> ["baz"]
["bar", ...["baz"]]
//=> ["bar","baz"]
["foo", ...["bar", "baz"]]
//=> ["foo","bar","baz"]
```

### Technical frame 3: Composing and Decomposing Data / Self-Similarity / mapping

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00910))_

> This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again. Functions can take functions as arguments, so let's 'extract' the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00909))_

<a id="atom-technical-atom-44d7051ae602810d"></a>
```
const truthyAll = ([first, ...rest]) => first === undefined
? []
: [!!first, ...truthyAll(rest)];
truthyAll([null, true, 25, false, "foo"])
//=> [false,true,true,false,true]
```

### Technical frame 4: Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01021))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01015))_

<a id="atom-technical-atom-5f9b1798e734d975"></a>
```
const cons = (a, d) => [a, d],
car
= ([a, d]) => a,
cdr
= ([a, d]) => d;
```

### Technical frame 5: Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01026))_

> Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is fas

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01025))_

<a id="atom-technical-atom-26303fe469ee0e47"></a>
```
cdr(oneToFive)
//=> [2,[3,[4,[5,null]]]]
```

### Technical frame 6: Garbage, Garbage Everywhere / so why arrays

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01036))_

> Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation).

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01035))_

<a id="atom-technical-atom-557e4bd3a4b86aac"></a>
> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements.

### Technical frame 7: Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01207))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01203))_

<a id="atom-technical-atom-b34cb1ee5a282e9c"></a>
> The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array.

### Technical frame 8: Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01207))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01204))_

<a id="atom-technical-atom-575252d5f4b2c744"></a>
> Whereas if you have a linked list, and you take it's 'rest,' your 'child' list shares its nodes with the 'parent' list.

### Technical frame 9: Copy on Write / Functional Iterators

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

### Technical frame 10: Copy on Write / Functional Iterators / iterating

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

### Technical frame 11: Copy on Write / Functional Iterators / unfolding and laziness

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

### Technical frame 12: Copy on Write / Functional Iterators / bonus

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01294))_

> This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01293))_

<a id="atom-technical-atom-da3ef04aced8adf4"></a>
```
const firstInIteration = (fn, iterator) =>
take(filterIteratorWith(fn, iterator), 1);
```

### Technical frame 13: Copy on Write / Functional Iterators / bonus

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01296))_

> JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01295))_

<a id="atom-technical-atom-305b589bdbaf0a36"></a>
```
const firstInArray = (fn, array) =>
array.filter(fn)[0];
```

### Technical frame 14: Served by the Pot: Collections / Iteration and Iterables / iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01540))_

> One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01536))_

<a id="atom-technical-atom-8f303d1919cf6aed"></a>
```
['some squares', ...someSquares]
//=> ["some squares", 1, 4, 9, 16, 25]
```

### Technical frame 15: Served by the Pot: Collections / Iteration and Iterables / iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01540))_

> One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01538))_

<a id="atom-technical-atom-dea9418dd6ee7e59"></a>
```
const firstAndSecondElement = (first, second) =>
({first, second})
firstAndSecondElement(...stack)
//=> {"first":5,"second":10}
```

### Technical frame 16: Served by the Pot: Collections / Iteration and Iterables / ordered collections

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01551))_

> This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator] , and ensuring that our iterators start at the beginning and work forward.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01550))_

<a id="atom-technical-atom-93d825a6af6fbea5"></a>
```
const abc = ["a", "b", "c"];
for (const i of abc) {
console.log(i)
}
//=>
a
b
c
for (const i of abc) {
console.log(i)
}
//=>
a
b
c
```

### Technical frame 17: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01579))_

> like our other operations, rest preserves the ordered collection semantics of its argument.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01578))_

<a id="atom-technical-atom-4b232b3666097328"></a>
```
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
const rest = (iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
iterator.next();
return iterator;
}
});
```

### Technical frame 18: Served by the Pot: Collections / Generating Iterables / recursive iterators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01613))_

> If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next , we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. In essence, both the generation and iteration implementations have stacks, but the generation version's stack is implicit , while the iteration version's stack is explicit .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01608))_

<a id="atom-technical-atom-22441ca6eac743d3"></a>
```
// Generation
const isIterable = (something) =>
!!something[Symbol.iterator];
const generate = (iterable) => {
for (let element of iterable) {
if (isIterable(element)) {
generate(element)
}
else {
console.log(element)
}
}
}
generate([1, [2, [3, 4], 5]])
//=>
1
2
3
4
5
```

### Technical frame 19: Served by the Pot: Collections / Generating Iterables / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01710))_

> append iterates over a collection of iterables, one element at a time. Things like arrays can be easily catenated, but append iterates lazily, so there's no need to construct intermediary results.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01709))_

<a id="atom-technical-atom-cf5f0292f04b4586"></a>
```
function * append (...iterables) {
for (const iterable of iterables) {
for (const element of iterable) {
yield element;
}
}
}
const lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\
"]);
for (const word of lyrics) {
console.log(word);
}
//=>
a
b
c
one
two
three
do
re
me
```

### Technical frame 20: Served by the Pot: Collections / Generating Iterables / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01710))_

> append iterates over a collection of iterables, one element at a time. Things like arrays can be easily catenated, but append iterates lazily, so there's no need to construct intermediary results.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01712))_

<a id="atom-technical-atom-d77f5e63d004d0aa"></a>
```
function * append (...iterables) {
for (const iterable of iterables) {
yield * iterable;
}
}
const lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\
"]);
for (const word of lyrics) {
console.log(word);
}
```

### Technical frame 21: Served by the Pot: Collections / Generating Iterables / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01710))_

> append iterates over a collection of iterables, one element at a time. Things like arrays can be easily catenated, but append iterates lazily, so there's no need to construct intermediary results.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01713))_

<a id="atom-technical-atom-4f414c5b2051fa87"></a>
```
//=>
a
b
c
one
two
thre
do
re
```

### Technical frame 22: Served by the Pot: Collections / Generating Iterables / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01710))_

> append iterates over a collection of iterables, one element at a time. Things like arrays can be easily catenated, but append iterates lazily, so there's no need to construct intermediary results.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01714))_

<a id="atom-technical-atom-61b4cb84b60ebc91"></a>
```
const isIterable = (something) =>
!!something[Symbol.iterator];
function * tree (iterable) {
for (const e of iterable) {
if (isIterable(e)) {
yield * tree(e);
}
else {
yield e;
}
}
};
for (const i of tree([1, [2, [3, 4
console.log(i);
}
//=>
1
2
3
4
5
```

### Technical frame 23: Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01761))_

> This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01760))_

<a id="atom-technical-atom-25a90abc89f4f9aa"></a>
```
Stack.from([ 0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.first()
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-copy-write]] - shared statements and technical atoms: Copy on Write shares source evidence from Copy on Write: This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunc ... [truncated]; Copy on Write shares technical record from Copy on Write: The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. (2 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from Composing and Decomposing Data / Self-Similarity: Let's convert our rules to array literals. The first rule is simple: [] is a list. How about the second rule? We can express that using a spread. Given an element e ... [truncated]; List shares technical record from Composing and Decomposing Data / Self-Similarity: [] //=> [] ["baz", ...[]] //=> ["baz"] ["bar", ...["baz"]] //=> ["bar","baz"] ["foo", ...["bar", "baz"]] //=> ["foo","bar","baz"] (3 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-functional-iterator]] - shared statements and technical atoms: Functional Iterators shares source evidence from Copy on Write / Functional Iterators / iterating: Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like ... [truncated]; Functional Iterators shares technical record from Copy on Write / Functional Iterators: const arraySum = ([first, ...rest], accumulator = 0) => first === undefined ? accumulator : arraySum(rest, first + accumulator) arraySum([1, 4, 9, 16, 25]) //=> 55 (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Garbage, Garbage Everywhere / some history: Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of ar ... [truncated]; Javascript shares technical record from Garbage, Garbage Everywhere / some history: const cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d; (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-iteration]] - shared technical atoms: Iteration shares technical record from Served by the Pot: Collections / Iteration and Iterables / iterables: ['some squares', ...someSquares] //=> ["some squares", 1, 4, 9, 16, 25] (4 shared atom(s))
- [[javascriptallonge-iterable]] - shared statements and technical atoms: Iterable shares source evidence from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that itera ... [truncated]; Iterable shares technical record from Served by the Pot: Collections / Iteration and Iterables / iterables: ['some squares', ...someSquares] //=> ["some squares", 1, 4, 9, 16, 25] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that itera ... [truncated]; Return shares technical record from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: const first = (iterable) => iterable[Symbol.iterator]().next().value; const rest = (iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator] ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-collection]] - shared statements and technical atoms: Collection shares source evidence from Served by the Pot: Collections / Iteration and Iterables: All of these actions involve going through the contents one by one. Acting on the elements of a collection one at a time is called iterating over the contents , and ... [truncated]; Collection shares technical record from Served by the Pot: Collections / Iteration and Iterables / ordered collections: const abc = ["a", "b", "c"]; for (const i of abc) { console.log(i) } //=> a b c for (const i of abc) { console.log(i) } //=> a b c (2 shared statement(s), 1 shared atom(s))

### Shared claims

- [[javascriptallonge-composing]] - shared statements: Composing shares source evidence from Composing and Decomposing Data / Self-Similarity / linear recursion: Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and com ... [truncated] (1 shared statement(s))
- [[javascriptallonge-solution]] - shared statements: Solution shares source evidence from Composing and Decomposing Data / Self-Similarity / linear recursion: Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and com ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
