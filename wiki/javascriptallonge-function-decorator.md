---
page_id: javascriptallonge-function-decorator
page_kind: concept
summary: Function Decorator: 2 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-function-decorator@b3bfcbf65740796b4a77aef5c1f09dd9
---

# Function Decorator

What [[javascriptallonge]] covers about function decorator:

## Statements

### And also: / Combinators and Function Decorators / function decorators

- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-c98ab3e6-00573))_


## Technical atoms

### Technical frame 1: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00573))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00572))_

<a id="atom-technical-atom-48b9732f10355b03"></a>
```
const nothing = not(something);
```


## Related pages

### Source structure

- [[javascriptallonge-section-and-also-combinators-and-function-decorators-function-decorators-a89378c3]] - source section: And also: / Combinators and Function Decorators / function decorators shares source evidence from And also: / Combinators and Function Decorators / function decorators: So instead of writing !someFunction(42) , we can write not(someFunction)(42) . Hardly progress. But like compose , we could write either:; And also: / Combinators and Function Decorators / function decorators shares technical record from And also: / Combinators and Function Decorators / function decorators: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (3 shared statement(s), 5 shared atom(s))

### Shared technical atoms

- [[javascriptallonge-combinator]] - shared statements and technical atoms: Combinator shares source evidence from And also: / Combinators and Function Decorators / function decorators: not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorator ... [truncated]; Combinator shares technical record from And also: / Combinators and Function Decorators / function decorators: const nothing = not(something); (1 shared statement(s), 1 shared atom(s))

### Topics

- [[javascriptallonge-decorator]] - broader topic: Decorator shares source evidence from And also: / Combinators and Function Decorators / function decorators: not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorator ... [truncated]; Decorator shares technical record from And also: / Combinators and Function Decorators / function decorators: const nothing = not(something); (1 shared statement(s), 1 shared atom(s))

## Source

- [[javascriptallonge]]
