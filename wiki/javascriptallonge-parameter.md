---
page_id: javascriptallonge-parameter
page_kind: concept
summary: Parameter: 6 statement(s) and 10 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-parameter@5166b58585be7a3d5ed5888f4e77d92b
---

# Parameter

What [[javascriptallonge]] covers about parameter:

## Statements

### const and lexical scope

- Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-c98ab3e6-00447))_

### are consts also from a shadowy planet?

- We just saw that values bound with const use lexical scope, just like values bound with parameters. They are looked up in the environment where they are declared. And we know that functions create environments. Parameters are declared when we create functions, so it makes sense that parameters are bound to environments created when we invoke functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00449))_

- Parameters are only bound when we invoke a function. That's why we made all these IIFEs. But const statements can appear inside blocks. What happens when we use a const inside of a block? We'll need a gratuitous block. We've seen if statements, what could be more gratuitous than: _(javascriptallonge.pdf (source-range-c98ab3e6-00466))_

### Left-Variadic Functions

- ECMAScript 2015 only permits gathering parameters from the end of the parameter list. Not the beginning. What to do? _(javascriptallonge.pdf (source-range-c98ab3e6-00706))_

### default arguments

- By writing our parameter list as (n, work = 1) => , we're stating that if a second parameter is not provided, work is to be bound to 1 . We can do similar things with our other tail-recursive functions: _(javascriptallonge.pdf (source-range-c98ab3e6-00988))_

### the vireo

- Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data. For arrays, we'd write cons = (first, second) => [first, second] . For objects we'd write: cons = (first, second) => {first, second} . In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-c98ab3e6-01338))_


## Technical atoms

### Technical frame 1: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00458))_

> And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the 'outer' environment? Let's rewrite things slightly differently:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00453))_

<a id="atom-technical-atom-6bd217294d9f9ffc"></a>
```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```

### Technical frame 2: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00466))_

> Parameters are only bound when we invoke a function. That's why we made all these IIFEs. But const statements can appear inside blocks. What happens when we use a const inside of a block? We'll need a gratuitous block. We've seen if statements, what could be more gratuitous than:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00464))_

<a id="atom-technical-atom-b2847d0a5b987159"></a>
```
((diameter) => {
const PI = 3.14159265;
(() => {
const PI = 3;
})();
return diameter * PI;
})(2)
//=> 6.2831853
```

### Technical frame 3: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00474))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00467))_

<a id="atom-technical-atom-fa9d38a0f871166d"></a>
```
if (true) {
// an immediately invoked block statement (IIBS)
}
Let’s try it:
((diameter) => {
const PI = 3;
if (true) {
const PI = 3.14159265;
return diameter * PI;
}
})(2)
//=> 6.2831853
((diameter) => {
const PI = 3.14159265;
if (true) {
const PI = 3;
}
return diameter * PI;
```

### Technical frame 4: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00474))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00468))_

<a id="atom-technical-atom-c164dd0fd5dca0c5"></a>
```
})(2)
//=> 6.2831853
```

### Technical frame 5: Left-Variadic Functions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00702))_

> This can be useful when writing certain kinds of destructuring algorithms. For example, we might want to have a function that builds some kind of team record. It accepts a coach, a captain, and an arbitrary number of players. Easy in ECMAScript 2015:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00701))_

<a id="atom-technical-atom-f8f8ac50da4371b1"></a>
```
const abccc = (a, b, ...c) => {
console.log(a);
console.log(b);
console.log(c);
};
abccc(1, 2, 3, 4, 5)
1
2
[3,4,5]
```

### Technical frame 6: destructuring parameters

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00858))_

> It looks like destructuring. It acts like destructuring. There is only one difference: We have not tried gathering. Let's do that:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00855))_

<a id="atom-technical-atom-4f625caf41adf771"></a>
```
foo()
bar("smaug")
baz(1, 2, 3)
```

### Technical frame 7: destructuring parameters

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00858))_

> It looks like destructuring. It acts like destructuring. There is only one difference: We have not tried gathering. Let's do that:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00857))_

<a id="atom-technical-atom-ffb8d12f5e160d9a"></a>
```
const foo = () => ...
const bar = (name) => ...
const baz = (a, b, c) => ...
```

### Technical frame 8: default arguments

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00990))_

> Now we don't need to use two functions. A default argument is concise and readable.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00989))_

<a id="atom-technical-atom-73987d80bbe79c69"></a>
```
const length = ([first, ...rest], numberToBeAdded = 0) =>
first === undefined
? numberToBeAdded
: length(rest, 1 + numberToBeAdded)
length(["foo", "bar", "baz"])
//=> 3
const mapWith = (fn, [first, ...rest], prepend = []) =>
first === undefined
? prepend
: mapWith(fn, rest, [...prepend, fn(first)]);
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Technical frame 9: the vireo

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01341))_

> For consistency with the way combinators are written as functions taking just one parameter, we'll curry 78 the function:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01340))_

<a id="atom-technical-atom-590de5a88990b16d"></a>
```
(first, second) => (selector) => selector(first)(second)
```

### Technical frame 10: the vireo

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01348))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01342))_

<a id="atom-technical-atom-1e1971c4388c6edb"></a>
```
(first) => (second) => (selector) => selector(first)(second)
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-statement]] - shared technical atoms: Statement shares technical record from are consts also from a shadowy planet?: if (true) { // an immediately invoked block statement (IIBS) } Let’s try it: ((diameter) => { const PI = 3; if (true) { const PI = 3.14159265; return diameter * PI; ... [truncated] (2 shared atom(s))
- [[javascriptallonge-binding]] - shared statements and technical atoms: Binding shares source evidence from const and lexical scope: Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope.; Binding shares technical record from are consts also from a shadowy planet?: ((diameter) => { const PI = 3.14159265; (() => { const PI = 3; })(); return diameter * PI; })(2) //=> 6.2831853 (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from default arguments: By writing our parameter list as (n, work = 1) => , we're stating that if a second parameter is not provided, work is to be bound to 1 . We can do similar things wit ... [truncated]; List shares technical record from default arguments: const length = ([first, ...rest], numberToBeAdded = 0) => first === undefined ? numberToBeAdded : length(rest, 1 + numberToBeAdded) length(["foo", "bar", "baz"]) //= ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-bind]] - shared technical atoms: Bind shares technical record from are consts also from a shadowy planet?: ((diameter) => { const PI = 3.14159265; (() => { const PI = 3; })(); return diameter * PI; })(2) //=> 6.2831853 (1 shared atom(s))
- [[javascriptallonge-data]] - shared technical atoms: Data shares technical record from the vireo: (first, second) => (selector) => selector(first)(second) (1 shared atom(s))
- [[javascriptallonge-structure]] - shared technical atoms: Structure shares technical record from the vireo: (first, second) => (selector) => selector(first)(second) (1 shared atom(s))

### Shared claims

- [[javascriptallonge-const]] - shared statements: Const shares source evidence from const and lexical scope: Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. (1 shared statement(s))
- [[javascriptallonge-ecmascript]] - shared statements: Ecmascript shares source evidence from Left-Variadic Functions: ECMAScript 2015 only permits gathering parameters from the end of the parameter list. Not the beginning. What to do? (1 shared statement(s))
- [[javascriptallonge-lexical-scope]] - shared statements: Lexical Scope shares source evidence from const and lexical scope: Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements: Return shares source evidence from the vireo: Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data. ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
