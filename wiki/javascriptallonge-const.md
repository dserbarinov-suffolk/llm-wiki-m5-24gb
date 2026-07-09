---
page_id: javascriptallonge-const
page_kind: concept
summary: const: 11 accepted assertion(s) and 10 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_97356ebb25f2546d@18a037041a65b28884bb548a11da98b5
---

# const

Source: [[javascriptallonge]]

## Statements

- Another way to write our 'circumference' function would be to pass PI along with the diameter argument, something like this:. (javascriptallonge.pdf p.51)
- This differs from our example above in that there is only one environment, rather than two. (javascriptallonge.pdf p.52)
- We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name. (javascriptallonge.pdf p.52)
- JavaScript gives us a way to do that, the const keyword. (javascriptallonge.pdf p.52)
- We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const :. (javascriptallonge.pdf p.52)
- That's much better than what we were writing. (javascriptallonge.pdf p.52)
- We use the const keyword in a const statement . (javascriptallonge.pdf p.52)
- We can bind any expression. (javascriptallonge.pdf p.53)
- A name that's bound to a function is a valid expression evaluating to a function. (javascriptallonge.pdf p.53)
- Amazing how such an important idea-naming functions- can be explained en passant in just a few words. (javascriptallonge.pdf p.53)
- 30 We're into the second chapter and we've finally named a function. (javascriptallonge.pdf p.53)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
(diameter, PI) => diameter * PI
```

<a id="atom-2"></a>
**Atom:** code block

```
((diameter, PI) => diameter * PI)(2, 3.14159265)
//=> 6.2831853
```

<a id="atom-3"></a>
**Atom:** code block

```
(diameter) => {
const PI = 3.14159265;
return diameter * PI
}
```

<a id="atom-4"></a>
**Atom:** code block

```
((diameter) =>
((PI) =>
```

<a id="atom-5"></a>
**Atom:** code block

```
diameter * PI)(3.14159265))(2)
Or:
((diameter, PI) => diameter * PI)(2, 3.14159265)
```

<a id="atom-6"></a>
**Atom:** code block

```
//=> 6.2831853
```

<a id="atom-7"></a>
**Atom:** code block

```
((diameter) => {
const PI = 3.14159265;
return diameter * PI
})(2)
//=> 6.2831853
```

<a id="atom-8"></a>
**Atom:** code block

```
(d) => {
const calc = (diameter) => {
const PI = 3.14159265;
return diameter * PI
};
return "The circumference is " + calc(d)
}
```

<a id="atom-9"></a>
**Atom:** rule

```
This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () .
```

<a id="atom-10"></a>
**Atom:** code block

```
(d) => {
const PI
= 3.14159265,
calc = (diameter) => diameter * PI;
return "The circumference is " + calc(d)
}
```
