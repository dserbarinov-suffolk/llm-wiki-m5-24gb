---
page_id: javascriptallonge-write
page_kind: concept
summary: Write: 9 statement(s) and 6 atom(s) from raw/javascriptallonge.pdf.
page_family: broad-topic
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-write@ffc312bf09e649784040d8ca14b1e20f
---

# Write

What [[javascriptallonge]] covers about write:

## Statements

### That Constant Coffee Craving / const

- Another way to write our 'circumference' function would be to pass PI along with the diameter argument, something like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00400))_

### Recipes with Basic Functions / Unary

- Wecould write ['1', '2', '3'].map((s) => parseInt(s)) , or we could come up with a decorator to do the job for us: _(javascriptallonge.pdf (source-range-c98ab3e6-00660))_

### Copy on Write / a few utilities / copy-on-write

- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.Wikipedia 73 _(javascriptallonge.pdf (source-range-c98ab3e6-01228))_

- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-c98ab3e6-01230))_

### Recipes with Data / Flip / self-currying flip

- Nowif we write mapWith = flip(map) , we can call mapWith(fn, list) or mapWith(fn)(list) , our choice. _(javascriptallonge.pdf (source-range-c98ab3e6-01441))_

### Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

- If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-c98ab3e6-01513))_

### Served by the Pot: Collections / Iteration and Iterables / iterables

- So, when a standard way to write iterators was added to the JavaScript language, it didn't make sense to use a method like .iterator() for it: That would conflict with existing code. Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator. _(javascriptallonge.pdf (source-range-c98ab3e6-01525))_

### Served by the Pot: Collections / Generating Iterables / state machines / We'll keep it simple:

- Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. _(javascriptallonge.pdf (source-range-c98ab3e6-01628))_

### Served by the Pot: Collections / Generating Iterables / generators and iterables

- Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call. _(javascriptallonge.pdf (source-range-c98ab3e6-01678))_


## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00660))_

> Wecould write ['1', '2', '3'].map((s) => parseInt(s)) , or we could come up with a decorator to do the job for us:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00661))_

<a id="atom-technical-atom-2cf055315b880cc0"></a>
```
const unary = (fn) =>
fn.length === 1
? fn
: function (something) {
return fn.call(this, something)
}
```

### Technical frame 2: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00660))_

> Wecould write ['1', '2', '3'].map((s) => parseInt(s)) , or we could come up with a decorator to do the job for us:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00663))_

<a id="atom-technical-atom-be76c990a2f932f1"></a>
```
['1', '2', '3'].map(unary(parseInt))
//=> [1, 2, 3]
```

### Technical frame 3: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

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


## Related pages

### Shared technical atoms

- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from Served by the Pot: Collections / Generating Iterables / generators and iterables: Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of r ... [truncated]; Object shares technical record from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: const collectionSum = (collection) => { const iterator = collection.iterator(); let eachIteration, sum = 0; while ((eachIteration = iterator(), !eachIteration.done)) ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-functional-iterator]] - shared statements and technical atoms: Functional Iterators shares source evidence from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an ... [truncated]; Functional Iterators shares technical record from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: const collectionSum = (collection) => { const iterator = collection.iterator(); let eachIteration, sum = 0; while ((eachIteration = iterator(), !eachIteration.done)) ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements and technical atoms: Iterator shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterables: So, when a standard way to write iterators was added to the JavaScript language, it didn't make sense to use a method like .iterator() for it: That would conflict wi ... [truncated]; Iterator shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Served by the Pot: Collections / Generating Iterables / generators and iterables: Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of r ... [truncated]; Javascript shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from Served by the Pot: Collections / Generating Iterables / generators and iterables: Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of r ... [truncated]; Return shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-doesn-t-work-because-parseint]] - shared technical atoms: Doesn'T Work Because Parseint shares technical record from Recipes with Basic Functions / Unary: const unary = (fn) => fn.length === 1 ? fn : function (something) { return fn.call(this, something) } (1 shared atom(s))
- [[javascriptallonge-generator]] - shared technical atoms: Generator shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared atom(s))
- [[javascriptallonge-iteration]] - shared technical atoms: Iteration shares technical record from Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: const collectionSum = (collection) => { const iterator = collection.iterator(); let eachIteration, sum = 0; while ((eachIteration = iterator(), !eachIteration.done)) ... [truncated] (1 shared atom(s))

### Shared claims

- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from Copy on Write / a few utilities / copy-on-write: Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) c ... [truncated] (2 shared statement(s))
- [[javascriptallonge-pattern]] - shared statements: Pattern shares source evidence from Copy on Write / a few utilities / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))

### Topics

- [[javascriptallonge-copy-write]] - narrower topic: Copy on Write shares source evidence from Copy on Write / a few utilities / copy-on-write: Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) c ... [truncated] (2 shared statement(s))

## Source

- [[javascriptallonge]]
