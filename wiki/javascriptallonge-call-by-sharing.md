---
page_id: javascriptallonge-call-by-sharing
page_kind: concept
summary: call by sharing: 11 accepted assertion(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_2028d72daaf88573@8e0af50e94514b68d0c519a4dbc26ef6
---

# call by sharing

Source: [[javascriptallonge]]

## Statements

- Now it is time to take another look at the distinction between value and reference types. (javascriptallonge.pdf p.42)
- At that time, we looked at how JavaScript distinguishes objects that are identical from objects that are not. (javascriptallonge.pdf p.42)
- Earlier, we distinguished JavaScript's value types from its reference types . (javascriptallonge.pdf p.42)
- There is a property that JavaScript strictly maintains: When a value-any value-is passed as an argument to a function, the value bound in the function's environment must be identical to the original. (javascriptallonge.pdf p.42)
- As you recall, value types like strings and numbers are identical to each other if they have the same content. (javascriptallonge.pdf p.42-43)
- Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. (javascriptallonge.pdf p.42-43)
- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. (javascriptallonge.pdf p.42-43)
- JavaScript places references to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. (javascriptallonge.pdf p.43)
- JavaScript does not place copies of reference values in any environment. (javascriptallonge.pdf p.43)
- Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types. (javascriptallonge.pdf p.43)
- 26 Unless the argument is NaN , which isn't equal to anything, including itself . (javascriptallonge.pdf p.43)

## Technical atoms

<a id="atom-1"></a>
**Atom:** rule

```
So JavaScript can make as many copies of strings, numbers, or booleans as it wishes.
```

<a id="atom-2"></a>
**Atom:** code block

```
(value) =>
((ref1, ref2) => ref1 === ref2)(value, value)
```
