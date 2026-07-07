---
page_id: javascriptallonge-binding
page_kind: concept
summary: Binding: 3 statement(s) and 8 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-binding@4d7b4cfe9f762685d179b434bb2acfb7
---

# Binding

What [[javascriptallonge]] covers about binding:

## Statements

### And also: / That Constant Coffee Craving / const and lexical scope

- Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-c98ab3e6-00447))_

### And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

- We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-c98ab3e6-00451))_

### Reassignment

- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment. _(javascriptallonge.pdf (source-range-c98ab3e6-01154))_


## Technical atoms

### Technical frame 1: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00460))_

> Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . Does that binding 'overwrite' the outer one? Will our function return 6 or 6.2831853 ? This is a book, you've already scanned ahead, so you know that the answer is no , the inner binding does not overwrite the outer binding:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00459))_

<a id="atom-technical-atom-7f4ba1b3dfbe5b5c"></a>
```
((PI) => {
((PI) => {})(3);
return (diameter) => diameter * PI;
})(3.14159265)
```

### Technical frame 2: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00462))_

> We say that when we bind a variable using a parameter inside another binding, the inner binding shadows the outer binding. It has effect inside its own scope, but does not affect the binding in the enclosing scope.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00461))_

<a id="atom-technical-atom-4878f2e3a529b233"></a>
```
((PI) => {
((PI) => {})(3);
return (diameter) => diameter * PI;
})(3.14159265)(2)
//=> 6.2831853
```

### Technical frame 3: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

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

### Technical frame 4: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00602))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00598))_

<a id="atom-technical-atom-5bb18c52a0c78571"></a>
```text
42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times.
43 We'll look at arrays and plain old javascript objects in depth later.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 42 | You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. |
| 43 | We'll look at arrays and plain old javascript objects in depth later. |

</details>

### Technical frame 5: Plain Old JavaScript Objects / literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01072))_

> (There are some other technical differences between binding a named function expression and using compact method syntax, but they are not relevant here. We will generally prefer compact method syntax whenever we can.)

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01071))_

<a id="atom-technical-atom-5fc0450b87f8fabc"></a>
```
const SecretDecoderRing = {
encode (plaintext) {
return plaintext
.split('')
.map( char => char.charCodeAt() )
.map( code => code + 1 )
.map( code => String.fromCharCode(code) )
.join('');
},
decode (cyphertext) {
return cyphertext
.split('')
.map( char => char.charCodeAt() )
.map( code => code - 1 )
.map( code => String.fromCharCode(code) )
.join('');
}
}
```

### Technical frame 6: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01149))_

> Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . We go from:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01148))_

<a id="atom-technical-atom-113c47faa991f857"></a>
```
(() => {
let age = 49;
if (true) {
let age = 50;
}
return age;
})()
//=> 49
```

### Technical frame 7: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01154))_

> Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01150))_

<a id="atom-technical-atom-137d15c932fddea1"></a>
```
{age: 49, '..': global-environment}
To:
{age: 50, '..': {age: 49, '..': global-environment}}
Then back to:
```

### Technical frame 8: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01154))_

> Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01151))_

<a id="atom-technical-atom-4e14a82a74557b9f"></a>
```
{age: 49, '..': global-environment}
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-bind]] - shared statements and technical atoms: Bind shares source evidence from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated]; Bind shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: ((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265) (1 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: ((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265) (2 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms: Object shares technical record from And also: / Magic Names / the function keyword: const SecretDecoderRing = { encode (plaintext) { return plaintext .split('') .map( char => char.charCodeAt() ) .map( code => code + 1 ) .map( code => String.fromChar ... [truncated] (2 shared atom(s))
- [[javascriptallonge-parameter]] - shared statements and technical atoms: Parameter shares source evidence from And also: / That Constant Coffee Craving / const and lexical scope: Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope.; Parameter shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: ((diameter) => { const PI = 3.14159265; (() => { const PI = 3; })(); return diameter * PI; })(2) //=> 6.2831853 (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from And also: / Magic Names / the function keyword: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-function-keyword]] - shared technical atoms: the function keyword shares technical record from And also: / Magic Names / the function keyword: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from And also: / Magic Names / the function keyword: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))

### Shared claims

- [[javascriptallonge-const]] - shared statements: Const shares source evidence from And also: / That Constant Coffee Craving / const and lexical scope: Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. (1 shared statement(s))
- [[javascriptallonge-lexical-scope]] - shared statements: Lexical Scope shares source evidence from And also: / That Constant Coffee Craving / const and lexical scope: Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. (1 shared statement(s))

## Source

- [[javascriptallonge]]
