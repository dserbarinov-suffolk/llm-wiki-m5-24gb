---
page_id: javascriptallonge-tail-calls-and-default-arguments
page_kind: concept
summary: topic-concept: 25 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_6e535ea85d759998@40bac315af1b819a40668040dd48ce30
---

# Tail Calls (and Default Arguments)

Source: [[javascriptallonge]]

## Statements

- The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustrating the basic principles behind using recursion to work with self-similar data structures, but they are not 'production-ready' implementations. (javascriptallonge.pdf p.117)
- One of the reasons they are not production-ready is that they consume memory proportional to the size of the array being folded. (javascriptallonge.pdf p.117)
- First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked. (javascriptallonge.pdf p.117)
- To do that, it has to evaluate fn(first) and mapWith(fn, rest) , then evaluate [fn(first), ..mapWith(fn, rest)] . (javascriptallonge.pdf p.117)
- first is not undefined , so it evaluates [fn(first), …mapWith(fn, rest)]. (javascriptallonge.pdf p.117)
- JavaScript cannot throw first away. (javascriptallonge.pdf p.117)
- So we know that JavaScript is going to hang on to 1 . (javascriptallonge.pdf p.117)
- And the same thing happens: JavaScript has to hang on to 2 (or 4 , or both, depending on the implementation), plus some housekeeping information so it remembers what to do with that value, while it calls the equivalent of mapWith((x) => x * x, [3, 4, 5]) . (javascriptallonge.pdf p.117-118)
- Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . (javascriptallonge.pdf p.117-118)
- It can start assembling the resulting array and start discarding the information it is saving. (javascriptallonge.pdf p.118)
- Furthermore, doubling the length of an array will double the amount of space we need on the stack, plus double all the work required to set up and tear down the housekeeping data for each call (these are called call frames , and they include the place where the function was called, an environment, and so on). (javascriptallonge.pdf p.118)
- That information is saved on a call stack , and it is quite expensive. (javascriptallonge.pdf p.118)
- In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error. (javascriptallonge.pdf p.118)
- In fact, there are several better ways. (javascriptallonge.pdf p.118)
- Making algorithms faster is a very highly studied field of computer science. (javascriptallonge.pdf p.118)

## Rules

- JavaScript cannot throw first away. (javascriptallonge.pdf p.117)
- It can start assembling the resulting array and start discarding the information it is saving. (javascriptallonge.pdf p.118)
- Furthermore, doubling the length of an array will double the amount of space we need on the stack, plus double all the work required to set up and tear down the housekeeping data for each call (these are called call frames , and they include the place where the function was called, an environment, and so on). (javascriptallonge.pdf p.118)
- In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error. (javascriptallonge.pdf p.118)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const mapWith = (fn, [first, ...rest]) =>
first === undefined
? []
: [fn(first), ...mapWith(fn, rest)];
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

<a id="atom-2"></a>
**Atom:** code block

```
const mapWith = function (fn, [first, ...rest]) {
if (first === undefined) {
return [];
}
else {
const _temp1 = fn(first),
_temp2 = mapWith(fn, rest),
_temp3 = [_temp1, ..._temp2];
return _temp3;
}
}
```

<a id="atom-3"></a>
**Atom:** rule

```
Note that while evaluating mapWith(fn, rest) , JavaScript must retain the value first or fn(first) , plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result.
```

<a id="atom-4"></a>
**Atom:** code block

```
mapWith((x) => x * x, [
0,
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
20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
0,
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
20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
90, 91, 92, 93, 94, 95, 96, 97, 98, 99
])
//=> ???
```


## Related pages

- [[javascriptallonge-self-similarity]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-factorial]] - contextualizes: source-supported topic dependency
