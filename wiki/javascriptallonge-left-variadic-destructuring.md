---
page_id: javascriptallonge-left-variadic-destructuring
page_kind: concept
summary: topic-concept: 11 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_ea2a86a2bbb210fb@3470cb9b533a60412219d3dd65383edf
---

# left-variadic destructuring

Source: [[javascriptallonge]]

## Statements

- Gathering arguments for functions is one of the ways JavaScript can destructure arrays. (javascriptallonge.pdf p.92)
- But we can write our own left-gathering function utility using the same principles without all the tedium:. (javascriptallonge.pdf p.93)
- With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function. (javascriptallonge.pdf p.93)

## Rules

- Gathering arguments for functions is one of the ways JavaScript can destructure arrays. (javascriptallonge.pdf p.92)
- But we can write our own left-gathering function utility using the same principles without all the tedium:. (javascriptallonge.pdf p.93)
- With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function. (javascriptallonge.pdf p.93)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid'];
first
//=> 'why'
butFirst
//=> ["hello","there","little","droid"]
```

<a id="atom-2"></a>
**Atom:** code block

```
const [...butLast, last] = ['why', 'hello', 'there', 'little', 'droid'];
//=> Unexpected token
```

<a id="atom-3"></a>
**Atom:** code block

```
const [butLast, last] = leftVariadic((butLast, last) => [butLast, last])(...['wh\
y', 'hello', 'there', 'little', 'droid']);
butLast
//=> ['why', 'hello', 'there', 'little']
last
//=> 'droid'
```

<a id="atom-4"></a>
**Atom:** code block

```
const leftGather = (outputArrayLength) => {
return function (inputArray) {
return [inputArray.slice(0, inputArray.length - outputArrayLength + 1)].conc\
at(
inputArray.slice(inputArray.length - outputArrayLength + 1)
)
}
};
const [butLast, last] = leftGather(2)(['why', 'hello', 'there', 'little', 'droid\
']);
butLast
//=> ['why', 'hello', 'there', 'little']
last
//=> 'droid'
```


## Related pages

- [[javascriptallonge-overcoming-limitations]] - contextualizes: source-supported topic dependency
