---
page_id: javascriptallonge-mutation
page_kind: concept
summary: topic-concept: 23 supported fragment(s) and 0 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_30a8c746c271a5ce@9576d736f6b7acdd324da66b3659d428
---

# Mutation

Source: [[javascriptallonge]]

## Statements

- In JavaScript, almost every type of value can mutate . (javascriptallonge.pdf p.141)
- Recall that you can access a value from within an array or an object using [] . (javascriptallonge.pdf p.141)
- Specifically, arrays and objects can mutate. (javascriptallonge.pdf p.141)
- Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. (javascriptallonge.pdf p.142)
- Both halloween and allHallowsEve are bound to the same array value within the local environment. (javascriptallonge.pdf p.142)
- In each of these examples, we have created two aliases for the same value. (javascriptallonge.pdf p.142)
- Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value. (javascriptallonge.pdf p.142)
- There are two nested environments, and each one binds a name to the exact same array value. (javascriptallonge.pdf p.142)
- The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. (javascriptallonge.pdf p.143)
- We haven't rebound the inner name to a different variable, we've mutated the value that both bindings share. (javascriptallonge.pdf p.143)
- Mutating existing objects has special implications when two bindings are aliases of the same value. (javascriptallonge.pdf p.143)
- Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. (javascriptallonge.pdf p.143)

## Rules

- In JavaScript, almost every type of value can mutate . (javascriptallonge.pdf p.141)
- Recall that you can access a value from within an array or an object using [] . (javascriptallonge.pdf p.141)
- Specifically, arrays and objects can mutate. (javascriptallonge.pdf p.141)
- Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value. (javascriptallonge.pdf p.142)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const oneTwoThree = [1, 2, 3];
oneTwoThree[0] = 'one';
oneTwoThree
//=> [ 'one', 2, 3 ]
```

<a id="atom-2"></a>
**Atom:** code block

```
const oneTwoThree = [1, 2, 3];
oneTwoThree[3] = 'four';
oneTwoThree
//=> [ 1, 2, 3, 'four' ]
```

<a id="atom-3"></a>
**Atom:** code block

```
const name = {firstName: 'Leonard', lastName: 'Braithwaite'};
name.middleName = 'Austin'
name
//=> { firstName: 'Leonard',
#
lastName: 'Braithwaite',
#
middleName: 'Austin' }
```

<a id="atom-4"></a>
**Atom:** code block

```
const allHallowsEve = [2012, 10, 31]
const halloween = allHallowsEve;
```

<a id="atom-5"></a>
**Atom:** code block

```
const allHallowsEve = [2012, 10, 31];
(function (halloween) {
// ...
})(allHallowsEve);
```

<a id="atom-6"></a>
**Atom:** code block

```
const allHallowsEve = [2012, 10, 31];
(function (halloween) {
halloween = [2013, 10, 31];
})(allHallowsEve);
allHallowsEve
//=> [2012, 10, 31]
```

<a id="atom-7"></a>
**Atom:** code block

```
const allHallowsEve = [2012, 10, 31];
(function (halloween) {
halloween[0] = 2013;
})(allHallowsEve);
allHallowsEve
//=> [2013, 10, 31]
```
