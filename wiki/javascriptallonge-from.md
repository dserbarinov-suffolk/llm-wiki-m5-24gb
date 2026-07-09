---
page_id: javascriptallonge-from
page_kind: concept
summary: topic-concept: 15 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_008f42192560c7c2@14b71dd1d4d0cc69b894ec6fb8045f4f
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

## Rules

- No, of course not, we can do anything we like with them. (javascriptallonge.pdf p.221)
- And we can assign properties to functions with a . (javascriptallonge.pdf p.222)
- We can do the same with our own collections. (javascriptallonge.pdf p.222)
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


## Related pages

- [[javascriptallonge-operations-on-ordered-collections]] - contextualizes: source-supported topic dependency
