---
page_id: javascriptallonge-section-and-also-naming-functions-function-declaration-caveats-34-d724d0dc
page_kind: source
summary: And also: / Naming Functions / function declaration caveats 34: 13 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-naming-functions-function-declaration-caveats-34-d724d0dc@9881b5bd8e53c81542ed455251ec4865
---

# And also: / Naming Functions / function declaration caveats 34

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-naming-functions-cae91ee1]] - broader source section: And also: / Naming Functions
- [[javascriptallonge-section-and-also-naming-functions-function-declarations-94e43325]] - previous source section: And also: / Naming Functions / function declarations

## Statements

- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-0e12e052-00543))_
- 34 A number of the caveats discussed here were described in Jyrly Zaytsev's excellent article Named function expressions demystified. _(javascriptallonge.pdf (source-range-0e12e052-00544))_
- Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization. _(javascriptallonge.pdf (source-range-0e12e052-00546))_
- Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. So this is a function declaration: _(javascriptallonge.pdf (source-range-0e12e052-00547))_
- The parentheses make this an expression, not a function declaration. _(javascriptallonge.pdf (source-range-0e12e052-00549))_
- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. _(javascriptallonge.pdf (source-range-0e12e052-00543))_
- Function declarations are not supposed to occur inside of blocks. _(javascriptallonge.pdf (source-range-0e12e052-00546))_
- Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. _(javascriptallonge.pdf (source-range-0e12e052-00547))_

## Technical atoms

### Technical frame 1: And also: / Naming Functions / function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00546))_

> Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00545))_

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00547))_

> Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. So this is a function declaration:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00546))_

> Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

### Technical frame 3: And also: / Naming Functions / function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00549))_

> The parentheses make this an expression, not a function declaration.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00548))_

```
function trueDat () { return true }
But this is not:
(function trueDat () { return true })
```
