---
page_id: javascriptallonge-iterating
page_kind: concept
summary: topic-concept: 20 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_8e7fdb98655f38e8@c43bf37e4a07c37e2f583bcc939b7bf8
---

# iterating

Source: [[javascriptallonge]]

## Statements

- Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. (javascriptallonge.pdf p.169)
- Nevertheless, there is some value in being able to express some algorithms as iteration. (javascriptallonge.pdf p.169)
- JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. (javascriptallonge.pdf p.169)
- And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 . (javascriptallonge.pdf p.169)
- Notice that buried inside our loop, we have bound the names done and value . (javascriptallonge.pdf p.169)
- We can put those into a POJO (a Plain Old JavaScript Object). (javascriptallonge.pdf p.169)
- The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. (javascriptallonge.pdf p.171)
- Now this is something else. (javascriptallonge.pdf p.171)
- We can write a different iterator for a different data structure. (javascriptallonge.pdf p.171)

## Rules

- Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. (javascriptallonge.pdf p.169)
- We can put those into a POJO (a Plain Old JavaScript Object). (javascriptallonge.pdf p.169)
- The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. (javascriptallonge.pdf p.171)
- We can write a different iterator for a different data structure. (javascriptallonge.pdf p.171)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

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

<a id="atom-2"></a>
**Atom:** code block

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

<a id="atom-3"></a>
**Atom:** code block

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

<a id="atom-4"></a>
**Atom:** code block

```
sum += eachIteration.value;
}
return sum;
}
iteratorSum(arrayIterator([1, 4, 9, 16, 25]))
//=> 55
```

<a id="atom-5"></a>
**Atom:** code block

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

<a id="atom-6"></a>
**Atom:** code block

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


## Related pages

- [[javascriptallonge-unfolding-and-laziness]] - contextualizes: source-supported topic dependency
