---
page_id: javascriptallonge-array-literals
page_kind: concept
summary: array literals: 5 accepted assertion(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_d96a87e4d377299e@94c35d29f6f1b0975ef2685d7643aa39
---

# array literals

Source: [[javascriptallonge]]

## Statements

- JavaScript has a literal syntax for creating an array: The [ and ] characters. (javascriptallonge.pdf p.101)
- This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. (javascriptallonge.pdf p.101)
- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. (javascriptallonge.pdf p.101)
- Array literals are expressions, and arrays are reference types . (javascriptallonge.pdf p.102)
- We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:. (javascriptallonge.pdf p.102)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
[]
//=> []
```

<a id="atom-2"></a>
**Atom:** code block

```
[1]
//=> [1]
[2, 3, 4]
//=> [2,3,4]
```

<a id="atom-3"></a>
**Atom:** code block

```
[ 2,
3,
2 + 2
]
//=> [2,3,4]
```

<a id="atom-4"></a>
**Atom:** code block

```
[[[[[]]]]]
```

<a id="atom-5"></a>
**Atom:** code block

```
const wrap = (something) => [something];
wrap("lunch")
//=> ["lunch"]
```

<a id="atom-6"></a>
**Atom:** code block

```
[] === []
//=> false
[2 + 2] === [2 + 2]
//=> false
const array_of_one = () => [1];
array_of_one() === array_of_one()
//=> false
```
