---
page_id: javascriptallonge-section-and-also-magic-names-the-function-keyword-55f3d121
page_kind: source
summary: And also: / Magic Names / the function keyword: 11 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-magic-names-the-function-keyword-55f3d121@129588342e103a530d877220f6e52263
---

# And also: / Magic Names / the function keyword

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-and-also-magic-names-magic-names-and-fat-arrows-10e3f519]] - next source section: And also: / Magic Names / magic names and fat arrows

### Source structure

- [[javascriptallonge-section-and-also-magic-names-0c5d7af9]] - broader source section: And also: / Magic Names

### Topics

- [[javascriptallonge-function-keyword]] - topic hub: opens the topic page for Function Keyword

## Statements

- There are two separate rules for these 'magic' names, one for when you invoke a function using the function keyword, and another for functions defined with 'fat arrows.' We'll begin with how things work for functions defined with the function keyword. _(javascriptallonge.pdf (source-range-c98ab3e6-00592))_
- The first magic name is this , and it is bound to something called the function's context. We will explore this in more detail when we start discussing objects and classes. The second magic name is very interesting, it's called arguments , and the most interesting thing about it is that it contains a list of arguments passed to a function: _(javascriptallonge.pdf (source-range-c98ab3e6-00593))_
- arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00597))_
- The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses. _(javascriptallonge.pdf (source-range-c98ab3e6-00602))_

## Technical atoms

### Technical frame 1: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00602))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00598))_

<a id="atom-technical-atom-5bb18c52a0c78571"></a>
```text
42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times.
43 We'll look at arrays and plain old javascript objects in depth later.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 42 | You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. |
| 43 | We'll look at arrays and plain old javascript objects in depth later. |

</details>
