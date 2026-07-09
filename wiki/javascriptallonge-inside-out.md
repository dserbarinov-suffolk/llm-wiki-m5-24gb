---
page_id: javascriptallonge-inside-out
page_kind: concept
summary: inside-out: 11 accepted assertion(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_4798dd76cc0ac53e@539b98ba2b7f71be9683de6d8ac3e685
---

# inside-out

Source: [[javascriptallonge]]

## Statements

- There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. (javascriptallonge.pdf p.50)
- A 'magic literal' like 3.14159265 is anathema to sustainable software development. (javascriptallonge.pdf p.50)
- Well, the first one seems simplest, but a half-century of experience has taught us that names matter. (javascriptallonge.pdf p.50)
- The third one is easiest for most people to read. (javascriptallonge.pdf p.50)
- Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated 'IIFE.'. (javascriptallonge.pdf p.50)
- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. (javascriptallonge.pdf p.50)
- Everything else is encapsulated in its body. (javascriptallonge.pdf p.51)
- That's how it should be, naming PI is its concern, not ours. (javascriptallonge.pdf p.51)
- Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. (javascriptallonge.pdf p.51)
- But then we've obfuscated our code, and we don't want to do that unless we absolutely have to. (javascriptallonge.pdf p.51)
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. (javascriptallonge.pdf p.51)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```

<a id="atom-2"></a>
**Atom:** code block

```
((diameter) => diameter * 3.14159265)(2)
//=> 6.2831853
((PI) =>
(diameter) => diameter * PI
)(3.14159265)(2)
//=> 6.2831853
((diameter) =>
((PI) =>
diameter * PI)(3.14159265))(2)
//=> 6.2831853
```

<a id="atom-3"></a>
**Atom:** code block

```
(diameter) =>
// ...
```

<a id="atom-4"></a>
**Atom:** code block

```
((PI) =>
// ...
)(3.14159265)
```

<a id="atom-5"></a>
**Atom:** code block

```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```

<a id="atom-6"></a>
**Atom:** code block

```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```
