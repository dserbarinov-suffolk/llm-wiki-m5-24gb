---
page_id: javascriptallonge-decorator
page_kind: concept
summary: Decorator: 4 statement(s) and 8 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-decorator@de4b8e8ff8f6247044f289a7fa8162e0
---

# Decorator

What [[javascriptallonge]] covers about decorator:

## Statements

### A Pull of the Lever: Prefaces / About JavaScript Allongé

- It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or code-centric. JavaScript idioms like function combinators and decorators leverage JavaScript's power to make code easier to read, modify, debug and refactor. _(javascriptallonge.pdf (source-range-c98ab3e6-00020))_

### And also: / Combinators and Function Decorators / function decorators

- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-c98ab3e6-00573))_

### And also: / Building Blocks / composition

- In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument. _(javascriptallonge.pdf (source-range-c98ab3e6-00582))_

### Recipes with Basic Functions / Maybe

- Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation: _(javascriptallonge.pdf (source-range-c98ab3e6-00695))_


## Technical atoms

### Technical frame 1: And also: / Combinators and Function Decorators / combinators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00558))_

> In this book, we will be using a looser definition of 'combinator:' Higher-order pure functions that take only functions as arguments and return a function. We won't be strict about using only previously defined combinators in their construction.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00557))_

<a id="atom-technical-atom-34eed5cf99dd08a1"></a>
```text
combinators
The word 'combinator' has a precise technical meaning in mathematics:
'A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.'-Wikipedia 35
If we were learning Combinatorial Logic, we'd start with the most basic combinators like S , K , and I , and work up from there to practical combinators. We'd learn that the fundamental combinators are named after birds following the example of Raymond Smullyan's famous book To Mock a Mockingbird 36 .
35 https://en.wikipedia.org/wiki/Combinatory_logic
36 http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 35 | https://en.wikipedia.org/wiki/Combinatory_logic |
| 36 | http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20 |

</details>

### Technical frame 2: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00573))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00565))_

<a id="atom-technical-atom-ece2f4b7b92ce2c5"></a>
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

### Technical frame 3: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00573))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00572))_

<a id="atom-technical-atom-48b9732f10355b03"></a>
```
const nothing = not(something);
```

### Technical frame 4: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00581))_

> If that was all there was to it, composition wouldn't matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00580))_

<a id="atom-technical-atom-f640f6d4abf32482"></a>
```
const compose = (a, b) => (c) => a(b(c));
const cookAndEat = compose(eat, cook);
```

### Technical frame 5: And also: / Building Blocks / composition

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00582))_

> In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00581))_

<a id="atom-technical-atom-6409eab3891c8c8f"></a>
> The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

### Technical frame 6: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00703))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00696))_

<a id="atom-technical-atom-88add223b9628933"></a>
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

### Technical frame 7: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00695))_

> Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00697))_

<a id="atom-technical-atom-b584cc27a63d4a4f"></a>
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

### Technical frame 8: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00703))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00698))_

<a id="atom-technical-atom-6df57b17b341935d"></a>
```
return fn.apply(this, args)
}
}
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-recipe]] - shared statements and technical atoms: Recipe shares source evidence from And also: / Building Blocks / composition: In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring ... [truncated]; Recipe shares technical record from Recipes with Basic Functions / Maybe: const maybe = (fn) => function (...args) { if (args.length === 0) { return } else { for (let arg of args) { if (arg == null) return; } (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé: It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or ... [truncated]; Javascript shares technical record from And also: / Combinators and Function Decorators / function decorators: const compose = (a, b) => (c) => a(b(c)); const cookAndEat = compose(eat, cook); (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from And also: / Combinators and Function Decorators / combinators: combinators The word 'combinator' has a precise technical meaning in mathematics: 'A combinator is a higher-order function that uses only function application and ea ... [truncated] (2 shared atom(s))
- [[javascriptallonge-combinator]] - shared statements and technical atoms: Combinator shares source evidence from And also: / Combinators and Function Decorators / function decorators: not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorator ... [truncated]; Combinator shares technical record from And also: / Combinators and Function Decorators / function decorators: const nothing = not(something); (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-functional]] - shared technical atoms: Functional shares technical record from Recipes with Basic Functions / Maybe: 50 https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad 51 https://github.com/raganwald/andand (1 shared atom(s))
- [[javascriptallonge-programming]] - shared technical atoms: Programming shares technical record from Recipes with Basic Functions / Maybe: 50 https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad 51 https://github.com/raganwald/andand (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from And also: / Combinators and Function Decorators / function decorators: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))

### Shared claims

- [[javascriptallonge-javascript-allong]] - shared statements: About JavaScript Allongé shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé: It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or ... [truncated] (1 shared statement(s))

### Topics

- [[javascriptallonge-function-decorator]] - narrower topic: Function Decorator shares source evidence from And also: / Combinators and Function Decorators / function decorators: not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorator ... [truncated]; Function Decorator shares technical record from And also: / Combinators and Function Decorators / function decorators: const nothing = not(something); (1 shared statement(s), 1 shared atom(s))

## Source

- [[javascriptallonge]]
