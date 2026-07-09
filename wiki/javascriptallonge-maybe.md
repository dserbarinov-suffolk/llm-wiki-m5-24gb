---
page_id: javascriptallonge-maybe
page_kind: concept
summary: Maybe: 5 accepted assertion(s) and 7 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_1c028b101b67cae6@8c3015fc968dca3d91fd7815005a3613
---

# Maybe

Source: [[javascriptallonge]]

## Statements

- A common problem in programming is checking for null or undefined (hereafter called 'nothing,' while all other values including 0 , [] and false will be called 'something'). (javascriptallonge.pdf p.86)
- Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. (javascriptallonge.pdf p.86)
- Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing:. (javascriptallonge.pdf p.86)
- Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:. (javascriptallonge.pdf p.86)
- If some code ever tries to call model.setSomething with nothing, the operation will be skipped. (javascriptallonge.pdf p.87)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const isSomething = (value) =>
value !== null && value !== void 0;
const checksForSomething = (value) => {
if (isSomething(value)) {
// function's true logic
}
}
```

<a id="atom-2"></a>
**Atom:** code block

```
var something =
isSomething(value)
? doesntCheckForSomething(value)
: value;
```

<a id="atom-3"></a>
**Atom:** code block

```
const maybe = (fn) =>
function (...args) {
if (args.length === 0) {
return
}
else {
for (let arg of args) {
if (arg == null) return;
}
```

<a id="atom-4"></a>
**Atom:** table

```text
50 https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad
51 https://github.com/raganwald/andand
```

<a id="atom-5"></a>
**Atom:** code block

```
return fn.apply(this, args)
}
}
```

<a id="atom-6"></a>
**Atom:** code block

```
maybe((a, b, c) => a + b + c)(1, 2, 3)
//=> 6
maybe((a, b, c) => a + b + c)(1, null, 3)
//=> undefined
```

<a id="atom-7"></a>
**Atom:** code block

```
function Model () {};
Model.prototype.setSomething = maybe(function (value) {
this.something = value;
});
```
