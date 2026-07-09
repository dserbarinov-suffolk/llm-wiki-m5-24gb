---
page_id: javascriptallonge-evaluation-time
page_kind: concept
summary: evaluation time: 3 accepted assertion(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_31748b77ca2fb57a@7cf5882f01f34cba29ca830a6e4395d1
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
