---
page_id: javascriptallonge-javascript-s-generators
page_kind: concept
summary: topic-concept: 19 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_30105c7d214d9656@2a6aebcbed633f7789eccf509dd4e5cd
---

# javascript's generators

Source: [[javascriptallonge]]

## Statements

- It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator. (javascriptallonge.pdf p.230)
- Given the title of this chapter, it is not a surprise that JavaScript makes this possible. (javascriptallonge.pdf p.230)
- An iterator written in a generation style is called a generator . (javascriptallonge.pdf p.230)
- We can write an iterator, but use a generation style of programming. (javascriptallonge.pdf p.230)
- This makes sense, because empty never yields anything. (javascriptallonge.pdf p.230)
- Generator functions can take an argument. (javascriptallonge.pdf p.230)
- Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . (javascriptallonge.pdf p.231)
- Invoking only more than once gives us fresh iterators each time:. (javascriptallonge.pdf p.231)

## Rules

- It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator. (javascriptallonge.pdf p.230)
- We can write an iterator, but use a generation style of programming. (javascriptallonge.pdf p.230)
- Generator functions can take an argument. (javascriptallonge.pdf p.230)
- Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . (javascriptallonge.pdf p.231)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
function * empty () {};
empty().next()
//=>
{"done":true}
```

<a id="atom-2"></a>
**Atom:** rule

```
When we invoke empty , we get an iterator with no elements.
```

<a id="atom-3"></a>
**Atom:** code block

```
function * only (something) {
yield something;
};
only("you").next()
//=>
{"done":false, value: "you"}
```

<a id="atom-4"></a>
**Atom:** code block

```
only("you").next()
//=>
{"done":false, value: "you"}
only("the lonely").next()
//=>
{"done":false, value: "the lonely"}
```

<a id="atom-5"></a>
**Atom:** code block

```
const sixteen = only("sixteen");
sixteen.next()
//=>
{"done":false, value: "sixteen"}
sixteen.next()
//=>
{"done":true}
```


## Related pages

- [[javascriptallonge-state-machines]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-generators-are-coroutines]] - contextualizes: source-supported topic dependency
