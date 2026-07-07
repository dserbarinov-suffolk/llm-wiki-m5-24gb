---
page_id: javascriptallonge-section-recipes-with-basic-functions-d7445960
page_kind: source
summary: Recipes with Basic Functions: 26 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-basic-functions-d7445960@93a543d87830df103773c05d71f0b122
---

# Recipes with Basic Functions

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-a-history-lesson-f921305a]] - next source section: a history lesson

### Source structure

- [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-574b019e]] - narrower source section: Recipes with Basic Functions / Left-Variadic Functions
- [[javascriptallonge-section-recipes-with-basic-functions-partial-application-70ce84b0]] - narrower source section: Recipes with Basic Functions / Partial Application
- [[javascriptallonge-section-recipes-with-basic-functions-tap-51486e75]] - narrower source section: Recipes with Basic Functions / Tap
- [[javascriptallonge-section-recipes-with-basic-functions-unary-d494fe78]] - narrower source section: Recipes with Basic Functions / Unary

## Statements

- Before combining ingredients, begin with implements so clean, they gleam. _(javascriptallonge.pdf (source-range-c98ab3e6-00637))_
- Having looked at basic pure functions and closures, we're going to see some practical recipes that focus on the premise of functions that return functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00638))_
- Before combining ingredients, begin with implements so clean, they gleam. _(javascriptallonge.pdf (source-range-c98ab3e6-00637))_

## Statements by subsection

### Recipes with Basic Functions / Disclaimer

- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven't been discussed in the text to this point, such as methods and/or prototypes. The overall use of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-c98ab3e6-00640))_
- The overall use of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-c98ab3e6-00640))_
- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven't been discussed in the text to this point, such as methods and/or prototypes. _(javascriptallonge.pdf (source-range-c98ab3e6-00640))_

### Recipes with Basic Functions / Maybe

- A common problem in programming is checking for null or undefined (hereafter called 'nothing,' while all other values including 0 , [] and false will be called 'something'). Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-c98ab3e6-00678))_
- Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing: _(javascriptallonge.pdf (source-range-c98ab3e6-00681))_
- Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation: _(javascriptallonge.pdf (source-range-c98ab3e6-00683))_
- If some code ever tries to call model.setSomething with nothing, the operation will be skipped. _(javascriptallonge.pdf (source-range-c98ab3e6-00691))_

### Recipes with Basic Functions / Once

- once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe: _(javascriptallonge.pdf (source-range-c98ab3e6-00693))_
- Very simple! You pass it a function, and you get a function back. That function will call your function once, and thereafter will return undefined whenever it is called. Let's try it: _(javascriptallonge.pdf (source-range-c98ab3e6-00695))_
- (Note: There are some subtleties with decorators like once that involve the intersection of state with methods. We'll look at that again in stateful method decorators.) _(javascriptallonge.pdf (source-range-c98ab3e6-00698))_
- It ensures that a function can only be called, well, once . _(javascriptallonge.pdf (source-range-c98ab3e6-00693))_
- That function will call your function once, and thereafter will return undefined whenever it is called. _(javascriptallonge.pdf (source-range-c98ab3e6-00695))_

## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00681))_

> Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00680))_

<a id="atom-technical-atom-35d89da91bd75da0"></a>
```
const isSomething = (value) =>
value !== null && value !== void 0;
const checksForSomething = (value) => {
if (isSomething(value)) {
// function's true logic
}
}
```

### Technical frame 2: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00691))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00684))_

<a id="atom-technical-atom-849e2382023c8bfc"></a>
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

### Technical frame 3: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00691))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00686))_

<a id="atom-technical-atom-8520aae83218fd0d"></a>
```
return fn.apply(this, args)
}
}
```

### Technical frame 4: Recipes with Basic Functions / Once

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00695))_

> Very simple! You pass it a function, and you get a function back. That function will call your function once, and thereafter will return undefined whenever it is called. Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00694))_

<a id="atom-technical-atom-0f3208d550e42a8b"></a>
```
const once = (fn) => {
let done = false;
return function () {
return done ? void 0 : ((done = true), fn.apply(this, arguments))
}
}
```
