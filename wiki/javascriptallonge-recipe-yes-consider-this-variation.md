---
page_id: javascriptallonge-recipe-yes-consider-this-variation
page_kind: recipe
summary: Yes. Consider this variation: reusable source-backed pattern with 9 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: yes-consider-this-variation
projection_coverage: recipe-javascriptallonge-recipe-yes-consider-this-variation@2e537992085faf1a98486c8e081bbd6e
---

# Yes. Consider this variation

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-yes-consider-this-variation-db4ad8a2]].
- Evidence roles: decision, explanation, example.

## Applicability And Rationale

- The answer is that pesky var i . _(javascriptallonge.pdf (source-range-0e12e052-01208))_
- So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3 . _(javascriptallonge.pdf (source-range-0e12e052-01210))_
- Now, at the time we created each function, i had a sensible value, like 0 , 1 , or 2 . _(javascriptallonge.pdf (source-range-0e12e052-01210))_
- But at the time we call one of the functions, i has the value 3 , which is why the loop terminated. _(javascriptallonge.pdf (source-range-0e12e052-01210))_
- This small error was a frequent cause of confusion, and in the days when there was no block-scoped let , programmers would need to know how to fake it, usually with an IIFE: _(javascriptallonge.pdf (source-range-0e12e052-01213))_
- This works, but let is so much simpler and cleaner that it was added to the language in the ECMAScript 2015 specification. _(javascriptallonge.pdf (source-range-0e12e052-01215))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01203)_

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

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01205)_

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

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01207)_

```
introductions[1]('Raganwald')
//=> 'Hello, Raganwald, my name is undefined'
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01209)_

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

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01212)_

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

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01214)_

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

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-yes-consider-this-variation-db4ad8a2]]
