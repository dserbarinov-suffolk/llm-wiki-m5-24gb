---
page_id: javascriptallonge-kestrel-and-the-idiot
page_kind: concept
summary: the kestrel and the idiot: 7 accepted assertion(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_40b20d1a91d8a154@934af5e10cceef48c60ff31bc01c38b1
---

# the kestrel and the idiot

Source: [[javascriptallonge]]

## Statements

- A constant function is a function that always returns the same thing, no matter what you give it. (javascriptallonge.pdf p.179)
- For example, (x) => 42 is a constant function that always evaluates to 42. (javascriptallonge.pdf p.179)
- The kestrel, or K , is a function that makes constant functions. (javascriptallonge.pdf p.179)
- You give it a value, and it returns a constant function that gives that value. (javascriptallonge.pdf p.179)
- The identity function is a function that evaluates to whatever parameter you pass it. (javascriptallonge.pdf p.179)
- Given two values, we can say that K always returns the first value: K(x)(y) => x (that's not valid JavaScript, but it's essentially how it works). (javascriptallonge.pdf p.179)
- Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value. (javascriptallonge.pdf p.180)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const K = (x) => (y) => x;
const fortyTwo = K(42);
fortyTwo(6)
//=> 42
fortyTwo("Hello")
//=> 42
```

<a id="atom-2"></a>
**Atom:** code block

```
K(6)(7)
//=> 6
K(12)(24)
//=> 12
```

<a id="atom-3"></a>
**Atom:** code block

```
Therefore, K(I)(x)(y) => y:
```

<a id="atom-4"></a>
**Atom:** code block

```
K(I)(6)(7)
//=> 7
K(I)(12)(24)
//=> 24
```

<a id="atom-5"></a>
**Atom:** code block

```
K("primus")("secundus")
//=> "primus"
K(I)("primus")("secundus")
//=> "secundus"
```

<a id="atom-6"></a>
**Atom:** code block

```
const first = K,
second = K(I);
first("primus")("secundus")
//=> "primus"
second("primus")("secundus")
//=> "secundus"
```
