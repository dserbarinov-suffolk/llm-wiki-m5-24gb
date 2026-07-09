---
page_id: javascriptallonge-evaluation-time
page_kind: concept
summary: topic-concept: 6 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_3fc1a66f51eb797f@5955b517478d87e663bb9ec8fab6db1b
---

# evaluation time

Source: [[javascriptallonge]]

## Statements

- Like any other expression, quasi-literals are evaluated late , when that line or lines of code is evaluated. (javascriptallonge.pdf p.204)
- Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked. (javascriptallonge.pdf p.204)
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. (javascriptallonge.pdf p.204)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const name = "Harry";
const greeting = (name) => `Hello my name is ${name}`;
greeting('Arthur Dent')
//=> 'Hello my name is Arthur Dent'
```

<a id="atom-2"></a>
**Atom:** code block

```
const greeting = (name) => 'Hello my name is ' + name;
greeting('Arthur Dent')
//=> 'Hello my name is Arthur Dent'
```


## Related pages

- [[javascriptallonge-quasi-literal]] - contextualizes: source-supported topic dependency
