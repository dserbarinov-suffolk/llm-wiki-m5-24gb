---
page_id: javascriptallonge-section-recipes-with-basic-functions-maybe-d9752e09
page_kind: source
summary: Recipes with Basic Functions / Maybe: 12 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-basic-functions-maybe-d9752e09@5f8ea0a1d767a3d4ac10827101455581
---

# Recipes with Basic Functions / Maybe

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-recipes-with-basic-functions-58df4c63]] - broader source section: Recipes with Basic Functions
- [[javascriptallonge-section-recipes-with-basic-functions-tap-bcbc81bc]] - previous source section: Recipes with Basic Functions / Tap
- [[javascriptallonge-section-recipes-with-basic-functions-once-9048fede]] - next source section: Recipes with Basic Functions / Once

## Statements

- A common problem in programming is checking for null or undefined (hereafter called 'nothing,' while all other values including 0 , [] and false will be called 'something'). Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-0e12e052-00690))_
- Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing: _(javascriptallonge.pdf (source-range-0e12e052-00693))_
- Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation: _(javascriptallonge.pdf (source-range-0e12e052-00695))_
- If some code ever tries to call model.setSomething with nothing, the operation will be skipped. _(javascriptallonge.pdf (source-range-0e12e052-00703))_

## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00693))_

> Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00692))_

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00695))_

> Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00694))_

```
var something =
isSomething(value)
? doesntCheckForSomething(value)
: value;
```

### Technical frame 3: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00703))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00696))_

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

### Technical frame 4: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00695))_

> Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00697))_

```text
50 https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad
51 https://github.com/raganwald/andand
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 50 | https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad |
| 51 | https://github.com/raganwald/andand |

</details>

### Technical frame 5: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00703))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00698))_

```
return fn.apply(this, args)
}
}
```

### Technical frame 6: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00703))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00700))_

```
maybe((a, b, c) => a + b + c)(1, 2, 3)
//=> 6
maybe((a, b, c) => a + b + c)(1, null, 3)
//=> undefined
```

### Technical frame 7: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00703))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00702))_

```
function Model () {};
Model.prototype.setSomething = maybe(function (value) {
this.something = value;
});
```
