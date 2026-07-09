---
page_id: javascriptallonge-recipe
page_kind: concept
summary: Recipe: 5 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-recipe@3b627f7576639807b3af6889357f40b6
---

# Recipe

What [[javascriptallonge]] covers about recipe:

## Statements

### Building Blocks / composition

- In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument. _(javascriptallonge.pdf (source-range-c98ab3e6-00572))_

### Recipes with Basic Functions / Disclaimer

- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven't been discussed in the text to this point, such as methods and/or prototypes. The overall use of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-c98ab3e6-00640))_

### Recipes with Basic Functions / Partial Application

- These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic. _(javascriptallonge.pdf (source-range-c98ab3e6-00643))_

### Recipes with Basic Functions / Maybe

- Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation: _(javascriptallonge.pdf (source-range-c98ab3e6-00683))_

### Recipes with Data / Disclaimer

- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven't been discussed in the text to this point, such as methods and/or prototypes. The overall use of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-c98ab3e6-01401))_


## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Partial Application

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00645))_

> As noted above, our partial recipe allows us to create functions that are partial applications of functions that are context aware. We'd need a different recipe if we wish to create partial applications of object methods.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00644))_

<a id="atom-technical-atom-bf9a96eab0c8c00a"></a>
```
const callFirst = (fn, larg) =>
function (...rest) {
return fn.call(this, larg, ...rest);
}
const callLast = (fn, rarg) =>
function (...rest) {
return fn.call(this, ...rest, rarg);
}
const greet = (me, you) =>
`Hello, ${you}, my name is ${me}`;
const heliosSaysHello = callFirst(greet, 'Helios');
heliosSaysHello('Eartha')
//=> 'Hello, Eartha, my name is Helios'
const sayHelloToCeline = callLast(greet, 'Celine');
sayHelloToCeline('Eartha')
//=> 'Hello, Celine, my name is Eartha'
```

### Technical frame 2: Recipes with Basic Functions / Maybe

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

### Technical frame 3: Recipes with Basic Functions / Maybe

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

### Technical frame 4: Recipes with Basic Functions / Maybe

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

### Source structure

- [[javascriptallonge-section-recipes-with-basic-functions-d7445960]] - source section: Recipes with Basic Functions
- [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-574b019e]] - source section: Recipes with Basic Functions / Left-Variadic Functions
- [[javascriptallonge-section-recipes-with-basic-functions-partial-application-70ce84b0]] - source section: Recipes with Basic Functions / Partial Application
- [[javascriptallonge-section-recipes-with-basic-functions-tap-51486e75]] - source section: Recipes with Basic Functions / Tap
- [[javascriptallonge-section-recipes-with-basic-functions-unary-d494fe78]] - source section: Recipes with Basic Functions / Unary
- [[javascriptallonge-section-recipes-with-data-4b3e2c99]] - source section: Recipes with Data
- [[javascriptallonge-section-recipes-with-data-flip-b1a8ea8d]] - source section: Recipes with Data / Flip
- [[javascriptallonge-section-recipes-with-data-flip-flipping-methods-852e9417]] - source section: Recipes with Data / Flip / flipping methods

### Shared technical atoms

- [[javascriptallonge-decorator]] - shared statements and technical atoms: Decorator shares source evidence from Building Blocks / composition: In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring ... [truncated]; Decorator shares technical record from Recipes with Basic Functions / Maybe: const maybe = (fn) => function (...args) { if (args.length === 0) { return } else { for (let arg of args) { if (arg == null) return; } (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-partial-application]] - shared statements and technical atoms: partial application shares source evidence from Recipes with Basic Functions / Partial Application: These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want ... [truncated]; partial application shares technical record from Recipes with Basic Functions / Partial Application: const callFirst = (fn, larg) => function (...rest) { return fn.call(this, larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call(this, ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from Recipes with Basic Functions / Partial Application: const callFirst = (fn, larg) => function (...rest) { return fn.call(this, larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call(this, ... [truncated] (1 shared atom(s))
- [[javascriptallonge-bind]] - shared technical atoms: Bind shares technical record from Recipes with Basic Functions / Partial Application: const callFirst = (fn, larg) => function (...rest) { return fn.call(this, larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call(this, ... [truncated] (1 shared atom(s))
- [[javascriptallonge-list]] - shared technical atoms: List shares technical record from Recipes with Basic Functions / Partial Application: const callFirst = (fn, larg) => function (...rest) { return fn.call(this, larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call(this, ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
