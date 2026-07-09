---
page_id: javascriptallonge-more-generators
page_kind: concept
summary: topic-concept: 11 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_6c1429cf94a63924@cc77ddf0c2ee78e663682f8511d4986b
---

# more generators

Source: [[javascriptallonge]]

## Statements

- Our OneTwoThree example used implicit state to output the numbers in sequence. (javascriptallonge.pdf p.237)
- And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own. (javascriptallonge.pdf p.239)
- We've writing a function that returns an iterator, but we used a generator to do it. (javascriptallonge.pdf p.239)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

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

<a id="atom-2"></a>
**Atom:** code block

```
8
9
10
...
```

<a id="atom-3"></a>
**Atom:** code block

```
const Fibonacci = {
[Symbol.iterator]: () => {
let a = 0, b = 1, state = 0;
return {
next: () => {
switch (state) {
case 0:
state = 1;
return {value: a};
case 1:
state = 2;
return {value: b};
case 2:
[a, b] = [b, a + b];
return {value: b};
}
}
}
}
};
for (let n of Fibonacci) {
console.log(n)
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
```

<a id="atom-4"></a>
**Atom:** code block

```
21
34
55
89
144
...
```

<a id="atom-5"></a>
**Atom:** code block

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

<a id="atom-6"></a>
**Atom:** code block

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


## Related pages

- [[javascriptallonge-generators-and-iterables]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-yielding-iterables]] - contextualizes: source-supported topic dependency
