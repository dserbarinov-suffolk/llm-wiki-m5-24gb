---
page_id: javascriptallonge-left-variadic-functions
page_kind: concept
summary: topic-concept: 11 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_976eaa00e937014f@ef40fc8da7e29ece52805644426a5547
---

# Left-Variadic Functions

Source: [[javascriptallonge]]

## Statements

- A variadic function is a function that is designed to accept a variable number of arguments. (javascriptallonge.pdf p.89)
- For example, we might want to have a function that builds some kind of team record. (javascriptallonge.pdf p.89)
- This can be useful when writing certain kinds of destructuring algorithms. (javascriptallonge.pdf p.89)
- 52 English is about as inconsistent as JavaScript: Functions with a fixed number of arguments can be unary, binary, ternary, and so forth. (javascriptallonge.pdf p.89)
- ECMAScript 2015 only permits gathering parameters from the end of the parameter list. (javascriptallonge.pdf p.90)

## Rules

- This can be useful when writing certain kinds of destructuring algorithms. (javascriptallonge.pdf p.89)
- 52 English is about as inconsistent as JavaScript: Functions with a fixed number of arguments can be unary, binary, ternary, and so forth. (javascriptallonge.pdf p.89)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const abccc = (a, b, ...c) => {
console.log(a);
console.log(b);
console.log(c);
};
abccc(1, 2, 3, 4, 5)
1
2
[3,4,5]
```

<a id="atom-2"></a>
**Atom:** code block

```
function team(coach, captain, ...players) {
console.log(`${captain} (captain)`);
for (let player of players) {
console.log(player);
}
console.log(`squad coached by ${coach}`);
}
team('Luis Enrique', 'Xavi Hernández', 'Marc-André ter Stegen',
'Martín Montoya', 'Gerard Piqué')
//=>
Xavi Hernández (captain)
Marc-André ter Stegen
Martín Montoya
Gerard Piqué
squad coached by Luis Enrique
But we can’t go the other way around:
```

<a id="atom-3"></a>
**Atom:** code block

```
function team2(...players, captain, coach) {
console.log(`${captain} (captain)`);
for (let player of players) {
console.log(player);
}
console.log(`squad coached by ${coach}`);
}
//=> Unexpected token
```


## Related pages

- [[javascriptallonge-once]] - contextualizes: source-supported topic dependency
