---
page_id: javascriptallonge-section-function-declaration-caveats-34-62da382e
page_kind: source
summary: function declaration caveats 34: 13 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-function-declaration-caveats-34-62da382e@7cdf3d0d7549059b4204272bfa605163
---

# function declaration caveats 34

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-function-declarations-c6aff434]] - previous source section: function declarations

## Statements

- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-c98ab3e6-00533))_
- 34 A number of the caveats discussed here were described in Jyrly Zaytsev's excellent article Named function expressions demystified. _(javascriptallonge.pdf (source-range-c98ab3e6-00534))_
- Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization. _(javascriptallonge.pdf (source-range-c98ab3e6-00536))_
- Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. So this is a function declaration: _(javascriptallonge.pdf (source-range-c98ab3e6-00537))_
- The parentheses make this an expression, not a function declaration. _(javascriptallonge.pdf (source-range-c98ab3e6-00539))_
- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. _(javascriptallonge.pdf (source-range-c98ab3e6-00533))_
- Function declarations are not supposed to occur inside of blocks. _(javascriptallonge.pdf (source-range-c98ab3e6-00536))_
- Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. _(javascriptallonge.pdf (source-range-c98ab3e6-00537))_

## Technical atoms

### Technical frame 1: function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00536))_

> Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00535))_

<a id="atom-technical-atom-68d5663ef5a9981c"></a>
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

### Technical frame 2: function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00537))_

> Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. So this is a function declaration:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00536))_

<a id="atom-technical-atom-f6e9174305a8c36c"></a>
> Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

### Technical frame 3: function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00539))_

> The parentheses make this an expression, not a function declaration.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00538))_

<a id="atom-technical-atom-edf9e0a9b8803541"></a>
```
function trueDat () { return true }
But this is not:
(function trueDat () { return true })
```
