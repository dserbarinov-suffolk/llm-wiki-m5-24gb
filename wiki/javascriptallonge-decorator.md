---
page_id: javascriptallonge-decorator
page_kind: concept
summary: Decorator: 4 statement(s) and 6 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-decorator@ce337f3fc41f5b25d411638c9cd15aab
---

# Decorator

What [[javascriptallonge]] covers about decorator:

## Statements

### A Pull of the Lever: Prefaces / About JavaScript Allongé

- It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or code-centric. JavaScript idioms like function combinators and decorators leverage JavaScript's power to make code easier to read, modify, debug and refactor. _(javascriptallonge.pdf (source-range-c98ab3e6-00018))_

### Combinators and Function Decorators / function decorators

- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-c98ab3e6-00563))_

### Building Blocks / composition

- In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument. _(javascriptallonge.pdf (source-range-c98ab3e6-00572))_

### Recipes with Basic Functions / Maybe

- Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation: _(javascriptallonge.pdf (source-range-c98ab3e6-00683))_


## Technical atoms

### Technical frame 1: Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00563))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00555))_

<a id="atom-technical-atom-73d86f3bb2def087"></a>
```text
function decorators
A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. Here's a ridiculously simple decorator: 38
37 As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context.
38 We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args)
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 37 | As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. |
| 38 | We'll see later why an even more useful version would be written (fn) => (...args) =>!fn(...args) |

</details>

### Technical frame 2: Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00563))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00562))_

<a id="atom-technical-atom-b5e17c842f1f8e4e"></a>
```
const nothing = not(something);
```

### Technical frame 3: Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00571))_

> If that was all there was to it, composition wouldn't matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00570))_

<a id="atom-technical-atom-70f9079dd32050af"></a>
```
const compose = (a, b) => (c) => a(b(c));
const cookAndEat = compose(eat, cook);
```

### Technical frame 4: Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00572))_

> In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00571))_

<a id="atom-technical-atom-cfaa3155b7ac1dea"></a>
> The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

### Technical frame 5: Recipes with Basic Functions / Maybe

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

### Technical frame 6: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00691))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00686))_

<a id="atom-technical-atom-8520aae83218fd0d"></a>
```
return fn.apply(this, args)
}
}
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé: It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or ... [truncated]; Javascript shares technical record from Combinators and Function Decorators / function decorators: const compose = (a, b) => (c) => a(b(c)); const cookAndEat = compose(eat, cook); (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-recipe]] - shared statements and technical atoms: Recipe shares source evidence from Building Blocks / composition: In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring ... [truncated]; Recipe shares technical record from Recipes with Basic Functions / Maybe: const maybe = (fn) => function (...args) { if (args.length === 0) { return } else { for (let arg of args) { if (arg == null) return; } (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-combinator]] - shared statements and technical atoms: Combinator shares source evidence from Combinators and Function Decorators / function decorators: not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorator ... [truncated]; Combinator shares technical record from Combinators and Function Decorators / function decorators: const nothing = not(something); (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from Combinators and Function Decorators / function decorators: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from Combinators and Function Decorators / function decorators: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))

### Shared claims

- [[javascriptallonge-javascript-allong]] - shared statements: About JavaScript Allongé shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé: It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or ... [truncated] (1 shared statement(s))

### Topics

- [[javascriptallonge-function-decorator]] - narrower topic: Function Decorator shares source evidence from Combinators and Function Decorators / function decorators: not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorator ... [truncated]; Function Decorator shares technical record from Combinators and Function Decorators / function decorators: const nothing = not(something); (1 shared statement(s), 1 shared atom(s))

## Source

- [[javascriptallonge]]
