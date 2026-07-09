---
page_id: javascriptallonge-rebinding
page_kind: concept
summary: topic-concept: 8 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_348bfb54986f4950@e6751845aa99ee43a964274962327358
---

# rebinding

Source: [[javascriptallonge]]

## Statements

- We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. (javascriptallonge.pdf p.61)
- JavaScript does not permit us to rebind a name that has been bound with const . (javascriptallonge.pdf p.61)
- This is valuable, as it greatly simplifies the analysis of programs to see at a glance that when something is bound with const , we need never worry that its value may change. (javascriptallonge.pdf p.61)

## Rules

- We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. (javascriptallonge.pdf p.61)
- This is valuable, as it greatly simplifies the analysis of programs to see at a glance that when something is bound with const , we need never worry that its value may change. (javascriptallonge.pdf p.61)

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


## Related pages

- [[javascriptallonge-are-consts-also-from-a-shadowy-planet]] - contextualizes: source-supported topic dependency
