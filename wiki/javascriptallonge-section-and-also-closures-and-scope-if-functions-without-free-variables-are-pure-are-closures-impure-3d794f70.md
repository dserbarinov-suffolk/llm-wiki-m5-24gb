---
page_id: javascriptallonge-section-and-also-closures-and-scope-if-functions-without-free-variables-are-pure-are-closures-impure-3d794f70
page_kind: source
summary: And also: / Closures and Scope / if functions without free variables are pure, are closures impure?: 27 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-closures-and-scope-if-functions-without-free-variables-are-pure-are-closures-impure-3d794f70@889875b46f888e1a3e66cb150e7176df
---

# And also: / Closures and Scope / if functions without free variables are pure, are closures impure?

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-and-also-closures-and-scope-it-s-always-the-environment-3905285c]] - next source section: And also: / Closures and Scope / it's always the environment

### Source structure

- [[javascriptallonge-section-and-also-closures-and-scope-ff45d11c]] - broader source section: And also: / Closures and Scope

## Statements

- The function (y) => x is interesting. It contains a free variable , x . 27 A free variable is one that is not bound within the function. Up to now, we've only seen one way to 'bind' a variable, namely by passing in an argument with the same name. Since the function (y) => x doesn't have an argument named x , the variable x isn't bound in this function, which makes it 'free.' _(javascriptallonge.pdf (source-range-0e12e052-00338))_
- Now that we know that variables used in a function are either bound or free, we can bifurcate functions into those with free variables and those without: _(javascriptallonge.pdf (source-range-0e12e052-00339))_
- Functions containing no free variables are called pure functions . _(javascriptallonge.pdf (source-range-0e12e052-00340))_
- Functions containing one or more free variables are called closures . _(javascriptallonge.pdf (source-range-0e12e052-00341))_
- Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we've already seen: _(javascriptallonge.pdf (source-range-0e12e052-00342))_
- The first function doesn't have any variables, therefore doesn't have any free variables. The second doesn't have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ... , and it doesn't have a free variable: The only variable anywhere in its body is x , which is certainly bound within (x) => ... . _(javascriptallonge.pdf (source-range-0e12e052-00343))_
- From this, we learn something: A pure function can contain a closure. _(javascriptallonge.pdf (source-range-0e12e052-00344))_
- If pure functions can contain closures, can a closure contain a pure function? Using only what we've learned so far, attempt to compose a closure that contains a pure function. If you can't, give your reasoning for why it's impossible. _(javascriptallonge.pdf (source-range-0e12e052-00346))_
- Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x . _(javascriptallonge.pdf (source-range-0e12e052-00347))_
- 27 You may also hear the term 'non-local variable.' Both are correct. _(javascriptallonge.pdf (source-range-0e12e052-00348))_
- 27 A free variable is one that is not bound within the function. _(javascriptallonge.pdf (source-range-0e12e052-00338))_
- has a free variable, but the entire expression refers to (x) => ... _(javascriptallonge.pdf (source-range-0e12e052-00343))_
- The second doesn't have any free variables, because its only variable is bound. _(javascriptallonge.pdf (source-range-0e12e052-00343))_
- , and it doesn't have a free variable: The only variable anywhere in its body is x , which is certainly bound within (x) => ... _(javascriptallonge.pdf (source-range-0e12e052-00343))_
- The first function doesn't have any variables, therefore doesn't have any free variables. _(javascriptallonge.pdf (source-range-0e12e052-00343))_
- The third one is actually two functions, one inside the other. _(javascriptallonge.pdf (source-range-0e12e052-00343))_
- Using only what we've learned so far, attempt to compose a closure that contains a pure function. _(javascriptallonge.pdf (source-range-0e12e052-00346))_

## Technical atoms

### Technical frame 1: And also: / Closures and Scope / if functions without free variables are pure, are closures impure?

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00346))_

> If pure functions can contain closures, can a closure contain a pure function? Using only what we've learned so far, attempt to compose a closure that contains a pure function. If you can't, give your reasoning for why it's impossible.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00345))_

<a id="atom-technical-atom-e32e1b6c17bb3ec8"></a>
> [Figure] (p.45)

### Technical frame 2: And also: / Closures and Scope / if functions without free variables are pure, are closures impure?

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00347))_

> Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00346))_

<a id="atom-technical-atom-e40f9d634f430538"></a>
> If pure functions can contain closures, can a closure contain a pure function?
