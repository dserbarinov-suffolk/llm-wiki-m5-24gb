---
page_id: javascriptallonge-yes-consider-this-variation
page_kind: concept
summary: Yes. Consider this variation:: 9 accepted assertion(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_4a1ec7ff2a63f6c0@377121b67c6a1bcaa3c9479218c91c5a
---

# Yes. Consider this variation:

Source: [[javascriptallonge]]

## Statements

- The answer is that pesky var i . (javascriptallonge.pdf p.155)
- So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3 . (javascriptallonge.pdf p.156)
- Now, at the time we created each function, i had a sensible value, like 0 , 1 , or 2 . (javascriptallonge.pdf p.156)
- But at the time we call one of the functions, i has the value 3 , which is why the loop terminated. (javascriptallonge.pdf p.156)
- This small error was a frequent cause of confusion, and in the days when there was no block-scoped let , programmers would need to know how to fake it, usually with an IIFE:. (javascriptallonge.pdf p.156)
- This works, but let is so much simpler and cleaner that it was added to the language in the ECMAScript 2015 specification. (javascriptallonge.pdf p.157)
- That does not mean that you should follow the exact same practice in your own code: The purpose of this book is to illustrate certain principles of programming. (javascriptallonge.pdf p.157)
- The purpose of your own code is to get things done. (javascriptallonge.pdf p.157)
- The two goals are often, but not always, aligned. (javascriptallonge.pdf p.157)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
var introductions = [],
names = ['Karl', 'Friedrich', 'Gauss'];
for (var i = 0; i < 3; i++) {
introductions[i] = "Hello, my name is " + names[i]
}
introductions
//=> [ 'Hello, my name is Karl',
//
'Hello, my name is Friedrich',
//
'Hello, my name is Gauss' ]
```

<a id="atom-2"></a>
**Atom:** code block

```
var introductions = [],
names = ['Karl', 'Friedrich', 'Gauss'];
for (var i = 0; i < 3; i++) {
introductions[i] = (soAndSo) =>
`Hello, ${soAndSo}, my name is ${names[i]}`
}
introductions
//=> [ [Function],
//
[Function],
//
[Function] ]
```

<a id="atom-3"></a>
**Atom:** code block

```
introductions[1]('Raganwald')
//=> 'Hello, Raganwald, my name is undefined'
```

<a id="atom-4"></a>
**Atom:** code block

```
var introductions = [],
names = ['Karl', 'Friedrich', 'Gauss'],
i = undefined;
for (i = 0; i < 3; i++) {
introductions[i] = function (soAndSo) {
return "Hello, " + soAndSo + ", my name is " + names[i]
}
}
introductions
```

<a id="atom-5"></a>
**Atom:** code block

```
let introductions = [],
names = ['Karl', 'Friedrich', 'Gauss'];
for (let i = 0; i < 3; i++) {
introductions[i] = (soAndSo) =>
`Hello, ${soAndSo}, my name is ${names[i]}`
}
introductions[1]('Raganwald')
//=> 'Hello, Raganwald, my name is Friedrich'
```

<a id="atom-6"></a>
**Atom:** code block

```
var introductions = [],
names = ['Karl', 'Friedrich', 'Gauss'];
for (var i = 0; i < 3; i++) {
((i) => {
introductions[i] = (soAndSo) =>
`Hello, ${soAndSo}, my name is ${names[i]}`
}
})(i)
}
introductions[1]('Raganwald')
//=> 'Hello, Raganwald, my name is Friedrich'
```
