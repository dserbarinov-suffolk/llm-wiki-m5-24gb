---
page_id: javascriptallonge-literal-object-syntax
page_kind: concept
summary: literal object syntax: 8 accepted assertion(s) and 10 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_380119f8ed2bf55b@e7a5468c89299d7d6a54d94c2933c3a3
---

# literal object syntax

Source: [[javascriptallonge]]

## Statements

- JavaScript has a literal syntax for creating objects. (javascriptallonge.pdf p.133)
- Two objects created with separate evaluations have differing identities, just like arrays:. (javascriptallonge.pdf p.133)
- Values contained within an object work just like values contained within an array, we access them by reference to the original:. (javascriptallonge.pdf p.133)
- Names needn't be alphanumeric strings. (javascriptallonge.pdf p.133)
- If the name is an alphanumeric string conforming to the same rules as names of variables, there's a simplified syntax for accessing the values:. (javascriptallonge.pdf p.133)
- Expressions can be used for keys as well. (javascriptallonge.pdf p.134)
- It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:. (javascriptallonge.pdf p.135)
- (There are some other technical differences between binding a named function expression and using compact method syntax, but they are not relevant here. (javascriptallonge.pdf p.135-136)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
{ year: 2012, month: 6, day: 14 }
```

<a id="atom-2"></a>
**Atom:** code block

```
{ year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 }
//=> false
Objects use [] to access the values by name, using a string:
{ year: 2012, month: 6, day: 14 }['day']
//=> 14
```

<a id="atom-3"></a>
**Atom:** code block

```
const unique = () => [],
x = unique(),
y = unique(),
z = unique(),
o = { a: x, b: y, c: z };
o['a'] === x && o['b'] === y && o['c'] === z
//=> true
```

<a id="atom-4"></a>
**Atom:** code block

```
{ 'first name': 'reginald', 'last name': 'lewis' }['first name']
//=> 'reginald'
```

<a id="atom-5"></a>
**Atom:** code block

```
const date = { year: 2012, month: 6, day: 14 };
date['day'] === date.day
//=> true
```

<a id="atom-6"></a>
**Atom:** code block

```
{
["p" + "i"]: 3.14159265
}
//=> {"pi":3.14159265}
```

<a id="atom-7"></a>
**Atom:** code block

```
const Mathematics = {
abs: (a) => a < 0 ? -a : a
};
Mathematics.abs(-5)
//=> 5
```

<a id="atom-8"></a>
**Atom:** code block

```
const SecretDecoderRing = {
encode: function (plaintext) {
return plaintext
.split('')
.map( char => char.charCodeAt() )
.map( code => code + 1 )
.map( code => String.fromCharCode(code) )
.join('');
},
decode: function (cyphertext) {
return cyphertext
.split('')
.map( char => char.charCodeAt() )
.map( code => code - 1 )
.map( code => String.fromCharCode(code) )
.join('');
}
}
```

<a id="atom-9"></a>
**Atom:** code block

```
const SecretDecoderRing = {
encode: function encode (plaintext) {
return plaintext
.split('')
.map( char => char.charCodeAt() )
.map( code => code + 1 )
.map( code => String.fromCharCode(code) )
.join('');
},
decode: function decode (cyphertext) {
return cyphertext
.split('')
.map( char => char.charCodeAt() )
.map( code => code - 1 )
.map( code => String.fromCharCode(code) )
.join('');
}
}
```

<a id="atom-10"></a>
**Atom:** code block

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
