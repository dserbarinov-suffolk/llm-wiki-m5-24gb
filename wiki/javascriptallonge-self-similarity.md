---
page_id: javascriptallonge-self-similarity
page_kind: concept
summary: topic-concept: 28 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_c1c028bd3dda52f8@f7bd307adbab0db86484f1befd91760e
---

# Self-Similarity

Source: [[javascriptallonge]]

## Statements

- Recursion is the root of computation since it trades description for time.-Alan Perlis, Epigrams in Programming 60. (javascriptallonge.pdf p.109)
- In Arrays and Destructuring Arguments, we worked with the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. (javascriptallonge.pdf p.109)
- We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. (javascriptallonge.pdf p.109)
- Some data structures, like lists, can obviously be seen as a collection of items. (javascriptallonge.pdf p.109)
- Some are empty, some have three items, some forty-two, some contain numbers, some contain strings, some a mixture of elements, there are all kinds of lists. (javascriptallonge.pdf p.109)
- The first rule is simple: [] is a list. (javascriptallonge.pdf p.109)
- Given an element e and a list list , [e, ..list] is a list. (javascriptallonge.pdf p.109)
- Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists:. (javascriptallonge.pdf p.109)
- We know that we can get the length of an array using its .length . (javascriptallonge.pdf p.110-111)
- 61 Well, actually, this does not work for arrays that contain undefined as a value, but we are not going to see that in our examples. (javascriptallonge.pdf p.110)
- We need something for when the array isn't empty. (javascriptallonge.pdf p.111)
- If an array is not empty, and we break it into two pieces, first and rest , the length of our array is going to be length(first) + length(rest) . (javascriptallonge.pdf p.111)
- If only there was a function we could call… Like length !. (javascriptallonge.pdf p.111)
- Well, the length of first is 1 , there's just one element at the front. (javascriptallonge.pdf p.111)
- Our length function is recursive , it calls itself. (javascriptallonge.pdf p.111)
- This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. (javascriptallonge.pdf p.111)

## Rules

- Some data structures, like lists, can obviously be seen as a collection of items. (javascriptallonge.pdf p.109)
- Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists:. (javascriptallonge.pdf p.109)
- We know that we can get the length of an array using its .length . (javascriptallonge.pdf p.110-111)
- If only there was a function we could call… Like length !. (javascriptallonge.pdf p.111)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

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

<a id="atom-2"></a>
**Atom:** code block

```
const [first, ...rest] = [];
first
//=> undefined
rest
//=> []:
const [first, ...rest] = ["foo"];
first
//=> "foo"
rest
//=> []
const [first, ...rest] = ["foo", "bar"];
first
//=> "foo"
rest
//=> ["bar"]
const [first, ...rest] = ["foo", "bar", "baz"];
first
//=> "foo"
rest
//=> ["bar","baz"]
For the purpose of this exploration, we will presume the following:61
const isEmpty = ([first, ...rest]) => first === undefined;
```

<a id="atom-3"></a>
**Atom:** code block

```
isEmpty([])
//=> true
isEmpty([0])
//=> false
isEmpty([[]])
//=> false
```

<a id="atom-4"></a>
**Atom:** code block

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: // ???
```

<a id="atom-5"></a>
**Atom:** code block

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: 1 + length(rest);
Let’s try it!
length([])
//=> 0
length(["foo"])
//=> 1
length(["foo", "bar", "baz"])
```

<a id="atom-6"></a>
**Atom:** code block

```
//=> 3
```


## Related pages

- [[javascriptallonge-arrays-and-destructuring-arguments]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-tail-calls-and-default-arguments]] - contextualizes: source-supported topic dependency
