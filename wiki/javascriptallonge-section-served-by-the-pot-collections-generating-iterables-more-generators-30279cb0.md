---
page_id: javascriptallonge-section-served-by-the-pot-collections-generating-iterables-more-generators-30279cb0
page_kind: source
summary: Served by the Pot: Collections / Generating Iterables / more generators: 9 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-generating-iterables-more-generators-30279cb0@ad101446799a2889b00bd78b00a1a4b1
---

# Served by the Pot: Collections / Generating Iterables / more generators

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-generators-and-iterables-adba5c82]] - previous source section: Served by the Pot: Collections / Generating Iterables / generators and iterables
- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-yielding-iterables-89322869]] - next source section: Served by the Pot: Collections / Generating Iterables / yielding iterables

### Source structure

- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-f68c47a5]] - broader source section: Served by the Pot: Collections / Generating Iterables

### Recipes

- [[javascriptallonge-recipe-more-generators]] - recipe pattern: more generators

### Topics

- [[javascriptallonge-generator]] - topic hub: opens the topic page for Generator

## Statements

- Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state: _(javascriptallonge.pdf (source-range-c98ab3e6-01690))_
- We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own. _(javascriptallonge.pdf (source-range-c98ab3e6-01695))_

## Technical atoms

### Technical frame 1: Served by the Pot: Collections / Generating Iterables / more generators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01690))_

> Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01688))_

<a id="atom-technical-atom-3577a4ec6b8f8bb0"></a>
```
const Numbers = {
*[Symbol.iterator] () {
let i = 0;
while (true) {
yield i++;
}
}
};
for (const i of Numbers) {
console.log(i);
}
//=>
0
1
2
3
4
5
6
7
```

### Technical frame 2: Served by the Pot: Collections / Generating Iterables / more generators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01690))_

> Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01689))_

<a id="atom-technical-atom-4076c026e05e9095"></a>
```
8
9
10
...
```

### Technical frame 3: Served by the Pot: Collections / Generating Iterables / more generators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01695))_

> We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01694))_

<a id="atom-technical-atom-338ddfa3091c4159"></a>
```
const Fibonacci = {
*[Symbol.iterator] () {
let a, b;
yield a = 0;
yield b = 1;
while (true) {
[a, b] = [b, a + b]
yield b;
}
}
}
for (const i of Fibonacci) {
console.log(i);
}
//=>
0
1
1
2
3
5
8
13
21
34
55
89
144
...
```

### Technical frame 4: Served by the Pot: Collections / Generating Iterables / more generators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01695))_

> We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01697))_

<a id="atom-technical-atom-71b8ed9c29ab713e"></a>
```
function * fibonacci () {
let a, b;
yield a = 0;
yield b = 1;
while (true) {
[a, b] = [b, a + b]
yield b;
}
}
for (const i of fibonacci()) {
console.log(i);
}
//=>
0
1
1
2
3
5
8
13
21
34
55
89
144
...
```
