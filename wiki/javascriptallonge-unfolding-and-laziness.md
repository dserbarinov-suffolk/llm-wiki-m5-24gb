---
page_id: javascriptallonge-unfolding-and-laziness
page_kind: concept
summary: unfolding and laziness: 6 accepted assertion(s) and 8 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_8753890e35a90ce7@96627bfd244d82d90f185983d28b4a93
---

# unfolding and laziness

Source: [[javascriptallonge]]

## Statements

- When they iterate over an array or linked list, they are traversing something that is already there. (javascriptallonge.pdf p.172)
- A function that starts with a seed and expands it into a data structure is called an unfold . (javascriptallonge.pdf p.173)
- This business of going on forever has some drawbacks. (javascriptallonge.pdf p.174)
- We can start with take , an easy function that returns an iterator that only returns a fixed number of elements:. (javascriptallonge.pdf p.174)
- We'll need an iterator that produces odd numbers. (javascriptallonge.pdf p.174)
- Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions. (javascriptallonge.pdf p.175)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

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

<a id="atom-2"></a>
**Atom:** code block

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

<a id="atom-3"></a>
**Atom:** code block

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

<a id="atom-4"></a>
**Atom:** code block

```
//=> 4
squares().value
//=> 9
```

<a id="atom-5"></a>
**Atom:** code block

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

<a id="atom-6"></a>
**Atom:** code block

```
const odds = () => {
```

<a id="atom-7"></a>
**Atom:** code block

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

<a id="atom-8"></a>
**Atom:** code block

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
