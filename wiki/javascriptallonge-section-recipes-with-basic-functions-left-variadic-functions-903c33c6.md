---
page_id: javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-903c33c6
page_kind: source
summary: Recipes with Basic Functions / Left-Variadic Functions: 27 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-903c33c6@b939dcf99233aa523ca60390274a5921
---

# Recipes with Basic Functions / Left-Variadic Functions

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-recipes-with-basic-functions-once-b6523716]] - previous source section: Recipes with Basic Functions / Once

### Source structure

- [[javascriptallonge-section-recipes-with-basic-functions-8e785fac]] - broader source section: Recipes with Basic Functions
- [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-a-history-lesson-68e4d278]] - narrower source section: Recipes with Basic Functions / Left-Variadic Functions / a history lesson
- [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-left-variadic-destructuring-15603a30]] - narrower source section: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring
- [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-overcoming-limitations-ac492fac]] - narrower source section: Recipes with Basic Functions / Left-Variadic Functions / overcoming limitations

## Statements

- A variadic function is a function that is designed to accept a variable number of arguments. 52 In JavaScript, you can make a variadic function by gathering parameters. For example: _(javascriptallonge.pdf (source-range-c98ab3e6-00712))_
- This can be useful when writing certain kinds of destructuring algorithms. For example, we might want to have a function that builds some kind of team record. It accepts a coach, a captain, and an arbitrary number of players. Easy in ECMAScript 2015: _(javascriptallonge.pdf (source-range-c98ab3e6-00714))_
- 52 English is about as inconsistent as JavaScript: Functions with a fixed number of arguments can be unary, binary, ternary, and so forth. But can they be 'variary?' No! They have to be 'variadic.' _(javascriptallonge.pdf (source-range-c98ab3e6-00716))_
- ECMAScript 2015 only permits gathering parameters from the end of the parameter list. Not the beginning. What to do? _(javascriptallonge.pdf (source-range-c98ab3e6-00718))_
- For example, we might want to have a function that builds some kind of team record. _(javascriptallonge.pdf (source-range-c98ab3e6-00714))_
- ECMAScript 2015 only permits gathering parameters from the end of the parameter list. _(javascriptallonge.pdf (source-range-c98ab3e6-00718))_

## Statements by subsection

### Recipes with Basic Functions / Left-Variadic Functions / a history lesson

- In 'Ye Olde Days,' 53 JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice , or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. Here it is in all of its ECMAScript-5 glory: _(javascriptallonge.pdf (source-range-c98ab3e6-00720))_
- This is a right-variadic function , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument. _(javascriptallonge.pdf (source-range-c98ab3e6-00726))_

### Recipes with Basic Functions / Left-Variadic Functions / overcoming limitations

- That's a left-variadic function . All left-variadic functions have one or more fixed arguments, and the rest are gathered into the leftmost argument. JavaScript doesn't do this. But if we wanted to write left-variadic functions, could we make ourselves a leftVariadic decorator to turn a function with one or more arguments into a left-variadic function? _(javascriptallonge.pdf (source-range-c98ab3e6-00730))_
- Our leftVariadic function is a decorator that turns any function into a function that gathers parameters from the left , instead of from the right. _(javascriptallonge.pdf (source-range-c98ab3e6-00734))_

### Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

- Gathering arguments for functions is one of the ways JavaScript can destructure arrays. Another way is when assigning variables, like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00736))_
- But we can write our own left-gathering function utility using the same principles without all the tedium: _(javascriptallonge.pdf (source-range-c98ab3e6-00742))_
- With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function. _(javascriptallonge.pdf (source-range-c98ab3e6-00744))_

## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Left-Variadic Functions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00714))_

> This can be useful when writing certain kinds of destructuring algorithms. For example, we might want to have a function that builds some kind of team record. It accepts a coach, a captain, and an arbitrary number of players. Easy in ECMAScript 2015:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00713))_

<a id="atom-technical-atom-1c53848651757b7c"></a>
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

### Technical frame 2: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00744))_

> With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00743))_

<a id="atom-technical-atom-a9bce88607965551"></a>
```
const leftGather = (outputArrayLength) => {
return function (inputArray) {
return [inputArray.slice(0, inputArray.length - outputArrayLength + 1)].conc\
at(
inputArray.slice(inputArray.length - outputArrayLength + 1)
)
}
};
const [butLast, last] = leftGather(2)(['why', 'hello', 'there', 'little', 'droid\
']);
butLast
//=> ['why', 'hello', 'there', 'little']
last
//=> 'droid'
```
