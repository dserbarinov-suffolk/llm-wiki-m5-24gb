---
page_id: javascriptallonge-from
page_kind: concept
summary: from: 7 accepted assertion(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_d5b4122584c3a224@2d3b19b08ad5e375f01df953ec671c7d
---

# from

Source: [[javascriptallonge]]

## Statements

- No, of course not, we can do anything we like with them. (javascriptallonge.pdf p.221)
- One useful thing is to write a .from function that gathers an iterable into a particular collection type. (javascriptallonge.pdf p.222)
- As you recall, functions are mutable objects. (javascriptallonge.pdf p.222)
- And we can assign properties to functions with a . (javascriptallonge.pdf p.222)
- We can do the same with our own collections. (javascriptallonge.pdf p.222)
- And if we assign a function to a property, we've created a method. (javascriptallonge.pdf p.222)
- Nowwecan go ' end to end,' If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that:. (javascriptallonge.pdf p.222)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
Array.from(UpTo1000)
//=> [1,81,121,361,441,841,961]
```

<a id="atom-2"></a>
**Atom:** code block

```
Stack3.from = function (iterable) {
const stack = this();
for (let element of iterable) {
stack.push(element);
}
return stack;
}
Pair1.from = (iterable) =>
(function iterationToList (iteration) {
const {done, value} = iteration.next();
return done ? EMPTY : Pair1(value, iterationToList(iteration));
})(iterable[Symbol.iterator]())
```

<a id="atom-3"></a>
**Atom:** code block

```
const numberList = Pair1.from(untilWith((x) => x > 10, Numbers));
Pair1.from(Squares)
//=> {"first":0,
"rest":{"first":1,
"rest":{"first":4,
"rest":{ ...
```
