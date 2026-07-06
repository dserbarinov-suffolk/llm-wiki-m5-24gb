---
page_id: javascriptallonge-variable
page_kind: concept
summary: Variable: 3 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-variable@be3a513b4f98759f60833e5762b90950
---

# Variable

What [[javascriptallonge]] covers about variable:

## Statements

### And also: / variables and bindings

- But there's another reason for learning the word antidisestablishmentarianism : We might learn how prefixes and postfixes work in English grammar. It's the same thing with (x) => (y) => x . It has a certain important meaning in its own right, and it's also an excellent excuse to learn about functions that make functions, environments, variables, and more. _(javascriptallonge.pdf (source-range-c98ab3e6-00296))_

- In order to talk about how this works, we should agree on a few terms (you may already know them, but let's check-in together and 'synchronize our dictionaries'). The first x , the one in (x) => ... , is an argument . The y in function (y) ... is another argument. The second x , the one in => x , is not an argument, it's an expression referring to a variable . Arguments and variables work the same way whether we're talking about (x) => (y) => x or just plain (x) => x . _(javascriptallonge.pdf (source-range-c98ab3e6-00297))_

- The value of a variable when evaluated in an environment is the value bound to the variable's name in that environment, which is '2' _(javascriptallonge.pdf (source-range-c98ab3e6-00311))_


## Technical atoms

### Technical frame 1: And also: / variables and bindings

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00295))_

> (x) => (y) => x just looks crazy, as if we are learning English as a second language and the teacher promises us that soon we will be using words like antidisestablishmentarianism . Besides a desire to use long words to sound impressive, this is not going to seem attractive until we find ourselves wanting to discuss the role of the Church of England in 19th century British politics.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00294))_

<a id="atom-technical-atom-3ef90bd4cce342bd"></a>
```
(x) => (y) => x
```

### Technical frame 2: And also: / variables and bindings

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00309))_

> The value '2' is bound to the name 'x' in the environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00301))_

<a id="atom-technical-atom-71caad9251a6dc1e"></a>
```
((x) => x)(2)
//=> 2
```

### Technical frame 3: And also: / variables and bindings

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00309))_

> The value '2' is bound to the name 'x' in the environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00305))_

<a id="atom-technical-atom-97705926f590cf82"></a>
> - One sub-expression, (x) => x evaluates to a function.


## Related pages

### Shared technical atoms

- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from And also: / variables and bindings: (x) => (y) => x (2 shared atom(s))

## Source

- [[javascriptallonge]]
