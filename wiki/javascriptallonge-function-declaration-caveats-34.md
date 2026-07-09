---
page_id: javascriptallonge-function-declaration-caveats-34
page_kind: concept
summary: function declaration caveats 34: 7 accepted assertion(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_5bb386ecb5d39b85@3fe336e51cefc02e87da70610c981939
---

# function declaration caveats 34

Source: [[javascriptallonge]]

## Statements

- Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea:. (javascriptallonge.pdf p.66)
- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. (javascriptallonge.pdf p.66)
- 34 A number of the caveats discussed here were described in Jyrly Zaytsev's excellent article Named function expressions demystified. (javascriptallonge.pdf p.66)
- Function declarations are not supposed to occur inside of blocks. (javascriptallonge.pdf p.67)
- The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. (javascriptallonge.pdf p.67)
- Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. (javascriptallonge.pdf p.67)
- The parentheses make this an expression, not a function declaration. (javascriptallonge.pdf p.67)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
(function (camelCase) {
return fizzbuzz();
if (camelCase) {
function fizzbuzz () {
return "Fizz" + "Buzz";
}
}
else {
function fizzbuzz () {
return "Fizz" + "Buzz";
}
}
})(true)
//=> 'FizzBuzz'? Or ERROR: Can't find variable: fizzbuzz?
```

<a id="atom-2"></a>
**Atom:** rule

```
Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.
```

<a id="atom-3"></a>
**Atom:** code block

```
function trueDat () { return true }
But this is not:
(function trueDat () { return true })
```
