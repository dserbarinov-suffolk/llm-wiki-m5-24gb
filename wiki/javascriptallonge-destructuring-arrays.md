---
page_id: javascriptallonge-destructuring-arrays
page_kind: concept
summary: topic-concept: 12 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_51017bfccaa0350f@bac33de0dcd853b3d221b4a3077b2235
---

# destructuring arrays

Source: [[javascriptallonge]]

## Statements

- There is another way to extract elements from arrays: Destructuring , a feature going back to Common Lisp, if not before. (javascriptallonge.pdf p.103)
- The line const wrapped = [something]; is interesting. (javascriptallonge.pdf p.103)
- The statement const [something] = wrapped ; destructures the array represented by wrapped , binding the value of its single element to the name something . (javascriptallonge.pdf p.103)
- We could do the same thing with (name) => name[1] , but destructuring is code that resembles the data it consumes, a valuable coding style. (javascriptallonge.pdf p.104)

## Rules

- We could do the same thing with (name) => name[1] , but destructuring is code that resembles the data it consumes, a valuable coding style. (javascriptallonge.pdf p.104)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const wrap = (something) => [something];
Let’s expand it to use a block and an extra name:
const wrap = (something) => {
const wrapped = [something];
```

<a id="atom-2"></a>
**Atom:** code block

```
const wrap = (something) => {
const wrapped = [something]
return wrapped;
}
wrap("package")
//=> ["package"]
```

<a id="atom-3"></a>
**Atom:** code block

```
const unwrap = (wrapped) => {
const [something] = wrapped;
return something;
}
unwrap(["present"])
//=> "present"
```

<a id="atom-4"></a>
**Atom:** code block

```
const surname = (name) => {
const [first, last] = name;
return last;
}
surname(["Reginald", "Braithwaite"])
//=> "Braithwaite"
```

<a id="atom-5"></a>
**Atom:** code block

```
const description = (nameAndOccupation) => {
const [[first, last], occupation] = nameAndOccupation;
return `${first} is a ${occupation}`;
}
description([["Reginald", "Braithwaite"], "programmer"])
//=> "Reginald is a programmer"
```


## Related pages

- [[javascriptallonge-element-references]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-gathering]] - contextualizes: source-supported topic dependency
