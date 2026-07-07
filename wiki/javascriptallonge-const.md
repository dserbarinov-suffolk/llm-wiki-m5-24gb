---
page_id: javascriptallonge-const
page_kind: concept
summary: Const: 6 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-const@68d27a4e1ac157a2ef5a287fc8e6992c
---

# Const

What [[javascriptallonge]] covers about const:

## Statements

### And also: / That Constant Coffee Craving / const and lexical scope

- This seems very straightforward, but alas, there are some semantics of binding names that we need to understand if we're to place const anywhere we like. The first thing to ask ourselves is, what happens if we use const to bind two different values to the 'same' name? _(javascriptallonge.pdf (source-range-c98ab3e6-00433))_

- Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-c98ab3e6-00447))_

### Reassignment / mixing let and const

- Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And: _(javascriptallonge.pdf (source-range-c98ab3e6-01159))_

- Shadowing a const with a let does not permit it to be rebound in its original scope. _(javascriptallonge.pdf (source-range-c98ab3e6-01161))_

### Reassignment / mixing let and const / var

- In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped. _(javascriptallonge.pdf (source-range-c98ab3e6-01176))_


## Technical atoms

### Technical frame 1: And also: / That Constant Coffee Craving / const and lexical scope

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00447))_

> Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00446))_

<a id="atom-technical-atom-32553b8a94b093c8"></a>
```
((diameter_fn) => {
const PI = 3;
return diameter_fn(2)
})(
(() => {
const PI = 3.14159265;
return (diameter) => diameter * PI
})()
)
//=> 6.2831853
```

### Technical frame 2: Reassignment / mixing let and const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01159))_

> Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01158))_

<a id="atom-technical-atom-73fcad6cbcb4f1b0"></a>
```
(() => {
let age = 49;
if (true) {
const age = 50;
}
age = 51;
return age;
})()
//=> 51
```

### Technical frame 3: Reassignment / mixing let and const

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01161))_

> Shadowing a const with a let does not permit it to be rebound in its original scope.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01160))_

<a id="atom-technical-atom-e61df7a501d78232"></a>
```
(() => {
const age = 49;
if (true) {
let age = 50;
}
age = 52;
return age;
})()
//=> ERROR: age is read-only
```


## Related pages

### Source structure

- [[javascriptallonge-section-and-also-that-constant-coffee-craving-const-37801120]] - source section: And also: / That Constant Coffee Craving / const shares source evidence from And also: / That Constant Coffee Craving / const: Another way to write our 'circumference' function would be to pass PI along with the diameter argument, something like this:; And also: / That Constant Coffee Craving / const shares technical record from And also: / That Constant Coffee Craving / const: (diameter, PI) => diameter * PI (11 shared statement(s), 10 shared atom(s))

### Shared technical atoms

- [[javascriptallonge-mixing]] - shared technical atoms: Mixing shares technical record from Reassignment / mixing let and const: (() => { let age = 49; if (true) { const age = 50; } age = 51; return age; })() //=> 51 (1 shared atom(s))

### Shared claims

- [[javascriptallonge-binding]] - shared statements: Binding shares source evidence from And also: / That Constant Coffee Craving / const and lexical scope: Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. (1 shared statement(s))
- [[javascriptallonge-lexical-scope]] - shared statements: Lexical Scope shares source evidence from And also: / That Constant Coffee Craving / const and lexical scope: Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. (1 shared statement(s))
- [[javascriptallonge-parameter]] - shared statements: Parameter shares source evidence from And also: / That Constant Coffee Craving / const and lexical scope: Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. (1 shared statement(s))

## Source

- [[javascriptallonge]]
