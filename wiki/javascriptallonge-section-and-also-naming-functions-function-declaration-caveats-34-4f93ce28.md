---
page_id: javascriptallonge-section-and-also-naming-functions-function-declaration-caveats-34-4f93ce28
page_kind: source
summary: And also: / Naming Functions / function declaration caveats 34: 13 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-naming-functions-function-declaration-caveats-34-4f93ce28@fd15b086a322c86b8b68d297cd081c8d
---

# And also: / Naming Functions / function declaration caveats 34

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-and-also-naming-functions-function-declarations-b1342e2a]] - previous source section: And also: / Naming Functions / function declarations

### Source structure

- [[javascriptallonge-section-and-also-naming-functions-c9513a66]] - broader source section: And also: / Naming Functions

## Statements

- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-c98ab3e6-00543))_
- 34 A number of the caveats discussed here were described in Jyrly Zaytsev's excellent article Named function expressions demystified. _(javascriptallonge.pdf (source-range-c98ab3e6-00544))_
- Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization. _(javascriptallonge.pdf (source-range-c98ab3e6-00546))_
- Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. So this is a function declaration: _(javascriptallonge.pdf (source-range-c98ab3e6-00547))_
- The parentheses make this an expression, not a function declaration. _(javascriptallonge.pdf (source-range-c98ab3e6-00549))_
- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. _(javascriptallonge.pdf (source-range-c98ab3e6-00543))_
- Function declarations are not supposed to occur inside of blocks. _(javascriptallonge.pdf (source-range-c98ab3e6-00546))_
- Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. _(javascriptallonge.pdf (source-range-c98ab3e6-00547))_

## Technical atoms

### Technical frame 1: And also: / Naming Functions / function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00546))_

> Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00545))_

<a id="atom-technical-atom-0a43a2ced43dfe34"></a>
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

### Technical frame 2: And also: / Naming Functions / function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00547))_

> Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. So this is a function declaration:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00546))_

<a id="atom-technical-atom-6dca4ba4c64161ea"></a>
> Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

### Technical frame 3: And also: / Naming Functions / function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00549))_

> The parentheses make this an expression, not a function declaration.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00548))_

<a id="atom-technical-atom-10f60b81014128d0"></a>
```
function trueDat () { return true }
But this is not:
(function trueDat () { return true })
```
