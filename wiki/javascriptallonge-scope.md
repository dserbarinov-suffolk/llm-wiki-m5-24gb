---
page_id: javascriptallonge-scope
page_kind: concept
summary: Scope: 2 statement(s) and 15 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-scope@0a2548c76998adad85d7f91e7bdb7c9e
---

# Scope

What [[javascriptallonge]] covers about scope:

## Statements

### And also: / Closures and Scope / shadowy variables from a shadowy planet

- When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor. _(javascriptallonge.pdf (source-range-c98ab3e6-00360))_


## Technical atoms

### Technical frame 1: And also: / Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00320))_

> The environment belonging to the function with signature (x) => ... becomes {x: 1, ...} , and the result of applying the function is another function value. It makes sense that the result value is a function, because the expression for (x) => ... 's body is:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00317))_

<a id="atom-technical-atom-e4d94fde69692549"></a>
```
((x) => (y) => x)(1)(2)
//=> 1
```

### Technical frame 2: And also: / Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00320))_

> The environment belonging to the function with signature (x) => ... becomes {x: 1, ...} , and the result of applying the function is another function value. It makes sense that the result value is a function, because the expression for (x) => ... 's body is:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00319))_

<a id="atom-technical-atom-ab0ea07f6bec952d"></a>
```
((x) => (y) => x)(1)
//=> [Function]
```

### Technical frame 3: And also: / Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00322))_

> So now we have a value representing that function. Then we're going to take the value of that function and apply it to the argument 2 , something like this:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00321))_

<a id="atom-technical-atom-d98f02450e768422"></a>
```
(y) => x
```

### Technical frame 4: And also: / Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00324))_

> So we seem to get a new environment {y: 2, ...} . How is the expression x going to be evaluated in that function's environment? There is no x in its environment, it must come from somewhere else.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00323))_

<a id="atom-technical-atom-6f973bd0e39629aa"></a>
```
((y) => x)(2)
```

### Technical frame 5: And also: / Closures and Scope

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00325))_

> This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from 'outside' of a function that are referenced inside a function. For example, here's the equivalent code in Ruby:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00326))_

<a id="atom-technical-atom-99dcb381f32a6b0b"></a>
```
lambda { |x|
lambda { |y| x }
}[1][2]
#=> 1
```

### Technical frame 6: And also: / Closures and Scope / if functions without free variables are pure, are closures impure?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00337))_

> Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00336))_

<a id="atom-technical-atom-aaca35d51fc517e3"></a>
> If pure functions can contain closures, can a closure contain a pure function?

### Technical frame 7: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00343))_

> (x) => x is called the I Combinator, or the Identity Function . (x) => (y) => x is called the K Combinator, or Kestrel . Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. a http://www.amzn.com/0192801422?tag=raganwald001-20

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00341))_

<a id="atom-technical-atom-7cd2e3295f4d04ba"></a>
> So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

### Technical frame 8: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00350))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00345))_

<a id="atom-technical-atom-5672c037e47a4143"></a>
```
bh
```

### Technical frame 9: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00350))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00347))_

<a id="atom-technical-atom-1bf92e9150c006ad"></a>
```
(x) =>
(y) =>
(z) => x + y + z
```

### Technical frame 10: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00350))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00349))_

<a id="atom-technical-atom-6fe6b5fb614bb8b4"></a>
```
(x, y, z) => x + y + z
```

### Technical frame 11: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00351))_

> The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00352))_

<a id="atom-technical-atom-07cf59cc21ab6fef"></a>
```
ah
bh
```

### Technical frame 12: And also: / Closures and Scope / shadowy variables from a shadowy planet

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00358))_

> The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x , it is ignored when evaluating x + y . JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00357))_

<a id="atom-technical-atom-b47eb83b86d8ebfa"></a>
```
(x) =>
(x, y) => x + y
```

### Technical frame 13: And also: / Closures and Scope / shadowy variables from a shadowy planet

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00360))_

> When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00359))_

<a id="atom-technical-atom-c23519ba9922cace"></a>
```
(x) =>
(x, y) =>
(w, z) =>
(w) =>
x + y + z
```

### Technical frame 14: And also: / Closures and Scope / which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00365))_

> JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00366))_

<a id="atom-technical-atom-6cb62b7189b018dc"></a>
> If you don't want your code to operate directly within the global environment, what can you do?

### Technical frame 15: And also: / Closures and Scope / which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00365))_

> JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00367))_

<a id="atom-technical-atom-8cdbcf80542c25d7"></a>
```
// top of the file
(() => {
// ... lots of JavaScript ...
})();
// bottom of the file
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from And also: / Closures and Scope / shadowy variables from a shadowy planet: When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is igno ... [truncated]; Javascript shares technical record from And also: / Closures and Scope / shadowy variables from a shadowy planet: (x) => (x, y) => x + y (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-closure]] - shared technical atoms: Closure shares technical record from And also: / Closures and Scope / if functions without free variables are pure, are closures impure?: If pure functions can contain closures, can a closure contain a pure function? (2 shared atom(s))
- [[javascriptallonge-evaluate]] - shared technical atoms: Evaluate shares technical record from And also: / Closures and Scope / it's always the environment: (x, y, z) => x + y + z (1 shared atom(s))
- [[javascriptallonge-programming]] - shared technical atoms: Programming shares technical record from And also: / Closures and Scope / it's always the environment: (x, y, z) => x + y + z (1 shared atom(s))
- [[javascriptallonge-pure]] - shared technical atoms: Pure shares technical record from And also: / Closures and Scope / if functions without free variables are pure, are closures impure?: If pure functions can contain closures, can a closure contain a pure function? (1 shared atom(s))

## Source

- [[javascriptallonge]]
