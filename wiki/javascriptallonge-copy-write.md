---
page_id: javascriptallonge-copy-write
page_kind: concept
summary: Copy on Write: 120 statement(s) and 63 atom(s) from raw/javascriptallonge.pdf.
page_family: broad-topic
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-copy-write@8c08f636595bbf9b3ec842e67af3a509
---

# Copy on Write

What [[javascriptallonge]] covers about copy on write:

## Statements

### Copy on Write

- We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: _(javascriptallonge.pdf (source-range-c98ab3e6-01200))_

- When you take the rest of an array with destructuring ( [first, ...rest] ), you are given a copy of the elements of the array. _(javascriptallonge.pdf (source-range-c98ab3e6-01201))_

- When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list. _(javascriptallonge.pdf (source-range-c98ab3e6-01202))_

### Copy on Write / a few utilities

- Our new at and set functions behave similarly to array[index] and array[index] = value . The main difference is that array[index] = value evaluates to value , while set(index, value, list) evaluates to the modified list . _(javascriptallonge.pdf (source-range-c98ab3e6-01212))_

### Copy on Write / a few utilities / copy-on-read

- So back to the problem of structure sharing. One strategy for avoiding problems is to be pessimistic . Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-c98ab3e6-01214))_

- This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely. _(javascriptallonge.pdf (source-range-c98ab3e6-01216))_

- As we expected, making a copy lets us modify the copy without interfering with the original. This is, however, expensive. Sometimes we don't need to make a copy because we won't be modifying the list. Our mapWith function would be very expensive if we make a copy every time we call rest(node) . _(javascriptallonge.pdf (source-range-c98ab3e6-01217))_

### Copy on Write / a few utilities / copy-on-write

- But our new parent and child lists are copies that contain the desired modifications, without interfering with each other: _(javascriptallonge.pdf (source-range-c98ab3e6-01224))_

- And now functions like mapWith that make copies without modifying anything, work at full speed. _(javascriptallonge.pdf (source-range-c98ab3e6-01226))_

- This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' _(javascriptallonge.pdf (source-range-c98ab3e6-01227))_

### Copy on Write / Tortoises, Hares, and Teleporting Turtles

- A good long while ago (The First Age of Internet Startups), someone asked me one of those pet algorithm questions. It was, 'Write an algorithm to detect a loop in a linked list, in constant space.' _(javascriptallonge.pdf (source-range-c98ab3e6-01233))_

- I think I told him that I was trying to figure out if I could adapt a hashing algorithm such as XORing everything together. This is the 'trick answer' to a question about finding a missing integer from a list, so I was trying the old, 'Transform this into a problem you've already solved 74 ' meta-algorithm. We moved on from there, and he didn't reveal the 'solution.' _(javascriptallonge.pdf (source-range-c98ab3e6-01235))_

- I went home and pondered the problem. I wanted to solve it. Eventually, I came up with something and tried it (In Java!) on my home PC. I sent him an email sharing my result, to demonstrate my ability to follow through. I then forgot about it for a while. Some time later, I was told that the correct solution was: _(javascriptallonge.pdf (source-range-c98ab3e6-01236))_

### Copy on Write / Functional Iterators

- The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays. _(javascriptallonge.pdf (source-range-c98ab3e6-01251))_

- Well, we call arraySum with an array, and it has baked into it a method for traversing the array. Perhaps we could extract both of those things. Let's rearrange our code a bit: _(javascriptallonge.pdf (source-range-c98ab3e6-01253))_

- What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable. _(javascriptallonge.pdf (source-range-c98ab3e6-01255))_

### Copy on Write / Functional Iterators / iterating

- Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. Nevertheless, there is some value in being able to express some algorithms as iteration. _(javascriptallonge.pdf (source-range-c98ab3e6-01260))_

- JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. Summing the elements of an array can be accomplished with: _(javascriptallonge.pdf (source-range-c98ab3e6-01261))_

- Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 . _(javascriptallonge.pdf (source-range-c98ab3e6-01263))_

### Copy on Write / Functional Iterators / unfolding and laziness

- Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let's consider the simplest example: _(javascriptallonge.pdf (source-range-c98ab3e6-01274))_

- A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators. _(javascriptallonge.pdf (source-range-c98ab3e6-01278))_

- This business of going on forever has some drawbacks. Let's introduce an idea: A function that takes an iterator and returns another iterator. We can start with take , an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-c98ab3e6-01282))_

### Copy on Write / Functional Iterators / bonus

- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-c98ab3e6-01291))_

- This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like: _(javascriptallonge.pdf (source-range-c98ab3e6-01294))_

- JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy. _(javascriptallonge.pdf (source-range-c98ab3e6-01296))_

### Copy on Write / Functional Iterators / caveat

- Please note that unlike most of the other functions discussed in this book, iterators are stateful . There are some important implications of stateful functions. One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. So as you traverse the new decorator, you're changing the state of the original! _(javascriptallonge.pdf (source-range-c98ab3e6-01298))_

- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-c98ab3e6-01299))_

### Copy on Write / Making Data Out Of Functions

- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-c98ab3e6-01302))_

- A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations. They searched for a radically simpler set of tools that could accomplish all of the same things. _(javascriptallonge.pdf (source-range-c98ab3e6-01304))_

- They established that arbitrary computations could be represented a small set of axiomatic components. For example, we don't need arrays to represent lists, or even POJOs to represent nodes in a linked list. We can model lists just using functions. _(javascriptallonge.pdf (source-range-c98ab3e6-01305))_

### Copy on Write / Making Data Out Of Functions / the kestrel and the idiot

- A constant function is a function that always returns the same thing, no matter what you give it. For example, (x) => 42 is a constant function that always evaluates to 42. The kestrel, or K , is a function that makes constant functions. You give it a value, and it returns a constant function that gives that value. _(javascriptallonge.pdf (source-range-c98ab3e6-01312))_

- The identity function is a function that evaluates to whatever parameter you pass it. So I(42) => 42 . Very simple, but useful. Now we'll take it one more step forward: Passing a value to K gets a function back, and passing a value to that function gets us a value. _(javascriptallonge.pdf (source-range-c98ab3e6-01315))_

- This is very interesting. Given two values, we can say that K always returns the first value: K(x)(y) => x (that's not valid JavaScript, but it's essentially how it works). _(javascriptallonge.pdf (source-range-c98ab3e6-01318))_

### Copy on Write / Making Data Out Of Functions / backwardness

- Our first and second functions are a little different than what most people are used to when we talk about functions that access data. If we represented a pair of values as an array, we'd write them like this: _(javascriptallonge.pdf (source-range-c98ab3e6-01328))_

- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it. _(javascriptallonge.pdf (source-range-c98ab3e6-01332))_

- But the first and second we built out of K and I don't work that way. You call them and pass them the bits, and they choose what to return. So if we wanted to use them with a two-element array, we'd need to have a piece of code that calls some code. _(javascriptallonge.pdf (source-range-c98ab3e6-01333))_

### Copy on Write / Making Data Out Of Functions / the vireo

- Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data. For arrays, we'd write cons = (first, second) => [first, second] . For objects we'd write: cons = (first, second) => {first, second} . In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-c98ab3e6-01338))_

- For 'data' we access with K and K(I) , our 'structure' is the function (selector) => selector("primus")("secundus") . Let's extract those into parameters: _(javascriptallonge.pdf (source-range-c98ab3e6-01339))_

- For consistency with the way combinators are written as functions taking just one parameter, we'll curry 78 the function: _(javascriptallonge.pdf (source-range-c98ab3e6-01341))_

### Copy on Write / Making Data Out Of Functions / lists with functions as data

- Here's another look at linked lists using POJOs. We use the term rest instead of second , but it's otherwise identical to what we have above: _(javascriptallonge.pdf (source-range-c98ab3e6-01351))_

- Presto, we can use pure functions to represent a linked list . And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else. _(javascriptallonge.pdf (source-range-c98ab3e6-01359))_

- We used functions to replace arrays and POJOs, but we still use JavaScript's built-in operators to test for equality ( === ) and to branch ?: . _(javascriptallonge.pdf (source-range-c98ab3e6-01361))_

### Copy on Write / Making Data Out Of Functions / say 'please'

- Wekeep using the same pattern in our functions: aPair === EMPTY ? doSomething : doSomethingElse . This follows the philosophy we used with data structures: The function doing the work inspects the data structure. _(javascriptallonge.pdf (source-range-c98ab3e6-01363))_

- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. Here's length again: _(javascriptallonge.pdf (source-range-c98ab3e6-01364))_

- Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. So let's disambiguate our names: _(javascriptallonge.pdf (source-range-c98ab3e6-01368))_

### Copy on Write / Making Data Out Of Functions / functions are not the real point

- There are lots of similar texts explaining how to construct complex semantics out of functions. You can establish that K and K(I) can represent true and false , model magnitudes with Church Numerals 79 or Surreal Numbers 80 , and build your way up to printing FizzBuzz. _(javascriptallonge.pdf (source-range-c98ab3e6-01375))_

- Functions are a fundamental building block of computation. They are 'axioms' of combinatory logic, and can be used to compute anything that JavaScript can compute. _(javascriptallonge.pdf (source-range-c98ab3e6-01377))_

- However, that is not the interesting thing to note here. Practically speaking, languages like JavaScript already provide arrays with mapping and folding methods, choice operations, and other rich constructs. Knowing how to make a linked list out of functions is not really necessary for the working programmer. (Knowing that it can be done, on the other hand, is very important to understanding computer science.) _(javascriptallonge.pdf (source-range-c98ab3e6-01378))_

### Copy on Write / Making Data Out Of Functions / a return to backward thinking

- To make pairs work, we did things backwards , we passed the first and rest functions to the pair, and the pair called our function. As it happened, the pair was composed by the vireo (or V combinator): (x) => (y) => (z) => z(x)(y) . _(javascriptallonge.pdf (source-range-c98ab3e6-01383))_

- But we could have done something completely different. We could have written a pair that stored its elements in an array, or a pair that stored its elements in a POJO. All we know is that we can pass the pair function a function of our own, at it will be called with the elements of the pair. _(javascriptallonge.pdf (source-range-c98ab3e6-01384))_

- The exact implementation of a pair is hidden from the code that uses a pair. Here, we'll prove it: _(javascriptallonge.pdf (source-range-c98ab3e6-01385))_

- And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-c98ab3e6-01203))_
- If we know that a list doesn't share any elements with another list, we can safely modify it. _(javascriptallonge.pdf (source-range-c98ab3e6-01207))_
- We'll end up reinventing reference counting and garbage collection. _(javascriptallonge.pdf (source-range-c98ab3e6-01207))_
- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.Wikipedia 73 _(javascriptallonge.pdf (source-range-c98ab3e6-01228))_
- Like all strategies, it makes a tradeoff: It's much cheaper than pessimistically copying structures when you make an infrequent number of small changes, but if you tend to make a lot of changes to some that you aren't sharing, it's more expensive. _(javascriptallonge.pdf (source-range-c98ab3e6-01229))_
- Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-c98ab3e6-01230))_
- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. _(javascriptallonge.pdf (source-range-c98ab3e6-01230))_
- No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you'll detect the loop. _(javascriptallonge.pdf (source-range-c98ab3e6-01240))_
- You have two node references, and one traverses the list at twice the speed of the other. _(javascriptallonge.pdf (source-range-c98ab3e6-01240))_
- It seems to be faster under certain circumstances, depending on the size of the loop and the relative costs of certain operations. _(javascriptallonge.pdf (source-range-c98ab3e6-01243))_
- What's interesting about these two algorithms is that they both tangle two separate concerns: How to traverse a data structure, and what to do with the elements that you encounter. _(javascriptallonge.pdf (source-range-c98ab3e6-01244))_
- Notice that buried inside our loop, we have bound the names done and value . _(javascriptallonge.pdf (source-range-c98ab3e6-01266))_
- We can put those into a POJO (a Plain Old JavaScript Object). _(javascriptallonge.pdf (source-range-c98ab3e6-01266))_
- The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. _(javascriptallonge.pdf (source-range-c98ab3e6-01269))_
- Now this is something else. _(javascriptallonge.pdf (source-range-c98ab3e6-01269))_
- We can write a different iterator for a different data structure. _(javascriptallonge.pdf (source-range-c98ab3e6-01270))_
- We'll need an iterator that produces odd numbers. _(javascriptallonge.pdf (source-range-c98ab3e6-01284))_
- Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions. _(javascriptallonge.pdf (source-range-c98ab3e6-01289))_
- The oscin.es 77 library contains code for all of the standard combinators and for experimenting using the standard notation. _(javascriptallonge.pdf (source-range-c98ab3e6-01307))_
- Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value. _(javascriptallonge.pdf (source-range-c98ab3e6-01326))_
- Our latin data structure is no longer a dumb data structure, it's a function. _(javascriptallonge.pdf (source-range-c98ab3e6-01336))_
- As an aside, the Vireo is a little like JavaScript's .apply function. _(javascriptallonge.pdf (source-range-c98ab3e6-01348))_
- It is known to most programmers as .tap . _(javascriptallonge.pdf (source-range-c98ab3e6-01348))_
- One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. _(javascriptallonge.pdf (source-range-c98ab3e6-01348))_
- We can write reverse and mapWith as well. _(javascriptallonge.pdf (source-range-c98ab3e6-01371))_
- We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else. _(javascriptallonge.pdf (source-range-c98ab3e6-01373))_
- Knowing how to make a list out of just functions is a little like knowing that photons are the Gauge Bosons 81 of the electromagnetic force. _(javascriptallonge.pdf (source-range-c98ab3e6-01379))_
- This is a little gratuitous, but it makes the point: The code that uses the data doesn't reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. _(javascriptallonge.pdf (source-range-c98ab3e6-01387))_
- We're passing list what we want done with an empty list, and what we want done with a list that has at least one element. _(javascriptallonge.pdf (source-range-c98ab3e6-01390))_
- We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-c98ab3e6-01390))_
- We can fix this with an isEmpty function, but now we're pushing even more knowledge about the structure of lists into the code that uses them. _(javascriptallonge.pdf (source-range-c98ab3e6-01393))_
- It presumes you can compare these things with the === operator. _(javascriptallonge.pdf (source-range-c98ab3e6-01393))_
- This is a fundamental principle of good design. _(javascriptallonge.pdf (source-range-c98ab3e6-01394))_
- Having a list know itself whether it is empty hides implementation information from the code that uses lists. _(javascriptallonge.pdf (source-range-c98ab3e6-01394))_
- It is a tenet of Object-Oriented Programming, but it is not exclusive to OOP: We can and should design data structures to hide implementation information from the code that use them, whether we are working with functions, objects, or both. _(javascriptallonge.pdf (source-range-c98ab3e6-01394))_
- Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. _(javascriptallonge.pdf (source-range-c98ab3e6-01396))_

## Technical atoms

### Technical frame 1: Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01207))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01203))_

<a id="atom-technical-atom-b34cb1ee5a282e9c"></a>
> The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array.

### Technical frame 2: Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01207))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01204))_

<a id="atom-technical-atom-575252d5f4b2c744"></a>
> Whereas if you have a linked list, and you take it's 'rest,' your 'child' list shares its nodes with the 'parent' list.

### Technical frame 3: Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01207))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01206))_

<a id="atom-technical-atom-9e5219ea584e3de1"></a>
```
const parentArray = [1, 2, 3];
const [aFirst, ...childArray] = parentArray;
parentArray[2] = "three";
childArray[0] = "two";
parentArray
//=> [1,2,"three"]
childArray
//=> ["two",3]
const EMPTY = { first: {}, rest: {} };
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
const childList = parentList.rest;
parentList.rest.rest.first = "three";
childList.first = "two";
parentList
//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\
{},"rest":{}}}}}
childList
//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}
```

### Technical frame 4: Copy on Write / a few utilities

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01212))_

> Our new at and set functions behave similarly to array[index] and array[index] = value . The main difference is that array[index] = value evaluates to value , while set(index, value, list) evaluates to the modified list .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01210))_

<a id="atom-technical-atom-9cde04494d451288"></a>
```
const copy = (node, head = null, tail = null) => {
if (node === EMPTY) {
return head;
}
else if (tail === null) {
const { first, rest } = node;
const newNode = { first, rest };
return copy(rest, newNode, newNode);
}
else {
const { first, rest } = node;
const newNode = { first, rest };
tail.rest = newNode;
return copy(node.rest, head, newNode);
}
}
const first = ({first, rest}) => first;
const rest = ({first, rest}) => rest;
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(rest(node), { first: first(node), rest: delayed });
const mapWith = (fn, node, delayed = EMPTY) =>
node === EMPTY
? reverse(delayed)
: mapWith(fn, rest(node), { first: fn(first(node)), rest: delayed });
const at = (index, list) =>
index === 0
? first(list)
: at(index - 1, rest(list));
const set = (index, value, list, originalList = list) =>
index === 0
? (list.first = value, originalList)
: set(index - 1, value, rest(list), originalList)
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
```

### Technical frame 5: Copy on Write / a few utilities

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01212))_

> Our new at and set functions behave similarly to array[index] and array[index] = value . The main difference is that array[index] = value evaluates to value , while set(index, value, list) evaluates to the modified list .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01211))_

<a id="atom-technical-atom-9fe6e0881f198a76"></a>
```
const childList = rest(parentList);
set(2, "three", parentList);
set(0, "two", childList);
parentList
//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\
{},"rest":{}}}}}
childList
//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}
```

### Technical frame 6: Copy on Write / a few utilities / copy-on-read

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01216))_

> This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01215))_

<a id="atom-technical-atom-508e8555d6dcf86c"></a>
```
const rest = ({first, rest}) => copy(rest);
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
const childList = rest(parentList);
const newParentList = set(2, "three", parentList);
set(0, "two", childList);
parentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\
rest":{}}}}}
childList
//=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

### Technical frame 7: Copy on Write / a few utilities / copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01224))_

> But our new parent and child lists are copies that contain the desired modifications, without interfering with each other:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01221))_

<a id="atom-technical-atom-fca227d571ee90b1"></a>
```
const rest = ({first, rest}) => rest;
const set = (index, value, list) =>
index === 0
? { first: value, rest: list.rest }
: { first: list.first, rest: set(index - 1, value, list.rest) };
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
const childList = rest(parentList);
const newParentList = set(2, "three", parentList);
const newChildList = set(0, "two", childList);
```

### Technical frame 8: Copy on Write / a few utilities / copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01224))_

> But our new parent and child lists are copies that contain the desired modifications, without interfering with each other:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01223))_

<a id="atom-technical-atom-77bddd22e842f0e0"></a>
```
parentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{"first":{},"rest":\
{}}}}}
childList
//=> {"first":2,"rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

### Technical frame 9: Copy on Write / a few utilities / copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01226))_

> And now functions like mapWith that make copies without modifying anything, work at full speed.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01225))_

<a id="atom-technical-atom-c80cb4a840bade48"></a>
```
newParentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\
rest":{}}}}}
newChildList
//=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

### Technical frame 10: Copy on Write / Tortoises, Hares, and Teleporting Turtles

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01240))_

> This algorithm is called 'The Tortoise and the Hare,' and was discovered by Robert Floyd in the 1960s. You have two node references, and one traverses the list at twice the speed of the other. No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you'll detect the loop.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01237))_

<a id="atom-technical-atom-06b047f12ccc23f1"></a>
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
const forceAppend = (list1, list2) => {
if (isEmpty(list1)) {
return "FAIL!"
}
if (isEmpty(list1.rest)) {
list1.rest = list2;
}
else {
forceAppend(list1.rest, list2);
```

### Technical frame 11: Copy on Write / Tortoises, Hares, and Teleporting Turtles

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01240))_

> This algorithm is called 'The Tortoise and the Hare,' and was discovered by Robert Floyd in the 1960s. You have two node references, and one traverses the list at twice the speed of the other. No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you'll detect the loop.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01239))_

<a id="atom-technical-atom-fc22e3e01a4b8455"></a>
```
}
}
const tortoiseAndHare = (aPair) => {
let tortoisePair = aPair,
harePair = aPair.rest;
while (true) {
if (isEmpty(tortoisePair) || isEmpty(harePair)) {
return false;
}
if (tortoisePair.first === harePair.first) {
return true;
}
harePair = harePair.rest;
if (isEmpty(harePair)) {
return false;
}
if (tortoisePair.first === harePair.first) {
return true;
}
tortoisePair = tortoisePair.rest;
harePair = harePair.rest;
}
};
const aList = list(1, 2, 3, 4, 5);
tortoiseAndHare(aList)
//=> false
forceAppend(aList, aList.rest.rest);
tortoiseAndHare(aList);
//=> true
```

### Technical frame 12: Copy on Write / Tortoises, Hares, and Teleporting Turtles

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01243))_

> Years later, I came across a discussion of this algorithm, The Tale of the Teleporting Turtle 75 . It seems to be faster under certain circumstances, depending on the size of the loop and the relative costs of certain operations.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01242))_

<a id="atom-technical-atom-9ffc2add1759b43a"></a>
```
const teleportingTurtle = (list) => {
let speed = 1,
rabbit = list,
turtle = rabbit;
while (true) {
for (let i = 0; i <= speed; i += 1) {
rabbit = rabbit.rest;
if (rabbit == null) {
return false;
}
if (rabbit === turtle) {
return true;
}
}
turtle = rabbit;
speed *= 2;
}
return false;
};
const aList = list(1, 2, 3, 4, 5);
teleportingTurtle(aList)
//=> false
forceAppend(aList, aList.rest.rest);
teleportingTurtle(aList);
//=> true
```

### Technical frame 13: Copy on Write / Functional Iterators

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

### Technical frame 14: Copy on Write / Functional Iterators

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

### Technical frame 15: Copy on Write / Functional Iterators

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

### Technical frame 16: Copy on Write / Functional Iterators

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

### Technical frame 17: Copy on Write / Functional Iterators / iterating

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

### Technical frame 18: Copy on Write / Functional Iterators / iterating

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

### Technical frame 19: Copy on Write / Functional Iterators / iterating

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

### Technical frame 20: Copy on Write / Functional Iterators / iterating

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

### Technical frame 21: Copy on Write / Functional Iterators / iterating

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

### Technical frame 22: Copy on Write / Functional Iterators / iterating

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

### Technical frame 23: Copy on Write / Functional Iterators / unfolding and laziness

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

### Technical frame 24: Copy on Write / Functional Iterators / unfolding and laziness

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

### Technical frame 25: Copy on Write / Functional Iterators / unfolding and laziness

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

### Technical frame 26: Copy on Write / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01282))_

> This business of going on forever has some drawbacks. Let's introduce an idea: A function that takes an iterator and returns another iterator. We can start with take , an easy function that returns an iterator that only returns a fixed number of elements:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01281))_

<a id="atom-technical-atom-b8970c6b291f5037"></a>
```
//=> 4
squares().value
//=> 9
```

### Technical frame 27: Copy on Write / Functional Iterators / unfolding and laziness

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

### Technical frame 28: Copy on Write / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01289))_

> Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01285))_

<a id="atom-technical-atom-3cbb0179c9f157ad"></a>
```
const odds = () => {
```

### Technical frame 29: Copy on Write / Functional Iterators / unfolding and laziness

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

### Technical frame 30: Copy on Write / Functional Iterators / unfolding and laziness

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

### Technical frame 31: Copy on Write / Functional Iterators / bonus

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01294))_

> This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01293))_

<a id="atom-technical-atom-da3ef04aced8adf4"></a>
```
const firstInIteration = (fn, iterator) =>
take(filterIteratorWith(fn, iterator), 1);
```

### Technical frame 32: Copy on Write / Functional Iterators / bonus

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01296))_

> JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01295))_

<a id="atom-technical-atom-305b589bdbaf0a36"></a>
```
const firstInArray = (fn, array) =>
array.filter(fn)[0];
```

### Technical frame 33: Copy on Write / Making Data Out Of Functions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01304))_

> A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations. They searched for a radically simpler set of tools that could accomplish all of the same things.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01303))_

<a id="atom-technical-atom-99dd059e4394fcc2"></a>
```
const EMPTY = {};
const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \
} } };
OneTwoThree.first
//=> 1
OneTwoThree.rest.first
//=> 2
OneTwoThree.rest.rest.first
//=> 3
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
length(OneTwoThree)
//=> 3
```

### Technical frame 34: Copy on Write / Making Data Out Of Functions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01305))_

> They established that arbitrary computations could be represented a small set of axiomatic components. For example, we don't need arrays to represent lists, or even POJOs to represent nodes in a linked list. We can model lists just using functions.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01309))_

<a id="atom-technical-atom-268f5812c47797c2"></a>
```text
76 http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422
77 http://oscin.es
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 76 | http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422 |
| 77 | http://oscin.es |

</details>

### Technical frame 35: Copy on Write / Making Data Out Of Functions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01307))_

> The oscin.es 77 library contains code for all of the standard combinators and for experimenting using the standard notation.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01310))_

<a id="atom-technical-atom-401769bef055ddca"></a>
```
const K = (x) => (y) => x;
const I = (x) => (x);
const V = (x) => (y) => (z) => z(x)(y);
```

### Technical frame 36: Copy on Write / Making Data Out Of Functions / the kestrel and the idiot

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01315))_

> The identity function is a function that evaluates to whatever parameter you pass it. So I(42) => 42 . Very simple, but useful. Now we'll take it one more step forward: Passing a value to K gets a function back, and passing a value to that function gets us a value.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01314))_

<a id="atom-technical-atom-40cf6e0c70a45cfc"></a>
```
const K = (x) => (y) => x;
const fortyTwo = K(42);
fortyTwo(6)
//=> 42
fortyTwo("Hello")
//=> 42
```

### Technical frame 37: Copy on Write / Making Data Out Of Functions / the kestrel and the idiot

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01318))_

> This is very interesting. Given two values, we can say that K always returns the first value: K(x)(y) => x (that's not valid JavaScript, but it's essentially how it works).

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01317))_

<a id="atom-technical-atom-f9cfbf2e862f853d"></a>
```
K(6)(7)
//=> 6
K(12)(24)
//=> 12
```

### Technical frame 38: Copy on Write / Making Data Out Of Functions / the kestrel and the idiot

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01326))_

> This is very interesting. Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01320))_

<a id="atom-technical-atom-ca77fb093f56d6ad"></a>
```
Therefore, K(I)(x)(y) => y:
```

### Technical frame 39: Copy on Write / Making Data Out Of Functions / the kestrel and the idiot

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01326))_

> This is very interesting. Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01321))_

<a id="atom-technical-atom-caa80955fd72f20a"></a>
```
K(I)(6)(7)
//=> 7
K(I)(12)(24)
//=> 24
```

### Technical frame 40: Copy on Write / Making Data Out Of Functions / the kestrel and the idiot

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01326))_

> This is very interesting. Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01323))_

<a id="atom-technical-atom-f53de75b3c44bed7"></a>
```
K("primus")("secundus")
//=> "primus"
K(I)("primus")("secundus")
//=> "secundus"
```

### Technical frame 41: Copy on Write / Making Data Out Of Functions / the kestrel and the idiot

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01326))_

> This is very interesting. Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01325))_

<a id="atom-technical-atom-3ee76c35ee226b51"></a>
```
const first = K,
second = K(I);
first("primus")("secundus")
//=> "primus"
second("primus")("secundus")
//=> "secundus"
```

### Technical frame 42: Copy on Write / Making Data Out Of Functions / backwardness

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01332))_

> In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01329))_

<a id="atom-technical-atom-66fc28ff3c959742"></a>
```
const first = ([first, second]) => first,
second = ([first, second]) => second;
const latin = ["primus", "secundus"];
first(latin)
//=> "primus"
second(latin)
//=> "secundus"
```

### Technical frame 43: Copy on Write / Making Data Out Of Functions / backwardness

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01332))_

> In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01331))_

<a id="atom-technical-atom-40d16bc114058bd1"></a>
```
const first = ({first, second}) => first,
second = ({first, second}) => second;
const latin = {first: "primus", second: "secundus"};
first(latin)
//=> "primus"
second(latin)
//=> "secundus"
```

### Technical frame 44: Copy on Write / Making Data Out Of Functions / backwardness

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01336))_

> Our latin data structure is no longer a dumb data structure, it's a function. And instead of passing latin to first or second , we pass first or second to latin . It's exactly backwards of the way we write functions that operate on data.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01335))_

<a id="atom-technical-atom-29b6a9211342a231"></a>
```
const first = K,
second = K(I);
const latin = (selector) => selector("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```

### Technical frame 45: Copy on Write / Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01341))_

> For consistency with the way combinators are written as functions taking just one parameter, we'll curry 78 the function:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01340))_

<a id="atom-technical-atom-590de5a88990b16d"></a>
```
(first, second) => (selector) => selector(first)(second)
```

### Technical frame 46: Copy on Write / Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01348))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01342))_

<a id="atom-technical-atom-1e1971c4388c6edb"></a>
```
(first) => (second) => (selector) => selector(first)(second)
```

### Technical frame 47: Copy on Write / Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01348))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01344))_

<a id="atom-technical-atom-6e9fd7c9270a7ba7"></a>
```
const first = K,
second = K(I),
pair = (first) => (second) => (selector) => selector(first)(second);
const latin = pair("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```

### Technical frame 48: Copy on Write / Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01348))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01345))_

<a id="atom-technical-atom-136eb8fe93527eb9"></a>
> If we change the names to x , y , and z , we get: (x) => (y) => (z) => z(x)(y) .

### Technical frame 49: Copy on Write / Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01348))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01347))_

<a id="atom-technical-atom-8b9f5d9d19ad1665"></a>
```
const first = K,
second = K(I),
pair = V;
const latin = pair("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```

### Technical frame 50: Copy on Write / Making Data Out Of Functions / lists with functions as data

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01359))_

> Presto, we can use pure functions to represent a linked list . And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01352))_

<a id="atom-technical-atom-8e8868472de89338"></a>
```
const first = ({first, rest}) => first,
rest
= ({first, rest}) => rest,
pair = (first, rest) => ({first, rest}),
EMPTY = ({});
const l123 = pair(1, pair(2, pair(3, EMPTY)));
first(l123)
//=> 1
first(rest(l123))
//=> 2
first(rest(rest(l123)))
//=3
```

### Technical frame 51: Copy on Write / Making Data Out Of Functions / lists with functions as data

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01359))_

> Presto, we can use pure functions to represent a linked list . And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01354))_

<a id="atom-technical-atom-674bd1bfff03f2e3"></a>
```
const length = (aPair) =>
aPair === EMPTY
? 0
: 1 + length(rest(aPair));
length(l123)
//=> 3
const reverse = (aPair, delayed = EMPTY) =>
aPair === EMPTY
? delayed
: reverse(rest(aPair), pair(first(aPair), delayed));
const mapWith = (fn, aPair, delayed = EMPTY) =>
aPair === EMPTY
? reverse(delayed)
: mapWith(fn, rest(aPair), pair(fn(first(aPair)), delayed));
const doubled = mapWith((x) => x * 2, l123);
first(doubled)
//=> 2
first(rest(doubled))
//=> 4
first(rest(rest(doubled)))
//=> 6
Can we do the same with the linked lists we build out of functions? Yes:
const first = K,
rest
= K(I),
pair = V,
EMPTY = (() => {});
const l123 = pair(1)(pair(2)(pair(3)(EMPTY)));
```

### Technical frame 52: Copy on Write / Making Data Out Of Functions / lists with functions as data

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01359))_

> Presto, we can use pure functions to represent a linked list . And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01355))_

<a id="atom-technical-atom-57616161c191feed"></a>
```
rest
= K(I),
pair = V,
EMPTY = (() => {});
const l123 = pair(1)(pair(
l123(first)
//=> 1
l123(rest)(first)
```

### Technical frame 53: Copy on Write / Making Data Out Of Functions / lists with functions as data

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01359))_

> Presto, we can use pure functions to represent a linked list . And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01356))_

<a id="atom-technical-atom-dbeee7a78ed8a18e"></a>
```
//=> 2
return l123(rest)(rest)(first)
//=> 3
We write them in a backwards way, but they seem to work. How about
```

### Technical frame 54: Copy on Write / Making Data Out Of Functions / lists with functions as data

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01359))_

> Presto, we can use pure functions to represent a linked list . And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01358))_

<a id="atom-technical-atom-5454fa939bbe1fe7"></a>
```
const length = (aPair) =>
aPair === EMPTY
? 0
: 1 + length(aPair(rest));
length(l123)
//=> 3
And mapWith?
const reverse = (aPair, delayed = EMPTY) =>
aPair === EMPTY
? delayed
: reverse(aPair(rest), pair(aPair(first))(delayed));
const mapWith = (fn, aPair, delayed = EMPTY) =>
aPair === EMPTY
? reverse(delayed)
: mapWith(fn, aPair(rest), pair(fn(aPair(first)))(delayed));
const doubled = mapWith((x) => x * 2, l123)
doubled(first)
//=> 2
doubled(rest)(first)
//=> 4
doubled(rest)(rest)(first)
//=> 6
```

### Technical frame 55: Copy on Write / Making Data Out Of Functions / say 'please'

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01368))_

> Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. So let's disambiguate our names:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01365))_

<a id="atom-technical-atom-a843850e11b45503"></a>
```
const length = (aPair) =>
aPair === EMPTY
? 0
: 1 + length(aPair(rest));
```

### Technical frame 56: Copy on Write / Making Data Out Of Functions / say 'please'

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01368))_

> Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. So let's disambiguate our names:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01367))_

<a id="atom-technical-atom-531fb37422f81400"></a>
```
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(rest)))
);
```

### Technical frame 57: Copy on Write / Making Data Out Of Functions / say 'please'

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01371))_

> We can write reverse and mapWith as well. We aren't being super-strict about emulating combinatory logic, we'll use default parameters:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01369))_

<a id="atom-technical-atom-5ed2d671c286a0c5"></a>
```
const pairFirst = K,
pairRest
= K(I),
pair = V;
const first = (list) => list(
() => "ERROR: Can't take first of an empty list",
(aPair) => aPair(pairFirst)
);
const rest = (list) => list(
```

### Technical frame 58: Copy on Write / Making Data Out Of Functions / say 'please'

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01371))_

> We can write reverse and mapWith as well. We aren't being super-strict about emulating combinatory logic, we'll use default parameters:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01370))_

<a id="atom-technical-atom-e4bdef73b9660258"></a>
```
() => "ERROR: Can't take first of an empty list",
(aPair) => aPair(pairRest)
);
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(pairRest)))
);
We’ll also write a handy list printer:
const print = (list) => list(
() => "",
(aPair) => `${aPair(pairFirst)} ${print(aPair(pairRest))}`
);
How would all this work? Let’s start with the obvious. What is an empty list?
const EMPTYLIST = (whenEmpty, unlessEmpty) => whenEmpty()
And what is a node of a list?
const node = (x) => (y) =>
(whenEmpty, unlessEmpty) => unlessEmpty(pair(x)(y));
Let’s try it:
const l123 = node(1)(node(2)(node(3)(EMPTYLIST)));
print(l123)
//=> 1 2 3
```

### Technical frame 59: Copy on Write / Making Data Out Of Functions / say 'please'

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01373))_

> We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01372))_

<a id="atom-technical-atom-a59b569dddae31b7"></a>
```
const reverse = (list, delayed = EMPTYLIST) => list(
() => delayed,
(aPair) => reverse(aPair(pairRest), node(aPair(pairFirst))(delayed))
);
print(reverse(l123));
//=> 3 2 1
const mapWith = (fn, list, delayed = EMPTYLIST) =>
list(
() => reverse(delayed),
(aPair) => mapWith(fn, aPair(pairRest), node(fn(aPair(pairFirst)))(delayed))
);
print(mapWith(x => x * x, reverse(l123)))
//=> 941
```

### Technical frame 60: Copy on Write / Making Data Out Of Functions / functions are not the real point

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01379))_

> Knowing how to make a list out of just functions is a little like knowing that photons are the Gauge Bosons 81 of the electromagnetic force. It's the QED of physics that underpins the Maxwell's Equations of programming. Deeply important, but not practical when you're building a bridge.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01380))_

<a id="atom-technical-atom-f2ed9b6962a2b6bc"></a>
```text
79 https://en.wikipedia.org/wiki/Church_encoding
81 https://en.wikipedia.org/wiki/Gauge_boson
80 https://en.wikipedia.org/wiki/Surreal_number
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 79 | https://en.wikipedia.org/wiki/Church_encoding |
| 81 | https://en.wikipedia.org/wiki/Gauge_boson |
| 80 | https://en.wikipedia.org/wiki/Surreal_number |

</details>

### Technical frame 61: Copy on Write / Making Data Out Of Functions / a return to backward thinking

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01387))_

> This is a little gratuitous, but it makes the point: The code that uses the data doesn't reach in and touch it: The code that uses the data provides some code and asks the data to do something with it.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01386))_

<a id="atom-technical-atom-158c298e9a01c3e8"></a>
```
const first = K,
second = K(I),
pair = (first) => (second) => {
const pojo = {first, second};
return (selector) => selector(pojo.first)(pojo.second);
};
const latin = pair("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```

### Technical frame 62: Copy on Write / Making Data Out Of Functions / a return to backward thinking

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01390))_

> We're passing list what we want done with an empty list, and what we want done with a list that has at least one element. We then ask list to do it, and provide a way for list to call the code we pass in.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01389))_

<a id="atom-technical-atom-207bb06cb1ba7fd3"></a>
```
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(pairRest)))
);
```

### Technical frame 63: Copy on Write / Making Data Out Of Functions / a return to backward thinking

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01393))_

> The line node === EMPTY presumes a lot of things. It presumes there is one canonical empty list value. It presumes you can compare these things with the === operator. We can fix this with an isEmpty function, but now we're pushing even more knowledge about the structure of lists into the code that uses them.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01392))_

<a id="atom-technical-atom-6a8e1866f0055ff3"></a>
```
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
```


## Related pages

### Source structure

- [[javascriptallonge-section-copy-on-write-d081f846]] - source section: Copy on Write shares source evidence from Copy on Write: We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them:; Copy on Write shares technical record from Copy on Write: The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. (120 shared statement(s), 63 shared atom(s))
- [[javascriptallonge-section-copy-on-write-a-few-utilities-copy-on-write-db9192e0]] - source section: Copy on Write / a few utilities / copy-on-write shares source evidence from Copy on Write / a few utilities / copy-on-write: But our new parent and child lists are copies that contain the desired modifications, without interfering with each other:; Copy on Write / a few utilities / copy-on-write shares technical record from Copy on Write / a few utilities / copy-on-write: const rest = ({first, rest}) => rest; const set = (index, value, list) => index === 0 ? { first: value, rest: list.rest } : { first: list.first, rest: set(index - 1, ... [truncated] (7 shared statement(s), 3 shared atom(s))

### Shared technical atoms

- [[javascriptallonge-functional-iterator]] - shared statements and technical atoms: Functional Iterators shares source evidence from Copy on Write / Functional Iterators: The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still re ... [truncated]; Functional Iterators shares technical record from Copy on Write / Functional Iterators: const arraySum = ([first, ...rest], accumulator = 0) => first === undefined ? accumulator : arraySum(rest, first + accumulator) arraySum([1, 4, 9, 16, 25]) //=> 55 (31 shared statement(s), 20 shared atom(s))
- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from Copy on Write: We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them:; List shares technical record from Copy on Write: The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. (7 shared statement(s), 19 shared atom(s))
- [[javascriptallonge-data]] - shared statements and technical atoms: Data shares source evidence from Copy on Write / Functional Iterators: What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function do ... [truncated]; Data shares technical record from Copy on Write / Functional Iterators / iterating: const EMPTY = null; const isEmpty = (node) => node === EMPTY; const pair = (first, rest = EMPTY) => ({first, rest}); const list = (...elements) => { const [first, .. ... [truncated] (5 shared statement(s), 9 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms: Element shares source evidence from Copy on Write: This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunc ... [truncated]; Element shares technical record from Copy on Write: The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. (2 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements and technical atoms: Iterator shares source evidence from Copy on Write / Functional Iterators / unfolding and laziness: Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions.; Iterator shares technical record from Copy on Write / Functional Iterators / unfolding and laziness: const NumberIterator = (number = 0) => () => ({ done: false, value: number++ }) fromOne = NumberIterator(1); fromOne().value; //=> 1 fromOne().value; //=> 2 fromOne( ... [truncated] (2 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Copy on Write / Functional Iterators / iterating: JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. Summing the elements of an array can be accomplished with:; Javascript shares technical record from Copy on Write / Functional Iterators / iterating: const arraySum = (array) => { let sum = 0; for (let i = 0; i < array.length; ++i) { sum += array[i]; } return sum } arraySum([1, 4, 9, 16, 25]) //=> 55 (4 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-structure]] - shared statements and technical atoms: Structure shares source evidence from Copy on Write / Functional Iterators: What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function do ... [truncated]; Structure shares technical record from Copy on Write / Functional Iterators / iterating: const EMPTY = null; const isEmpty = (node) => node === EMPTY; const pair = (first, rest = EMPTY) => ({first, rest}); const list = (...elements) => { const [first, .. ... [truncated] (3 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-parameter]] - shared statements and technical atoms: Parameter shares source evidence from Copy on Write / Making Data Out Of Functions / the vireo: Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data. ... [truncated]; Parameter shares technical record from Copy on Write / Making Data Out Of Functions / the vireo: (first, second) => (selector) => selector(first)(second) (1 shared statement(s), 2 shared atom(s))

### Shared claims

- [[javascriptallonge-return]] - shared statements: Return shares source evidence from Copy on Write / Functional Iterators / iterating: Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iterator ... [truncated] (2 shared statement(s))
- [[javascriptallonge-kestrel]] - shared statements: Kestrel shares source evidence from Copy on Write / Making Data Out Of Functions / the kestrel and the idiot: A constant function is a function that always returns the same thing, no matter what you give it. For example, (x) => 42 is a constant function that always evaluates ... [truncated] (1 shared statement(s))
- [[javascriptallonge-pattern]] - shared statements: Pattern shares source evidence from Copy on Write / a few utilities / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))

### Topics

- [[javascriptallonge-copy]] - broader topic: Copy shares source evidence from Copy on Write / a few utilities / copy-on-write: This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:'; Copy shares technical record from Copy on Write / a few utilities / copy-on-write: const rest = ({first, rest}) => rest; const set = (index, value, list) => index === 0 ? { first: value, rest: list.rest } : { first: list.first, rest: set(index - 1, ... [truncated] (3 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-write]] - broader topic: Write shares source evidence from Copy on Write / a few utilities / copy-on-write: Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) c ... [truncated]; Write shares technical record from Copy on Write / Making Data Out Of Functions: 76 http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422 77 http://oscin.es (2 shared statement(s), 2 shared atom(s))

## Source

- [[javascriptallonge]]
