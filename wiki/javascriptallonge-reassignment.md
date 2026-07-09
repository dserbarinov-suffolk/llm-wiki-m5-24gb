---
page_id: javascriptallonge-reassignment
page_kind: concept
summary: topic-concept: 15 supported fragment(s) and 0 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_d8ff2856b01602d4@63bb8a94a5e4e1b2c7b0c8a0f17ffa80
---

# Reassignment

Source: [[javascriptallonge]]

## Statements

- Like some imperative programming languages, JavaScript allows you to re-assign the value bound to parameters. (javascriptallonge.pdf p.148)
- JavaScript does not permit us to rebind a name that has been bound with const . (javascriptallonge.pdf p.149)
- We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. (javascriptallonge.pdf p.149)
- What we want is a statement that works like const , but permits us to rebind variables. (javascriptallonge.pdf p.149)
- The key is to understand that we are rebinding a different value to the same name in the same environment. (javascriptallonge.pdf p.149)
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . (javascriptallonge.pdf p.149)
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. (javascriptallonge.pdf p.150)

## Rules

- We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. (javascriptallonge.pdf p.149)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const evenStevens = (n) => {
if (n === 0) {
return true;
}
else if (n == 1) {
return false;
}
else {
n = n - 2;
return evenStevens(n);
}
}
evenStevens(42)
//=> true
```

<a id="atom-2"></a>
**Atom:** code block

```
evenStevens = (n) => {
if (n === 0) {
return true;
}
else if (n == 1) {
return false;
}
else {
return evenStevens(n - 2);
}
}
//=> ERROR, evenStevens is read-only
```

<a id="atom-3"></a>
**Atom:** code block

```
let age = 52;
age = 53;
age
//=> 53
```

<a id="atom-4"></a>
**Atom:** code block

```
(() => {
let age = 49;
if (true) {
let age = 50;
}
return age;
})()
//=> 49
```

<a id="atom-5"></a>
**Atom:** code block

```
{age: 49, '..': global-environment}
To:
{age: 50, '..': {age: 49, '..': global-environment}}
Then back to:
```

<a id="atom-6"></a>
**Atom:** code block

```
{age: 49, '..': global-environment}
```

<a id="atom-7"></a>
**Atom:** code block

```
(() => {
let age = 49;
if (true) {
age = 50;
}
return age;
})()
//=> 50
```
