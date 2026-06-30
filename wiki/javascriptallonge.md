---
page_id: javascriptallonge
page_kind: source
summary: Claim-ledger projection (coding): 2043 usable entries, 661 technical atoms, 373 needs-review, 286 linked page(s); write decision write-with-review-work.
page_family: source-manifest
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: sources
source_id: javascriptallonge.pdf
projection_coverage: projection-coverage-58c39ea10bb8ad18@1608c864086a21b3
---

# A Pull of the Lever: Prefaces

### JavaScript Allongé, the 'Six' Edition

#### Programming from Functions to Classes in ECMAScript 2015

#### Reg 'raganwald' Braithwaite

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00005))_

> This version was published on 2017-11-03

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00006))_

> [Figure] (p.2)

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00009))_

| A Pull of the Lever: Prefaces................................... | i |
| --- | --- |
| About JavaScript Allongé................................... | ii |
| What JavaScript Allongé is. And isn’t............................. | v |
| Foreword to the “Six” edition................................. | viii |
| Forewords to the First Edition................................. | ix |
| About The Sample PDF.................................... | xi |
| Prelude: Values and Expressions over Coffee......................... | xiii |
| values are expressions..................................... | xiv |
| values and identity....................................... | xvi |
| A Rich Aroma: Basic Numbers.................................. | 1 |
| The first sip: Basic Functions................................... | 5 |
| As Little As Possible About Functions, But No Less..................... | 7 |
| Ah. I’d Like to Have an Argument, Please........................... | 16 |
| Closures and Scope...................................... | 21 |
| That Constant Coffee Craving................................ | 26 |
| Naming Functions....................................... | 39 |
| Combinators and Function Decorators............................ | 45 |
| Building Blocks........................................ | 48 |
| Magic Names.......................................... | 51 |
| Summary............................................ | 55 |
| Recipes with Basic Functions.................................. | 56 |
| Partial Application....................................... | 57 |
| Unary.............................................. | 59 |
| Tap............................................... | 61 |
| Maybe............................................. | 63 |
| Once.............................................. | 65 |
| Left-Variadic Functions.................................... | 66 |
| Picking the Bean: Choice and Truthiness............................ | 71 |

<details>
<summary>Raw table text</summary>

```text
Contents
| A Pull of the Lever: Prefaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | i |
| --- | --- |
| About JavaScript Allongé . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ii |
| What JavaScript Allongé is. And isn’t. . . . . . . . . . . . . . . . . . . . . . . . . . . . . | v |
| Foreword to the “Six” edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | viii |
| Forewords to the First Edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | ix |
| About The Sample PDF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xi |
| Prelude: Values and Expressions over Coffee . . . . . . . . . . . . . . . . . . . . . . . . . | xiii |
| values are expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xiv |
| values and identity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | xvi |
| A Rich Aroma: Basic Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 1 |
| The first sip: Basic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 5 |
| As Little As Possible About Functions, But No Less . . . . . . . . . . . . . . . . . . . . . | 7 |
| Ah. I’d Like to Have an Argument, Please. . . . . . . . . . . . . . . . . . . . . . . . . . . | 16 |
| Closures and Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 21 |
| That Constant Coffee Craving . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 26 |
| Naming Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 39 |
| Combinators and Function Decorators . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 45 |
| Building Blocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 48 |
| Magic Names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 51 |
| Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 55 |
| Recipes with Basic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 56 |
| Partial Application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 57 |
| Unary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 59 |
| Tap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 61 |
| Maybe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 63 |
| Once . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 65 |
| Left-Variadic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 66 |
| Picking the Bean: Choice and Truthiness . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 71 |
```

</details>

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00010))_

| Composing and Decomposing Data....... | ........................ | 77 |
| --- | --- | --- |
| Arrays and Destructuring Arguments.... | ........................ | 78 |
| Self-Similarity................. | ........................ | 86 |
| Tail Calls (and Default Arguments)...... | ........................ | 94 |
| Garbage, Garbage Everywhere........ | ........................ | 103 |
| Plain Old JavaScript Objects......... | ........................ | 109 |
| Mutation.................... | ........................ | 118 |
| Reassignment................. | ........................ | 125 |
| Copy on Write................. | ........................ | 135 |
| Tortoises, Hares, and Teleporting Turtles... | ........................ | 141 |
| Functional Iterators.............. | ........................ | 144 |
| Making Data Out Of Functions........ | ........................ | 154 |
| Recipes with Data................. | ........................ | 168 |
| mapWith.................... | ........................ | 170 |
| Flip....................... | ........................ | 172 |
| Object.assign.................. | ........................ | 175 |
| Why?...................... | ........................ | 178 |
| A Warm Cup: Basic Strings and Quasi-Literals | ........................ | 179 |
| Served by the Pot: Collections.......... | ........................ | 182 |
| Iteration and Iterables............. | ........................ | 183 |
| Generating Iterables.............. | ........................ | 201 |
| Lazy and Eager Collections.......... | ........................ | 223 |
| Interlude: The Carpenter Interviews for a Job | ........................ | 238 |
| Interactive Generators............. | ........................ | 250 |
| Basic Operations on Iterables......... | ........................ | 261 |
| The Golden Crema: Appendices and Afterwords | ....................... | 265 |
| How to run the examples........... | ........................ | 266 |
| Thanks!..................... | ........................ | 268 |
| Copyright Notice................ | ........................ | 270 |
| About The Author............... | ........................ | 274 |

<details>
<summary>Raw table text</summary>

```text
Contents
| Composing and Decomposing Data . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 77 |
| --- | --- | --- |
| Arrays and Destructuring Arguments . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 78 |
| Self-Similarity . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 86 |
| Tail Calls (and Default Arguments) . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 94 |
| Garbage, Garbage Everywhere . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 103 |
| Plain Old JavaScript Objects . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 109 |
| Mutation . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 118 |
| Reassignment . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 125 |
| Copy on Write . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 135 |
| Tortoises, Hares, and Teleporting Turtles . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 141 |
| Functional Iterators . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 144 |
| Making Data Out Of Functions . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 154 |
| Recipes with Data . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 168 |
| mapWith . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 170 |
| Flip . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 172 |
| Object.assign . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 175 |
| Why? . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 178 |
| A Warm Cup: Basic Strings and Quasi-Literals | . . . . . . . . . . . . . . . . . . . . . . . . | 179 |
| Served by the Pot: Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 182 |
| Iteration and Iterables . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 183 |
| Generating Iterables . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 201 |
| Lazy and Eager Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 223 |
| Interlude: The Carpenter Interviews for a Job | . . . . . . . . . . . . . . . . . . . . . . . . | 238 |
| Interactive Generators . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 250 |
| Basic Operations on Iterables . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 261 |
| The Golden Crema: Appendices and Afterwords | . . . . . . . . . . . . . . . . . . . . . . . | 265 |
| How to run the examples . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 266 |
| Thanks! . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 268 |
| Copyright Notice . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 270 |
| About The Author . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 274 |
```

</details>

## A Pull of the Lever: Prefaces

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00012))_

> [Figure] (p.6)

#### About JavaScript Allongé

- It's written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope. _(javascriptallonge.pdf (source-range-0e12e052-00018))_
- JavaScript Allongé is a first and foremost, a book about programming with functions . _(javascriptallonge.pdf (source-range-0e12e052-00018))_
- It's written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope. _(javascriptallonge.pdf (source-range-0e12e052-00018))_
- JavaScript Allongé begins at the beginning, with values and expressions, and builds from there to discuss types, identity, functions, closures, scopes, collections, iterators, and many more subjects up to working with classes and instances. _(javascriptallonge.pdf (source-range-0e12e052-00019))_
- JavaScript idioms like function combinators and decorators leverage JavaScript's power to make code easier to read, modify, debug and refactor. _(javascriptallonge.pdf (source-range-0e12e052-00020))_
- It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or code-centric. _(javascriptallonge.pdf (source-range-0e12e052-00020))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00018))_

> If those terms seem unfamiliar, don't worry: JavaScript Allongé takes great delight in explaining what they mean and why they matter.

##### why the 'six' edition?

- Features like destructuring, block-structured variables, iterables, generators, and the class keyword are poised to make JavaScript programming more expressive. _(javascriptallonge.pdf (source-range-0e12e052-00023))_
- ECMAScript 2015 (formerly called ECMAScript 6 or 'ES6'), is ushering in a very large number of improvements to the way programmers can write small, powerful components and combine them into larger, fully featured programs. _(javascriptallonge.pdf (source-range-0e12e052-00023))_
- For example, JavaScript did not include block-structured variables. _(javascriptallonge.pdf (source-range-0e12e052-00024))_
- Over time, programmers discovered ways to roll their own versions of important features. _(javascriptallonge.pdf (source-range-0e12e052-00024))_
- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. _(javascriptallonge.pdf (source-range-0e12e052-00024))_
- For example, JavaScript did not include block-structured variables. _(javascriptallonge.pdf (source-range-0e12e052-00024))_
- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. _(javascriptallonge.pdf (source-range-0e12e052-00024))_
- And the variable i is scoped locally to the code within the braces. _(javascriptallonge.pdf (source-range-0e12e052-00027))_
- Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write: _(javascriptallonge.pdf (source-range-0e12e052-00027))_
- And the variable i is scoped locally to the code within the braces. _(javascriptallonge.pdf (source-range-0e12e052-00027))_
- Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write: _(javascriptallonge.pdf (source-range-0e12e052-00027))_
- Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. _(javascriptallonge.pdf (source-range-0e12e052-00030))_
- Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like: _(javascriptallonge.pdf (source-range-0e12e052-00032))_
- Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like: _(javascriptallonge.pdf (source-range-0e12e052-00032))_
- The first edition of JavaScript Allongé explained these and many other patterns for writing flexible and composable programs in JavaScript, but the intention wasn't to explain how to work around JavaScript's missing features: The intention was to explain why the style of programming exemplified by the missing features is important. _(javascriptallonge.pdf (source-range-0e12e052-00034))_
- Working around the missing features was a necessary evil. _(javascriptallonge.pdf (source-range-0e12e052-00035))_
- But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. _(javascriptallonge.pdf (source-range-0e12e052-00036))_
- But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. _(javascriptallonge.pdf (source-range-0e12e052-00036))_
- And i is scoped to the for loop. _(javascriptallonge.pdf (source-range-0e12e052-00038))_
- Not having to work around these kinds of missing features makes JavaScript Allongé a better book , because it can focus on the why to do something and when to do it, instead of on the how to make it work _(javascriptallonge.pdf (source-range-0e12e052-00040))_
- Not having to work around these kinds of missing features makes JavaScript Allongé a better book , because it can focus on the why to do something and when to do it, instead of on the how to make it work _(javascriptallonge.pdf (source-range-0e12e052-00040))_
- JavaScript Allongé, The 'Six' Edition packs all the goodness of JavaScript Allongé into a new, updated package that is relevant for programmers working with (or planning to work with) the latest version of JavaScript. _(javascriptallonge.pdf (source-range-0e12e052-00041))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00025))_

> For example, block-structured languages allow us to write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00026))_

```
for (int i = 0; i < array.length; ++i) {
// ...
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00027))_

> And the variable i is scoped locally to the code within the braces. Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00028))_

```
var i;
for (i = 0; i < array.length; ++i) {
(function (i) {
// ...
})(i)
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00030))_

> Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Ruby, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00031))_

```
def foo (first, *rest)
# ...
end
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00032))_

> Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00033))_

```
function foo () {
var first = arguments[0],
rest
= [].slice.call(arguments, 1);
// ...
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00036))_

> But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. With ECMASCript 2015, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00037))_

```
for (let i = 0; i < array.length; ++i) {
// ...
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00038, source-range-0e12e052-00040))_

> And i is scoped to the for loop. We can also write: And presto, rest collects the rest of the arguments without a lot of malarky involving slicing arguments . Not having to work around these kinds of missing features makes JavaScript Allongé a better book , because it can focus on the why to do something and when to do it, instead of on the how to make it work

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00039))_

```
function foo (first, ...rest) {
// ...
}
```

##### that's nice. is that the only reason?

- If it were just a matter of updating the syntax, the original version of JavaScript Allongé could have simply iterated, slowly replacing old syntax with new. _(javascriptallonge.pdf (source-range-0e12e052-00044))_
- It would have continued to say much the same things, only with new syntax. _(javascriptallonge.pdf (source-range-0e12e052-00044))_
- It would have continued to say much the same things, only with new syntax. _(javascriptallonge.pdf (source-range-0e12e052-00044))_
- The original JavaScript Allongé was not just written to teach JavaScript: It was written to describe certain ideas in programming: Working with small, independent entities that compose together to make bigger programs. _(javascriptallonge.pdf (source-range-0e12e052-00045))_
- Thus, the focus on things like writing decorators. _(javascriptallonge.pdf (source-range-0e12e052-00045))_
- As noted above, JavaScript was chosen as the language for Allongé because it hit a sweet spot of having a large audience of programmers and having certain language features that happen to work well with this style of programming. _(javascriptallonge.pdf (source-range-0e12e052-00046))_
- As noted above, JavaScript was chosen as the language for Allongé because it hit a sweet spot of having a large audience of programmers and having certain language features that happen to work well with this style of programming. _(javascriptallonge.pdf (source-range-0e12e052-00046))_
- It makes a number of interesting programming techniques easy to explain and easy to use. _(javascriptallonge.pdf (source-range-0e12e052-00047))_
- ECMAScript 2015 does more than simply update the language with some simpler syntax for a few things and help us avoid warts. _(javascriptallonge.pdf (source-range-0e12e052-00047))_
- But the common thread that runs through all these things is that since they are all simple objects and simple functions, we can use the same set of 'programming with functions' techniques to build programs by composing small, flexible, and decoupled entities. _(javascriptallonge.pdf (source-range-0e12e052-00048))_
- Thus, the 'six' edition introduces classes and mixins. _(javascriptallonge.pdf (source-range-0e12e052-00048))_
- But even so, in a way it is still explaining the exact same original idea that programs are built out of small, flexible functions composed together. _(javascriptallonge.pdf (source-range-0e12e052-00050))_
- And introducing these new ideas did add substantially to its bulk. _(javascriptallonge.pdf (source-range-0e12e052-00050))_
- Introducing so many new ideas did require a major rethink of the way the book was organized. _(javascriptallonge.pdf (source-range-0e12e052-00050))_

#### What JavaScript Allongé is. And isn't.

- JavaScript Allongé is a book about programming with functions. _(javascriptallonge.pdf (source-range-0e12e052-00054))_
- The intention is to improve the way we think about programs. _(javascriptallonge.pdf (source-range-0e12e052-00055))_
- The focus in this book on the underlying ideas, what we might call the fundamentals, and how they combine to form new ideas. _(javascriptallonge.pdf (source-range-0e12e052-00055))_
- But while JavaScript Allongé attempts to be provocative, it is not prescriptive . _(javascriptallonge.pdf (source-range-0e12e052-00056))_
- There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others. _(javascriptallonge.pdf (source-range-0e12e052-00056))_
- There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others. _(javascriptallonge.pdf (source-range-0e12e052-00056))_
- People often say that software should be written for people to read. _(javascriptallonge.pdf (source-range-0e12e052-00057))_
- Software development is a complex field. _(javascriptallonge.pdf (source-range-0e12e052-00057))_
- For example, business software written in-house has a very different set of requirements than a library written to be publicly distributed as open-source. _(javascriptallonge.pdf (source-range-0e12e052-00058))_
- For example, business software written in-house has a very different set of requirements than a library written to be publicly distributed as open-source. _(javascriptallonge.pdf (source-range-0e12e052-00058))_
- Choices in software development must also consider the question of consistency. _(javascriptallonge.pdf (source-range-0e12e052-00059))_
- If a particular codebase is written with lots of helper functions that place the subject first, like this: _(javascriptallonge.pdf (source-range-0e12e052-00059))_
- Then it can be jarring to add new helpers written that place the verb first, like this: _(javascriptallonge.pdf (source-range-0e12e052-00061))_
- Then it can be jarring to add new helpers written that place the verb first, like this: _(javascriptallonge.pdf (source-range-0e12e052-00061))_
- Debuggers encourage the use of functions with explicit or implicit names. _(javascriptallonge.pdf (source-range-0e12e052-00064))_
- The use of linters 1 makes checking for certain types of undesirable code very cheap. _(javascriptallonge.pdf (source-range-0e12e052-00064))_
- Finally, choices in software development cannot ignore the tooling that is used to create and maintain software. _(javascriptallonge.pdf (source-range-0e12e052-00064))_
- The use of source-code control systems with integrated diffing rewards making certain types of focused changes. _(javascriptallonge.pdf (source-range-0e12e052-00064))_
- Continuous integration encourages the creation of software in tandem with and factored to facilitate the creation of automated test suites. _(javascriptallonge.pdf (source-range-0e12e052-00064))_
- JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn't a book about practicing, it's a book about thinking. _(javascriptallonge.pdf (source-range-0e12e052-00065))_
- JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn't a book about practicing, it's a book about thinking. _(javascriptallonge.pdf (source-range-0e12e052-00065))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00052))_

> [Figure] (p.10)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00059))_

> Choices in software development must also consider the question of consistency. If a particular codebase is written with lots of helper functions that place the subject first, like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00060))_

```
const mapWith = (iterable, fn) =>
({
[Symbol.iterator]: function* () {
for (let element of iterable) {
yield fn(element);
}
}
});
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00061))_

> Then it can be jarring to add new helpers written that place the verb first, like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00062))_

```
const filterWith = (fn, iterable) =>
({
[Symbol.iterator]: function* () {
for (let element of iterable) {
if (!!fn(element)) yield element;
}
}
});
```

##### how this book is organized

- Code examples within each chapter are small and emphasize exposition rather than serving as patterns for everyday use. _(javascriptallonge.pdf (source-range-0e12e052-00067))_
- Code examples within each chapter are small and emphasize exposition rather than serving as patterns for everyday use. _(javascriptallonge.pdf (source-range-0e12e052-00067))_
- Following some of the chapters are a series of recipes designed to show the application of the chapter's ideas in practical form. _(javascriptallonge.pdf (source-range-0e12e052-00069))_
- While the content of each chapter builds naturally on what was discussed in the previous chapter, the recipes may draw upon any aspect of the JavaScript programming language. _(javascriptallonge.pdf (source-range-0e12e052-00069))_

#### Foreword to the 'Six' edition

- That version was planned to have numerous new features (interfaces, namespaces, packages, multimethods, etc.), which would have turned JavaScript into a completely new language. _(javascriptallonge.pdf (source-range-0e12e052-00071))_
- Getting there took a while - in a way, the origins of ES6 date back to the year 2000: After ECMAScript 3 was finished, TC39 (the committee evolving JavaScript) started to work on ECMAScript 4. _(javascriptallonge.pdf (source-range-0e12e052-00071))_
- After internal conflict, a settlement was reached in July 2008 and a new plan was made - to abandon ECMAScript 4 and to replace it with two upgrades: _(javascriptallonge.pdf (source-range-0e12e052-00071))_
- ECMAScript 6 (short name: ES6; official name: ECMAScript 2015) was ratified as a standard on June 17. _(javascriptallonge.pdf (source-range-0e12e052-00071))_
- After internal conflict, a settlement was reached in July 2008 and a new plan was made - to abandon ECMAScript 4 and to replace it with two upgrades: _(javascriptallonge.pdf (source-range-0e12e052-00071))_
- Getting there took a while - in a way, the origins of ES6 date back to the year 2000: After ECMAScript 3 was finished, TC39 (the committee evolving JavaScript) started to work on ECMAScript 4. _(javascriptallonge.pdf (source-range-0e12e052-00071))_
- - A smaller upgrade would bring a few minor enhancements to ECMAScript 3. _(javascriptallonge.pdf (source-range-0e12e052-00072))_
- - A larger upgrade would substantially improve JavaScript, but without being as radical as ECMAScript 4. _(javascriptallonge.pdf (source-range-0e12e052-00073))_
- This upgrade became ECMAScript 6 (some features that were initially discussed will show up later, in upcoming ECMAScript versions). _(javascriptallonge.pdf (source-range-0e12e052-00073))_

## ECMAScript 6 has three major groups of features:

- For example: classes and modules. _(javascriptallonge.pdf (source-range-0e12e052-00075))_
- For example: Generators, proxies and WeakMaps. _(javascriptallonge.pdf (source-range-0e12e052-00080))_
- With ECMAScript 6, JavaScript has become much larger as a language. _(javascriptallonge.pdf (source-range-0e12e052-00081))_
- You will learn much about functional programming and object-oriented programming. _(javascriptallonge.pdf (source-range-0e12e052-00081))_
- JavaScript Allongé, the 'Six' Edition is both a comprehensive tour of its features and a rich collection of techniques for making better use of them. _(javascriptallonge.pdf (source-range-0e12e052-00081))_
- And you'll do so via ES6 code, handed to you in small, easily digestible pieces. _(javascriptallonge.pdf (source-range-0e12e052-00081))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00081))_

> With ECMAScript 6, JavaScript has become much larger as a language. JavaScript Allongé, the 'Six' Edition is both a comprehensive tour of its features and a rich collection of techniques for making better use of them. You will learn much about functional programming and object-oriented programming. And you'll do so via ES6 code, handed to you in small, easily digestible pieces.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00083))_

```text
2 http://www.2ality.com
4 http://exploringjs.com
3 http://ecmanauten.de
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 2 | http://www.2ality.com |
| 4 | http://exploringjs.com |
| 3 | http://ecmanauten.de |

</details>

#### Forewords to the First Edition

##### michael fogus

- However, Reg sent me a copy of his book and I was humbled. _(javascriptallonge.pdf (source-range-0e12e052-00086))_
- As a life-long bibliophile and long-time follower of Reg's online work, I was excited when he started writing books. _(javascriptallonge.pdf (source-range-0e12e052-00086))_
- Not only was this a great book, but it was also a great way to write and distribute books. _(javascriptallonge.pdf (source-range-0e12e052-00086))_
- Not only was this a great book, but it was also a great way to write and distribute books. _(javascriptallonge.pdf (source-range-0e12e052-00086))_
- The act of writing is an iterative process with (very often) tight revision loops. _(javascriptallonge.pdf (source-range-0e12e052-00087))_
- On more than one occasion I've found myself attempting to reify feedback with content that either no longer existed or was changed beyond recognition. _(javascriptallonge.pdf (source-range-0e12e052-00087))_
- However, the process of soliciting feedback, gathering responses, sending out copies, waiting for people to actually read it (if they ever do), receiving feedback and then ultimately making sense out of how to use it takes weeks and sometimes months. _(javascriptallonge.pdf (source-range-0e12e052-00087))_
- However, the process of soliciting feedback, gathering responses, sending out copies, waiting for people to actually read it (if they ever do), receiving feedback and then ultimately making sense out of how to use it takes weeks and sometimes months. _(javascriptallonge.pdf (source-range-0e12e052-00087))_
- No matter how much of an expert you think you are, JavaScript Allongé has something to teach you… about coffee. _(javascriptallonge.pdf (source-range-0e12e052-00088))_
- Reg has crafted (and continues to craft) not only an interesting book from the perspective of a connoisseur, but also an entertaining exploration into some of the most interesting aspects of his art. _(javascriptallonge.pdf (source-range-0e12e052-00088))_
- Reg has crafted (and continues to craft) not only an interesting book from the perspective of a connoisseur, but also an entertaining exploration into some of the most interesting aspects of his art. _(javascriptallonge.pdf (source-range-0e12e052-00088))_
- As a staunch advocate of functional programming, much of what Reg has written rings true to me. _(javascriptallonge.pdf (source-range-0e12e052-00089))_
- However, you'll not be beaten about the head and neck with dogma. _(javascriptallonge.pdf (source-range-0e12e052-00089))_
- As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time. _(javascriptallonge.pdf (source-range-0e12e052-00089))_
- While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. _(javascriptallonge.pdf (source-range-0e12e052-00089))_

##### matthew knox

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00093))_

```text
matthew knox
A different kind of language requires a different kind of book.
JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor strictly dynamic, and it supports procedural, object-oriented (in several flavors!), and functional programming. Many books try to hide most of those capabilities away, giving you recipes for writing JavaScript in a way that approximates class-centric programming in other languages. Not JavaScript Allongé. It starts with the fundamentals of values, functions, and objects, and then guides you through JavaScript from the inside with exploratory bits of code that illustrate scoping, combinators, context, state, prototypes, and constructors.
5 http://www.fogus.me
Like JavaScript itself, this book gives you a gentle start before showing you its full depth, and like a Cafe Allongé, it's over too soon. Enjoy!
-Matthew Knox, mattknox.com 6
6 http://mattknox.com
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 5 | http://www.fogus.me Like JavaScript itself, this book gives you a gentle start before showing you its full depth, and like a Cafe Allongé, it's over too soon. Enjoy! -Matthew Knox, mattknox.com 6 |
| 6 | http://mattknox.com |

</details>

#### About The Sample PDF

- This sample edition of the book includes just a portion of the complete book. _(javascriptallonge.pdf (source-range-0e12e052-00095))_
- If you read JavaScript Allongé, The 'six' edition and it doesn't blow your mind, your money will be cheerfully refunded. _(javascriptallonge.pdf (source-range-0e12e052-00095))_
- No, this is not the author: But he has free coffee! _(javascriptallonge.pdf (source-range-0e12e052-00099))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00098))_

> [Figure] (p.17)

## Prelude: Values and Expressions over Coffee

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00101))_

```text
Prelude: Values and Expressions over Coffee
The following material is extremely basic, however like most stories, the best way to begin is to start at the very beginning.
Imagine we are visiting our favourite coffee shop. They will make for you just about any drink you desire, from a short, intense espresso ristretto through a dry cappuccino, up to those coffee-flavoured desert concoctions featuring various concentrated syrups and milks. (You tolerate the existence of sugary drinks because they provide a sufficient profit margin to the establishment to finance your hanging out there all day using their WiFi and ordering a $3 drink every few hours.)
You express your order at one end of their counter, the folks behind the counter perform their magic, and deliver the coffee you value at the other end. This is exactly how the JavaScript environment works for the purpose of this book. We are going to dispense with web servers, browsers and other complexities and deal with this simple model: You give the computer an expression 8 , and it returns a value 9 , just as you express your wishes to a barista and receive a coffee in return.
8 https://en.wikipedia.org/wiki/Expression_
9 https://en.wikipedia.org/wiki/Value_
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 8 | https://en.wikipedia.org/wiki/Expression_ |
| 9 | https://en.wikipedia.org/wiki/Value_ |

</details>

#### values are expressions

- Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). _(javascriptallonge.pdf (source-range-0e12e052-00103))_
- You say, 'I want one of these.' The barista is no fool, she gives it straight back to you, and you get exactly what you want. _(javascriptallonge.pdf (source-range-0e12e052-00103))_
- All values are expressions. _(javascriptallonge.pdf (source-range-0e12e052-00103))_
- Yup, you hand over a cup with some coffee infused through partially caramelized sugar. _(javascriptallonge.pdf (source-range-0e12e052-00103))_
- Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). _(javascriptallonge.pdf (source-range-0e12e052-00103))_
- The answer is, this is both an expression and a value. _(javascriptallonge.pdf (source-range-0e12e052-00107))_
- All values are expressions. _(javascriptallonge.pdf (source-range-0e12e052-00109))_
- Instead of handing over the finished coffee, we can hand over the ingredients. _(javascriptallonge.pdf (source-range-0e12e052-00109))_
- Astute readers will realize we're omitting something. _(javascriptallonge.pdf (source-range-0e12e052-00110))_
- Ground coffee is a value. _(javascriptallonge.pdf (source-range-0e12e052-00111))_
- 11 Boiling water is a value. _(javascriptallonge.pdf (source-range-0e12e052-00111))_
- Boiling water plus ground coffee is an expression. _(javascriptallonge.pdf (source-range-0e12e052-00111))_
- So, boiling water plus ground coffee is an expression, but it isn't a value. _(javascriptallonge.pdf (source-range-0e12e052-00111))_
- And then you're shown another cup of coffee. _(javascriptallonge.pdf (source-range-0e12e052-00119))_
- First, sometimes, the cups are of different kinds. _(javascriptallonge.pdf (source-range-0e12e052-00120))_
- One is a demitasse, the other a mug. _(javascriptallonge.pdf (source-range-0e12e052-00120))_
- This corresponds to comparing two things in JavaScript that have different types . _(javascriptallonge.pdf (source-range-0e12e052-00120))_
- For example, the string "2" is not the same thing as the number 2 . _(javascriptallonge.pdf (source-range-0e12e052-00120))_
- For example, the string "2" is not the same thing as the number 2 . _(javascriptallonge.pdf (source-range-0e12e052-00120))_
- One holds a single, one a double. _(javascriptallonge.pdf (source-range-0e12e052-00122))_
- This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 . _(javascriptallonge.pdf (source-range-0e12e052-00122))_
- This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 . _(javascriptallonge.pdf (source-range-0e12e052-00122))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00104))_

> Let's try this with something the computer understands easily:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00107))_

> 10 The way you can tell that it's both is very easy: When you type it into JavaScript, you get the same thing back, just like our café Cubano:

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00107))_

> The answer is, this is both an expression and a value. 10 The way you can tell that it's both is very easy: When you type it into JavaScript, you get the same thing back, just like our café Cubano:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00108))_

```
42
//=> 42
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00109))_

> All values are expressions. That's easy! Are there any other kinds of expressions? Sure! let's go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let's hand over some ground coffee plus some boiling water.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00111))_

> And if we hand over the espresso, we get the espresso right back.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00112))_

> Let's try this as well with something else the computer understands easily:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00113))_

```
"JavaScript" + " " + "Allonge"
//=> "JavaScript Allonge"
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00112))_

> Let's try this as well with something else the computer understands easily:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00114))_

```text
10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' and so does the computer.
11 In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 10 | Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' and so does the computer. |
| 11 | In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values. |

</details>

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00112))_

> Let's try this as well with something else the computer understands easily:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00115))_

> Nowwesee that 'strings' are values, and you can make an expression out of strings and an operator + . Since strings are values, they are also expressions by themselves. But strings with operators are not values, they are expressions. Now we know what was missing with our 'coffee grounds plus hot water' example. The coffee grounds were a value, the boiling hot water was a value, and the 'plus' operator between them made the whole thing an expression that was not a value.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00116))_

```text
2 In JavaScript, we test whether two values are identical with the operator, and whether they are === not identical with the operator: !== 2 === 2 //=> true 'hello' !== 'goodbye' //=> true How does work, exactly? Imagine that you’re shown a cup of coffee. And then you’re shown === another cup of coffee. Are the two cups “identical?” In JavaScript, there are four possibilities: First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types. For example, the string "2" is not the same thing as the number 2. Strings and numbers are different types, so strings and numbers are never identical:
2 === '2' //=> false true !== 'true' //=> true Second, sometimes, the cups are of the same type–perhaps two espresso cups–but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2. true === false //=> false
2 !== 5 //=> true 'two' === 'five' //=> false What if the cups are of the same type and the contents are the same? Well, JavaScript’s third and fourth possibilities cover that. Prelude: Values and Expressions over Coffee xvii value types Third, some types of cups have no distinguishing marks on them. If they are the same kind of cup, and they hold the same contents, we have no way to tell the difference between them. This is the case with the strings, numbers, and booleans we have seen so far.
2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably. We haven’t encountered the fourth possibility yet. Stretching the metaphor somewhat, some types of cups have a serial number on the bottom. So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them. Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d’Italia reference types So what kinds of values might be the same type and have the same contents, but not be considered identical to JavaScript? Let’s meet a data structure that is very common in contemporary programming languages, the Array (other languages sometimes call it a List or a Vector). Prelude: Values and Expressions over Coffee xviii An array looks like this: [1, 2, 3]. This is an expression, and you can combine [] with other expressions. Go wild with things like: [2-1, 2, 2+1] [1, 1+1, 1+1+1] Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of is identical to every other value of 42? Try these for yourself: 42 [2-1, 2, 2+1] === [1,2,3] [1,2,3] === [1, 2, 3] [1, 2, 3] === [1, 2, 3] How about that! When you type or any of its variations, you are typing an expression [1, 2, 3] that generates its own unique array that is not identical to any other array, even if that other array also looks like 3]. It’s as if JavaScript is generating new cups of coffee with serial numbers [1, 2, on the bottom. They look the same, but if you examine them with ===, you see that they are different. Every time you evaluate an expression (including typing something in) to create an array, you’re creating a new, distinct value even if it appears to be the same as some other array value. As we’ll see, this is true of many other kinds of values, including functions, the main subject of this book.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 2 | In JavaScript, we test whether two values are identical with the operator, and whether they are === not identical with the operator:!== 2 === 2 //=> true 'hello'!== 'goodbye' //=> true How does work, exactly? Imagine that you’re shown a cup of coffee. And then you’re shown === another cup of coffee. Are the two cups “identical?” In JavaScript, there are four possibilities: First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types. For example, the string "2" is not the same thing as the number 2. Strings and numbers are different types, so strings and numbers are never identical: |
| 2 | === '2' //=> false true!== 'true' //=> true Second, sometimes, the cups are of the same type–perhaps two espresso cups–but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2. true === false //=> false 2!== 5 //=> true 'two' === 'five' //=> false What if the cups are of the same type and the contents are the same? Well, JavaScript’s third and fourth possibilities cover that. Prelude: Values and Expressions over Coffee xvii value types Third, some types of cups have no distinguishing marks on them. If they are the same kind of cup, and they hold the same contents, we have no way to tell the difference between them. This is the case with the strings, numbers, and booleans we have seen so far. |
| 2 | + 2 === 4 //=> true (2 + 2 === 4) === (2!== 5) //=> true Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably. We haven’t encountered the fourth possibility yet. Stretching the metaphor somewhat, some types of cups have a serial number on the bottom. So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them. Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d’Italia reference types So what kinds of values might be the same type and have the same contents, but not be considered identical to JavaScript? Let’s meet a data structure that is very common in contemporary programming languages, the Array (other languages sometimes call it a List or a Vector). Prelude: Values and Expressions over Coffee xviii An array looks like this: [1, 2, 3]. This is an expression, and you can combine [] with other expressions. Go wild with things like: [2-1, 2, 2+1] [1, 1+1, 1+1+1] Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of is identical to every other value of 42? Try these for yourself: 42 [2-1, 2, 2+1] === [1,2,3] [1,2,3] === [1, 2, 3] [1, 2, 3] === [1, 2, 3] How about that! When you type or any of its variations, you are typing an expression [1, 2, 3] that generates its own unique array that is not identical to any other array, even if that other array also looks like 3]. It’s as if JavaScript is generating new cups of coffee with serial numbers [1, 2, on the bottom. They look the same, but if you examine them with ===, you see that they are different. Every time you evaluate an expression (including typing something in) to create an array, you’re creating a new, distinct value even if it appears to be the same as some other array value. As we’ll see, this is true of many other kinds of values, including functions, the main subject of this book. |

</details>

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00117))_

> In JavaScript, we test whether two values are identical with the === operator, and whether they are not identical with the !== operator:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00118))_

```
2 === 2
//=> true
'hello' !== 'goodbye'
//=> true
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00120))_

> First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types . For example, the string "2" is not the same thing as the number 2 . Strings and numbers are different types, so strings and numbers are never identical:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00121))_

```
2 === '2'
//=> false
true !== 'true'
//=> true
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00122))_

> Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00123))_

```
true === false
//=> false
2 !== 5
//=> true
'two' === 'five'
//=> false
```

##### value types

- This is the case with the strings, numbers, and booleans we have seen so far. _(javascriptallonge.pdf (source-range-0e12e052-00126))_
- Third, some types of cups have no distinguishing marks on them. _(javascriptallonge.pdf (source-range-0e12e052-00126))_
- If they are the same kind of cup, and they hold the same contents, we have no way to tell the difference between them. _(javascriptallonge.pdf (source-range-0e12e052-00126))_
- Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same 'content.' Strings, numbers, and booleans are examples of what JavaScript calls 'value' or 'primitive' types. _(javascriptallonge.pdf (source-range-0e12e052-00128))_
- We'll use both terms interchangeably. _(javascriptallonge.pdf (source-range-0e12e052-00128))_
- Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d'Italia _(javascriptallonge.pdf (source-range-0e12e052-00131))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00128))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same 'content.' Strings, numbers, and booleans are examples of what JavaScript calls 'value' or 'primitive' types. We'll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00127))_

```
2 + 2 === 4
//=> true
(2 + 2 === 4) === (2 !== 5)
//=> true
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00128))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same 'content.' Strings, numbers, and booleans are examples of what JavaScript calls 'value' or 'primitive' types. We'll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00129))_

> So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00128))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same 'content.' Strings, numbers, and booleans are examples of what JavaScript calls 'value' or 'primitive' types. We'll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00130))_

> [Figure] (p.22)

##### reference types

- This is an expression, and you can combine [] with other expressions. _(javascriptallonge.pdf (source-range-0e12e052-00134))_
- Notice that you are always generating arrays with the same contents. _(javascriptallonge.pdf (source-range-0e12e052-00136))_
- When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own unique array that is not identical to any other array, even if that other array also looks like [1, 2, 3] . _(javascriptallonge.pdf (source-range-0e12e052-00138))_
- They look the same, but if you examine them with === , you see that they are different. _(javascriptallonge.pdf (source-range-0e12e052-00139))_
- As we'll see, this is true of many other kinds of values, including functions , the main subject of this book. _(javascriptallonge.pdf (source-range-0e12e052-00139))_
- Every time you evaluate an expression (including typing something in) to create an array, you're creating a new, distinct value even if it appears to be the same as some other array value. _(javascriptallonge.pdf (source-range-0e12e052-00139))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00134))_

> An array looks like this: [1, 2, 3] . This is an expression, and you can combine [] with other expressions. Go wild with things like:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00135))_

```
[2-1, 2, 2+1]
[1, 1+1, 1+1+1]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00136))_

> Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of 42 is identical to every other value of 42 ? Try these for yourself:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00137))_

```
[2-1, 2, 2+1] === [1,2,3]
[1,2,3] === [1, 2, 3]
[1, 2, 3] === [1, 2, 3]
```

## A Rich Aroma: Basic Numbers

- Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. _(javascriptallonge.pdf (source-range-0e12e052-00143))_
- In computer science, a literal is a notation for representing a fixed value in source code. _(javascriptallonge.pdf (source-range-0e12e052-00143))_
- Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. _(javascriptallonge.pdf (source-range-0e12e052-00143))_
- If we start a literal with a zero, it is an octal literal. _(javascriptallonge.pdf (source-range-0e12e052-00144))_
- Not all numbers are base ten. _(javascriptallonge.pdf (source-range-0e12e052-00144))_
- It represents the number forty-two, which is 42 base 10. _(javascriptallonge.pdf (source-range-0e12e052-00144))_
- We saw that an expression consisting solely of numbers, like 42 , is a literal. _(javascriptallonge.pdf (source-range-0e12e052-00144))_
- So the literal 042 is 42 base 8, which is actually 34 base 10. _(javascriptallonge.pdf (source-range-0e12e052-00144))_
- A computer's internal representation for numbers is important to understand. _(javascriptallonge.pdf (source-range-0e12e052-00146))_
- Internally, both 042 and 34 have the same representation, as double-precision floating point 13 numbers. _(javascriptallonge.pdf (source-range-0e12e052-00146))_
- For example, the largest integer JavaScript can safely 14 handle is 9007199254740991 , or 2 '53' - 1 . _(javascriptallonge.pdf (source-range-0e12e052-00147))_
- For example, the largest integer JavaScript can safely 14 handle is 9007199254740991 , or 2 '53' - 1 . _(javascriptallonge.pdf (source-range-0e12e052-00147))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00141))_

> [Figure] (p.24)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00143))_

> In computer science, a literal is a notation for representing a fixed value in source code. Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. An anonymous function is a literal for the function type.Wikipedia 12

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00146))_

> The machine's representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the computer's behaviour surprises us if we don't know a little about what it's doing 'under the hood.'

##### floating

- We can, for example, write 1.5 or 33.33 , and JavaScript represents these literals as floating point numbers. _(javascriptallonge.pdf (source-range-0e12e052-00149))_
- But we mentioned that numbers are represented internally as floating point, meaning that they need not be just integers. _(javascriptallonge.pdf (source-range-0e12e052-00149))_
- We can, for example, write 1.5 or 33.33 , and JavaScript represents these literals as floating point numbers. _(javascriptallonge.pdf (source-range-0e12e052-00149))_
- Most programmers never encounter the limit on the magnitude of an integer. _(javascriptallonge.pdf (source-range-0e12e052-00149))_
- It's tempting to think we now have everything we need to do things like handle amounts of money, but as the late John Belushi would say, 'Nooooooooooooooooooooo.' A computer's internal representation for a floating point number is binary, while our literal number was in base ten. _(javascriptallonge.pdf (source-range-0e12e052-00150))_
- This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2. _(javascriptallonge.pdf (source-range-0e12e052-00150))_
- This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2. _(javascriptallonge.pdf (source-range-0e12e052-00150))_
- But as a rule, if you need to work with real numbers, you should have more than a nodding acquaintance with the IEEE Standard for Floating-Point Arithmetic 15 . _(javascriptallonge.pdf (source-range-0e12e052-00157))_
- In this book, we need not think about such details, but outside of this book, we must. _(javascriptallonge.pdf (source-range-0e12e052-00157))_
- For example, '$43.21' will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21 . _(javascriptallonge.pdf (source-range-0e12e052-00157))_
- For example, '$43.21' will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21 . _(javascriptallonge.pdf (source-range-0e12e052-00157))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00151))_

> One of the most oft-repeated examples is this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00152))_

```
1.0
//=> 1
1.0 + 1.0
//=> 2
1.0 + 1.0 + 1.0
//=> 3
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00154))_

```text
13 http://en.wikipedia.org/wiki/Double-precision_floating-point_format
14 Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js , it will happily report that the answer is 18014398509481982 . But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 13 | http://en.wikipedia.org/wiki/Double-precision_floating-point_format |
| 14 | Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations. |

</details>

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00155))_

```
0.1
//=> 0.1
0.1 + 0.1
//=> 0.2
0.1 + 0.1 + 0.1
//=> 0.30000000000000004
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00156))_

> This kind of 'inexactitude' can be ignored when performing calculations that have an acceptable deviation. For example, when centering some text on a page, as long as the difference between what you might calculate longhand and JavaScript's calculation is less than a pixel, there is no observable error.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00156))_

> This kind of 'inexactitude' can be ignored when performing calculations that have an acceptable deviation. For example, when centering some text on a page, as long as the difference between what you might calculate longhand and JavaScript's calculation is less than a pixel, there is no observable error.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00157))_

> Professional programmers almost never use floating point numbers to represent monetary amounts.

##### operations on numbers

- As we've seen, JavaScript has many common arithmetic operators. _(javascriptallonge.pdf (source-range-0e12e052-00159))_
- These can be combined to make more complex expressions, like 2 * 5 + 1 . _(javascriptallonge.pdf (source-range-0e12e052-00159))_
- In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. _(javascriptallonge.pdf (source-range-0e12e052-00160))_
- JavaScript has many more operators. _(javascriptallonge.pdf (source-range-0e12e052-00162))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00160, source-range-0e12e052-00162))_

> In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. So: JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2) , because the * operator has a higher precedence than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2 , this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the nam

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00161))_

```
2 * 5 + 1
//=> 11
1 + 5 * 2
//=> 11
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00163))_

> In addition to the common + , -, * , and / , JavaScript also supports modulus, % , and unary negation, -:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00165))_

> [Figure] (p.27)

## The first sip: Basic Functions

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00168))_

> [Figure] (p.29)

#### As Little As Possible About Functions, But No Less

- Like numbers, strings, and arrays, they have a representation. _(javascriptallonge.pdf (source-range-0e12e052-00170))_
- Functions represent computations to be performed. _(javascriptallonge.pdf (source-range-0e12e052-00170))_
- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. _(javascriptallonge.pdf (source-range-0e12e052-00170))_
- This is a function that is applied to no values and returns 0 . _(javascriptallonge.pdf (source-range-0e12e052-00172))_
- This seems to break our rule that if an expression is also a value, JavaScript will give the same value back to us. _(javascriptallonge.pdf (source-range-0e12e052-00174))_
- The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. _(javascriptallonge.pdf (source-range-0e12e052-00174))_
- I'd prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. _(javascriptallonge.pdf (source-range-0e12e052-00176))_
- But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function. _(javascriptallonge.pdf (source-range-0e12e052-00176))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00170))_

> In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represent computations to be performed. Like numbers, strings, and arrays, they have a representation. Let's start with the second simplest possible function. 16 In JavaScript, it looks like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00171))_

```
() => 0
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00172, source-range-0e12e052-00174))_

> This is a function that is applied to no values and returns 0 . Let's verify that our function is a value like all others: What!? Why didn't it type back () => 0 for us? This seems to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What's going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00173))_

```
(() => 0)
//=> [Function]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00172))_

> This is a function that is applied to no values and returns 0 . Let's verify that our function is a value like all others:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00174))_

> If you try the same thing in a browser, you may see something else.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00174))_

> What!? Why didn't it type back () => 0 for us? This seems to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What's going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a br

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00175))_

> 16 The simplest possible function is () => {} , we'll see that later.

##### functions and identities

- Value types share the same identity if they have the same contents. _(javascriptallonge.pdf (source-range-0e12e052-00178))_
- You recall that we have two types of values with respect to identity: Value types and reference types. _(javascriptallonge.pdf (source-range-0e12e052-00178))_
- Reference types do not. _(javascriptallonge.pdf (source-range-0e12e052-00178))_
- Like arrays, every time you evaluate an expression to produce a function, you get a new function that is not identical to any other function, even if you use the same expression to generate it. _(javascriptallonge.pdf (source-range-0e12e052-00181))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00179))_

> Which kind are functions? Let's try them out and see. For reasons of appeasing the JavaScript parser, we'll enclose our functions in parentheses:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00180))_

```
(() => 0) === (() => 0)
//=> false
```

##### applying functions

- The way we use functions is to apply them to zero or more values called arguments . _(javascriptallonge.pdf (source-range-0e12e052-00183))_
- We'll put it in parentheses 17 to keep the parser happy, like we did above: (() => 0) . _(javascriptallonge.pdf (source-range-0e12e052-00186))_
- Since we aren't giving it any arguments, we'll simply write () after the expression. _(javascriptallonge.pdf (source-range-0e12e052-00186))_
- 17 If you're used to other programming languages, you've probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. _(javascriptallonge.pdf (source-range-0e12e052-00188))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00184, source-range-0e12e052-00186))_

> Here's how we apply a function to some values in JavaScript: Let's say that fn_expr is an expression that when evaluated, produces a function. Let's call the arguments args . Here's how to apply a function to some arguments: Right now, we only know about one such expression: () => 0 , so let's use it. We'll put it in parentheses 17 to keep the parser happy, like we did above: (() => 0) . Since we aren't giving it any arguments, we'll simply write () after the expression. So we write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00185))_

```
fn_expr(args)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00186))_

> Right now, we only know about one such expression: () => 0 , so let's use it. We'll put it in parentheses 17 to keep the parser happy, like we did above: (() => 0) . Since we aren't giving it any arguments, we'll simply write () after the expression. So we write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00187))_

```
(() => 0)()
//=> 0
```

##### functions that return values and evaluate expressions

- We know that (() => 0)() returns 0 , and this is unsurprising. _(javascriptallonge.pdf (source-range-0e12e052-00190))_
- Values like 0 are expressions, as are things like 40 + 2 . _(javascriptallonge.pdf (source-range-0e12e052-00193))_
- In the prelude, we looked at expressions. _(javascriptallonge.pdf (source-range-0e12e052-00193))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-0e12e052-00195))_
- We can put any expression to the right of the arrow. _(javascriptallonge.pdf (source-range-0e12e052-00195))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-0e12e052-00195))_
- Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-0e12e052-00198))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00190))_

> We've seen () => 0 . We know that (() => 0)() returns 0 , and this is unsurprising. Likewise, the following all ought to be obvious:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00191))_

```
(() => 1)()
//=> 1
(() => "Hello, JavaScript")()
//=> "Hello, JavaScript"
(() => Infinity)()
//=> Infinity
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00192))_

> Well, the last one's a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00194))_

```
(() => 1 + 1)()
//=> 2
(() => "Hello, " + "JavaScript")()
//=> "Hello, JavaScript"
(() => Infinity * Infinity)()
//=> Infinity
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00197))_

```
(() => (() => 0)())()
//=> 0
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00198))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00199))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00199))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00200))_

```
(() =>
(() => 0
)()
)()
//=> 0
```

##### commas

- The comma operator in JavaScript is interesting. _(javascriptallonge.pdf (source-range-0e12e052-00203))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00203))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00204))_

```
//=> 2
(1 + 1, 2 + 2)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00205))_

> We can use commas with functions to create functions that evaluate multiple expressions:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00206))_

```
(() => (1 + 1, 2 + 2))()
//=> 4
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00205))_

> We can use commas with functions to create functions that evaluate multiple expressions:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00207))_

> This is useful when trying to do things that might involve side-effects , but we'll get to that later.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00207))_

> This is useful when trying to do things that might involve side-effects , but we'll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00208))_

```
() =>
(1 + 1, 2 + 2)
```

## Or even:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00210))_

```
() => (
1 + 1,
2 + 2
)
```

##### the simplest possible block

- There's another thing we can put to the right of an arrow, a block . _(javascriptallonge.pdf (source-range-0e12e052-00212))_
- It returns the result of evaluating a block that has no statements. _(javascriptallonge.pdf (source-range-0e12e052-00215))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00213, source-range-0e12e052-00215))_

> So, this is a valid function: It returns the result of evaluating a block that has no statements. What would that be? Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00214))_

```
() => {}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00215))_

> It returns the result of evaluating a block that has no statements. What would that be? Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00216))_

```
(() => {})()
//=> undefined
```

##### undefined

- It will crop up again. _(javascriptallonge.pdf (source-range-0e12e052-00219))_
- In JavaScript, the absence of a value is written undefined , and it means there is no value. _(javascriptallonge.pdf (source-range-0e12e052-00219))_
- In JavaScript, the absence of a value is written undefined , and it means there is no value. _(javascriptallonge.pdf (source-range-0e12e052-00219))_
- Like numbers, booleans and strings, JavaScript can print out the value undefined . _(javascriptallonge.pdf (source-range-0e12e052-00222))_
- No matter how you evaluate undefined , you get an identical value back. _(javascriptallonge.pdf (source-range-0e12e052-00224))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-0e12e052-00225))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-0e12e052-00225))_
- You might think that undefined in JavaScript is equivalent to NULL in SQL. _(javascriptallonge.pdf (source-range-0e12e052-00226))_
- In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can't be equal. _(javascriptallonge.pdf (source-range-0e12e052-00226))_
- In JavaScript, every undefined is identical to every other undefined . _(javascriptallonge.pdf (source-range-0e12e052-00226))_
- In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can't be equal. _(javascriptallonge.pdf (source-range-0e12e052-00226))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00219))_

> In JavaScript, the absence of a value is written undefined , and it means there is no value. It will crop up again. undefined is its own type of value, and it acts like a value type:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00220))_

```
undefined
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00219))_

> In JavaScript, the absence of a value is written undefined , and it means there is no value. It will crop up again. undefined is its own type of value, and it acts like a value type:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00221))_

```
//=> undefined
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00224))_

> No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-)

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00223))_

```
undefined === undefined
//=> true
(() => {})() === (() => {})()
//=> true
(() => {})() === undefined
//=> true
```

##### void

- void is an operator that takes any value and evaluates to undefined , always. _(javascriptallonge.pdf (source-range-0e12e052-00233))_
- The second form works most of the time, but it is possible to break it by reassigning undefined to a different value, something we'll discuss in Reassignment and Mutation. _(javascriptallonge.pdf (source-range-0e12e052-00234))_
- The first form works but it's cumbersome. _(javascriptallonge.pdf (source-range-0e12e052-00234))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00231, source-range-0e12e052-00233))_

> There's a third way, with JavaScript's void operator. Behold: void is an operator that takes any value and evaluates to undefined , always. So, when we deliberately want an undefined value, should we use the first, second, or third form? 19 The answer is, use void . By convention, use void 0 .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00232))_

```
void 0
//=> undefined
void 1
//=> undefined
void (2 + 2)
//=> undefined
```

##### back on the block

- We haven't discussed these statements . _(javascriptallonge.pdf (source-range-0e12e052-00240))_
- Although they aren't very practical, these are valid JavaScript functions, and they return undefined when applied: _(javascriptallonge.pdf (source-range-0e12e052-00241))_
- There are many kinds of JavaScript statements, but the first kind is one we've already met. _(javascriptallonge.pdf (source-range-0e12e052-00241))_
- As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way: _(javascriptallonge.pdf (source-range-0e12e052-00243))_
- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined : _(javascriptallonge.pdf (source-range-0e12e052-00245))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00238))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00236))_

```text
back on the block
Back to our function. We evaluated this:
19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This was actually the preferred mechanism until void became commonplace.
20 As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined . We have no idea.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 19 | Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This was actually the preferred mechanism until void became commonplace. |
| 20 | As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined. We have no idea. |

</details>

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00238))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00237))_

```
(() => {})()
//=> undefined
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00241, source-range-0e12e052-00243))_

> There are many kinds of JavaScript statements, but the first kind is one we've already met. An expression is a JavaScript statement. Although they aren't very practical, these are valid JavaScript functions, and they return undefined when applied: As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00242))_

```
() => { 2 + 2 }
() => { 1 + 1; 2 + 2 }
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00243))_

> As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00244))_

```
() => {
1 + 1;
2 + 2
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00245))_

> But no matter how we arrange them, a block with one or more expressions still evaluates to undefined :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00246))_

```text
//=> undefined
We said that the function returns the result of evaluating a block, and we said that a block is a
(possibly empty) list of JavaScript statements separated by semicolons.21
Something like: { statement1; statement2; statement3; ... ; statementn }
We haven’t discussed these statements. What’s a statement?
There are many kinds of JavaScript statements, but the first kind is one we’ve already met. An
expression is a JavaScript statement. Although they aren’t very practical, these are valid JavaScript
functions, and they return undefined when applied:
() => { 2 + 2 }
() => { 1 + 1; 2 + 2 }
As we saw with commas above, we can rearrange these functions onto multiple lines when we feel
its more readable that way:
() => {
1 + 1;
2 + 2
}
But no matter how we arrange them, a block with one or more expressions still evaluates to
undefined:
(() => { 2 + 2 })()
//=> undefined
(() => { 1 + 1; 2 + 2 })()
//=> undefined
(() => {
1 + 1;
2 + 2
})()
//=> undefined
As you can see, a block with one expression does not behave like an expression, and a block with
more than one expression does not behave like an expression constructed with the comma operator:
21You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semi-
colon insertion. Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in
should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it’s part of
the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them.
The first sip: Basic Functions
14
(() => 2 + 2)()
//=> 4
(() => { 2 + 2 })()
//=> undefined
(() => (1 + 1, 2 + 2))()
//=> 4
(() => { 1 + 1; 2 + 2 })()
//=> undefined
So how do we get a function that evaluates a block to return a value when applied? With the return
keyword and any expression:
(() => { return 0 })()
//=> 0
(() => { return 1 })()
//=> 1
(() => { return 'Hello ' + 'World' })()
// 'Hello World'
The return keyword creates a return statement that immediately terminates the function application
and returns the result of evaluating its expression. For example:
(() => {
1 + 1;
return 2 + 2
})()
//=> 4
And also:
(() => {
return 1 + 1;
2 + 2
})()
//=> 2
The return statement is the first statement we’ve seen, and it behaves differently than an expression.
For example, you can’t use one as the expression in a simple function, because it isn’t an expression:
The first sip: Basic Functions
15
(() => return 0)()
//=> ERROR
Statements belong inside blocks and only inside blocks. Some languages simplify this by making
everything an expression, but JavaScript maintains this distinction, so when learning JavaScript we
also learn about statements like function declarations, for loops, if statements, and so forth. We’ll
see a few more of these later.
functions that evaluate to functions
If an expression that evaluates to a function is, well, an expression, and if a return statement can
have any expression on its right side… Can we put an expression that evaluates to a function on the
right side of a function expression?
Yes:
() => () => 0
That’s a function! It’s a function that when applied, evaluates to a function that when applied,
evaluates to 0. So we have a function, that returns a function, that returns zero. Likewise:
() => () => true
That’s a function, that returns a function, that returns true:
(() => () => true)()()
//=> true
We could, of course, do the same thing with a block if we wanted:
() => () => { return true; }
But we generally don’t.
Well. We’ve been very clever, but so far this all seems very abstract. Diffraction of a crystal is
beautiful and interesting in its own right, but you can’t blame us for wanting to be shown a practical
use for it, like being able to determine the composition of a star millions of light years away. So… In
the next chapter, “I’d Like to Have an Argument, Please,” we’ll see how to make functions practical.
The first sip: Basic Functions
16
Ah. I’d Like to Have an Argument, Please.22
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 1 | + 1; |
| 2 | + 2 But no matter how we arrange them, a block with one or more expressions still evaluates to undefined: (() => {2 + 2})() //=> undefined (() => {1 + 1; 2 + 2})() //=> undefined |
| 1 | + 1; |
| 2 | + 2 //=> undefined As you can see, a block with one expression does not behave like an expression, and a block with more than one expression does not behave like an expression constructed with the comma operator: 21You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semi- colon insertion. Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. |
| 14 | The first sip: Basic Functions (() => 2 + 2)() //=> 4 (() => {2 + 2})() //=> undefined (() => (1 + 1, 2 + 2))() //=> 4 (() => {1 + 1; 2 + 2})() //=> undefined So how do we get a function that evaluates a block to return a value when applied? With the return keyword and any expression: (() => {return 0})() //=> 0 (() => {return 1})() //=> 1 (() => {return 'Hello ' + 'World'})() // 'Hello World' The return keyword creates a return statement that immediately terminates the function application and returns the result of evaluating its expression. For example: |
| 1 | + 1; return 2 + 2 //=> 4 return 1 + 1; |
| 2 | And also: + 2 //=> 2 The return statement is the first statement we’ve seen, and it behaves differently than an expression. For example, you can’t use one as the expression in a simple function, because it isn’t an expression: |
| 15 | The first sip: Basic Functions (() => return 0)() //=> ERROR Statements belong inside blocks and only inside blocks. Some languages simplify this by making everything an expression, but JavaScript maintains this distinction, so when learning JavaScript we also learn about statements like function declarations, for loops, if statements, and so forth. We’ll see a few more of these later. functions that evaluate to functions If an expression that evaluates to a function is, well, an expression, and if a return statement can have any expression on its right side… Can we put an expression that evaluates to a function on the right side of a function expression? Yes: () => () => 0 That’s a function! It’s a function that when applied, evaluates to a function that when applied, evaluates to 0. So we have a function, that returns a function, that returns zero. Likewise: () => () => true That’s a function, that returns a function, that returns true: (() => () => true)()() //=> true We could, of course, do the same thing with a block if we wanted: () => () => {return true;} But we generally don’t. Well. We’ve been very clever, but so far this all seems very abstract. Diffraction of a crystal is beautiful and interesting in its own right, but you can’t blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. So… In the next chapter, “I’d Like to Have an Argument, Please,” we’ll see how to make functions practical. |
| 16 | The first sip: Basic Functions Ah. I’d Like to Have an Argument, Please.22 |

</details>

## And also:

- Statements belong inside blocks and only inside blocks. _(javascriptallonge.pdf (source-range-0e12e052-00251))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00249))_

> The return statement is the first statement we've seen, and it behaves differently than an expression. For example, you can't use one as the expression in a simple function, because it isn't an expression:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00248))_

```
(() => {
return 1 + 1;
2 + 2
})()
//=> 2
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00249))_

> The return statement is the first statement we've seen, and it behaves differently than an expression. For example, you can't use one as the expression in a simple function, because it isn't an expression:

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00249))_

> The return statement is the first statement we've seen, and it behaves differently than an expression. For example, you can't use one as the expression in a simple function, because it isn't an expression:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00250))_

```
(() => return 0)()
//=> ERROR
```

##### functions that evaluate to functions

- So we have a function, that returns a function, that returns zero . _(javascriptallonge.pdf (source-range-0e12e052-00256))_
- It's a function that when applied, evaluates to a function that when applied, evaluates to 0 . _(javascriptallonge.pdf (source-range-0e12e052-00256))_
- We've been very clever, but so far this all seems very abstract. _(javascriptallonge.pdf (source-range-0e12e052-00263))_
- Diffraction of a crystal is beautiful and interesting in its own right, but you can't blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. _(javascriptallonge.pdf (source-range-0e12e052-00263))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00253))_

> If an expression that evaluates to a function is, well, an expression, and if a return statement can have any expression on its right side… Can we put an expression that evaluates to a function on the right side of a function expression?

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00255))_

```
() => () => 0
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00256))_

> That's a function! It's a function that when applied, evaluates to a function that when applied, evaluates to 0 . So we have a function, that returns a function, that returns zero . Likewise:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00257))_

```
() => () => true
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00258))_

> That's a function, that returns a function, that returns true :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00259))_

```
(() => () => true)()()
//=> true
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00260))_

> We could, of course, do the same thing with a block if we wanted:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00261))_

```
() => () => { return true; }
```

#### Ah. I'd Like to Have an Argument, Please. 22

- We haven't even said what an argument is , only that our functions don't have any. _(javascriptallonge.pdf (source-range-0e12e052-00265))_
- Up to now, we've looked at functions without arguments. _(javascriptallonge.pdf (source-range-0e12e052-00265))_
- We haven't even said what an argument is , only that our functions don't have any. _(javascriptallonge.pdf (source-range-0e12e052-00265))_
- Most programmers are perfectly familiar with arguments (often called 'parameters'). _(javascriptallonge.pdf (source-range-0e12e052-00266))_
- So you know what they are, and I know that you know what they are, but please be patient with the explanation! _(javascriptallonge.pdf (source-range-0e12e052-00266))_
- This function has one argument, room , and an empty body. _(javascriptallonge.pdf (source-range-0e12e052-00269))_
- I'm sure you are perfectly comfortable with the idea that this function has two arguments, room , and board . _(javascriptallonge.pdf (source-range-0e12e052-00271))_
- I read that aloud as 'When applied to a value representing the diameter, this function returns the diameter times 3.14159265.' _(javascriptallonge.pdf (source-range-0e12e052-00273))_
- To apply a function with an argument (or arguments), we put the argument (or arguments) within the parentheses, like this: _(javascriptallonge.pdf (source-range-0e12e052-00274))_
- You won't be surprised to see how to write and apply a function to two arguments: _(javascriptallonge.pdf (source-range-0e12e052-00276))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00267))_

> Let's make a function with an argument:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00268))_

```
(room) => {}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00269))_

> This function has one argument, room , and an empty body. Here's a function with two arguments and an empty body:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00270))_

```
(room, board) => {}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00271))_

> I'm sure you are perfectly comfortable with the idea that this function has two arguments, room , and board . What does one do with the arguments? Use them in the body, of course. What do you think this is?

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00272))_

```
(diameter) => diameter * 3.14159265
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00274))_

> Remember that to apply a function with no arguments, we wrote (() => {})() . To apply a function with an argument (or arguments), we put the argument (or arguments) within the parentheses, like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00275))_

```
((diameter) => diameter * 3.14159265)(2)
//=> 6.2831853
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00276))_

> You won't be surprised to see how to write and apply a function to two arguments:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00278))_

```
((room, board) => room + board)(800, 150)
//=> 950
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00276))_

> You won't be surprised to see how to write and apply a function to two arguments:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00279))_

> [Figure] (p.40)

##### a quick summary of functions and bodies

- How arguments are used in a body's expression is probably perfectly obvious to you from the examples, especially if you've used any programming language (except for the dialect of BASIC-which I recall from my secondary school-that didn't allow parameters when you called a procedure). _(javascriptallonge.pdf (source-range-0e12e052-00281))_
- How arguments are used in a body's expression is probably perfectly obvious to you from the examples, especially if you've used any programming language (except for the dialect of BASIC-which I recall from my secondary school-that didn't allow parameters when you called a procedure). _(javascriptallonge.pdf (source-range-0e12e052-00281))_
- Expressions consist either of representations of values (like 3.14159265 , true , and undefined ), operators that combine expressions (like 3 + 2 ), some special forms like [1, 2, 3] for creating arrays out of expressions, or function ( arguments ) { body-statements } for creating functions. _(javascriptallonge.pdf (source-range-0e12e052-00282))_
- One of the important possible statements is a return statement. _(javascriptallonge.pdf (source-range-0e12e052-00283))_
- This loose definition is recursive, so we can intuit (or use our experience with other languages) that since a function can contain a return statement with an expression, we can write a function that returns a function, or an array that contains another array expression. _(javascriptallonge.pdf (source-range-0e12e052-00284))_

##### call by value

- That means that when you write some code that appears to apply a function to an expression or expressions, JavaScript evaluates all of those expressions and applies the functions to the resulting value(s). _(javascriptallonge.pdf (source-range-0e12e052-00286))_
- That means that when you write some code that appears to apply a function to an expression or expressions, JavaScript evaluates all of those expressions and applies the functions to the resulting value(s). _(javascriptallonge.pdf (source-range-0e12e052-00286))_
- What happened internally is that the expression 1 + 1 was evaluated first, resulting in 2 . _(javascriptallonge.pdf (source-range-0e12e052-00290))_
- Then our circumference function was applied to 2 . _(javascriptallonge.pdf (source-range-0e12e052-00290))_
- Then our circumference function was applied to 2 . _(javascriptallonge.pdf (source-range-0e12e052-00290))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00288))_

> So when you write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00289))_

```
((diameter) => diameter * 3.14159265)(1 + 1)
//=> 6.2831853
```

#### variables and bindings

- Right now everything looks simple and straightforward, and we can move on to talk about arguments in more detail. _(javascriptallonge.pdf (source-range-0e12e052-00293))_
- Besides a desire to use long words to sound impressive, this is not going to seem attractive until we find ourselves wanting to discuss the role of the Church of England in 19th century British politics. _(javascriptallonge.pdf (source-range-0e12e052-00295))_
- But there's another reason for learning the word antidisestablishmentarianism : We might learn how prefixes and postfixes work in English grammar. _(javascriptallonge.pdf (source-range-0e12e052-00296))_
- It has a certain important meaning in its own right, and it's also an excellent excuse to learn about functions that make functions, environments, variables, and more. _(javascriptallonge.pdf (source-range-0e12e052-00296))_
- The second x , the one in => x , is not an argument, it's an expression referring to a variable . _(javascriptallonge.pdf (source-range-0e12e052-00297))_
- Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. _(javascriptallonge.pdf (source-range-0e12e052-00298))_
- Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. _(javascriptallonge.pdf (source-range-0e12e052-00298))_
- You can apply a function to one or more functions. _(javascriptallonge.pdf (source-range-0e12e052-00299))_
- 24 We said that you can't apply a function to an expression. _(javascriptallonge.pdf (source-range-0e12e052-00299))_
- This has interesting applications, and they will be explored much more thoroughly in Functions That Are Applied to Functions. _(javascriptallonge.pdf (source-range-0e12e052-00299))_
- Well for arguments, that is very simple. _(javascriptallonge.pdf (source-range-0e12e052-00300))_
- When you apply the function to the arguments, an entry is placed in the dictionary for each argument. _(javascriptallonge.pdf (source-range-0e12e052-00300))_
- - The value '2' is bound to the name 'x' in the environment. _(javascriptallonge.pdf (source-range-0e12e052-00309))_
- - The expression 'x' (the right side of the function) is evaluated within the environment we just created. _(javascriptallonge.pdf (source-range-0e12e052-00310))_
- - The expression 'x' (the right side of the function) is evaluated within the environment we just created. _(javascriptallonge.pdf (source-range-0e12e052-00310))_
- - The value of a variable when evaluated in an environment is the value bound to the variable's name in that environment, which is '2' _(javascriptallonge.pdf (source-range-0e12e052-00311))_
- meaning, that the environment is a dictionary, and that the value 2 is bound to the name x , and that there might be other stuff in that dictionary we aren't discussing right now. _(javascriptallonge.pdf (source-range-0e12e052-00313))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00293))_

> Right now everything looks simple and straightforward, and we can move on to talk about arguments in more detail. And we're going to work our way up from (diameter) => diameter * 3.14159265 to functions like:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00294))_

```
(x) => (y) => x
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00300))_

> How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dictionary for each argument. So when we write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00301))_

```
((x) => x)(2)
//=> 2
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00302))_

> What happens is this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00305))_

> - One sub-expression, (x) => x evaluates to a function.

#### call by sharing

- Now it is time to take another look at the distinction between value and reference types. _(javascriptallonge.pdf (source-range-0e12e052-00315))_
- At that time, we looked at how JavaScript distinguishes objects that are identical from objects that are not. _(javascriptallonge.pdf (source-range-0e12e052-00315))_
- Earlier, we distinguished JavaScript's value types from its reference types . _(javascriptallonge.pdf (source-range-0e12e052-00315))_
- There is a property that JavaScript strictly maintains: When a value-any value-is passed as an argument to a function, the value bound in the function's environment must be identical to the original. _(javascriptallonge.pdf (source-range-0e12e052-00316))_
- Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. _(javascriptallonge.pdf (source-range-0e12e052-00317))_
- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. _(javascriptallonge.pdf (source-range-0e12e052-00317))_
- As you recall, value types like strings and numbers are identical to each other if they have the same content. _(javascriptallonge.pdf (source-range-0e12e052-00317))_
- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. _(javascriptallonge.pdf (source-range-0e12e052-00317))_
- JavaScript does not place copies of reference values in any environment. _(javascriptallonge.pdf (source-range-0e12e052-00319))_
- JavaScript places references to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-0e12e052-00319))_
- Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types. _(javascriptallonge.pdf (source-range-0e12e052-00320))_
- 26 Unless the argument is NaN , which isn't equal to anything, including itself . _(javascriptallonge.pdf (source-range-0e12e052-00323))_
- 26 Unless the argument is NaN , which isn't equal to anything, including itself . _(javascriptallonge.pdf (source-range-0e12e052-00323))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00317))_

> So JavaScript can make as many copies of strings, numbers, or booleans as it wishes.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00321))_

> And with that, we're ready to look at closures . When we combine our knowledge of value types, reference types, arguments, and closures, we'll understand why this function always evaluates to true no matter what argument 26 you apply it to:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00322))_

```
(value) =>
((ref1, ref2) => ref1 === ref2)(value, value)
```

### Closures and Scope

- It makes sense that the result value is a function, because the expression for (x) => ... _(javascriptallonge.pdf (source-range-0e12e052-00329))_
- It makes sense that the result value is a function, because the expression for (x) => ... _(javascriptallonge.pdf (source-range-0e12e052-00329))_
- So now we have a value representing that function. _(javascriptallonge.pdf (source-range-0e12e052-00331))_
- There is no x in its environment, it must come from somewhere else. _(javascriptallonge.pdf (source-range-0e12e052-00333))_
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from 'outside' of a function that are referenced inside a function. _(javascriptallonge.pdf (source-range-0e12e052-00334))_
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from 'outside' of a function that are referenced inside a function. _(javascriptallonge.pdf (source-range-0e12e052-00334))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00325, source-range-0e12e052-00327))_

> It's time to see how a function within a function works: First off, let's use what we learned above. Given ( some function )( some argument ) , we know that we apply the function to the argument, create an environment, bind the value of the argument to the name, and evaluate the function's expression. So we do that first with this code:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00326))_

```
((x) => (y) => x)(1)(2)
//=> 1
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00327, source-range-0e12e052-00329))_

> First off, let's use what we learned above. Given ( some function )( some argument ) , we know that we apply the function to the argument, create an environment, bind the value of the argument to the name, and evaluate the function's expression. So we do that first with this code: The environment belonging to the function with signature (x) => ... becomes {x: 1, ...} , and the result of applying the function is another function value. It makes sense that the result value is a function, because t

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00328))_

```
((x) => (y) => x)(1)
//=> [Function]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00329))_

> The environment belonging to the function with signature (x) => ... becomes {x: 1, ...} , and the result of applying the function is another function value. It makes sense that the result value is a function, because the expression for (x) => ... 's body is:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00330))_

```
(y) => x
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00331))_

> So now we have a value representing that function. Then we're going to take the value of that function and apply it to the argument 2 , something like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00332))_

```
((y) => x)(2)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00334))_

> This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from 'outside' of a function that are referenced inside a function. For example, here's the equivalent code in Ruby:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00335))_

```
lambda { |x|
lambda { |y| x }
}[1][2]
#=> 1
```

#### if functions without free variables are pure, are closures impure?

- 27 A free variable is one that is not bound within the function. _(javascriptallonge.pdf (source-range-0e12e052-00338))_
- Since the function (y) => x doesn't have an argument named x , the variable x isn't bound in this function, which makes it 'free.' _(javascriptallonge.pdf (source-range-0e12e052-00338))_
- It contains a free variable , x . _(javascriptallonge.pdf (source-range-0e12e052-00338))_
- 27 A free variable is one that is not bound within the function. _(javascriptallonge.pdf (source-range-0e12e052-00338))_
- Now that we know that variables used in a function are either bound or free, we can bifurcate functions into those with free variables and those without: _(javascriptallonge.pdf (source-range-0e12e052-00339))_
- - Functions containing no free variables are called pure functions . _(javascriptallonge.pdf (source-range-0e12e052-00340))_
- - Functions containing one or more free variables are called closures . _(javascriptallonge.pdf (source-range-0e12e052-00341))_
- Pure functions are easiest to understand. _(javascriptallonge.pdf (source-range-0e12e052-00342))_
- They always mean the same thing wherever you use them. _(javascriptallonge.pdf (source-range-0e12e052-00342))_
- The second doesn't have any free variables, because its only variable is bound. _(javascriptallonge.pdf (source-range-0e12e052-00343))_
- , and it doesn't have a free variable: The only variable anywhere in its body is x , which is certainly bound within (x) => ... _(javascriptallonge.pdf (source-range-0e12e052-00343))_
- The third one is actually two functions, one inside the other. _(javascriptallonge.pdf (source-range-0e12e052-00343))_
- The first function doesn't have any variables, therefore doesn't have any free variables. _(javascriptallonge.pdf (source-range-0e12e052-00343))_
- has a free variable, but the entire expression refers to (x) => ... _(javascriptallonge.pdf (source-range-0e12e052-00343))_
- The second doesn't have any free variables, because its only variable is bound. _(javascriptallonge.pdf (source-range-0e12e052-00343))_
- , and it doesn't have a free variable: The only variable anywhere in its body is x , which is certainly bound within (x) => ... _(javascriptallonge.pdf (source-range-0e12e052-00343))_
- The first function doesn't have any variables, therefore doesn't have any free variables. _(javascriptallonge.pdf (source-range-0e12e052-00343))_
- The third one is actually two functions, one inside the other. _(javascriptallonge.pdf (source-range-0e12e052-00343))_
- From this, we learn something: A pure function can contain a closure. _(javascriptallonge.pdf (source-range-0e12e052-00344))_
- Using only what we've learned so far, attempt to compose a closure that contains a pure function. _(javascriptallonge.pdf (source-range-0e12e052-00346))_
- If you can't, give your reasoning for why it's impossible. _(javascriptallonge.pdf (source-range-0e12e052-00346))_
- Using only what we've learned so far, attempt to compose a closure that contains a pure function. _(javascriptallonge.pdf (source-range-0e12e052-00346))_
- We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x . _(javascriptallonge.pdf (source-range-0e12e052-00347))_
- If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . _(javascriptallonge.pdf (source-range-0e12e052-00347))_
- 27 You may also hear the term 'non-local variable.' Both are correct. _(javascriptallonge.pdf (source-range-0e12e052-00348))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00342, source-range-0e12e052-00347))_

> Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we've already seen: Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magi

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00345))_

> [Figure] (p.45)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00347))_

> Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00346))_

> If pure functions can contain closures, can a closure contain a pure function?

#### it's always the environment

- As we've said before, all functions are associated with an environment. _(javascriptallonge.pdf (source-range-0e12e052-00350))_
- We also hand-waved something when describing our environment. _(javascriptallonge.pdf (source-range-0e12e052-00350))_
- To understand how closures are evaluated, we need to revisit environments. _(javascriptallonge.pdf (source-range-0e12e052-00350))_
- As we've said before, all functions are associated with an environment. _(javascriptallonge.pdf (source-range-0e12e052-00350))_
- (x) => (y) => x is called the K Combinator, or Kestrel . _(javascriptallonge.pdf (source-range-0e12e052-00353))_
- (x) => x is called the I Combinator, or the Identity Function . _(javascriptallonge.pdf (source-range-0e12e052-00353))_
- Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. _(javascriptallonge.pdf (source-range-0e12e052-00353))_
- (x) => (y) => x is called the K Combinator, or Kestrel . _(javascriptallonge.pdf (source-range-0e12e052-00353))_
- (x) => x is called the I Combinator, or the Identity Function . _(javascriptallonge.pdf (source-range-0e12e052-00353))_
- The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) . _(javascriptallonge.pdf (source-range-0e12e052-00360))_
- Only you call it with (1)(2)(3) instead of (1, 2, 3) . _(javascriptallonge.pdf (source-range-0e12e052-00360))_
- Calling a curried function with only some of its arguments is sometimes called partial application b . _(javascriptallonge.pdf (source-range-0e12e052-00361))_
- Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-0e12e052-00361))_
- The first function is the result of currying a the second function. _(javascriptallonge.pdf (source-range-0e12e052-00361))_
- Calling a curried function with only some of its arguments is sometimes called partial application b . _(javascriptallonge.pdf (source-range-0e12e052-00361))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00350))_

> To understand how closures are evaluated, we need to revisit environments. As we've said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...} ? Let's fill in the blanks!

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00351))_

> So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00353))_

> (x) => x is called the I Combinator, or the Identity Function . (x) => (y) => x is called the K Combinator, or Kestrel . Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. a http://www.amzn.com/0192801422?tag=raganwald001-20

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00355))_

```
bh
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00356))_

> Functions can have grandparents too:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00357))_

```
(x) =>
(y) =>
(z) => x + y + z
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00358, source-range-0e12e052-00361))_

> This function does much the same thing as: The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00359))_

```
(x, y, z) => x + y + z
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00362))_

```
ah
bh
```

#### shadowy variables from a shadowy planet

- An interesting thing happens when a variable has the same name as an ancestor environment's variable. _(javascriptallonge.pdf (source-range-0e12e052-00366))_
- Although its parent also defines an x , it is ignored when evaluating x + y . _(javascriptallonge.pdf (source-range-0e12e052-00368))_
- The function (x, y) => x + y is a pure function, because its x is defined within its own environment. _(javascriptallonge.pdf (source-range-0e12e052-00368))_
- JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. _(javascriptallonge.pdf (source-range-0e12e052-00368))_
- The function (x, y) => x + y is a pure function, because its x is defined within its own environment. _(javascriptallonge.pdf (source-range-0e12e052-00368))_
- The x in the great-great-grandparent scope is ignored, as are both w s. _(javascriptallonge.pdf (source-range-0e12e052-00370))_
- When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor. _(javascriptallonge.pdf (source-range-0e12e052-00370))_
- When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. _(javascriptallonge.pdf (source-range-0e12e052-00370))_
- This is often a good thing. _(javascriptallonge.pdf (source-range-0e12e052-00371))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00366, source-range-0e12e052-00368))_

> An interesting thing happens when a variable has the same name as an ancestor environment's variable. Consider: The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x , it is ignored when evaluating x + y . JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00367))_

```
(x) =>
(x, y) => x + y
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00368))_

> The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x , it is ignored when evaluating x + y . JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00369))_

```
(x) =>
(x, y) =>
(w, z) =>
(w) =>
x + y + z
```

#### which came first, the chicken or the egg?

- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. _(javascriptallonge.pdf (source-range-0e12e052-00373))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. _(javascriptallonge.pdf (source-range-0e12e052-00375))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. _(javascriptallonge.pdf (source-range-0e12e052-00375))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00375))_

> JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00376))_

> If you don't want your code to operate directly within the global environment, what can you do?

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00376))_

> Sometimes, programmers wish to avoid this. If you don't want your code to operate directly within the global environment, what can you do? Create an environment for them, of course. Many programmers choose to write every JavaScript file like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00377))_

```
// top of the file
(() => {
// ... lots of JavaScript ...
})();
// bottom of the file
```

### That Constant Coffee Craving

- Naming things is a critical part of programming, but all we've seen so far is how to name arguments. _(javascriptallonge.pdf (source-range-0e12e052-00380))_
- This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. _(javascriptallonge.pdf (source-range-0e12e052-00380))_
- Up to now, all we've really seen are anonymous functions , functions that don't have a name. _(javascriptallonge.pdf (source-range-0e12e052-00380))_
- In order to bind 3.14159265 to the name PI , we'll need a function with a parameter of PI applied to an argument of 3.14159265 . _(javascriptallonge.pdf (source-range-0e12e052-00383))_
- This expression, when evaluated, returns a function that calculates circumferences. _(javascriptallonge.pdf (source-range-0e12e052-00387))_
- All of our 'functions' are expressions. _(javascriptallonge.pdf (source-range-0e12e052-00387))_
- This one has a few more moving parts, that's all. _(javascriptallonge.pdf (source-range-0e12e052-00387))_
- That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. _(javascriptallonge.pdf (source-range-0e12e052-00387))_
- But we can use it just like (diameter) => diameter * 3.14159265 . _(javascriptallonge.pdf (source-range-0e12e052-00387))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00381))_

> There are other ways to name things in JavaScript, but before we learn some of those, let's see how to use what we already have to name things. Let's revisit a very simple example:

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00383))_

> In order to bind 3.14159265 to the name PI , we'll need a function with a parameter of PI applied to an argument of 3.14159265 . If we put our function expression in parentheses, we can apply it to the argument of 3.14159265 :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00384))_

```
((PI) =>
// ????
)(3.14159265)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00385))_

> What do we put inside our new function that binds 3.14159265 to the name PI when evaluated? Our circumference function, of course:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00386))_

```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00388))_

> Let's test it:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00390))_

```
((diameter) => diameter * 3.14159265)(2)
//=> 6.2831853
((PI) =>
(diameter) => diameter * PI
)(3.14159265)(2)
//=> 6.2831853
```

#### inside-out

- There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. _(javascriptallonge.pdf (source-range-0e12e052-00393))_
- There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. _(javascriptallonge.pdf (source-range-0e12e052-00393))_
- Well, the first one seems simplest, but a half-century of experience has taught us that names matter. _(javascriptallonge.pdf (source-range-0e12e052-00397))_
- A 'magic literal' like 3.14159265 is anathema to sustainable software development. _(javascriptallonge.pdf (source-range-0e12e052-00397))_
- The third one is easiest for most people to read. _(javascriptallonge.pdf (source-range-0e12e052-00398))_
- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-0e12e052-00399))_
- Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated 'IIFE.' _(javascriptallonge.pdf (source-range-0e12e052-00399))_
- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-0e12e052-00399))_
- Everything else is encapsulated in its body. _(javascriptallonge.pdf (source-range-0e12e052-00401))_
- That's how it should be, naming PI is its concern, not ours. _(javascriptallonge.pdf (source-range-0e12e052-00401))_
- Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. _(javascriptallonge.pdf (source-range-0e12e052-00405))_
- But then we've obfuscated our code, and we don't want to do that unless we absolutely have to. _(javascriptallonge.pdf (source-range-0e12e052-00407))_
- But then we've obfuscated our code, and we don't want to do that unless we absolutely have to. _(javascriptallonge.pdf (source-range-0e12e052-00407))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. _(javascriptallonge.pdf (source-range-0e12e052-00408))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. _(javascriptallonge.pdf (source-range-0e12e052-00408))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00393, source-range-0e12e052-00395))_

> There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. We can turn things inside-out by putting the binding inside our diameter calculating function, like this: It produces the same result as our previous expressions for a diameter-calculating function:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00394))_

```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00395))_

> It produces the same result as our previous expressions for a diameter-calculating function:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00396))_

```
((diameter) => diameter * 3.14159265)(2)
//=> 6.2831853
((PI) =>
(diameter) => diameter * PI
)(3.14159265)(2)
//=> 6.2831853
((diameter) =>
((PI) =>
diameter * PI)(3.14159265))(2)
//=> 6.2831853
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00399))_

> 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated 'IIFE.'

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00400))_

```
(diameter) =>
// ...
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00401))_

> Everything else is encapsulated in its body. That's how it should be, naming PI is its concern, not ours. The other formulation:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00402))_

```
((PI) =>
// ...
)(3.14159265)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00401))_

> Everything else is encapsulated in its body. That's how it should be, naming PI is its concern, not ours. The other formulation:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00404))_

```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00406))_

```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```

#### const

- Another way to write our 'circumference' function would be to pass PI along with the diameter argument, something like this: _(javascriptallonge.pdf (source-range-0e12e052-00410))_
- This differs from our example above in that there is only one environment, rather than two. _(javascriptallonge.pdf (source-range-0e12e052-00414))_
- We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name. _(javascriptallonge.pdf (source-range-0e12e052-00414))_
- This differs from our example above in that there is only one environment, rather than two. _(javascriptallonge.pdf (source-range-0e12e052-00414))_
- We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const : _(javascriptallonge.pdf (source-range-0e12e052-00415))_
- JavaScript gives us a way to do that, the const keyword. _(javascriptallonge.pdf (source-range-0e12e052-00415))_
- That's much better than what we were writing. _(javascriptallonge.pdf (source-range-0e12e052-00417))_
- We use the const keyword in a const statement . _(javascriptallonge.pdf (source-range-0e12e052-00418))_
- We can bind any expression. _(javascriptallonge.pdf (source-range-0e12e052-00425))_
- A name that's bound to a function is a valid expression evaluating to a function. _(javascriptallonge.pdf (source-range-0e12e052-00427))_
- Amazing how such an important idea-naming functions-can be explained en passant in just a few words. _(javascriptallonge.pdf (source-range-0e12e052-00428))_
- 30 We're into the second chapter and we've finally named a function. _(javascriptallonge.pdf (source-range-0e12e052-00431))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00410))_

> Another way to write our 'circumference' function would be to pass PI along with the diameter argument, something like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00411))_

```
(diameter, PI) => diameter * PI
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00412, source-range-0e12e052-00414))_

> And we could use it like this: This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00413))_

```
((diameter, PI) => diameter * PI)(2, 3.14159265)
//=> 6.2831853
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00415))_

> JavaScript gives us a way to do that, the const keyword. We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00416))_

```
(diameter) => {
const PI = 3.14159265;
return diameter * PI
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00419))_

> It works just as we want. Instead of:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00420))_

```
((diameter) =>
((PI) =>
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00419))_

> It works just as we want. Instead of:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00421))_

```
diameter * PI)(3.14159265))(2)
Or:
((diameter, PI) => diameter * PI)(2, 3.14159265)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00419))_

> It works just as we want. Instead of:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00422))_

```
//=> 6.2831853
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00423))_

> We write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00424))_

```
((diameter) => {
const PI = 3.14159265;
return diameter * PI
})(2)
//=> 6.2831853
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00425))_

> We can bind any expression. Functions are expressions, so we can bind helper functions:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00426))_

```
(d) => {
const calc = (diameter) => {
const PI = 3.14159265;
return diameter * PI
};
return "The circumference is " + calc(d)
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00425))_

> We can bind any expression. Functions are expressions, so we can bind helper functions:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00427))_

> This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () .

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00429))_

> Wecan bind more than one name-value pair by separating them with commas. For readability, most people put one binding per line:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00430))_

```
(d) => {
const PI
= 3.14159265,
calc = (diameter) => diameter * PI;
return "The circumference is " + calc(d)
}
```

#### nested blocks

- But there are other kinds of blocks. _(javascriptallonge.pdf (source-range-0e12e052-00433))_
- Up to now, we've only ever seen blocks we use as the body of functions. _(javascriptallonge.pdf (source-range-0e12e052-00433))_
- Up to now, we've only ever seen blocks we use as the body of functions. _(javascriptallonge.pdf (source-range-0e12e052-00433))_
- The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. _(javascriptallonge.pdf (source-range-0e12e052-00437))_
- We've used a block as the else clause, and since it's a block, we've placed a const statement inside it. _(javascriptallonge.pdf (source-range-0e12e052-00441))_
- We've used a block as the else clause, and since it's a block, we've placed a const statement inside it. _(javascriptallonge.pdf (source-range-0e12e052-00441))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00433))_

> One of the places you can find blocks is in an if statement.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00433))_

> Up to now, we've only ever seen blocks we use as the body of functions. But there are other kinds of blocks. One of the places you can find blocks is in an if statement. In JavaScript, an if statement looks like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00434))_

```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else
return !even(x - 1);
}
return even(n)
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00435))_

> And it works for fairly small numbers:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00436))_

```
((n) => {
const even = (x) => {
if (x === 0)
return true;
else
return !even(x - 1);
}
return even(n)
})(13)
//=> false
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00437))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00438))_

```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else {
const odd = (y) => !even(y);
return odd(x - 1);
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00437))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00439))_

```
}
return even(n)
}
And this also works:
((n) => {
const even = (x) => {
if (x === 0)
return true;
else {
const odd = (y) => !even(y);
return odd(x - 1);
}
}
return even(n)
})(42)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00437))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00440))_

```
//=> true
```

#### const and lexical scope

- This seems very straightforward, but alas, there are some semantics of binding names that we need to understand if we're to place const anywhere we like. _(javascriptallonge.pdf (source-range-0e12e052-00443))_
- It's more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we've elided. _(javascriptallonge.pdf (source-range-0e12e052-00447))_
- We can use any expression in there, and that expression can invoke diameter_fn . _(javascriptallonge.pdf (source-range-0e12e052-00447))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn . _(javascriptallonge.pdf (source-range-0e12e052-00449))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn . _(javascriptallonge.pdf (source-range-0e12e052-00449))_
- We can see that PI is bound in an environment surrounding (diameter) => diameter * PI , we don't need to know where diameter_fn is invoked. _(javascriptallonge.pdf (source-range-0e12e052-00450))_
- Although we have bound 3 to PI in the environment surrounding diameter_fn(2) , the value that counts is 3.14159265 , the value we bound to PI in the environment surrounding (diameter) ⇒ diameter * PI. _(javascriptallonge.pdf (source-range-0e12e052-00453))_
- That much we can carefully work out from the way closures work. _(javascriptallonge.pdf (source-range-0e12e052-00454))_
- Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-0e12e052-00457))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00445))_

> Here's the second formulation of our diameter function, bound to a name using an IIFE:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00446))_

```
((diameter_fn) =>
// ...
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00447, source-range-0e12e052-00450))_

> It's more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we've elided. We can use any expression in there, and that expression can invoke diameter_fn . For example: This is called lexical scoping 31 , because we can discover where a name is bound by looking at the source code for the program. We can see that PI is bound in an environment surrounding (diameter) => diameter * PI , we don't need to know where di

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00448))_

```
((diameter_fn) =>
diameter_fn(2)
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
//=> 6.2831853
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00451))_

> We can test this by deliberately creating a 'conflict:'

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00452))_

```
((diameter_fn) =>
((PI) =>
diameter_fn(2)
)(3)
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
//=> 6.2831853
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00454))_

> That much we can carefully work out from the way closures work. Does const work the same way? Let's find out:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00456))_

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

#### are consts also from a shadowy planet?

- Parameters are declared when we create functions, so it makes sense that parameters are bound to environments created when we invoke functions. _(javascriptallonge.pdf (source-range-0e12e052-00459))_
- They are looked up in the environment where they are declared. _(javascriptallonge.pdf (source-range-0e12e052-00459))_
- We just saw that values bound with const use lexical scope, just like values bound with parameters. _(javascriptallonge.pdf (source-range-0e12e052-00459))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. _(javascriptallonge.pdf (source-range-0e12e052-00460))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. _(javascriptallonge.pdf (source-range-0e12e052-00460))_
- But instead of binding two different variables to the same name in two different places, we'll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-0e12e052-00461))_
- And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. _(javascriptallonge.pdf (source-range-0e12e052-00468))_
- This is a book, you've already scanned ahead, so you know that the answer is no , the inner binding does not overwrite the outer binding: _(javascriptallonge.pdf (source-range-0e12e052-00470))_
- Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . _(javascriptallonge.pdf (source-range-0e12e052-00470))_
- It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-0e12e052-00472))_
- We say that when we bind a variable using a parameter inside another binding, the inner binding shadows the outer binding. _(javascriptallonge.pdf (source-range-0e12e052-00472))_
- It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-0e12e052-00472))_
- We'll need a gratuitous block. _(javascriptallonge.pdf (source-range-0e12e052-00476))_
- Parameters are only bound when we invoke a function. _(javascriptallonge.pdf (source-range-0e12e052-00476))_
- But const statements can appear inside blocks. _(javascriptallonge.pdf (source-range-0e12e052-00476))_
- Parameters are only bound when we invoke a function. _(javascriptallonge.pdf (source-range-0e12e052-00476))_
- But const statements can appear inside blocks. _(javascriptallonge.pdf (source-range-0e12e052-00476))_
- This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. _(javascriptallonge.pdf (source-range-0e12e052-00484))_
- Typically, we want to bind our names as close to where we need them as possible. _(javascriptallonge.pdf (source-range-0e12e052-00484))_
- This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. _(javascriptallonge.pdf (source-range-0e12e052-00484))_
- Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it. _(javascriptallonge.pdf (source-range-0e12e052-00484))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00462))_

> Let's start, as above, by doing this with parameters. We'll start with:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00463))_

```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00464))_

> And gratuitously wrap it in another IIFE so that we can bind PI to something else:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00465))_

```
((PI) =>
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)(3)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00466))_

> This still evaluates to a function that calculates diameters:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00467))_

```
((PI) =>
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)(3)(2)
//=> 6.2831853
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00468, source-range-0e12e052-00470))_

> And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the 'outer' environment? Let's rewrite things slightly differently: Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . Does that binding 'overwrite' the outer one? Will our function return 6 or 6.2831853 ? This is a book, you've already scanned ahead, so you know that t

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00469))_

```
((PI) => {
((PI) => {})(3);
return (diameter) => diameter * PI;
})(3.14159265)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00470))_

> Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . Does that binding 'overwrite' the outer one? Will our function return 6 or 6.2831853 ? This is a book, you've already scanned ahead, so you know that the answer is no , the inner binding does not overwrite the outer binding:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00471))_

```
((PI) => {
((PI) => {})(3);
return (diameter) => diameter * PI;
})(3.14159265)(2)
//=> 6.2831853
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00472))_

> We say that when we bind a variable using a parameter inside another binding, the inner binding shadows the outer binding. It has effect inside its own scope, but does not affect the binding in the enclosing scope.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00474))_

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00476))_

> Parameters are only bound when we invoke a function. That's why we made all these IIFEs. But const statements can appear inside blocks. What happens when we use a const inside of a block? We'll need a gratuitous block. We've seen if statements, what could be more gratuitous than:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00477))_

```
if (true) {
// an immediately invoked block statement (IIBS)
}
Let’s try it:
((diameter) => {
const PI = 3;
if (true) {
const PI = 3.14159265;
return diameter * PI;
}
})(2)
//=> 6.2831853
((diameter) => {
const PI = 3.14159265;
if (true) {
const PI = 3;
}
return diameter * PI;
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00476))_

> Parameters are only bound when we invoke a function. That's why we made all these IIFEs. But const statements can appear inside blocks. What happens when we use a const inside of a block? We'll need a gratuitous block. We've seen if statements, what could be more gratuitous than:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00478))_

```
})(2)
//=> 6.2831853
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00480, source-range-0e12e052-00482))_

> This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function's scope. In that case, we'd see things like this: If const always bound its value to the name defined in the function's environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would 'work:'

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00481))_

```
((diameter) => {
const PI = 3.14159265;
if (true) {
const PI = 3;
}
return diameter * PI;
})(2)
//=> would return 6 if const had function scope
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00480))_

> This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function's scope. In that case, we'd see things like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00482))_

> If const always bound its value to the name defined in the function's environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00482))_

> If const always bound its value to the name defined in the function's environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would 'work:'

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00483))_

```
((diameter) => {
if (true) {
const PI = 3.14159265;
}
return diameter * PI;
})(2)
//=> would return 6.2831853 if const had function scope
```

#### rebinding

- JavaScript does not permit us to rebind a name that has been bound with const . _(javascriptallonge.pdf (source-range-0e12e052-00491))_
- We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-0e12e052-00491))_
- This is valuable, as it greatly simplifies the analysis of programs to see at a glance that when something is bound with const , we need never worry that its value may change. _(javascriptallonge.pdf (source-range-0e12e052-00492))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00486))_

> By default, JavaScript permits us to rebind new values to names bound with a parameter. For example, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00488))_

```
const evenStevens = (n) => {
if (n === 0) {
return true;
}
else if (n == 1) {
return false;
}
else {
n = n - 2;
return evenStevens(n);
}
}
evenStevens(42)
//=> true
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00489))_

> The line n = n -2; rebinds a new value to the name n . We will discuss this at much greater length in Reassignment, but long before we do, let's try a similar thing with a name bound using const . We've already bound evenStevens using const , let's try rebinding it:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00490))_

```
evenStevens = (n) => {
if (n === 0) {
return true;
}
else if (n == 1) {
return false;
}
else {
return evenStevens(n - 2);
}
}
//=> ERROR, evenStevens is read-only
```

### Naming Functions

- This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous. _(javascriptallonge.pdf (source-range-0e12e052-00496))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00494, source-range-0e12e052-00496))_

> Let's get right to it. This code does not name a function: It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 . This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00495))_

```
const repeat = (str) => str + str
```

#### the function keyword

- JavaScript does have a syntax for naming a function, we use the function keyword. _(javascriptallonge.pdf (source-range-0e12e052-00498))_
- Until ECMAScript 2015 was created, function was the usual syntax for writing functions. _(javascriptallonge.pdf (source-range-0e12e052-00498))_
- - Something else we're about to discuss is optional. _(javascriptallonge.pdf (source-range-0e12e052-00505))_
- - We have arguments in parentheses, just like fat arrow functions. _(javascriptallonge.pdf (source-range-0e12e052-00506))_
- - We do not have a fat arrow, we go directly to the body. _(javascriptallonge.pdf (source-range-0e12e052-00507))_
- This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-0e12e052-00508))_
- - We always use a block, we cannot write function (str) str + str . _(javascriptallonge.pdf (source-range-0e12e052-00508))_
- This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-0e12e052-00508))_
- In this expression, double is the name in the environment, but repeat is the function's actual name. _(javascriptallonge.pdf (source-range-0e12e052-00518))_
- While the name of the function is a property of the function, not of the environment. _(javascriptallonge.pdf (source-range-0e12e052-00518))_
- That may seem confusing, but think of the binding names as properties of the environment, not of the function. _(javascriptallonge.pdf (source-range-0e12e052-00518))_
- 33 'Yes of course?' Well, in chapter of a book dedicated to naming functions, it is not surprising that feature we mention has something to do with naming functions. _(javascriptallonge.pdf (source-range-0e12e052-00522))_
- Now, the function's actual name has no effect on the environment in which it is used. _(javascriptallonge.pdf (source-range-0e12e052-00524))_
- So 'actualName' isn't bound in the environment where we use the named function expression. _(javascriptallonge.pdf (source-range-0e12e052-00526))_
- Here's a function that determines whether a positive integer is even or not. _(javascriptallonge.pdf (source-range-0e12e052-00526))_
- Clearly, the name even is bound to the function within the function's body . _(javascriptallonge.pdf (source-range-0e12e052-00528))_
- Clearly, the name even is bound to the function within the function's body . _(javascriptallonge.pdf (source-range-0e12e052-00528))_
- even is bound within the function itself, but not outside it. _(javascriptallonge.pdf (source-range-0e12e052-00530))_
- This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere else, you needn't. _(javascriptallonge.pdf (source-range-0e12e052-00530))_
- even is bound within the function itself, but not outside it. _(javascriptallonge.pdf (source-range-0e12e052-00530))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00499))_

> Here's our repeat function written using a 'fat arrow'

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00500))_

```
(str) => str + str
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00501))_

> And here's (almost) the exact same function written using the function keyword:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00502))_

```
function (str) { return str + str }
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00508))_

> We always use a block, we cannot write function (str) str + str . This means that if we want our functions to return a value, we always need to use the return keyword

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00509))_

> If we leave out the 'something optional' that comes after the function keyword, we can translate all of the fat arrow functions that we've seen into function keyword functions, e.g.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00509))_

> If we leave out the 'something optional' that comes after the function keyword, we can translate all of the fat arrow functions that we've seen into function keyword functions, e.g.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00510))_

```
(n) => (1.618**n - -1.618**-n) / 2.236
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00511, source-range-0e12e052-00513))_

> Can be written as: This still does not name a function, but as we noted above, functions written with the function keyword have an optional 'something else.' Could that 'something else' name a function? Yes, of course. 33

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00512))_

```
function (n) {
return (1.618**n - -1.618**-n) / 2.236;
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00514))_

> Here are our example functions written with names:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00515))_

```
const repeat = function repeat (str) {
return str + str;
};
const fib = function fib (n) {
return (1.618**n - -1.618**-n) / 2.236;
};
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00514))_

> Here are our example functions written with names:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00516))_

> Placing a name between the function keyword and the argument list names the function. Confusingly, the name of the function is not exactly the same thing as the name we may choose to bind to the value of the function. For example, we can write:

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00516))_

> Placing a name between the function keyword and the argument list names the function. Confusingly, the name of the function is not exactly the same thing as the name we may choose to bind to the value of the function. For example, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00517))_

```
const double = function repeat (str) {
return str + str;
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00519))_

> And indeed the name is a property:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00520))_

```
double.name
//=> 'repeat'
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00521))_

> In this book we are not examining JavaScript's tooling such as debuggers baked into browsers, but we will note that when you are navigating call stacks in all modern tools, the function's binding name is ignored but its actual name is displayed, so naming functions is very useful even if they don't get a formal binding, e.g.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00523))_

```
someBackboneView.on('click', function clickHandler () {
//...
});
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00524))_

> Now, the function's actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00525))_

```
const bindingName = function actualName () {
//...
};
bindingName
//=> [Function: actualName]
actualName
//=> ReferenceError: actualName is not defined
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00526))_

> So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines whether a positive integer is even or not. We'll use it in an IIFE so that we don't have to bind it to a name with const :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00527))_

```
(function even (n) {
if (n === 0) {
return true
}
else return !even(n - 1)
})(5)
//=> false
(function even (n) {
if (n === 0) {
return true
}
else return !even(n - 1)
})(2)
//=> true
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00526, source-range-0e12e052-00530))_

> So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines whether a positive integer is even or not. We'll use it in an IIFE so that we don't have to bind it to a name with const : even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere 

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00529))_

```
even
//=> Can't find variable: even
```

#### function declarations

- There is another syntax for naming and/or defining a function. _(javascriptallonge.pdf (source-range-0e12e052-00532))_
- In that it binds a name in the environment to a named function. _(javascriptallonge.pdf (source-range-0e12e052-00535))_
- First, function declarations are hoisted to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-0e12e052-00535))_
- However, there are two important differences. _(javascriptallonge.pdf (source-range-0e12e052-00535))_
- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. _(javascriptallonge.pdf (source-range-0e12e052-00538))_
- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. _(javascriptallonge.pdf (source-range-0e12e052-00538))_
- The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). _(javascriptallonge.pdf (source-range-0e12e052-00541))_
- It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code. _(javascriptallonge.pdf (source-range-0e12e052-00541))_
- This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. _(javascriptallonge.pdf (source-range-0e12e052-00541))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00532))_

> There is another syntax for naming and/or defining a function. It's called a function declaration statement , and it looks a lot like a named function expression, only we use it as a statement:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00533))_

```
function someName () {
// ...
}
This behaves a little like:
const someName = function someName ()
// ...
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00532, source-range-0e12e052-00536))_

> There is another syntax for naming and/or defining a function. It's called a function declaration statement , and it looks a lot like a named function expression, only we use it as a statement: Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00534))_

```
{
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00536))_

> Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const :

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00536))_

> Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00537))_

```
(function () {
return fizzbuzz();
const fizzbuzz = function fizzbuzz () {
return "Fizz" + "Buzz";
}
})()
//=> undefined is not a function (evaluating 'fizzbuzz()')
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00538))_

> We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00539))_

```
(function () {
return fizzbuzz();
function fizzbuzz () {
return "Fizz" + "Buzz";
}
})()
//=> 'FizzBuzz'
Although fizzbuzz is declared later in the function, JavaScript behaves as if we’d written:
(function () {
const fizzbuzz = function fizzbuzz () {
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00538))_

> We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00540))_

```
const fizzbuzz = function fizzbuzz ()
return "Fizz" + "Buzz";
}
return fizzbuzz();
})()
```

#### function declaration caveats 34

- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. _(javascriptallonge.pdf (source-range-0e12e052-00543))_
- Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-0e12e052-00543))_
- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. _(javascriptallonge.pdf (source-range-0e12e052-00543))_
- 34 A number of the caveats discussed here were described in Jyrly Zaytsev's excellent article Named function expressions demystified. _(javascriptallonge.pdf (source-range-0e12e052-00544))_
- Function declarations are not supposed to occur inside of blocks. _(javascriptallonge.pdf (source-range-0e12e052-00546))_
- The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. _(javascriptallonge.pdf (source-range-0e12e052-00546))_
- Function declarations are not supposed to occur inside of blocks. _(javascriptallonge.pdf (source-range-0e12e052-00546))_
- Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. _(javascriptallonge.pdf (source-range-0e12e052-00547))_
- Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. _(javascriptallonge.pdf (source-range-0e12e052-00547))_
- The parentheses make this an expression, not a function declaration. _(javascriptallonge.pdf (source-range-0e12e052-00549))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00544))_

> 34 A number of the caveats discussed here were described in Jyrly Zaytsev's excellent article Named function expressions demystified.

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00544))_

> 34 A number of the caveats discussed here were described in Jyrly Zaytsev's excellent article Named function expressions demystified.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00546))_

> Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00547))_

> Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. So this is a function declaration:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00548))_

```
function trueDat () { return true }
But this is not:
(function trueDat () { return true })
```

### Combinators and Function Decorators

#### higher-order functions

- JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. _(javascriptallonge.pdf (source-range-0e12e052-00552))_
- Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. _(javascriptallonge.pdf (source-range-0e12e052-00552))_
- But before we go on, we'll talk about some specific types of higher-order functions. _(javascriptallonge.pdf (source-range-0e12e052-00555))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00553))_

> Here's a very simple higher-order function that takes a function as an argument:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00554))_

```
const repeat = (num, fn) =>
(num > 0)
? (repeat(num - 1, fn), fn(num))
: undefined
repeat(3, function (n) {
console.log(`Hello ${n}`)
})
//=>
'Hello 1'
'Hello 2'
'Hello 3'
undefined
```

#### combinators

- We won't be strict about using only previously defined combinators in their construction. _(javascriptallonge.pdf (source-range-0e12e052-00558))_
- We won't be strict about using only previously defined combinators in their construction. _(javascriptallonge.pdf (source-range-0e12e052-00558))_
- This is, of course, just one example of many. _(javascriptallonge.pdf (source-range-0e12e052-00561))_
- While some programmers believe 'There Should Only Be One Way To Do It,' having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously. _(javascriptallonge.pdf (source-range-0e12e052-00561))_
- While some programmers believe 'There Should Only Be One Way To Do It,' having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously. _(javascriptallonge.pdf (source-range-0e12e052-00561))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00557))_

```text
combinators
The word 'combinator' has a precise technical meaning in mathematics:
'A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.'-Wikipedia 35
If we were learning Combinatorial Logic, we'd start with the most basic combinators like S , K , and I , and work up from there to practical combinators. We'd learn that the fundamental combinators are named after birds following the example of Raymond Smullyan's famous book To Mock a Mockingbird 36 .
35 https://en.wikipedia.org/wiki/Combinatory_logic
36 http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 35 | https://en.wikipedia.org/wiki/Combinatory_logic |
| 36 | http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20 |

</details>

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00559))_

> Let's start with a useful combinator: Most programmers call it Compose , although the logicians call it the B combinator or 'Bluebird.' Here is the typical 37 programming implementation:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00560))_

```
const compose = (a, b) =>
(c) => a(b(c))
Let’s say we have:
const addOne = (number) => number + 1;
const doubleOf = (number) => number * 2;
With compose, anywhere you would write
const doubleOfAddOne = (number) => doubleOf(addOne(number));
You could also write:
const doubleOfAddOne = compose(doubleOf, addOne);
```

#### a balanced statement about combinators

- So one perspective is that combinators are useful when you want to emphasize what you're doing and how it fits together, and more explicit code is useful when you want to emphasize what you're working with. _(javascriptallonge.pdf (source-range-0e12e052-00563))_
- Code that uses a lot of combinators tends to name the verbs and adverbs (like doubleOf , addOne , and compose ) while avoiding language keywords and the names of nouns (like number ). _(javascriptallonge.pdf (source-range-0e12e052-00563))_

#### function decorators

- So instead of writing !someFunction(42) , we can write not(someFunction)(42) . _(javascriptallonge.pdf (source-range-0e12e052-00567))_
- Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-0e12e052-00573))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. _(javascriptallonge.pdf (source-range-0e12e052-00573))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. _(javascriptallonge.pdf (source-range-0e12e052-00573))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00565))_

```text
function decorators
A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. Here's a ridiculously simple decorator: 38
37 As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context.
38 We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args)
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 37 | As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. |
| 38 | We'll see later why an even more useful version would be written (fn) => (...args) =>!fn(...args) |

</details>

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00566))_

```
const not = (fn) => (x) => !fn(x)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00567))_

> So instead of writing !someFunction(42) , we can write not(someFunction)(42) . Hardly progress. But like compose , we could write either:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00568))_

```
const something = (x) => x != null;
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00569))_

> And elsewhere, write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00570))_

```
const nothing = (x) => !something(x);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00571, source-range-0e12e052-00573))_

> Or we could write: not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00572))_

```
const nothing = not(something);
```

### Building Blocks

- The weakness is that you will. _(javascriptallonge.pdf (source-range-0e12e052-00575))_
- The strength of JavaScript is that you can do anything. _(javascriptallonge.pdf (source-range-0e12e052-00575))_
- Although you needn't restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks. _(javascriptallonge.pdf (source-range-0e12e052-00575))_
- There are ifs, fors, returns, everything thrown higgledy piggledy together. _(javascriptallonge.pdf (source-range-0e12e052-00575))_
- When you look at functions within functions in JavaScript, there's a bit of a 'spaghetti code' look to it. _(javascriptallonge.pdf (source-range-0e12e052-00575))_

#### composition

- It's really that simple: Whenever you are chaining two or more functions together, you're composing them. _(javascriptallonge.pdf (source-range-0e12e052-00579))_
- You can compose them with explicit JavaScript code as we've just done. _(javascriptallonge.pdf (source-range-0e12e052-00579))_
- If that was all there was to it, composition wouldn't matter much. _(javascriptallonge.pdf (source-range-0e12e052-00581))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-0e12e052-00581))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-0e12e052-00581))_
- We'll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined ) as an argument. _(javascriptallonge.pdf (source-range-0e12e052-00582))_
- Once is useful for ensuring that certain side effects are not repeated. _(javascriptallonge.pdf (source-range-0e12e052-00582))_
- In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. _(javascriptallonge.pdf (source-range-0e12e052-00582))_
- In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once. _(javascriptallonge.pdf (source-range-0e12e052-00582))_
- But once and maybe compose, so you can chain them together as you see fit: _(javascriptallonge.pdf (source-range-0e12e052-00583))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00577))_

> One of the most basic of these building blocks is composition :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00578))_

```
const cookAndEat = (food) => eat(cook(food));
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00579))_

> It's really that simple: Whenever you are chaining two or more functions together, you're composing them. You can compose them with explicit JavaScript code as we've just done. You can also generalize composition with the B Combinator or 'compose' that we saw in Combinators and Decorators:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00580))_

```
const compose = (a, b) => (c) => a(b(c));
const cookAndEat = compose(eat, cook);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00579))_

> It's really that simple: Whenever you are chaining two or more functions together, you're composing them. You can compose them with explicit JavaScript code as we've just done. You can also generalize composition with the B Combinator or 'compose' that we saw in Combinators and Decorators:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00581))_

> The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00581))_

> If that was all there was to it, composition wouldn't matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00583))_

> Of course, you needn't use combinators to implement either of these ideas, you can use if statements.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00583))_

> Of course, you needn't use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00584))_

```
const actuallyTransfer= (from, to, amount) =>
// do something
const invokeTransfer = once(maybe(actuallyTransfer(...)));
```

#### partial application

- Another basic building block is partial application . _(javascriptallonge.pdf (source-range-0e12e052-00586))_
- In that case, we can't get the final value, but we can get a function that represents part of our application. _(javascriptallonge.pdf (source-range-0e12e052-00586))_
- The Underscore 39 library provides a higher-order function called map . _(javascriptallonge.pdf (source-range-0e12e052-00587))_
- Code is easier than words for this. _(javascriptallonge.pdf (source-range-0e12e052-00587))_
- We can abstract this one level higher. _(javascriptallonge.pdf (source-range-0e12e052-00592))_
- mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-0e12e052-00592))_
- The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. _(javascriptallonge.pdf (source-range-0e12e052-00592))_
- The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely: _(javascriptallonge.pdf (source-range-0e12e052-00594))_
- Partial application also has a combinator, which we'll see in the partial recipe. _(javascriptallonge.pdf (source-range-0e12e052-00598))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00587, source-range-0e12e052-00590))_

> Code is easier than words for this. The Underscore 39 library provides a higher-order function called map . 40 It applies another function to each element of an array, like this: This code implements a partial application of the map function by applying the function (n) => n * n as its second argument:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00588))_

```
_.map([1, 2, 3], (n) => n * n)
//=> [1, 4, 9]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00590))_

> This code implements a partial application of the map function by applying the function (n) => n * n as its second argument:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00591))_

```
const squareAll = (array) => map(array,
(n) => n * n);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00592))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00593))_

```
const mapWith = (fn) =>
(array) => map(array, fn);
const squareAll = mapWith((n) => n * n);
squareAll([1, 2, 3])
//=> [1, 4, 9]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00594))_

> We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00595))_

```text
39 http://underscorejs.org
41 If we don't want to sort out Underscore, we can also write the following: const map = (a, fn) => a.map(fn); , and trust that it works even though we haven't discussed methods yet.
40 Modern JavaScript implementations provide a map method for arrays, but Underscore's implementation also works with older browsers if you are working with that headache.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 39 | http://underscorejs.org |
| 41 | If we don't want to sort out Underscore, we can also write the following: const map = (a, fn) => a.map(fn);, and trust that it works even though we haven't discussed methods yet. |
| 40 | Modern JavaScript implementations provide a map method for arrays, but Underscore's implementation also works with older browsers if you are working with that headache. |

</details>

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00594))_

> We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00596))_

```
const safeSquareAll = mapWith(maybe((n) => n * n));
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00594))_

> We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00597))_

```
safeSquareAll([1, null, 2, 3])
//=> [1, null, 4, 9]
```

### Magic Names

- What we haven't discussed so far is that JavaScript also binds values to some 'magic' names in addition to any you put in the argument list. _(javascriptallonge.pdf (source-range-0e12e052-00600))_
- When a function is applied to arguments (or 'called'), JavaScript binds the values of arguments to the function's argument names in an environment created for the function's execution. _(javascriptallonge.pdf (source-range-0e12e052-00600))_

#### the function keyword

- There are two separate rules for these 'magic' names, one for when you invoke a function using the function keyword, and another for functions defined with 'fat arrows.' We'll begin with how things work for functions defined with the function keyword. _(javascriptallonge.pdf (source-range-0e12e052-00602))_
- The first magic name is this , and it is bound to something called the function's context. _(javascriptallonge.pdf (source-range-0e12e052-00603))_
- The second magic name is very interesting, it's called arguments , and the most interesting thing about it is that it contains a list of arguments passed to a function: _(javascriptallonge.pdf (source-range-0e12e052-00603))_
- arguments always contains all of the arguments passed to a function, regardless of how many are declared. _(javascriptallonge.pdf (source-range-0e12e052-00607))_
- We'll see it used in many of the recipes, starting off with partial application and ellipses. _(javascriptallonge.pdf (source-range-0e12e052-00612))_
- The most common use of the arguments binding is to build functions that can take a variable number of arguments. _(javascriptallonge.pdf (source-range-0e12e052-00612))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00603))_

> The first magic name is this , and it is bound to something called the function's context. We will explore this in more detail when we start discussing objects and classes. The second magic name is very interesting, it's called arguments , and the most interesting thing about it is that it contains a list of arguments passed to a function:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00604))_

```
const plus = function (a, b) {
return arguments[0] + arguments[1];
}
plus(2,3)
//=> 5
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00605, source-range-0e12e052-00607))_

> Although arguments looks like an array, it isn't an array: It's more like an object 43 that happens to bind some values to properties with names that look like integers starting with zero: arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00606))_

```
const args = function (a, b) {
return arguments;
}
args(2,3)
//=> { '0': 2, '1': 3 }
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00607))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00608))_

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00607))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00609))_

```
const plus = function () {
return arguments[0] + arguments[1];
}
plus(2,3)
//=> 5
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00610))_

> When discussing objects, we'll discuss properties in more depth. Here's something interesting about arguments :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00611))_

```
const howMany = function () {
return arguments['length'];
}
howMany()
//=> 0
howMany('hello')
//=> 1
howMany('sharks', 'are', 'apex', 'predators')
//=> 4
```

#### magic names and fat arrows

- The magic names this and arguments have a different behaviour when you invoke a function that was defined with a fat arrow: Instead of being bound when the function is invoked, the fat arrow function always acquires the bindings for this and arguments from its enclosing scope, just like any other binding. _(javascriptallonge.pdf (source-range-0e12e052-00614))_
- For example, when this expression's inner function is defined with function , arguments[0] refers to its only argument, "inner" : _(javascriptallonge.pdf (source-range-0e12e052-00615))_
- For example, when this expression's inner function is defined with function , arguments[0] refers to its only argument, "inner" : _(javascriptallonge.pdf (source-range-0e12e052-00615))_
- But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function . _(javascriptallonge.pdf (source-range-0e12e052-00617))_
- Although it seems quixotic for the two syntaxes to have different semantics, it makes sense when you consider the design goal: Fat arrow functions are designed to be very lightweight and are often used with constructs like mapping or callbacks to emulate syntax. _(javascriptallonge.pdf (source-range-0e12e052-00619))_
- It uses mapWith , which we discussed in Building Blocks. _(javascriptallonge.pdf (source-range-0e12e052-00620))_
- To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. _(javascriptallonge.pdf (source-range-0e12e052-00620))_
- Our 'fat arrow' function (column) => column * arguments[0] doesn't bind arguments when it's invoked. _(javascriptallonge.pdf (source-range-0e12e052-00622))_
- This works just fine, because arguments[0] refers to the 3 we passed to the function row . _(javascriptallonge.pdf (source-range-0e12e052-00622))_
- This works just fine, because arguments[0] refers to the 3 we passed to the function row . _(javascriptallonge.pdf (source-range-0e12e052-00622))_
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. _(javascriptallonge.pdf (source-range-0e12e052-00623))_
- 44 Yes, we also used the name mapWith for working with ordinary collections elsewhere. _(javascriptallonge.pdf (source-range-0e12e052-00623))_
- But for the purposes of discussing ideas, we can use the same name twice in two different contexts. _(javascriptallonge.pdf (source-range-0e12e052-00623))_
- It's the same idea, after all. _(javascriptallonge.pdf (source-range-0e12e052-00623))_
- Although this example is clearly unrealistic, there is a general design principle that deserves attention. _(javascriptallonge.pdf (source-range-0e12e052-00626))_
- Sometimes, a function is meant to be used as a Big-F function. _(javascriptallonge.pdf (source-range-0e12e052-00626))_
- It's a simple representation of an expression to be computed. _(javascriptallonge.pdf (source-range-0e12e052-00627))_
- In our example above, row is a Big-F function, but (column) => column * arguments[0] is a small-f function, it exists just to give mapWith something to apply. _(javascriptallonge.pdf (source-range-0e12e052-00627))_
- Having magic variables apply to Big-F functions but not to small-G functions makes it much easier to use small-F functions as syntax, treating them as expressions or blocks that can be passed to functions like mapWith . _(javascriptallonge.pdf (source-range-0e12e052-00628))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00615))_

> For example, when this expression's inner function is defined with function , arguments[0] refers to its only argument, "inner" :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00616))_

```
(function () {
return (function () { return arguments[0]; })('inner');
})('outer')
//=> "inner"
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00617))_

> But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function . And thus arguments[0] will refer to "outer" , not to "inner" :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00618))_

```
(function () {
return (() => arguments[0])('inner');
})('outer')
//=> "outer"
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00620, source-range-0e12e052-00622))_

> To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. It uses mapWith , which we discussed in Building Blocks. 44 We'll use arguments just to show the difference between using a fat arrow and the function keyword: This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind arguments when it's invoked. But if we 

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00621))_

```
const row = function () {
return mapWith(
(column) => column * arguments[0],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
)
}
row(3)
//=> [3,6,9,12,15,18,21,24,27,30,33,36]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00623, source-range-0e12e052-00625))_

> 44 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. Now our inner function binds arguments[0] every time it is invoked, so we get the same result as if we'd written function (column)

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00624))_

```
const row = function () {
return mapWith(
function (column) { return column * arguments[0] },
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
)
}
row(3)
//=> [1,4,9,16,25,36,49,64,81,100,121,144]
```

### Summary

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00630))_

> [Figure] (p.78)

#### Functions

- - Functions are values that can be part of expressions, returned from other functions, and so forth. _(javascriptallonge.pdf (source-range-0e12e052-00632))_
- - Functions are reference values . _(javascriptallonge.pdf (source-range-0e12e052-00633))_
- - Functions are applied to arguments. _(javascriptallonge.pdf (source-range-0e12e052-00634))_
- - Fat arrow functions have expressions or blocks as their bodies. _(javascriptallonge.pdf (source-range-0e12e052-00636))_
- - function keyword functions always have blocks as their bodies. _(javascriptallonge.pdf (source-range-0e12e052-00637))_
- - Function bodies have zero or more statements. _(javascriptallonge.pdf (source-range-0e12e052-00638))_
- - Block bodies evaluate to whatever is returned with the return keyword, or to undefined . _(javascriptallonge.pdf (source-range-0e12e052-00640))_
- - JavaScript uses const to bind values to names within block scope. _(javascriptallonge.pdf (source-range-0e12e052-00641))_
- - JavaScript uses const to bind values to names within block scope. _(javascriptallonge.pdf (source-range-0e12e052-00641))_
- - JavaScript uses function declarations to bind functions to names within function scope. _(javascriptallonge.pdf (source-range-0e12e052-00642))_
- - JavaScript uses function declarations to bind functions to names within function scope. _(javascriptallonge.pdf (source-range-0e12e052-00642))_
- - Blocks also create scopes if const statements are within them. _(javascriptallonge.pdf (source-range-0e12e052-00644))_
- - Blocks also create scopes if const statements are within them. _(javascriptallonge.pdf (source-range-0e12e052-00644))_
- - Scopes are nested and free variable references closed over. _(javascriptallonge.pdf (source-range-0e12e052-00645))_
- - Variables can shadow variables in an enclosing scope. _(javascriptallonge.pdf (source-range-0e12e052-00646))_

## Recipes with Basic Functions

- Before combining ingredients, begin with implements so clean, they gleam. _(javascriptallonge.pdf (source-range-0e12e052-00649))_
- Before combining ingredients, begin with implements so clean, they gleam. _(javascriptallonge.pdf (source-range-0e12e052-00649))_
- Having looked at basic pure functions and closures, we're going to see some practical recipes that focus on the premise of functions that return functions. _(javascriptallonge.pdf (source-range-0e12e052-00650))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00648))_

> [Figure] (p.79)

#### Disclaimer

- The overall use of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-0e12e052-00652))_
- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven't been discussed in the text to this point, such as methods and/or prototypes. _(javascriptallonge.pdf (source-range-0e12e052-00652))_
- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven't been discussed in the text to this point, such as methods and/or prototypes. _(javascriptallonge.pdf (source-range-0e12e052-00652))_
- The overall use of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-0e12e052-00652))_

### Partial Application

- These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. _(javascriptallonge.pdf (source-range-0e12e052-00655))_
- 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. _(javascriptallonge.pdf (source-range-0e12e052-00655))_
- As noted above, our partial recipe allows us to create functions that are partial applications of functions that are context aware. _(javascriptallonge.pdf (source-range-0e12e052-00657))_
- We'd need a different recipe if we wish to create partial applications of object methods. _(javascriptallonge.pdf (source-range-0e12e052-00657))_
- We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument: _(javascriptallonge.pdf (source-range-0e12e052-00660))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00654))_

```text
Partial Application
In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libraries provide some form of partial application. You'll find examples in Lemonad 45 from Michael Fogus, Functional JavaScript 46 from Oliver Steele and the terse but handy node-ap 47 from James Halliday.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 45 | from Michael Fogus, Functional JavaScript |
| 46 | from Oliver Steele and the terse but handy node-ap |
| 47 | from James Halliday. |

</details>

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00655, source-range-0e12e052-00657))_

> These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic. As noted above, our partial recipe allows us to create functions that are partial applications of functions that are context aware. We'd need a different recipe 

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00656))_

```
const callFirst = (fn, larg) =>
function (...rest) {
return fn.call(this, larg, ...rest);
}
const callLast = (fn, rarg) =>
function (...rest) {
return fn.call(this, ...rest, rarg);
}
const greet = (me, you) =>
`Hello, ${you}, my name is ${me}`;
const heliosSaysHello = callFirst(greet, 'Helios');
heliosSaysHello('Eartha')
//=> 'Hello, Eartha, my name is Helios'
const sayHelloToCeline = callLast(greet, 'Celine');
sayHelloToCeline('Eartha')
//=> 'Hello, Celine, my name is Eartha'
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00655))_

> These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00658))_

```text
45 https://github.com/fogus/lemonad 46 http://osteele.com/sources/javascript/functional/ 47 https://github.com/substack/node-ap 48
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 45 | https://github.com/fogus/lemonad |
| 46 | http://osteele.com/sources/javascript/functional/ |
| 47 | https://github.com/substack/node-ap 48 |

</details>

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00660))_

> We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00661))_

```
const callLeft = (fn, ...args) =>
(...remainingArgs) =>
fn(...args, ...remainingArgs);
const callRight = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
```

### Unary

- The most common use case is to fix a problem. _(javascriptallonge.pdf (source-range-0e12e052-00664))_
- JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. _(javascriptallonge.pdf (source-range-0e12e052-00664))_
- But some functions have optional second or even third arguments. _(javascriptallonge.pdf (source-range-0e12e052-00669))_
- And when you call parseInt with map , the index is interpreted as a radix. _(javascriptallonge.pdf (source-range-0e12e052-00671))_
- What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-0e12e052-00671))_
- What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-0e12e052-00671))_
- This doesn't work because parseInt is defined as parseInt(string[, radix]) . _(javascriptallonge.pdf (source-range-0e12e052-00671))_
- This doesn't work because parseInt is defined as parseInt(string[, radix]) . _(javascriptallonge.pdf (source-range-0e12e052-00671))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00664))_

> The most common use case is to fix a problem. JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. Here it is in action:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00665))_

```
['1', '2', '3'].map(parseFloat)
//=> [1, 2, 3]
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00668))_

```
[1, 2, 3].map(function (element, index, arr) {
console.log({element: element, index: index, arr: arr})
})
//=> { element: 1, index: 0, arr: [ 1, 2, 3 ] }
//
{ element: 2, index: 1, arr: [ 1, 2, 3 ] }
//
{ element: 3, index: 2, arr: [ 1, 2, 3 ] }
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00667, source-range-0e12e052-00671))_

> Let's try it: This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00669))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00669, source-range-0e12e052-00671))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example: This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00670))_

```
['1', '2', '3'].map(parseInt)
//=> [1, NaN, NaN]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00671))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00672))_

> Wecould write ['1', '2', '3'].map((s) => parseInt(s)) , or we could come up with a decorator to do the job for us:

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00672))_

> Wecould write ['1', '2', '3'].map((s) => parseInt(s)) , or we could come up with a decorator to do the job for us:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00673))_

```
const unary = (fn) =>
fn.length === 1
? fn
: function (something) {
return fn.call(this, something)
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00674))_

> And now we can write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00675))_

```
['1', '2', '3'].map(unary(parseInt))
//=> [1, 2, 3]
```

### Tap

- One is when you want to do something with a value for sideeffects, but keep the value around. _(javascriptallonge.pdf (source-range-0e12e052-00680))_
- It has some surprising applications. _(javascriptallonge.pdf (source-range-0e12e052-00680))_
- tap is a traditional name borrowed from various Unix shell commands. _(javascriptallonge.pdf (source-range-0e12e052-00682))_
- tap can do more than just act as a debugging aid. _(javascriptallonge.pdf (source-range-0e12e052-00688))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00679))_

```
const K = (x) => (y) => x;
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00680))_

> It has some surprising applications. One is when you want to do something with a value for sideeffects, but keep the value around. Behold:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00681))_

```
const tap = (value) =>
(fn) => (
typeof(fn) === 'function' && fn(value),
value
)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00684))_

> Let's enhance our recipe so that it works both ways:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00686))_

```
const tap = (value, fn) => {
const curried = (fn) => (
typeof(fn) === 'function' && fn(value),
value
);
return fn === undefined
? curried
: curried(fn);
}
Now we can write:
tap('espresso')((it) => {
console.log(`Our drink is '${it}'`)
});
//=> Our drink is 'espresso'
'espresso'
Or:
tap('espresso', (it) => {
console.log(`Our drink is '${it}'`)
});
//=> Our drink is 'espresso'
'espresso'
```

### Maybe

- Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-0e12e052-00690))_
- A common problem in programming is checking for null or undefined (hereafter called 'nothing,' while all other values including 0 , [] and false will be called 'something'). _(javascriptallonge.pdf (source-range-0e12e052-00690))_
- Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing: _(javascriptallonge.pdf (source-range-0e12e052-00693))_
- Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation: _(javascriptallonge.pdf (source-range-0e12e052-00695))_
- If some code ever tries to call model.setSomething with nothing, the operation will be skipped. _(javascriptallonge.pdf (source-range-0e12e052-00703))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00691))_

> This recipe concerns a pattern that is very common: A function fn takes a value as a parameter, and its behaviour by design is to do nothing if the parameter is nothing:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00692))_

```
const isSomething = (value) =>
value !== null && value !== void 0;
const checksForSomething = (value) => {
if (isSomething(value)) {
// function's true logic
}
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00693))_

> Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00694))_

```
var something =
isSomething(value)
? doesntCheckForSomething(value)
: value;
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00695))_

> Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00696))_

```
const maybe = (fn) =>
function (...args) {
if (args.length === 0) {
return
}
else {
for (let arg of args) {
if (arg == null) return;
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00695))_

> Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00697))_

```text
50 https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad
51 https://github.com/raganwald/andand
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 50 | https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad |
| 51 | https://github.com/raganwald/andand |

</details>

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00695))_

> Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00698))_

```
return fn.apply(this, args)
}
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00699))_

> maybe reduces the logic of checking for nothing to a function call:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00700))_

```
maybe((a, b, c) => a + b + c)(1, 2, 3)
//=> 6
maybe((a, b, c) => a + b + c)(1, null, 3)
//=> undefined
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00701))_

> As a bonus, maybe plays very nicely with instance methods, we'll discuss those later:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00702))_

```
function Model () {};
Model.prototype.setSomething = maybe(function (value) {
this.something = value;
});
```

### Once

- once is an extremely helpful combinator. _(javascriptallonge.pdf (source-range-0e12e052-00705))_
- It ensures that a function can only be called, well, once . _(javascriptallonge.pdf (source-range-0e12e052-00705))_
- It ensures that a function can only be called, well, once . _(javascriptallonge.pdf (source-range-0e12e052-00705))_
- That function will call your function once, and thereafter will return undefined whenever it is called. _(javascriptallonge.pdf (source-range-0e12e052-00707))_
- That function will call your function once, and thereafter will return undefined whenever it is called. _(javascriptallonge.pdf (source-range-0e12e052-00707))_
- (Note: There are some subtleties with decorators like once that involve the intersection of state with methods. _(javascriptallonge.pdf (source-range-0e12e052-00710))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00705))_

> once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00706))_

```
const once = (fn) => {
let done = false;
return function () {
return done ? void 0 : ((done = true), fn.apply(this, arguments))
}
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00707))_

> Very simple! You pass it a function, and you get a function back. That function will call your function once, and thereafter will return undefined whenever it is called. Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00708))_

```
const askedOnBlindDate = once(
() => "sure, why not?"
);
askedOnBlindDate()
//=> 'sure, why not?'
askedOnBlindDate()
//=> undefined
askedOnBlindDate()
//=> undefined
```

### Left-Variadic Functions

- A variadic function is a function that is designed to accept a variable number of arguments. _(javascriptallonge.pdf (source-range-0e12e052-00712))_
- For example, we might want to have a function that builds some kind of team record. _(javascriptallonge.pdf (source-range-0e12e052-00714))_
- This can be useful when writing certain kinds of destructuring algorithms. _(javascriptallonge.pdf (source-range-0e12e052-00714))_
- For example, we might want to have a function that builds some kind of team record. _(javascriptallonge.pdf (source-range-0e12e052-00714))_
- 52 English is about as inconsistent as JavaScript: Functions with a fixed number of arguments can be unary, binary, ternary, and so forth. _(javascriptallonge.pdf (source-range-0e12e052-00716))_
- ECMAScript 2015 only permits gathering parameters from the end of the parameter list. _(javascriptallonge.pdf (source-range-0e12e052-00718))_
- ECMAScript 2015 only permits gathering parameters from the end of the parameter list. _(javascriptallonge.pdf (source-range-0e12e052-00718))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00712))_

> A variadic function is a function that is designed to accept a variable number of arguments. 52 In JavaScript, you can make a variadic function by gathering parameters. For example:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00713))_

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00714))_

> This can be useful when writing certain kinds of destructuring algorithms. For example, we might want to have a function that builds some kind of team record. It accepts a coach, a captain, and an arbitrary number of players. Easy in ECMAScript 2015:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00715))_

```
function team(coach, captain, ...players) {
console.log(`${captain} (captain)`);
for (let player of players) {
console.log(player);
}
console.log(`squad coached by ${coach}`);
}
team('Luis Enrique', 'Xavi Hernández', 'Marc-André ter Stegen',
'Martín Montoya', 'Gerard Piqué')
//=>
Xavi Hernández (captain)
Marc-André ter Stegen
Martín Montoya
Gerard Piqué
squad coached by Luis Enrique
But we can’t go the other way around:
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00714))_

> This can be useful when writing certain kinds of destructuring algorithms. For example, we might want to have a function that builds some kind of team record. It accepts a coach, a captain, and an arbitrary number of players. Easy in ECMAScript 2015:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00717))_

```
function team2(...players, captain, coach) {
console.log(`${captain} (captain)`);
for (let player of players) {
console.log(player);
}
console.log(`squad coached by ${coach}`);
}
//=> Unexpected token
```

#### a history lesson

- In 'Ye Olde Days,' 53 JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice , or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. _(javascriptallonge.pdf (source-range-0e12e052-00720))_
- This is a right-variadic function , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument. _(javascriptallonge.pdf (source-range-0e12e052-00726))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00720, source-range-0e12e052-00723))_

> In 'Ye Olde Days,' 53 JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice , or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. Here it is in all of its ECMAScript-5 glory: We don't need rightVariadic any more, because instead of:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00721))_

```
var __slice = Array.prototype.slice;
function rightVariadic (fn) {
if (fn.length < 1) return fn;
return function () {
var ordinaryArgs = (1 <= arguments.length ?
__slice.call(arguments, 0, fn.length - 1) : []),
restOfTheArgsList = __slice.call(arguments, fn.length - 1),
args = (fn.length <= arguments.length ?
ordinaryArgs.concat([restOfTheArgsList]) : []);
return fn.apply(this, args);
}
};
var firstAndButFirst = rightVariadic(function test (first, butFirst) {
return [first, butFirst]
});
firstAndButFirst('why', 'hello', 'there', 'little', 'droid')
//=> ["why",["hello","there","little","droid"]]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00723))_

> We don't need rightVariadic any more, because instead of:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00724))_

```
var firstAndButFirst = rightVariadic(
function test (first, butFirst) {
return [first, butFirst]
});
We now simply write:
const firstAndButFirst = (first, ...butFirst)
[first, butFirst];
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00723))_

> We don't need rightVariadic any more, because instead of:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00725))_

```
=>
```

#### overcoming limitations

- All left-variadic functions have one or more fixed arguments, and the rest are gathered into the leftmost argument. _(javascriptallonge.pdf (source-range-0e12e052-00730))_
- Our leftVariadic function is a decorator that turns any function into a function that gathers parameters from the left , instead of from the right. _(javascriptallonge.pdf (source-range-0e12e052-00734))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00728))_

> It's nice to have progress. But as noted above, we can't write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00729))_

```
const butLastAndLast = (...butLast, last) =>
[butLast, last];
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00731))_

> We sure can, by using the techniques from rightVariadic . Mind you, we can take advantage of modern JavaScript to simplify the code:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00732))_

```
const leftVariadic = (fn) => {
if (fn.length < 1) {
return fn;
}
else {
return function (...args) {
const gathered = args.slice(0, args.length - fn.length + 1),
spread
= args.slice(args.length - fn.length + 1);
return fn.apply(
this, [gathered].concat(spread)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00731))_

> We sure can, by using the techniques from rightVariadic . Mind you, we can take advantage of modern JavaScript to simplify the code:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00733))_

```
);
}
}
};
const butLastAndLast = leftVariadic((butLast, last) => [butLast, last]);
butLastAndLast('why', 'hello', 'there', 'little', 'droid')
//=> [["why","hello","there","little"],"droid"]
```

#### left-variadic destructuring

- Gathering arguments for functions is one of the ways JavaScript can destructure arrays. _(javascriptallonge.pdf (source-range-0e12e052-00736))_
- But we can write our own left-gathering function utility using the same principles without all the tedium: _(javascriptallonge.pdf (source-range-0e12e052-00742))_
- With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function. _(javascriptallonge.pdf (source-range-0e12e052-00744))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00736))_

> Gathering arguments for functions is one of the ways JavaScript can destructure arrays. Another way is when assigning variables, like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00737))_

```
const [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid'];
first
//=> 'why'
butFirst
//=> ["hello","there","little","droid"]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00738))_

> As with parameters, we can't gather values from the left when destructuring an array:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00739))_

```
const [...butLast, last] = ['why', 'hello', 'there', 'little', 'droid'];
//=> Unexpected token
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00740))_

> We could use leftVariadic the hard way:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00741))_

```
const [butLast, last] = leftVariadic((butLast, last) => [butLast, last])(...['wh\
y', 'hello', 'there', 'little', 'droid']);
butLast
//=> ['why', 'hello', 'there', 'little']
last
//=> 'droid'
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00742, source-range-0e12e052-00744))_

> But we can write our own left-gathering function utility using the same principles without all the tedium: With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00743))_

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

## Picking the Bean: Choice and Truthiness

- In addition to numbers, we often need to represent a much more basic idea of truth or falsehood. _(javascriptallonge.pdf (source-range-0e12e052-00748))_
- All values of true are === all other values of true. _(javascriptallonge.pdf (source-range-0e12e052-00754))_
- true and false are value types. _(javascriptallonge.pdf (source-range-0e12e052-00754))_
- Now, note well: We have said what happens if you pass boolean values to ! _(javascriptallonge.pdf (source-range-0e12e052-00758))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00746))_

> [Figure] (p.94)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00754))_

> true and false are value types. All values of true are === all other values of true. We can see that is the case by looking at some operators we can perform on boolean values, ! , && , and || . To being with, ! is a unary prefix operator that negates its argument. So:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00755))_

```
!true
//=> false
!false
//=> true
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00756))_

> The && and || operators are binary infix operators that perform 'logical and' and 'logical or' respectively:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00757))_

```
false && false //=> false
false && true
//=> false
true
&& false //=> false
true
&& true
//=> true
false || false //=> false
false || true
//=> true
true
|| false //=> true
true
|| true
//=> true
```

#### truthiness and the ternary operator

- So are null and undefined , values that semantically represent 'no value.' NaN is falsy, a value representing the result of a calculation that is not a number. _(javascriptallonge.pdf (source-range-0e12e052-00760))_
- 54 And there are more: 0 is falsy, a value representing 'none of something.' The empty string, '' is falsy, a value representing having no characters. _(javascriptallonge.pdf (source-range-0e12e052-00760))_
- In JavaScript, there is a notion of 'truthiness.' Every value is either 'truthy' or 'falsy.' Obviously, false is falsy. _(javascriptallonge.pdf (source-range-0e12e052-00760))_
- (Many other languages that have a notion of truthiness consider zero and the empty string to be truthy, not falsy, so beware of blindly transliterating code from one language to another!) _(javascriptallonge.pdf (source-range-0e12e052-00761))_
- Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' . _(javascriptallonge.pdf (source-range-0e12e052-00761))_
- Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' . _(javascriptallonge.pdf (source-range-0e12e052-00761))_
- The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on truthiness , not on boolean values. _(javascriptallonge.pdf (source-range-0e12e052-00762))_
- If first is not truthy, it evaluates third and that is its value. _(javascriptallonge.pdf (source-range-0e12e052-00763))_
- JavaScript inherited an operator from the C family of languages, the ternary operator. _(javascriptallonge.pdf (source-range-0e12e052-00763))_
- It evaluates first , and if first is 'truthy', it evaluates second and that is its value. _(javascriptallonge.pdf (source-range-0e12e052-00763))_
- It's the only operator that takes three arguments. _(javascriptallonge.pdf (source-range-0e12e052-00763))_
- It also doesn't introduce braces, and that can be a help or a hindrance if we want to introduce a new scope or use statements. _(javascriptallonge.pdf (source-range-0e12e052-00765))_
- This is a lot like the if statement, however it is an expression , not a statement, and that can be very valuable. _(javascriptallonge.pdf (source-range-0e12e052-00765))_
- Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true . _(javascriptallonge.pdf (source-range-0e12e052-00769))_
- Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true . _(javascriptallonge.pdf (source-range-0e12e052-00769))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00766))_

> Here're some simple examples of the ternary operator:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00767))_

```
true ? 'Hello' : 'Good bye'
//=> 'Hello'
0 ? 'Hello' : 'Good bye'
//=> 'Good bye'
[1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal'
//=> 'Pentatonic'
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00766))_

> Here're some simple examples of the ternary operator:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00768))_

```text
//=> 'Hello'
0 ? 'Hello' : 'Good bye'
//=> 'Good bye'
[1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal'
//=> 'Pentatonic'
The fact that either the second or the third (but not both) expressions are evaluated can have
important repercussions. Consider this hypothetical example:
const status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\
den';
We certainly don’t want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAutho-
rized(currentUser) returns true.
truthiness and operators
Our logical operators !, &&, and || are a little more subtle than our examples above implied. ! is the
simplest. It always returns false if its argument is truthy, and true is its argument is not truthy:
!5
//=> false
!undefined
//=> true
Programmers often take advantage of this behaviour to observe that !!(someExpression) will
always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript
(and other languages with similar semantics), when you see something like !!currentUser(), this
Picking the Bean: Choice and Truthiness
74
is an idiom that means “true if currentUser is truthy.” Thus, a function like currentUser() is free to
return null, or undefined, or false if there is no current user.
Thus, !! is the way we write “is truthy” in JavaScript. How about && and ||? What haven’t we
discussed?
First, and unlike !, && and || do not necessarily evaluate to true or false. To be precise:
• && evaluates its left-hand expression.
– If its left-hand expression evaluates to something falsy, && returns the value of its left-
hand expression without evaluating its right-hand expression.
– If its left-hand expression evaluates to something truthy, && evaluates its right-hand
expression and returns the value of the right-hand expression.
• || evaluates its left-hand expression.
– If its left-hand expression evaluates to something truthy, || returns the value of its left-
hand expression without evaluating its right-hand expression.
– If its left-hand expression evaluates to something false, || evaluates its right-hand
expression and returns the value of the right-hand expression.
If we look at our examples above, we see that when we pass true and false to && and ||, we do
indeed get true or false as a result. But when we pass other values, we no longer get true or false:
1 || 2
//=> 1
null && undefined
//=> null
undefined && null
//=> undefined
In JavaScript, && and || aren’t boolean logical operators in the logical sense. They don’t operate
strictly on logical values, and they don’t commute: a || b is not always equal to b || a, and the
same goes for &&.
This is not a subtle distinction.
|| and && are control-flow operators
We’ve seen the ternary operator: It is a control-flow operator, not a logical operator. The same is
true of && and ||. Consider this tail-recursive function that determines whether a positive integer
is even:
For example:
Picking the Bean: Choice and Truthiness
75
const even = (n) =>
n === 0 || (n !== 1 && even(n - 2))
even(42)
//=> true
If n === 0, JavaScript does not evaluate (n !== 1 && even(n - 2)). This is very important!
Imagine that JavaScript evaluated both sides of the || operator before determining its value. n ===
0 would be true. What about (n !== 1 && even(n - 2))? Well, it would evaluate even(n - 2), or
even(-2)
This leads us to evaluate n === 0 || (n !== 1 && even(n - 2)) all over again, and this time we
end up evaluating even(-4). And then even(-6). and so on and so forth until JavaScript throws up
its hands and runs out of stack space.
But that’s not what happens. || and && have short-cut semantics. In this case, if n === 0, JavaScript
does not evaluate (n !== 1 && even(n - 2)). Likewise, if n === 1, JavaScript evaluates n !== 1
&& even(n - 2) as false without ever evaluating even(n - 2).
This is more than just an optimization. It’s best to think of || and && as control-flow operators. The
expression on the left is always evaluated, and its value determines whether the expression on the
right is evaluated or not.
function parameters are eager
In contrast to the behaviour of the ternary operator, ||, and &&, function parameters are always
eagerly evaluated:
const or = (a, b) => a || b
const and = (a, b) => a && b
const even = (n) =>
or(n === 0, and(n !== 1, even(n - 2)))
even(42)
//=> Maximum call stack size exceeded.
Now our expression or(n === 0, and(n !== 1, even(n - 2))) is calling functions, and JavaScript
always evaluates the expressions for parameters before passing the values to a function to invoke.
This leads to the infinite recursion we fear.
If we need to have functions with control-flow semantics, we can pass anonymous functions. We
obviously don’t need anything like this for or and and, but to demonstrate the technique:
Picking the Bean: Choice and Truthiness
76
const or = (a, b) => a() || b()
const and = (a, b) => a() && b()
const even = (n) =>
or(() => n === 0, () => and(() => n !== 1, () => even(n - 2)))
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 74 | is an idiom that means “true if currentUser is truthy.” Thus, a function like currentUser() is free to return null, or undefined, or false if there is no current user. Thus,!! is the way we write “is truthy” in JavaScript. How about && and \|\|? What haven’t we discussed? First, and unlike!, && and \|\| do not necessarily evaluate to true or false. To be precise: • && evaluates its left-hand expression. – If its left-hand expression evaluates to something falsy, && returns the value of its left- hand expression without evaluating its right-hand expression. – If its left-hand expression evaluates to something truthy, && evaluates its right-hand expression and returns the value of the right-hand expression. • \|\| evaluates its left-hand expression. – If its left-hand expression evaluates to something truthy, \|\| returns the value of its left- hand expression without evaluating its right-hand expression. – If its left-hand expression evaluates to something false, \|\| evaluates its right-hand expression and returns the value of the right-hand expression. If we look at our examples above, we see that when we pass true and false to && and \|\|, we do indeed get true or false as a result. But when we pass other values, we no longer get true or false: |
| 1 | \|\| 2 //=> 1 null && undefined //=> null undefined && null //=> undefined In JavaScript, && and \|\| aren’t boolean logical operators in the logical sense. They don’t operate strictly on logical values, and they don’t commute: a \|\| b is not always equal to b \|\| a, and the same goes for &&. This is not a subtle distinction. \|\| and && are control-flow operators We’ve seen the ternary operator: It is a control-flow operator, not a logical operator. The same is true of && and \|\|. Consider this tail-recursive function that determines whether a positive integer is even: |
| 75 | For example: Picking the Bean: Choice and Truthiness const even = (n) => n === 0 \|\| (n!== 1 && even(n - 2)) even(42) //=> true If n === 0, JavaScript does not evaluate (n!== 1 && even(n - 2)). This is very important! Imagine that JavaScript evaluated both sides of the \|\| operator before determining its value. n === |
| 0 | would be true. What about (n!== 1 && even(n - 2))? Well, it would evaluate even(n - 2), or even(-2) This leads us to evaluate n === 0 \|\| (n!== 1 && even(n - 2)) all over again, and this time we end up evaluating even(-4). And then even(-6). and so on and so forth until JavaScript throws up its hands and runs out of stack space. But that’s not what happens. \|\| and && have short-cut semantics. In this case, if n === 0, JavaScript does not evaluate (n!== 1 && even(n - 2)). Likewise, if n === 1, JavaScript evaluates n!== 1 && even(n - 2) as false without ever evaluating even(n - 2). This is more than just an optimization. It’s best to think of \|\| and && as control-flow operators. The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. function parameters are eager In contrast to the behaviour of the ternary operator, \|\|, and &&, function parameters are always eagerly evaluated: const or = (a, b) => a \|\| b const and = (a, b) => a && b const even = (n) => or(n === 0, and(n!== 1, even(n - 2))) even(42) //=> Maximum call stack size exceeded. Now our expression or(n === 0, and(n!== 1, even(n - 2))) is calling functions, and JavaScript always evaluates the expressions for parameters before passing the values to a function to invoke. This leads to the infinite recursion we fear. If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don’t need anything like this for or and and, but to demonstrate the technique: |
| 76 | Picking the Bean: Choice and Truthiness const or = (a, b) => a() \|\| b() const and = (a, b) => a() && b() const even = (n) => or(() => n === 0, () => and(() => n!== 1, () => even(n - 2))) |

</details>

#### truthiness and operators

- It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-0e12e052-00771))_
- , && , and || are a little more subtle than our examples above implied. _(javascriptallonge.pdf (source-range-0e12e052-00771))_
- Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. _(javascriptallonge.pdf (source-range-0e12e052-00773))_
- So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user. _(javascriptallonge.pdf (source-range-0e12e052-00773))_
- So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user. _(javascriptallonge.pdf (source-range-0e12e052-00773))_
- , && and || do not necessarily evaluate to true or false . _(javascriptallonge.pdf (source-range-0e12e052-00775))_
- If we look at our examples above, we see that when we pass true and false to && and || , we do indeed get true or false as a result. _(javascriptallonge.pdf (source-range-0e12e052-00782))_
- They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && . _(javascriptallonge.pdf (source-range-0e12e052-00784))_
- This is not a subtle distinction. _(javascriptallonge.pdf (source-range-0e12e052-00785))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00771, source-range-0e12e052-00773))_

> Our logical operators ! , && , and || are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is not truthy: Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idi

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00772))_

```
!5
//=> false
!undefined
//=> true
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00782))_

> But when we pass other values, we no longer get true or false :

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00782))_

> If we look at our examples above, we see that when we pass true and false to && and || , we do indeed get true or false as a result. But when we pass other values, we no longer get true or false :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00783))_

```
1 || 2
//=> 1
null && undefined
//=> null
undefined && null
//=> undefined
```

#### || and && are control-flow operators

- We've seen the ternary operator: It is a control-flow operator, not a logical operator. _(javascriptallonge.pdf (source-range-0e12e052-00787))_
- This is more than just an optimization. _(javascriptallonge.pdf (source-range-0e12e052-00793))_
- The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. _(javascriptallonge.pdf (source-range-0e12e052-00793))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00789))_

```
const even = (n) =>
n === 0 || (n !== 1 && even(n - 2))
even(42)
//=> true
```

#### function parameters are eager

- This leads to the infinite recursion we fear. _(javascriptallonge.pdf (source-range-0e12e052-00797))_
- If we need to have functions with control-flow semantics, we can pass anonymous functions. _(javascriptallonge.pdf (source-range-0e12e052-00798))_
- Here we've passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation. _(javascriptallonge.pdf (source-range-0e12e052-00800))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00795))_

> In contrast to the behaviour of the ternary operator, || , and && , function parameters are always eagerly evaluated :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00796))_

```
const or = (a, b) => a || b
const and = (a, b) => a && b
const even = (n) =>
or(n === 0, and(n !== 1, even(n - 2)))
even(42)
//=> Maximum call stack size exceeded.
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00798))_

> If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don't need anything like this for or and and , but to demonstrate the technique:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00799))_

```
const or = (a, b) => a() || b()
const and = (a, b) => a() && b()
const even = (n) =>
or(() => n === 0, () => and(() => n !== 1, () => even(n - 2)))
even(7)
//=> false
```

#### summary

- - Logical operators are based on truthiness and falsiness, not the strict values true and false . _(javascriptallonge.pdf (source-range-0e12e052-00802))_
- - The ternary operator ( ?: ), || , and && are control flow operators, they do not always return true or false , and they have short-cut semantics. _(javascriptallonge.pdf (source-range-0e12e052-00804))_
- - Function invocation uses eager evaluation, so if we need to roll our own control-flow semantics, we pass it functions, not expressions. _(javascriptallonge.pdf (source-range-0e12e052-00805))_

## Composing and Decomposing Data

- Recursion is the root of computation since it trades description for time.-Alan Perlis, Epigrams in Programming 55 _(javascriptallonge.pdf (source-range-0e12e052-00809))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00807))_

> [Figure] (p.100)

### Arrays and Destructuring Arguments

- Arrays are JavaScript's 'native' representation of lists. _(javascriptallonge.pdf (source-range-0e12e052-00812))_
- Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-0e12e052-00812))_
- While we have mentioned arrays briefly, we haven't had a close look at them. _(javascriptallonge.pdf (source-range-0e12e052-00812))_
- Strings are important because they represent writing. _(javascriptallonge.pdf (source-range-0e12e052-00812))_
- Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-0e12e052-00812))_
- Strings are important because they represent writing. _(javascriptallonge.pdf (source-range-0e12e052-00812))_

#### array literals

- JavaScript has a literal syntax for creating an array: The [ and ] characters. _(javascriptallonge.pdf (source-range-0e12e052-00814))_
- This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. _(javascriptallonge.pdf (source-range-0e12e052-00822))_
- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-0e12e052-00822))_
- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-0e12e052-00822))_
- We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements: _(javascriptallonge.pdf (source-range-0e12e052-00825))_
- Array literals are expressions, and arrays are reference types . _(javascriptallonge.pdf (source-range-0e12e052-00825))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00814))_

> JavaScript has a literal syntax for creating an array: The [ and ] characters. We can create an empty array:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00815))_

```
[]
//=> []
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00816))_

> We can create an array with one or more elements by placing them between the brackets and separating the items with commas. Whitespace is optional:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00817))_

```
[1]
//=> [1]
[2, 3, 4]
//=> [2,3,4]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00818))_

> Any expression will work:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00819))_

```
[ 2,
3,
2 + 2
]
//=> [2,3,4]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00820))_

> Including an expression denoting another array:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00821))_

```
[[[[[]]]]]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00823))_

> Any expression will do, including names:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00824))_

```
const wrap = (something) => [something];
wrap("lunch")
//=> ["lunch"]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00825))_

> Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00826))_

```
[] === []
//=> false
[2 + 2] === [2 + 2]
//=> false
const array_of_one = () => [1];
array_of_one() === array_of_one()
//=> false
```

#### element references

- Array elements can be extracted using [ and ] as postfix operators. _(javascriptallonge.pdf (source-range-0e12e052-00828))_
- As we can see, JavaScript Arrays are zero-based 56 . _(javascriptallonge.pdf (source-range-0e12e052-00830))_
- We know that every array is its own unique entity, with its own unique reference. _(javascriptallonge.pdf (source-range-0e12e052-00831))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00828))_

> Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00829))_

```
const oneTwoThree = ["one", "two", "three"];
oneTwoThree[0]
//=> 'one'
oneTwoThree[1]
//=> 'two'
oneTwoThree[2]
//=> 'three'
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00830))_

> As we can see, JavaScript Arrays are zero-based 56 .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00833))_

```
const x = [],
a = [x];
a[0] === x
//=> true, arrays store references to the things you put in them.
```

#### destructuring arrays

- There is another way to extract elements from arrays: Destructuring , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-0e12e052-00835))_
- There is another way to extract elements from arrays: Destructuring , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-0e12e052-00835))_
- The line const wrapped = [something]; is interesting. _(javascriptallonge.pdf (source-range-0e12e052-00838))_
- The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . _(javascriptallonge.pdf (source-range-0e12e052-00841))_
- We could do the same thing with (name) => name[1] , but destructuring is code that resembles the data it consumes, a valuable coding style. _(javascriptallonge.pdf (source-range-0e12e052-00843))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00835))_

> There is another way to extract elements from arrays: Destructuring , a feature going back to Common Lisp, if not before. We saw how to construct an array literal using [ , expressions, , and ] . Here's an example of an array literal that uses a name:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00836))_

```
const wrap = (something) => [something];
Let’s expand it to use a block and an extra name:
const wrap = (something) => {
const wrapped = [something];
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00835))_

> There is another way to extract elements from arrays: Destructuring , a feature going back to Common Lisp, if not before. We saw how to construct an array literal using [ , expressions, , and ] . Here's an example of an array literal that uses a name:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00837))_

```
const wrap = (something) => {
const wrapped = [something]
return wrapped;
}
wrap("package")
//=> ["package"]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00839))_

> In JavaScript, we can actually reverse the statement and place the template on the left and a value on the right:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00840))_

```
const unwrap = (wrapped) => {
const [something] = wrapped;
return something;
}
unwrap(["present"])
//=> "present"
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00841))_

> The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do the same thing with more than one element:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00842))_

```
const surname = (name) => {
const [first, last] = name;
return last;
}
surname(["Reginald", "Braithwaite"])
//=> "Braithwaite"
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00844))_

> Destructuring can nest:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00845))_

```
const description = (nameAndOccupation) => {
const [[first, last], occupation] = nameAndOccupation;
return `${first} is a ${occupation}`;
}
description([["Reginald", "Braithwaite"], "programmer"])
//=> "Reginald is a programmer"
```

#### gathering

- Sometimes we need to extract arrays from arrays. _(javascriptallonge.pdf (source-range-0e12e052-00847))_
- Here is the most common pattern: Extracting the head and gathering everything but the head from an array: _(javascriptallonge.pdf (source-range-0e12e052-00847))_
- car and cdr 57 are archaic terms that go back to an implementation of Lisp running on the IBM 704 computer. _(javascriptallonge.pdf (source-range-0e12e052-00849))_
- notation does not provide a universal patten-matching capability. _(javascriptallonge.pdf (source-range-0e12e052-00850))_
- to place the elements of an array inside another array. _(javascriptallonge.pdf (source-range-0e12e052-00854))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00847))_

> Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00848))_

```
const [car, ...cdr] = [1, 2, 3, 4, 5];
car
//=> 1
cdr
//=> [2, 3, 4, 5]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00850))_

> Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00851))_

```text
57 https://en.wikipedia.org/wiki/CAR_and_CDR
58 Kyle Simpson is the author of You Don't Know JS, available here
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 57 | https://en.wikipedia.org/wiki/CAR_and_CDR |
| 58 | Kyle Simpson is the author of You Don't Know JS, available here |

</details>

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00850))_

> Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00852))_

```
const [...butLast, last] = [1, 2, 3, 4, 5];
//=> ERROR
const [first, ..., last] = [1, 2, 3, 4, 5];
//=> ERROR
Now, when we introduced destructuring, we saw that it is kind-of-sort-of the reverse of array literals.
So if
const wrapped = [something];
Then:
const [unwrapped] = something;
What is the reverse of gathering? We know that:
const [car, ...cdr] = [1, 2, 3, 4, 5];
What is the reverse? It would be:
const cons = [car, ...cdr];
Let’s try it:
const oneTwoThree = ["one", "two", "three"];
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00850))_

> Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00853))_

```
Let’s try it:
const oneTwoThree = ["one", "two", "
["zero", ...oneTwoThree]
//=> ["zero","one","two","three"]
```

#### destructuring is not pattern matching

- If it does, assignments are made where appropriate. _(javascriptallonge.pdf (source-range-0e12e052-00856))_
- But this is not how JavaScript works. _(javascriptallonge.pdf (source-range-0e12e052-00859))_
- JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. _(javascriptallonge.pdf (source-range-0e12e052-00859))_
- That match would fail because the array doesn't have an element to assign to what . _(javascriptallonge.pdf (source-range-0e12e052-00859))_
- That match would fail because the array doesn't have an element to assign to what . _(javascriptallonge.pdf (source-range-0e12e052-00859))_
- From its very inception, JavaScript has striven to avoid catastrophic errors. _(javascriptallonge.pdf (source-range-0e12e052-00863))_
- As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. _(javascriptallonge.pdf (source-range-0e12e052-00863))_
- This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-0e12e052-00863))_
- This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-0e12e052-00863))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00857, source-range-0e12e052-00859))_

> In such a language, if you wrote something like: That match would fail because the array doesn't have an element to assign to what . But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. Therefore:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00858))_

```
const [what] = [];
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00859))_

> That match would fail because the array doesn't have an element to assign to what . But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. Therefore:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00860))_

```
const [what] = [];
what
//=> undefined
const [which, what,
who
//=> undefined
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00859, source-range-0e12e052-00863))_

> That match would fail because the array doesn't have an element to assign to what . But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. Therefore: From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00861))_

```
const [...they] = [];
they
//=> []
const [which, what, .
they
//=> []
```

#### destructuring and return values

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00865))_

> Some languages support multiple return values: A function can return several things at once, like a value and an error code. This can easily be emulated in JavaScript with destructuring:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00866))_

```
const description = (nameAndOccupation) => {
if (nameAndOccupation.length < 2) {
return ["", "occupation missing"]
}
else {
const [[first, last], occupation] = nameAndOccupation;
return [`${first} is a ${occupation}`, "ok"];
}
}
const [reg, status] = description([["Reginald", "Braithwaite"], "programmer"]);
reg
//=> "Reginald is a programmer"
status
//=> "ok"
```

#### destructuring parameters

- There is only one difference: We have not tried gathering. _(javascriptallonge.pdf (source-range-0e12e052-00872))_
- There is only one difference: We have not tried gathering. _(javascriptallonge.pdf (source-range-0e12e052-00872))_
- This is very useful indeed, and we'll see more of it in a moment. _(javascriptallonge.pdf (source-range-0e12e052-00874))_
- 59 Gathering in parameters has a long history, and the usual terms are to call gathering 'pattern matching' and to call a name that is bound to gathered values a 'rest parameter.' The term 'rest' is perfectly compatible with gather: 'Rest' is the noun, and 'gather' is the verb. _(javascriptallonge.pdf (source-range-0e12e052-00875))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00868))_

> Consider the way we pass arguments to parameters:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00869))_

```
foo()
bar("smaug")
baz(1, 2, 3)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00870))_

> It is very much like an array literal. And consider how we bind values to parameter names:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00871))_

```
const foo = () => ...
const bar = (name) => ...
const baz = (a, b, c) => ...
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00872))_

> It looks like destructuring. It acts like destructuring. There is only one difference: We have not tried gathering. Let's do that:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00873))_

```
const numbers = (...nums) => nums;
numbers(1, 2, 3, 4, 5)
//=> [1,2,3,4,5]
const headAndTail = (head, ...tail) => [head, tail];
headAndTail(1, 2, 3, 4, 5)
//=> [1,[2,3,4,5]]
```

### Self-Similarity

- Recursion is the root of computation since it trades description for time.-Alan Perlis, Epigrams in Programming 60 _(javascriptallonge.pdf (source-range-0e12e052-00877))_
- In Arrays and Destructuring Arguments, we worked with the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-0e12e052-00878))_
- We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-0e12e052-00879))_
- Some are empty, some have three items, some forty-two, some contain numbers, some contain strings, some a mixture of elements, there are all kinds of lists. _(javascriptallonge.pdf (source-range-0e12e052-00880))_
- Some data structures, like lists, can obviously be seen as a collection of items. _(javascriptallonge.pdf (source-range-0e12e052-00880))_
- - Consists of an element concatenated with a list . _(javascriptallonge.pdf (source-range-0e12e052-00883))_
- The first rule is simple: [] is a list. _(javascriptallonge.pdf (source-range-0e12e052-00884))_
- Given an element e and a list list , [e, ...list] is a list. _(javascriptallonge.pdf (source-range-0e12e052-00884))_
- Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists: _(javascriptallonge.pdf (source-range-0e12e052-00886))_
- We know that we can get the length of an array using its .length . _(javascriptallonge.pdf (source-range-0e12e052-00891))_
- 61 Well, actually, this does not work for arrays that contain undefined as a value, but we are not going to see that in our examples. _(javascriptallonge.pdf (source-range-0e12e052-00892))_
- Well, the length of first is 1 , there's just one element at the front. _(javascriptallonge.pdf (source-range-0e12e052-00895))_
- If an array is not empty, and we break it into two pieces, first and rest , the length of our array is going to be length(first) + length(rest) . _(javascriptallonge.pdf (source-range-0e12e052-00895))_
- We need something for when the array isn't empty. _(javascriptallonge.pdf (source-range-0e12e052-00895))_
- If only there was a function we could call… Like length ! _(javascriptallonge.pdf (source-range-0e12e052-00895))_
- If only there was a function we could call… Like length ! _(javascriptallonge.pdf (source-range-0e12e052-00895))_
- Our length function is recursive , it calls itself. _(javascriptallonge.pdf (source-range-0e12e052-00898))_
- This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-0e12e052-00898))_
- This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-0e12e052-00898))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00884))_

> Let's convert our rules to array literals. The first rule is simple: [] is a list. How about the second rule? We can express that using a spread. Given an element e and a list list , [e, ...list] is a list. We can test this manually by building up a list:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00885))_

```
[]
//=> []
["baz", ...[]]
//=> ["baz"]
["bar", ...["baz"]]
//=> ["bar","baz"]
["foo", ...["bar", "baz"]]
//=> ["foo","bar","baz"]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00886))_

> Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00889))_

```
const [first, ...rest] = [];
first
//=> undefined
rest
//=> []:
const [first, ...rest] = ["foo"];
first
//=> "foo"
rest
//=> []
const [first, ...rest] = ["foo", "bar"];
first
//=> "foo"
rest
//=> ["bar"]
const [first, ...rest] = ["foo", "bar", "baz"];
first
//=> "foo"
rest
//=> ["bar","baz"]
For the purpose of this exploration, we will presume the following:61
const isEmpty = ([first, ...rest]) => first === undefined;
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00890))_

```
isEmpty([])
//=> true
isEmpty([0])
//=> false
isEmpty([[]])
//=> false
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00893))_

> First, we pick what we call a terminal case . What is the length of an empty array? 0 . So let's start our function with the observation that if an array is empty, the length is 0 :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00894))_

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: // ???
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00893, source-range-0e12e052-00898))_

> First, we pick what we call a terminal case . What is the length of an empty array? 0 . So let's start our function with the observation that if an array is empty, the length is 0 : Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00896))_

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: 1 + length(rest);
Let’s try it!
length([])
//=> 0
length(["foo"])
//=> 1
length(["foo", "bar", "baz"])
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00898))_

> Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00897))_

```
//=> 3
```

#### linear recursion

- When promising students are trying to choose between pure mathematics and applied engineering, they are given a two-part aptitude test. _(javascriptallonge.pdf (source-range-0e12e052-00901))_
- In the first part, they are led to a laboratory bench and told to follow the instructions printed on the card. _(javascriptallonge.pdf (source-range-0e12e052-00901))_
- After a bit the water boils, and they turn off the burner and are lead to a second bench. _(javascriptallonge.pdf (source-range-0e12e052-00902))_
- Of course, all the students know what to do: They fill the beaker with water, place the stand on the burner and the beaker on the stand, then they turn the burner on and use the sparker to ignite the flame. _(javascriptallonge.pdf (source-range-0e12e052-00902))_
- After a bit the water boils, and they turn off the burner and are lead to a second bench. _(javascriptallonge.pdf (source-range-0e12e052-00902))_
- Of course, all the students know what to do: They fill the beaker with water, place the stand on the burner and the beaker on the stand, then they turn the burner on and use the sparker to ignite the flame. _(javascriptallonge.pdf (source-range-0e12e052-00902))_
- Once again, there is a card that reads, 'boil water.' But this time, the beaker is on the stand over the burner, as left behind by the previous student. _(javascriptallonge.pdf (source-range-0e12e052-00903))_
- Whereas the mathematicians take the beaker off the stand and empty it, thus reducing the situation to a problem they have already solved. _(javascriptallonge.pdf (source-range-0e12e052-00903))_
- Whereas the mathematicians take the beaker off the stand and empty it, thus reducing the situation to a problem they have already solved. _(javascriptallonge.pdf (source-range-0e12e052-00903))_
- There is more to recursive solutions that simply functions that invoke themselves. _(javascriptallonge.pdf (source-range-0e12e052-00904))_
- - When all small problems have been solved, compose the solutions into one big solution _(javascriptallonge.pdf (source-range-0e12e052-00908))_
- The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. _(javascriptallonge.pdf (source-range-0e12e052-00909))_
- Our solutions are a little simpler in that we don't really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. _(javascriptallonge.pdf (source-range-0e12e052-00909))_
- Our solutions are a little simpler in that we don't really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. _(javascriptallonge.pdf (source-range-0e12e052-00909))_
- The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. _(javascriptallonge.pdf (source-range-0e12e052-00909))_
- This simpler form of 'divide and conquer' is called linear recursion . _(javascriptallonge.pdf (source-range-0e12e052-00910))_
- Sometimes we want to flatten an array, that is, an array of arrays needs to be turned into one array of elements that aren't arrays. _(javascriptallonge.pdf (source-range-0e12e052-00910))_
- This simpler form of 'divide and conquer' is called linear recursion . _(javascriptallonge.pdf (source-range-0e12e052-00910))_
- We need a test for the terminal case. _(javascriptallonge.pdf (source-range-0e12e052-00911))_
- Whereas if an element is an array, we'll flatten it and put it together with the rest of our solution. _(javascriptallonge.pdf (source-range-0e12e052-00913))_
- The next terminal case is that if an element isn't an array, we don't flatten it, and can put it together with the rest of our solution directly. _(javascriptallonge.pdf (source-range-0e12e052-00913))_
- The usual 'terminal case' will be that flattening an empty array will produce an empty array. _(javascriptallonge.pdf (source-range-0e12e052-00913))_
- Whereas if an element is an array, we'll flatten it and put it together with the rest of our solution. _(javascriptallonge.pdf (source-range-0e12e052-00913))_
- Unfolds can be thought of a 'path' through a data structure, and flattening a tree is equivalent to a depth-first traverse. _(javascriptallonge.pdf (source-range-0e12e052-00915))_
- 62 flatten is a very simple unfold, a function that takes a seed value and turns it into an array. _(javascriptallonge.pdf (source-range-0e12e052-00915))_
- Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions. _(javascriptallonge.pdf (source-range-0e12e052-00917))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00911))_

> We already know how to divide arrays into smaller pieces. How do we decide whether a smaller problem is solvable? We need a test for the terminal case. Happily, there is something along these lines provided for us:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00912))_

```
Array.isArray("foo")
//=> false
Array.isArray(["foo"])
//=> true
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00914))_

> So our first cut at a flatten function will look like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00916))_

```
const flatten = ([first, ...rest]) => {
if (first === undefined) {
return [];
}
else if (!Array.isArray(first)) {
return [first, ...flatten(rest)];
}
else {
return [...flatten(first), ...flatten(rest)];
}
}
flatten(["foo", [3, 4, []]])
//=> ["foo",3,4]
```

#### mapping

- Another common problem is applying a function to every element of an array. _(javascriptallonge.pdf (source-range-0e12e052-00919))_
- This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again. _(javascriptallonge.pdf (source-range-0e12e052-00924))_
- This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again. _(javascriptallonge.pdf (source-range-0e12e052-00924))_
- Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution. _(javascriptallonge.pdf (source-range-0e12e052-00927))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00920))_

> If we want to square each number in a list, we could write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00921))_

```
const squareAll = ([first, ...rest]) => first === undefined
? []
: [first * first, ...squareAll(rest)\
];
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00922))_

> And if we wanted to 'truthify' each element in a list, we could write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00923))_

```
const truthyAll = ([first, ...rest]) => first === undefined
? []
: [!!first, ...truthyAll(rest)];
truthyAll([null, true, 25, false, "foo"])
//=> [false,true,true,false,true]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00925))_

> Given the signature:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00926))_

```
const mapWith = (fn, array) => // ...
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00927))_

> Wecanwrite it out using a ternary operator. Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00928))_

```
const mapWith = (fn, [first, ...rest]) =>
first === undefined
? []
: [fn(first), ...mapWith(fn, rest)];
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
mapWith((x) => !!x, [null, true, 25, false, "foo"])
//=> [false,true,true,false,true]
```

#### folding

- Our foldWith function is a generalization of our mapWith function. _(javascriptallonge.pdf (source-range-0e12e052-00939))_
- And to return to our first example, our version of length can be written as a fold: _(javascriptallonge.pdf (source-range-0e12e052-00943))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00930, source-range-0e12e052-00932))_

> With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn't. A function to compute the sum of the squares of a list of numbers might look like this: There are two differences between sumSquares and our maps above:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00931))_

```
const sumSquares = ([first, ...rest]) => first === undefined
? 0
: first * first + sumSquares(rest);
sumSquares([1, 2, 3, 4, 5])
//=> 55
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00935))_

> Let's rewrite mapWith so that we can use it to sum squares.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00936))_

```
const foldWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: fn(first, foldWith(fn, terminalValue, rest));
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00937))_

> And now we supply a function that does slightly more than our mapping functions:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00938))_

```
foldWith((number, rest) => number * number + rest, 0, [1, 2, 3, 4, 5])
//=> 55
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00939))_

> Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00940))_

```
const squareAll = (array) => foldWith((first, rest) => [first * first, ...rest],\
[], array);
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00941))_

> And if we like, we can write mapWith using foldWith :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00942))_

```
const mapWith = (fn, array) => foldWith((first, rest) => [fn(first), ...rest], [\
], array),
squareAll = (array) => mapWith((x) => x * x, array);
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00943))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00944))_

```
const length = (array) => foldWith((first, rest) => 1 + rest, 0, array);
length([1, 2, 3, 4, 5])
//=> 5
```

#### summary

- Its basic form parallels the way linear data structures like lists are constructed: This helps make it understandable. _(javascriptallonge.pdf (source-range-0e12e052-00946))_
- And finally, while folding is a special case of linear recursion, mapping is a special case of folding. _(javascriptallonge.pdf (source-range-0e12e052-00946))_
- Its specialized cases of mapping and folding are especially useful and can be used to build other functions. _(javascriptallonge.pdf (source-range-0e12e052-00946))_
- Linear recursion is a basic building block of algorithms. _(javascriptallonge.pdf (source-range-0e12e052-00946))_

### Tail Calls (and Default Arguments)

- One of the reasons they are not production-ready is that they consume memory proportional to the size of the array being folded. _(javascriptallonge.pdf (source-range-0e12e052-00948))_
- The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustrating the basic principles behind using recursion to work with self-similar data structures, but they are not 'production-ready' implementations. _(javascriptallonge.pdf (source-range-0e12e052-00948))_
- first is not undefined , so it evaluates [fn(first), …mapWith(fn, rest)]. _(javascriptallonge.pdf (source-range-0e12e052-00951))_
- To do that, it has to evaluate fn(first) and mapWith(fn, rest) , then evaluate [fn(first), ...mapWith(fn, rest)] . _(javascriptallonge.pdf (source-range-0e12e052-00951))_
- First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked. _(javascriptallonge.pdf (source-range-0e12e052-00951))_
- To do that, it has to evaluate fn(first) and mapWith(fn, rest) , then evaluate [fn(first), ...mapWith(fn, rest)] . _(javascriptallonge.pdf (source-range-0e12e052-00951))_
- So we know that JavaScript is going to hang on to 1 . _(javascriptallonge.pdf (source-range-0e12e052-00954))_
- JavaScript cannot throw first away. _(javascriptallonge.pdf (source-range-0e12e052-00954))_
- Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . _(javascriptallonge.pdf (source-range-0e12e052-00955))_
- And the same thing happens: JavaScript has to hang on to 2 (or 4 , or both, depending on the implementation), plus some housekeeping information so it remembers what to do with that value, while it calls the equivalent of mapWith((x) => x * x, [3, 4, 5]) . _(javascriptallonge.pdf (source-range-0e12e052-00955))_
- It can start assembling the resulting array and start discarding the information it is saving. _(javascriptallonge.pdf (source-range-0e12e052-00956))_
- That information is saved on a call stack , and it is quite expensive. _(javascriptallonge.pdf (source-range-0e12e052-00957))_
- Furthermore, doubling the length of an array will double the amount of space we need on the stack, plus double all the work required to set up and tear down the housekeeping data for each call (these are called call frames , and they include the place where the function was called, an environment, and so on). _(javascriptallonge.pdf (source-range-0e12e052-00957))_
- In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error. _(javascriptallonge.pdf (source-range-0e12e052-00958))_
- In fact, there are several better ways. _(javascriptallonge.pdf (source-range-0e12e052-00960))_
- Making algorithms faster is a very highly studied field of computer science. _(javascriptallonge.pdf (source-range-0e12e052-00960))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00949))_

> Let's look at how. Here's our extremely simple mapWith function again:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00950))_

```
const mapWith = (fn, [first, ...rest]) =>
first === undefined
? []
: [fn(first), ...mapWith(fn, rest)];
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00952, source-range-0e12e052-00954))_

> This is roughly equivalent to writing: Note that while evaluating mapWith(fn, rest) , JavaScript must retain the value first or fn(first) , plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result. JavaScript cannot throw first away. So we know that JavaScript is going to hang on to 1 .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00953))_

```
const mapWith = function (fn, [first, ...rest]) {
if (first === undefined) {
return [];
}
else {
const _temp1 = fn(first),
_temp2 = mapWith(fn, rest),
_temp3 = [_temp1, ..._temp2];
return _temp3;
}
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00952))_

> This is roughly equivalent to writing:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00954))_

> Note that while evaluating mapWith(fn, rest) , JavaScript must retain the value first or fn(first) , plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00958))_

> In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00959))_

```
mapWith((x) => x * x, [
0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
90, 91, 92, 93, 94, 95, 96, 97, 98, 99
])
//=> ???
```

#### tail-call optimization

- A'tail-call' occurs when a function's last act is to invoke another function, and then return whatever the other function returns. _(javascriptallonge.pdf (source-range-0e12e052-00962))_
- A'tail-call' occurs when a function's last act is to invoke another function, and then return whatever the other function returns. _(javascriptallonge.pdf (source-range-0e12e052-00962))_
- But the third is fn.apply(this, args) . _(javascriptallonge.pdf (source-range-0e12e052-00964))_
- This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. _(javascriptallonge.pdf (source-range-0e12e052-00964))_
- This is a tail-call, because it invokes another function and returns its result. _(javascriptallonge.pdf (source-range-0e12e052-00964))_
- There are three places it returns. _(javascriptallonge.pdf (source-range-0e12e052-00964))_
- It isn't going to do any more work, so it can throw its existing stack frame away. _(javascriptallonge.pdf (source-range-0e12e052-00964))_
- This is a tail-call, because it invokes another function and returns its result. _(javascriptallonge.pdf (source-range-0e12e052-00964))_
- This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. _(javascriptallonge.pdf (source-range-0e12e052-00964))_
- And in fact, it does exactly that: It throws the stack frame away, and does not consume extra memory when making a maybe -wrapped call. _(javascriptallonge.pdf (source-range-0e12e052-00965))_
- This is a very important characteristic of JavaScript: If a function makes a call in tail position, JavaScript optimizes away the function call overhead and stack space. _(javascriptallonge.pdf (source-range-0e12e052-00965))_
- That is excellent, but one wrapping is not a big deal. _(javascriptallonge.pdf (source-range-0e12e052-00966))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) . _(javascriptallonge.pdf (source-range-0e12e052-00968))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) . _(javascriptallonge.pdf (source-range-0e12e052-00968))_
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length , the other happens after the recursive call. _(javascriptallonge.pdf (source-range-0e12e052-00969))_
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length , the other happens after the recursive call. _(javascriptallonge.pdf (source-range-0e12e052-00969))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00962, source-range-0e12e052-00964))_

> A'tail-call' occurs when a function's last act is to invoke another function, and then return whatever the other function returns. For example, consider the maybe function decorator: There are three places it returns. The first two don't return anything, they don't matter. But the third is fn.apply(this, args) . This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript ca

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00963))_

```
const maybe = (fn) =>
function (...args) {
if (args.length === 0) {
return;
}
else {
for (let arg of args) {
if (arg == null) return;
}
return fn.apply(this, args);
}
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00966, source-range-0e12e052-00968))_

> That is excellent, but one wrapping is not a big deal. When would we really care? Consider this implementation of length : The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00967))_

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: 1 + length(rest);
```

#### converting non-tail-calls to tail-calls

- The obvious solution is push the 1 + work into the call to length . _(javascriptallonge.pdf (source-range-0e12e052-00972))_
- Now that we've seen how it works, we can clean up the 0 + numberToBeAdded business. _(javascriptallonge.pdf (source-range-0e12e052-00974))_
- This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. _(javascriptallonge.pdf (source-range-0e12e052-00977))_
- And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization. _(javascriptallonge.pdf (source-range-0e12e052-00981))_
- We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. _(javascriptallonge.pdf (source-range-0e12e052-00981))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00972, source-range-0e12e052-00974))_

> The obvious solution is push the 1 + work into the call to length . Here's our first cut: This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we've seen how it works, we can clean up the 0 + numberToBeAdded business. But while we're doing that, it's annoying to remember to call it with a zero. Let's fix that:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00973))_

```
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) =>
first === undefined
? 0 + numberToBeAdded
: lengthDelaysWork(rest, 1 + numberToBeAdded)
lengthDelaysWork(["foo", "bar", "baz"], 0)
//=> 3
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00974))_

> This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we've seen how it works, we can clean up the 0 + numberToBeAdded business. But while we're doing that, it's annoying to remember to call it with a zero. Let's fix that:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00975))_

```
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) =>
first === undefined
? numberToBeAdded
: lengthDelaysWork(rest, 1 + numberToBeAdded)
const length = (n) =>
lengthDelaysWork(n, 0);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00974))_

> This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we've seen how it works, we can clean up the 0 + numberToBeAdded business. But while we're doing that, it's annoying to remember to call it with a zero. Let's fix that:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00976))_

```
Or we could use partial application:
const callLast = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
const length = callLast(lengthDelaysWork, 0);
length(["foo", "bar", "baz"])
//=> 3
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00977))_

> This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00978))_

```
const mapWithDelaysWork = (fn, [first, ...rest], prepend) =>
first === undefined
? prepend
: mapWithDelaysWork(fn, rest, [...prepend, fn(first)]);
const mapWith = callLast(mapWithDelaysWork, []);
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
We can use it with ridiculously large arrays:
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00977))_

> This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00979))_

```
mapWith((x) => x * x, [
0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10,
11,
12,
13,
14,
15,
16,
17,
18,
19,
20,
21,
22,
23,
24,
25,
26,
27,
28,
29,
30,
31,
32,
33,
34,
35,
36,
37,
38,
39,
40,
41,
42,
43,
44,
45,
46,
47,
48,
49,
50,
51,
52,
53,
54,
55,
56,
57,
58,
59,
60,
61,
62,
63,
64,
65,
66,
67,
68,
69,
70,
71,
72,
73,
74,
75,
76,
77,
78,
79,
80,
81,
82,
83,
84,
85,
86,
87,
88,
89,
90,
91,
92,
93,
94,
95,
96,
97,
98,
99,
// ...
2980, 2981, 2982, 2983, 2984, 2985, 2986, 2987, 2988, 2989,
2990, 2991, 2992, 2993, 2994, 2995, 2996, 2997, 2998, 2999 ])
//=> [0,1,4,9,16,25,36,49,64,81,100,121,144,169,196, ...
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00977))_

> This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00980))_

| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |

<details>
<summary>Raw table text</summary>

```text
converting non-tail-calls to tail-calls
| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |
```

</details>

### factorials

- , is the product of all positive integers less than or equal to n . _(javascriptallonge.pdf (source-range-0e12e052-00984))_
- While this is mathematically elegant, it is computational filigree 63 . _(javascriptallonge.pdf (source-range-0e12e052-00988))_
- Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n -1) . _(javascriptallonge.pdf (source-range-0e12e052-00989))_
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-0e12e052-00994))_
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-0e12e052-00994))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00984))_

> In mathematics, the factorial of a non-negative integer n , denoted by n! , is the product of all positive integers less than or equal to n . For example:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00985))_

```
5! = 5
x
4
x
3
x
2
x
1 = 120.
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00986, source-range-0e12e052-00989))_

> The naïve function for calcuating the factorial of a positive integer follows directly from the definition: Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n -1) . We can do the same conversion, pass in the work to be done:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00987))_

```
const factorial = (n) =>
n == 1
? n
: n * factorial(n - 1);
factorial(1)
//=> 1
factorial(5)
//=> 120
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00989))_

> Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n -1) . We can do the same conversion, pass in the work to be done:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00990))_

```
const factorialWithDelayedWork = (n, work) =>
n === 1
? work
: factorialWithDelayedWork(n - 1, n * work);
const factorial = (n) =>
factorialWithDelayedWork(n, 1);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00991))_

> Or we could use partial application:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00993))_

```
const callLast = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
const factorial = callLast(factorialWithDelayedWork, 1);
factorial(1)
//=> 1
factorial(5)
//=> 120
```

### default arguments

- But when it calls itself, it will call factorial(5, 6) and that will not mean factorial(5, 1) . _(javascriptallonge.pdf (source-range-0e12e052-00999))_
- What we really want is this: We want to write something like factorial(6) , and have JavaScript automatically know that we really mean factorial(6, 1) . _(javascriptallonge.pdf (source-range-0e12e052-00999))_
- By writing our parameter list as (n, work = 1) => , we're stating that if a second parameter is not provided, work is to be bound to 1 . _(javascriptallonge.pdf (source-range-0e12e052-01002))_
- A default argument is concise and readable. _(javascriptallonge.pdf (source-range-0e12e052-01004))_
- Now we don't need to use two functions. _(javascriptallonge.pdf (source-range-0e12e052-01004))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00996))_

> Our problem is that we can directly write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00997))_

```
const factorial = (n, work) =>
n === 1
? work
: factorial(n - 1, n * work);
factorial(1, 1)
//=> 1
factorial(5, 1)
//=> 120
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00996))_

> Our problem is that we can directly write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00998))_

> But it is hideous to have to always add a 1 parameter, we'd be demanding that everyone using the factorial function know that we are using a tail-recursive implementation.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01000))_

> JavaScript provides this exact syntax, it's called a default argument , and it looks like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01001))_

```
const factorial = (n, work = 1) =>
n === 1
? work
: factorial(n - 1, n * work);
factorial(1)
//=> 1
factorial(6)
//=> 720
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01002))_

> By writing our parameter list as (n, work = 1) => , we're stating that if a second parameter is not provided, work is to be bound to 1 . We can do similar things with our other tail-recursive functions:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01003))_

```
const length = ([first, ...rest], numberToBeAdded = 0) =>
first === undefined
? numberToBeAdded
: length(rest, 1 + numberToBeAdded)
length(["foo", "bar", "baz"])
//=> 3
const mapWith = (fn, [first, ...rest], prepend = []) =>
first === undefined
? prepend
: mapWith(fn, rest, [...prepend, fn(first)]);
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### defaults and destructuring

- Now we learn that we can create a default parameter argument. _(javascriptallonge.pdf (source-range-0e12e052-01006))_
- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-0e12e052-01008))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01006))_

> Wesawearlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we create a default destructuring assignment?

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01007))_

```
const [first, second = "two"] = ["one"];
`${first} . ${second}`
//=> "one . two"
const [first, second = "two"] = ["primus", "secundus"];
`${first} . ${second}`
//=> "primus . secundus"
```

## Garbage, Garbage Everywhere

- We have now seen how to use Tail Calls to execute mapWith in constant space: _(javascriptallonge.pdf (source-range-0e12e052-01012))_
- The right tool to discover why it's still slow is a memory profiler, but a simple inspection of the program will reveal the following: _(javascriptallonge.pdf (source-range-0e12e052-01014))_
- But when we try it on very large arrays, we discover that it is still very slow. _(javascriptallonge.pdf (source-range-0e12e052-01014))_
- To do that, we take the array in prepend and push fn(first) onto the end, creating a new array that will be passed to the next invocation of mapWith . _(javascriptallonge.pdf (source-range-0e12e052-01015))_
- In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. _(javascriptallonge.pdf (source-range-0e12e052-01017))_
- The array we had in prepend is no longer used. _(javascriptallonge.pdf (source-range-0e12e052-01017))_
- Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend . _(javascriptallonge.pdf (source-range-0e12e052-01017))_
- Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend . _(javascriptallonge.pdf (source-range-0e12e052-01017))_
- Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another. _(javascriptallonge.pdf (source-range-0e12e052-01018))_
- We may not be creating 3,000 stack frames, but we are creating three thousand new arrays and copying elements into each and every one of them. _(javascriptallonge.pdf (source-range-0e12e052-01018))_
- Key Point : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded. _(javascriptallonge.pdf (source-range-0e12e052-01019))_
- Key Point : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded. _(javascriptallonge.pdf (source-range-0e12e052-01019))_
- But this is not how JavaScript's built-in arrays work. _(javascriptallonge.pdf (source-range-0e12e052-01021))_
- 64 It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. _(javascriptallonge.pdf (source-range-0e12e052-01021))_
- 64 It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. _(javascriptallonge.pdf (source-range-0e12e052-01021))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01010))_

> [Figure] (p.126)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01012))_

> We have now seen how to use Tail Calls to execute mapWith in constant space:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01013))_

```
const mapWith = (fn, [first, ...rest], prepend = []) =>
first === undefined
? prepend
: mapWith(fn, rest, [...prepend, fn(first)]);
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01022))_

> [Figure] (p.128)

### some history

- In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. _(javascriptallonge.pdf (source-range-0e12e052-01026))_
- In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. _(javascriptallonge.pdf (source-range-0e12e052-01026))_
- The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells. _(javascriptallonge.pdf (source-range-0e12e052-01027))_
- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. _(javascriptallonge.pdf (source-range-0e12e052-01027))_
- Lisp's basic data type is often said to be the list, but in actuality it was the 'cons cell,' the term used to describe two 15-bit values stored in one word. _(javascriptallonge.pdf (source-range-0e12e052-01027))_
- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. _(javascriptallonge.pdf (source-range-0e12e052-01027))_
- Lists were represented as linked lists of cons cells, with each cell's head pointing to an element and the tail pointing to another cons cell. _(javascriptallonge.pdf (source-range-0e12e052-01028))_
- Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being the others), and computers in the late 1950s were extremely small and slow by today's standards. _(javascriptallonge.pdf (source-range-0e12e052-01029))_
- Although the 704 used core memory, it still used vacuum tubes for its logic. _(javascriptallonge.pdf (source-range-0e12e052-01029))_
- This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . _(javascriptallonge.pdf (source-range-0e12e052-01037))_
- This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . _(javascriptallonge.pdf (source-range-0e12e052-01037))_
- car is very fast, it simply extracts the first element of the cons cell. _(javascriptallonge.pdf (source-range-0e12e052-01039))_
- Getting one reference to a structure that already exists is faster than copying a bunch of elements. _(javascriptallonge.pdf (source-range-0e12e052-01042))_
- In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. _(javascriptallonge.pdf (source-range-0e12e052-01042))_
- There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. _(javascriptallonge.pdf (source-range-0e12e052-01042))_
- In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. _(javascriptallonge.pdf (source-range-0e12e052-01042))_
- In Lisp, it's blazingly fast because it happens in hardware. _(javascriptallonge.pdf (source-range-0e12e052-01042))_
- So now we understand that in Lisp, a lot of things use linked lists, and they do that in part because it was what the hardware made possible. _(javascriptallonge.pdf (source-range-0e12e052-01043))_
- So now we understand that in Lisp, a lot of things use linked lists, and they do that in part because it was what the hardware made possible. _(javascriptallonge.pdf (source-range-0e12e052-01043))_
- That being said, it is easy to understand and helps us grasp how literals and destructuring works, and how recursive algorithms ought to mirror the self-similarity of the data structures they manipulate. _(javascriptallonge.pdf (source-range-0e12e052-01045))_
- And so it is today that languages like JavaScript have arrays that are slow to split into the equivalent of a car / cdr pair, but instructional examples of recursive programs still have echoes of their Lisp origins. _(javascriptallonge.pdf (source-range-0e12e052-01045))_
- We'll look at linked lists again when we look at Plain Old JavaScript Objects. _(javascriptallonge.pdf (source-range-0e12e052-01046))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01025))_

```text
some history
Once upon a time, there was a programming language called Lisp 65 , an acronym for LISt Processing. 66 Lisp was one of the very first high-level languages, the very first implementation was written for the IBM 704 67 computer. (The very first FORTRAN implementation was also written for the 704).
The 704 had a 36-bit word, meaning that it was very fast to store and retrieve 36-bit values. The CPU's instruction set featured two important macros: CAR would fetch 15 bits representing the Contents of the Address part of the Register, while CDR would fetch the Contents of the Decrement part of the Register.
65 https://en.wikipedia.org/wiki/Lisp_
67 https://en.wikipedia.org/wiki/IBM_704
66 Lisp is still very much alive, and one of the most interesting and exciting programming languages in use today is Clojure, a Lisp dialect that runs on the JVM, along with its sibling ClojureScript, Clojure that transpiles to JavaScript.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 66 | Lisp was one of the very first high-level languages, the very first implementation was written for the IBM 704 |
| 67 | computer. (The very first FORTRAN implementation was also written for the 704). The 704 had a 36-bit word, meaning that it was very fast to store and retrieve 36-bit values. The CPU's instruction set featured two important macros: CAR would fetch 15 bits representing the Contents of the Address part of the Register, while CDR would fetch the Contents of the Decrement part of the Register. |
| 65 | https://en.wikipedia.org/wiki/Lisp_ |
| 67 | https://en.wikipedia.org/wiki/IBM_704 |
| 66 | Lisp is still very much alive, and one of the most interesting and exciting programming languages in use today is Clojure, a Lisp dialect that runs on the JVM, along with its sibling ClojureScript, Clojure that transpiles to JavaScript. |

</details>

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01026))_

> If you had two 15-bit values and wished to write them to the register, the CONS macro would take the values and write them to a 36-bit word.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01030))_

> Here's the scheme in JavaScript, using two-element arrays to represent cons cells:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01031))_

```
const cons = (a, d) => [a, d],
car
= ([a, d]) => a,
cdr
= ([a, d]) => d;
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01032))_

> We can make a list by calling cons repeatedly, and terminating it with null :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01033))_

```
const oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, null)))));
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01032))_

> We can make a list by calling cons repeatedly, and terminating it with null :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01034))_

```
oneToFive
//=> [1,[2,[3,[4,[5,null]]]]]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01035))_

> Notice that though JavaScript displays our list as if it is composed of arrays nested within each other like Russian Dolls, in reality the arrays refer to each other with references, so [1,[2,[3,[4,[5,null]]]]] is actually more like:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01036))_

```
const node5 = [5,null],
node4 = [4, node5],
node3 = [3, node4],
node2 = [2, node3],
node1 = [1, node2];
const oneToFive = node1;
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01037))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01038))_

```
car(oneToFive)
//=> 1
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01040, source-range-0e12e052-01042))_

> But what about the rest of the list? cdr does the trick: Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Gettin

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01041))_

```
cdr(oneToFive)
//=> [2,[3,[4,[5,null]]]]
```

### so why arrays

- But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. _(javascriptallonge.pdf (source-range-0e12e052-01050))_
- Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. _(javascriptallonge.pdf (source-range-0e12e052-01050))_
- If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list. _(javascriptallonge.pdf (source-range-0e12e052-01051))_
- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-0e12e052-01052))_
- For these and other reasons, almost all languages today make it possible to use a fast array or vector type that is optimized for iteration, and even Lisp now has a variety of data structures that are optimized for specific use cases. _(javascriptallonge.pdf (source-range-0e12e052-01053))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01049))_

> If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list?

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01050))_

> And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01050))_

> Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. In addition to the extra fetches to dereference pointers, pointer chasing suffers from cache misses. And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01051))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements.

### summary

- Although we showed how to use tail calls to map and fold over arrays with [first, ...rest] , in reality this is not how it ought to be done. _(javascriptallonge.pdf (source-range-0e12e052-01055))_
- But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. _(javascriptallonge.pdf (source-range-0e12e052-01055))_
- But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. _(javascriptallonge.pdf (source-range-0e12e052-01055))_

## Plain Old JavaScript Objects

- Lists are not the only way to represent collections of things, but they are the 'oldest' data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. _(javascriptallonge.pdf (source-range-0e12e052-01057))_
- Lists are not the only way to represent collections of things, but they are the 'oldest' data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. _(javascriptallonge.pdf (source-range-0e12e052-01057))_
- Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. _(javascriptallonge.pdf (source-range-0e12e052-01060))_
- So back when lists were the only things available, programmers would introduce constants to make things easier on themselves: _(javascriptallonge.pdf (source-range-0e12e052-01060))_
- So back when lists were the only things available, programmers would introduce constants to make things easier on themselves: _(javascriptallonge.pdf (source-range-0e12e052-01060))_
- Over time, this need to build heterogeneous data structures with access to members by name evolved into the Dictionary 69 data type, a mapping from a unique set of objects to another set of objects. _(javascriptallonge.pdf (source-range-0e12e052-01062))_
- Now they could write user[NAME][LAST] or user[OCCUPATION][TITLE] instead of user[0][1] or user[1][0] . _(javascriptallonge.pdf (source-range-0e12e052-01062))_
- Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0 , we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else. _(javascriptallonge.pdf (source-range-0e12e052-01063))_
- Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0 , we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else. _(javascriptallonge.pdf (source-range-0e12e052-01063))_
- JavaScript has dictionaries, and it calls them 'objects.' The word 'object' is loaded in programming circles, due to the widespread use of the term 'object-oriented programming' that was coined by Alan Kay but has since come to mean many, many things to many different people. _(javascriptallonge.pdf (source-range-0e12e052-01064))_
- In JavaScript, an object is a map from string keys to values. _(javascriptallonge.pdf (source-range-0e12e052-01065))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01057))_

> Lists are not the only way to represent collections of things, but they are the 'oldest' data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. Lists are obviously very handy for homogeneous collections of things, like a shopping list:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01058))_

```
const remember = ["the milk", "the coffee beans", "the biscotti"];
And they can be used to store heterogeneous things in various levels of structure:
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01057))_

> Lists are not the only way to represent collections of things, but they are the 'oldest' data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. Lists are obviously very handy for homogeneous collections of things, like a shopping list:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01059))_

```
const user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\
vaScript Spessore", "CoffeeScript Ristretto"]]];
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01060))_

> Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01061))_

```
const NAME = 0,
FIRST = 0,
LAST = 1,
OCCUPATION = 1,
TITLE = 0,
RESPONSIBILITIES = 1;
const user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\
vaScript Spessore", "CoffeeScript Ristretto"]]];
```

### literal object syntax

- JavaScript has a literal syntax for creating objects. _(javascriptallonge.pdf (source-range-0e12e052-01068))_
- Two objects created with separate evaluations have differing identities, just like arrays: _(javascriptallonge.pdf (source-range-0e12e052-01070))_
- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-0e12e052-01072))_
- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-0e12e052-01072))_
- Names needn't be alphanumeric strings. _(javascriptallonge.pdf (source-range-0e12e052-01074))_
- If the name is an alphanumeric string conforming to the same rules as names of variables, there's a simplified syntax for accessing the values: _(javascriptallonge.pdf (source-range-0e12e052-01076))_
- Expressions can be used for keys as well. _(javascriptallonge.pdf (source-range-0e12e052-01078))_
- It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords: _(javascriptallonge.pdf (source-range-0e12e052-01086))_
- (There are some other technical differences between binding a named function expression and using compact method syntax, but they are not relevant here. _(javascriptallonge.pdf (source-range-0e12e052-01088))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01068))_

> JavaScript has a literal syntax for creating objects. This object maps values to the keys year , month , and day :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01069))_

```
{ year: 2012, month: 6, day: 14 }
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01070))_

> Two objects created with separate evaluations have differing identities, just like arrays:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01071))_

```
{ year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 }
//=> false
Objects use [] to access the values by name, using a string:
{ year: 2012, month: 6, day: 14 }['day']
//=> 14
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01072))_

> Values contained within an object work just like values contained within an array, we access them by reference to the original:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01073))_

```
const unique = () => [],
x = unique(),
y = unique(),
z = unique(),
o = { a: x, b: y, c: z };
o['a'] === x && o['b'] === y && o['c'] === z
//=> true
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01074))_

> Names needn't be alphanumeric strings. For anything else, enclose the label in quotes:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01075))_

```
{ 'first name': 'reginald', 'last name': 'lewis' }['first name']
//=> 'reginald'
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01076))_

> If the name is an alphanumeric string conforming to the same rules as names of variables, there's a simplified syntax for accessing the values:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01077))_

```
const date = { year: 2012, month: 6, day: 14 };
date['day'] === date.day
//=> true
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01078))_

> Expressions can be used for keys as well. The syntax is to enclose the key's expression in [ and ] :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01079))_

```
{
["p" + "i"]: 3.14159265
}
//=> {"pi":3.14159265}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01080))_

> All containers can contain any value, including functions or other containers, like a fat arrow function:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01081))_

```
const Mathematics = {
abs: (a) => a < 0 ? -a : a
};
Mathematics.abs(-5)
//=> 5
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01082))_

> Or proper functions:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01083))_

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01084))_

> Or named function expressions:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01085))_

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01086))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01087))_

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

### destructuring objects

- It is very common to write things like title: title when destructuring objects. _(javascriptallonge.pdf (source-range-0e12e052-01095))_
- When the label is a valid variable name, it's often the most obvious variable name as well. _(javascriptallonge.pdf (source-range-0e12e052-01095))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01090))_

> Just as we saw with arrays, we can write destructuring assignments with literal object syntax. So, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01091))_

```
const user = {
name: { first: "Reginald",
last: "Braithwaite"
},
occupation: { title: "Author",
responsibilities: [ "JavaScript Allongé",
"JavaScript Spessore",
"CoffeeScript Ristretto"
]
}
};
user.name.last
//=> "Braithwaite"
user.occupation.title
//=> "Author"
And we can also write:
const {name: { first: given, last: surname}, occupation: { title: title }
er;
surname
//=> "Braithwaite"
title
//=> "Author"
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01092))_

> And of course, we destructure parameters:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01093))_

```
} = us\
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01092))_

> And of course, we destructure parameters:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01094))_

```
const description = ({name: { first: given }, occupation: { title: title } }) =>
`${given} is a ${title}`;
description(user)
//=> "Reginald is a Author"
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01095))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01096))_

```
const description = ({name: { first }, occupation: { title } }) =>
`${first} is a ${title}`;
description(user)
//=> "Reginald is a Author"
And that same syntax works for literals:
const abbrev = ({name: { first, last }, occupation: { title } }) => {
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01095))_

> Terrible grammar and capitalization, but let's move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it's often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01097))_

```
const abbrev = ({name: { first, last }, occupation: { title } }) =>
return { first, last, title};
}
abbrev(user)
//=> {"first":"Reginald","last":"Braithwaite","title":"Author"}
```

### revisiting linked lists

- But now that we've looked at objects, we can use an object instead of a two-element array. _(javascriptallonge.pdf (source-range-0e12e052-01101))_
- In essence, this simple implementation used functions to create an abstraction with named elements. _(javascriptallonge.pdf (source-range-0e12e052-01101))_
- As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. _(javascriptallonge.pdf (source-range-0e12e052-01104))_
- The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. _(javascriptallonge.pdf (source-range-0e12e052-01106))_
- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-0e12e052-01106))_
- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-0e12e052-01106))_
- We could follow the strategy of delaying the work. _(javascriptallonge.pdf (source-range-0e12e052-01107))_
- We have unwittingly reversed the list. _(javascriptallonge.pdf (source-range-0e12e052-01109))_
- This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we're going to get a backwards copy of the list. _(javascriptallonge.pdf (source-range-0e12e052-01109))_
- Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away. _(javascriptallonge.pdf (source-range-0e12e052-01111))_
- Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away. _(javascriptallonge.pdf (source-range-0e12e052-01111))_
- Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. _(javascriptallonge.pdf (source-range-0e12e052-01111))_
- Mind you, this is still much, much faster than making partial copies of arrays. _(javascriptallonge.pdf (source-range-0e12e052-01112))_
- Whereas our naïve array algorithm created 2 n superfluous arrays and copied n 2 superfluous values. _(javascriptallonge.pdf (source-range-0e12e052-01112))_
- For a list of length n , wecreated n superfluous nodes and copied n superfluous values. _(javascriptallonge.pdf (source-range-0e12e052-01112))_
- Whereas our naïve array algorithm created 2 n superfluous arrays and copied n 2 superfluous values. _(javascriptallonge.pdf (source-range-0e12e052-01112))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01099))_

> Earlier, we used two-element arrays as nodes in a linked list:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01100))_

```
const cons = (a, d) => [a, d],
car
= ([a, d]) => a,
cdr
= ([a, d]) => d;
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01101, source-range-0e12e052-01104))_

> In essence, this simple implementation used functions to create an abstraction with named elements. But now that we've looked at objects, we can use an object instead of a two-element array. While we're at it, let's use contemporary names. So our linked list nodes will be formed from { first, rest } What about mapping? Well, let's start with the simplest possible thing, making a copy of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01102))_

```
In that case, a linked list of the numbers 1, 2, and 3 will look like this: { first: 1, rest: { first:
2, rest: { first: 3, rest: EMPTY } } }.
We can then perform the equivalent of [first, ...rest] with direct property accessors:
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01101, source-range-0e12e052-01104))_

> In essence, this simple implementation used functions to create an abstraction with named elements. But now that we've looked at objects, we can use an object instead of a two-element array. While we're at it, let's use contemporary names. So our linked list nodes will be formed from { first, rest } What about mapping? Well, let's start with the simplest possible thing, making a copy of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01103))_

```
const EMPTY = {};
const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \
} } };
OneTwoThree.first
//=> 1
OneTwoThree.rest
//=> {"first":2,"rest":{"first":3,"rest":{}}}
OneTwoThree.rest.rest.first
//=> 3
Taking the length of a linked list is easy:
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
length(OneTwoThree)
//=> 3
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01104))_

> What about mapping? Well, let's start with the simplest possible thing, making a copy of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn't fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01105))_

```
const slowcopy = (node) =>
node === EMPTY
? EMPTY
: { first: node.first, rest: slowcopy(node.rest)};
slowcopy(OneTwoThree)
//=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{}}}}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01107))_

> We could follow the strategy of delaying the work. Let's write that naively:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01108))_

```
const copy2 = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: copy2(node.rest, { first: node.first, rest: delayed });
copy2(OneTwoThree)
//=> {"first":3,"rest":{"first":2,"rest":{"first":1,"rest":{}}}}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01109, source-range-0e12e052-01111))_

> Well, well, well. We have unwittingly reversed the list. This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we're going to get a backwards copy of the list. This isn't a bad thing by any stretch of the imagination. Let's call it what it is: Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. Likewise, it takes twice 

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01110))_

```
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
And now, we can make a reversing map:
const reverseMapWith = (fn, node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverseMapWith(fn, node.rest, { first: fn(node.first), rest: delayed });
reverseMapWith((x) => x * x, OneTwoThree)
//=> {"first":9,"rest":{"first":4,"rest":{"first":1,"rest":{}}}}
And a regular mapWith follows:
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
const mapWith = (fn, node, delayed = EMPTY) =>
node === EMPTY
? reverse(delayed)
: mapWith(fn, node.rest, { first: fn(node.first), rest: delayed });
mapWith((x) => x * x, OneTwoThree)
//=> {"first":1,"rest":{"first":4,"rest":{"first":9,"rest":{}}}}
```

## Mutation

- Specifically, arrays and objects can mutate. _(javascriptallonge.pdf (source-range-0e12e052-01116))_
- Recall that you can access a value from within an array or an object using [] . _(javascriptallonge.pdf (source-range-0e12e052-01116))_
- In JavaScript, almost every type of value can mutate . _(javascriptallonge.pdf (source-range-0e12e052-01116))_
- Recall that you can access a value from within an array or an object using [] . _(javascriptallonge.pdf (source-range-0e12e052-01116))_
- Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. _(javascriptallonge.pdf (source-range-0e12e052-01122))_
- Both halloween and allHallowsEve are bound to the same array value within the local environment. _(javascriptallonge.pdf (source-range-0e12e052-01124))_
- Both halloween and allHallowsEve are bound to the same array value within the local environment. _(javascriptallonge.pdf (source-range-0e12e052-01124))_
- There are two nested environments, and each one binds a name to the exact same array value. _(javascriptallonge.pdf (source-range-0e12e052-01126))_
- Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value. _(javascriptallonge.pdf (source-range-0e12e052-01126))_
- In each of these examples, we have created two aliases for the same value. _(javascriptallonge.pdf (source-range-0e12e052-01126))_
- Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value. _(javascriptallonge.pdf (source-range-0e12e052-01126))_
- The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. _(javascriptallonge.pdf (source-range-0e12e052-01129))_
- The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. _(javascriptallonge.pdf (source-range-0e12e052-01129))_
- We haven't rebound the inner name to a different variable, we've mutated the value that both bindings share. _(javascriptallonge.pdf (source-range-0e12e052-01131))_
- Mutating existing objects has special implications when two bindings are aliases of the same value. _(javascriptallonge.pdf (source-range-0e12e052-01133))_
- JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects. _(javascriptallonge.pdf (source-range-0e12e052-01133))_
- Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. _(javascriptallonge.pdf (source-range-0e12e052-01135))_
- Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. _(javascriptallonge.pdf (source-range-0e12e052-01135))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01114))_

> [Figure] (p.141)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01116))_

> In JavaScript, almost every type of value can mutate . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using [] . You can reassign a value using [] = :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01117))_

```
const oneTwoThree = [1, 2, 3];
oneTwoThree[0] = 'one';
oneTwoThree
//=> [ 'one', 2, 3 ]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01118))_

> You can even add a value:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01119))_

```
const oneTwoThree = [1, 2, 3];
oneTwoThree[3] = 'four';
oneTwoThree
//=> [ 1, 2, 3, 'four' ]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01120))_

> You can do the same thing with both syntaxes for accessing objects:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01121))_

```
const name = {firstName: 'Leonard', lastName: 'Braithwaite'};
name.middleName = 'Austin'
name
//=> { firstName: 'Leonard',
#
lastName: 'Braithwaite',
#
middleName: 'Austin' }
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01122))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01123))_

```
const allHallowsEve = [2012, 10, 31]
const halloween = allHallowsEve;
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01124, source-range-0e12e052-01126))_

> Both halloween and allHallowsEve are bound to the same array value within the local environment. And also: There are two nested environments, and each one binds a name to the exact same array value. In each of these examples, we have created two aliases for the same value. Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01125))_

```
const allHallowsEve = [2012, 10, 31];
(function (halloween) {
// ...
})(allHallowsEve);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01127, source-range-0e12e052-01129))_

> This is vital. Consider what we already know about shadowing: The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we mutate the value in the inner environment?

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01128))_

```
const allHallowsEve = [2012, 10, 31];
(function (halloween) {
halloween = [2013, 10, 31];
})(allHallowsEve);
allHallowsEve
//=> [2012, 10, 31]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01127))_

> This is vital. Consider what we already know about shadowing:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01130))_

```
const allHallowsEve = [2012, 10, 31];
(function (halloween) {
halloween[0] = 2013;
})(allHallowsEve);
allHallowsEve
//=> [2013, 10, 31]
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01132))_

> [Figure] (p.143)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01133))_

> JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects. Mutating existing objects has special implications when two bindings are aliases of the same value.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01134))_

> [Figure] (p.143)

### mutation and data structures

- It is possible to compute anything without ever mutating an existing entity. _(javascriptallonge.pdf (source-range-0e12e052-01137))_
- In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about. _(javascriptallonge.pdf (source-range-0e12e052-01137))_
- Mutation is a surprisingly complex subject. _(javascriptallonge.pdf (source-range-0e12e052-01137))_
- By this pattern, we would be happy to use mutation to construct the list while running mapWith . _(javascriptallonge.pdf (source-range-0e12e052-01138))_
- While we're executing the mapWith function, we're constructing a new linked list. _(javascriptallonge.pdf (source-range-0e12e052-01138))_
- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. _(javascriptallonge.pdf (source-range-0e12e052-01138))_
- The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. _(javascriptallonge.pdf (source-range-0e12e052-01145))_
- We just use the data, and the less we mutate it, the fewer the times we have to think about whether making changes will be 'safe.' _(javascriptallonge.pdf (source-range-0e12e052-01146))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01138))_

> One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists from Plain Old JavaScript Objects. While we're executing the mapWith function, we're constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01139))_

> But after returning the new list, we then become conservative about mutation. This also makes sense: Linked lists often use structure sharing. For example:

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01139))_

> But after returning the new list, we then become conservative about mutation. This also makes sense: Linked lists often use structure sharing. For example:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01141))_

```
const EMPTY = {};
const OneToFive = { first: 1,
rest: {
first: 2,
rest: {
first: 3,
rest: {
first: 4,
rest: {
first: 5,
rest: EMPTY } } } } };
OneToFive
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\
r","rest":{"first":"five","rest":{}}}}}}
const ThreeToFive = OneToFive.rest.rest;
ThreeToFive
//=> {"first":3,"rest":{"first":4,"rest":{"first":5,"rest":{}}}}
ThreeToFive.first = "three";
ThreeToFive.rest.first = "four";
ThreeToFive.rest.rest.first = "five";
ThreeToFive
//=> {"first":"three","rest":{"first":"four","rest":{"first":"five","rest":{}}\
}}
OneToFive
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\
r","rest":{"first":"five","rest":{}}}}}}
Changes made to ThreeToFive affect OneToFive, because they share the same structure. When we
wrote ThreeToFive = OneToFive.rest.rest;, we weren’t making a brand new copy of {"first":3,"rest":{"firs
we were getting a reference to the same chain of nodes.
Structure sharing like this is what makes linked lists so fast for taking everything but the first item
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01142))_

> of a list: We aren't making a new list, we're using some of the old list. Whereas destructuring an array with [first, ...rest] does make a copy, so:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01143))_

```
const OneToFive = [1, 2, 3, 4, 5];
OneToFive
//=> [1,2,3,4,5]
const [a, b, ...ThreeToFive] = OneToFive;
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01142))_

> of a list: We aren't making a new list, we're using some of the old list. Whereas destructuring an array with [first, ...rest] does make a copy, so:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01144))_

```
OneToFive
//=> [1,2,3,4,5]
const [a, b, ...ThreeToFive] =
ThreeToFive
//=> [3, 4, 5]
ThreeToFive[0] = "three";
ThreeToFive[1] = "four";
ThreeToFive[2] = "five";
ThreeToFive
//=> ["three","four","five"]
OneToFive
//=> [1,2,3,4,5]
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01146))_

> We don't have to remember to use copying operations when we pass it as a value to a function, or extract some data from it.

### building with mutation

- As noted, one pattern is to be more liberal about mutation when building a data structure. _(javascriptallonge.pdf (source-range-0e12e052-01148))_
- If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation: _(javascriptallonge.pdf (source-range-0e12e052-01150))_
- This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. _(javascriptallonge.pdf (source-range-0e12e052-01152))_
- Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. _(javascriptallonge.pdf (source-range-0e12e052-01152))_
- But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time. _(javascriptallonge.pdf (source-range-0e12e052-01152))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01148))_

> As noted, one pattern is to be more liberal about mutation when building a data structure. Consider our copy algorithm. Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01149))_

```
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
const copy = (node) => reverse(reverse(node));
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01150))_

> If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01151))_

```
const copy = (node, head = null, tail = null) => {
if (node === EMPTY) {
return head;
}
else if (tail === null) {
const { first, rest } = node;
const newNode = { first, rest };
return copy(rest, newNode, newNode);
}
else {
const { first, rest } = node;
const newNode = { first, rest };
tail.rest = newNode;
return copy(node.rest, head, newNode);
}
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01153))_

> Armed with this basic copy implementation, we can write mapWith :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01154))_

```
const mapWith = (fn, node, head = null, tail = null) => {
if (node === EMPTY) {
return head;
}
else if (tail === null) {
const { first, rest } = node;
const newNode = { first: fn(first), rest };
return mapWith(fn, rest, newNode, newNode);
}
else {
const { first, rest } = node;
const newNode = { first: fn(first), rest };
tail.rest = newNode;
return mapWith(fn, node.rest, head, newNode);
}
}
mapWith((x) => 1.0 / x, OneToFive)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01153))_

> Armed with this basic copy implementation, we can write mapWith :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01155))_

```
//=> {"first":1,"rest":{"first":0.5,"rest":{"first":0.3333333333333333,"rest":\
{"first":0.25,"rest":{"first":0.2,"rest":{}}}}}}
```

## Reassignment

- Like some imperative programming languages, JavaScript allows you to re-assign the value bound to parameters. _(javascriptallonge.pdf (source-range-0e12e052-01157))_
- JavaScript does not permit us to rebind a name that has been bound with const . _(javascriptallonge.pdf (source-range-0e12e052-01162))_
- We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-0e12e052-01162))_
- What we want is a statement that works like const , but permits us to rebind variables. _(javascriptallonge.pdf (source-range-0e12e052-01163))_
- The key is to understand that we are rebinding a different value to the same name in the same environment. _(javascriptallonge.pdf (source-range-0e12e052-01165))_
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . _(javascriptallonge.pdf (source-range-0e12e052-01168))_
- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . _(javascriptallonge.pdf (source-range-0e12e052-01168))_
- However, if we don't shadow age with let , reassigning within the block changes the original: _(javascriptallonge.pdf (source-range-0e12e052-01171))_
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. _(javascriptallonge.pdf (source-range-0e12e052-01173))_
- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. _(javascriptallonge.pdf (source-range-0e12e052-01173))_
- It then rebinds the name in that environment. _(javascriptallonge.pdf (source-range-0e12e052-01173))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01158))_

> By default, JavaScript permits us to rebind new values to names bound with a parameter. For example, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01159))_

```
const evenStevens = (n) => {
if (n === 0) {
return true;
}
else if (n == 1) {
return false;
}
else {
n = n - 2;
return evenStevens(n);
}
}
evenStevens(42)
//=> true
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01160))_

> The line n = n -2; rebinds a new value to the name n . We will discuss this at much greater length in Reassignment, but long before we do, let's try a similar thing with a name bound using const . We've already bound evenStevens using const , let's try rebinding it:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01161))_

```
evenStevens = (n) => {
if (n === 0) {
return true;
}
else if (n == 1) {
return false;
}
else {
return evenStevens(n - 2);
}
}
//=> ERROR, evenStevens is read-only
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01163))_

> Rebinding parameters is usually avoided, but what about rebinding names we declare within a function? What we want is a statement that works like const , but permits us to rebind variables. JavaScript has such a thing, it's called let :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01164))_

```
let age = 52;
age = 53;
age
//=> 53
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01166, source-range-0e12e052-01168))_

> So let's consider what happens with a shadowed variable: Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . We go from:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01167))_

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01168))_

> Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . We go from:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01169))_

```
{age: 49, '..': global-environment}
To:
{age: 50, '..': {age: 49, '..': global-environment}}
Then back to:
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01168))_

> Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . We go from:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01170))_

```
{age: 49, '..': global-environment}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01171))_

> However, if we don't shadow age with let , reassigning within the block changes the original:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01172))_

```
(() => {
let age = 49;
if (true) {
age = 50;
}
return age;
})()
//=> 50
```

### mixing let and const

- The suggestion is that shadowing a variable is confusing code. _(javascriptallonge.pdf (source-range-0e12e052-01175))_
- Shadowing a let with a const does not change our ability to rebind the variable in its original scope. _(javascriptallonge.pdf (source-range-0e12e052-01178))_
- Shadowing a const with a let does not permit it to be rebound in its original scope. _(javascriptallonge.pdf (source-range-0e12e052-01180))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01176))_

> If you dislike deliberately shadowing variables, you'll probably take an even more opprobrious view of mixing const and let semantics with a shadowed variable:

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01176))_

> If you dislike deliberately shadowing variables, you'll probably take an even more opprobrious view of mixing const and let semantics with a shadowed variable:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01177))_

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01178))_

> Shadowing a let with a const does not change our ability to rebind the variable in its original scope. And:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01179))_

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

#### var

- JavaScript has one more way to bind a name to a value, var . _(javascriptallonge.pdf (source-range-0e12e052-01182))_
- First, var is not block scoped, it's function scoped, just like function declarations: _(javascriptallonge.pdf (source-range-0e12e052-01186))_
- Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. _(javascriptallonge.pdf (source-range-0e12e052-01188))_
- But, again, it is unwise to expect consistency. _(javascriptallonge.pdf (source-range-0e12e052-01189))_
- A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. _(javascriptallonge.pdf (source-range-0e12e052-01189))_
- A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. _(javascriptallonge.pdf (source-range-0e12e052-01189))_
- But it's not like const and let in that it's function scoped, not block scoped. _(javascriptallonge.pdf (source-range-0e12e052-01195))_
- In that way, var is a little like const and let , we should always declare and bind names before using them. _(javascriptallonge.pdf (source-range-0e12e052-01195))_
- In that way, var is a little like const and let , we should always declare and bind names before using them. _(javascriptallonge.pdf (source-range-0e12e052-01195))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01182))_

> JavaScript has one more way to bind a name to a value, var . 71 var looks a lot like let :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01183))_

```
const factorial = (n) => {
let x = n;
if (x === 1) {
return 1;
}
else {
--x;
return n * factorial(x);
}
}
factorial(5)
//=> 120
const factorial2 = (n) => {
var x = n;
if (x === 1) {
return 1;
}
else {
--x;
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01182))_

> JavaScript has one more way to bind a name to a value, var . 71 var looks a lot like let :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01185))_

```
return n * factorial2(x);
}
}
factorial2(5)
//=> 120
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01186, source-range-0e12e052-01189))_

> But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations: But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. Note this example of a function that uses a helper:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01187))_

```
(() => {
var age = 49;
if (true) {
var age = 50;
}
return age;
})()
//=> 50
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01189, source-range-0e12e052-01191))_

> But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. Note this example of a function that uses a helper: JavaScript interprets this code as if we had written:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01190))_

```
const factorial = (n) => {
return innerFactorial(n, 1);
function innerFactorial (x, y) {
if (x == 1) {
return y;
}
else {
return innerFactorial(x-1, x * y);
}
}
}
factorial(4)
//=> 24
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01191))_

> JavaScript interprets this code as if we had written:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01192))_

```
const factorial = (n) => {
let innerFactorial = function innerFactorial (x, y) {
if (x == 1) {
return y;
}
else {
return innerFactorial(x-1, x * y);
}
}
return innerFactorial(n, 1);
}
JavaScript hoists the let and the assignment. But not so with var:
const factorial = (n) => {
return innerFactorial(n, 1);
var innerFactorial = function innerFactorial (x, y) {
if (x == 1) {
return y;
}
else {
return innerFactorial(x-1, x * y);
}
}
}
factorial(4)
//=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01193))_

> JavaScript hoists the declaration, but not the assignment. It is as if we'd written:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01194))_

```
const factorial = (n) => {
let innerFactorial = undefined;
return innerFactorial(n, 1);
innerFactorial = function innerFactorial (x, y) {
if (x == 1) {
return y;
}
else {
return innerFactorial(x-1, x * y);
}
}
}
factorial(4)
//=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```

### why const and let were invented

- However, its functional scope was a problem. _(javascriptallonge.pdf (source-range-0e12e052-01197))_
- For nearly twenty years, variables were declared with var (not counting parameters and function declarations, of course). _(javascriptallonge.pdf (source-range-0e12e052-01197))_
- We haven't looked at it yet, but JavaScript provides a for loop for your iterating pleasure and convenience. _(javascriptallonge.pdf (source-range-0e12e052-01198))_
- Hopefully, you can think of a faster way to calculate this sum. _(javascriptallonge.pdf (source-range-0e12e052-01200))_
- 72 And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. _(javascriptallonge.pdf (source-range-0e12e052-01200))_
- The other kids were adding the numbers like this: 1 + 2 + 3 + . _(javascriptallonge.pdf (source-range-0e12e052-01201))_
- 72 There is a well known story about Karl Friedrich Gauss when he was in elementary school. _(javascriptallonge.pdf (source-range-0e12e052-01201))_
- But Gauss rearranged the numbers to add them like this: (1 + 100) + (2 + 99) + (3 + 98) + . _(javascriptallonge.pdf (source-range-0e12e052-01201))_
- There are 50 pairs of numbers, so the answer is 50*101 = 5050. _(javascriptallonge.pdf (source-range-0e12e052-01201))_
- If you notice every pair of numbers adds up to 101. _(javascriptallonge.pdf (source-range-0e12e052-01201))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01198, source-range-0e12e052-01201))_

> We haven't looked at it yet, but JavaScript provides a for loop for your iterating pleasure and convenience. It looks a lot like the for loop in C. Here it is with var : 72 There is a well known story about Karl Friedrich Gauss when he was in elementary school. His teacher got mad at the class and told them to add the numbers 1 to 100 and give him the answer by the end of the class. About 30 seconds later Gauss gave him the answer. The other kids were adding the numbers like this: 1 + 2 + 3 + . 

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01199))_

```
var sum = 0;
for (var i = 1; i <= 100; i++) {
sum = sum + i
}
sum
#=> 5050
```

## Yes. Consider this variation:

- The answer is that pesky var i . _(javascriptallonge.pdf (source-range-0e12e052-01208))_
- So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3 . _(javascriptallonge.pdf (source-range-0e12e052-01210))_
- Now, at the time we created each function, i had a sensible value, like 0 , 1 , or 2 . _(javascriptallonge.pdf (source-range-0e12e052-01210))_
- But at the time we call one of the functions, i has the value 3 , which is why the loop terminated. _(javascriptallonge.pdf (source-range-0e12e052-01210))_
- So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3 . _(javascriptallonge.pdf (source-range-0e12e052-01210))_
- This small error was a frequent cause of confusion, and in the days when there was no block-scoped let , programmers would need to know how to fake it, usually with an IIFE: _(javascriptallonge.pdf (source-range-0e12e052-01213))_
- This works, but let is so much simpler and cleaner that it was added to the language in the ECMAScript 2015 specification. _(javascriptallonge.pdf (source-range-0e12e052-01215))_
- The two goals are often, but not always, aligned. _(javascriptallonge.pdf (source-range-0e12e052-01216))_
- That does not mean that you should follow the exact same practice in your own code: The purpose of this book is to illustrate certain principles of programming. _(javascriptallonge.pdf (source-range-0e12e052-01216))_
- The purpose of your own code is to get things done. _(javascriptallonge.pdf (source-range-0e12e052-01216))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01203))_

```
var introductions = [],
names = ['Karl', 'Friedrich', 'Gauss'];
for (var i = 0; i < 3; i++) {
introductions[i] = "Hello, my name is " + names[i]
}
introductions
//=> [ 'Hello, my name is Karl',
//
'Hello, my name is Friedrich',
//
'Hello, my name is Gauss' ]
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01205))_

```
var introductions = [],
names = ['Karl', 'Friedrich', 'Gauss'];
for (var i = 0; i < 3; i++) {
introductions[i] = (soAndSo) =>
`Hello, ${soAndSo}, my name is ${names[i]}`
}
introductions
//=> [ [Function],
//
[Function],
//
[Function] ]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01206, source-range-0e12e052-01208))_

> Again, so far, so good. Let's try one of our functions: What went wrong? Why didn't it give us 'Hello, Raganwald, my name is Friedrich'? The answer is that pesky var i . Remember that i is bound in the surrounding environment, so it's as if we wrote:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01207))_

```
introductions[1]('Raganwald')
//=> 'Hello, Raganwald, my name is undefined'
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01208))_

> What went wrong? Why didn't it give us 'Hello, Raganwald, my name is Friedrich'? The answer is that pesky var i . Remember that i is bound in the surrounding environment, so it's as if we wrote:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01209))_

```
var introductions = [],
names = ['Karl', 'Friedrich', 'Gauss'],
i = undefined;
for (i = 0; i < 3; i++) {
introductions[i] = function (soAndSo) {
return "Hello, " + soAndSo + ", my name is " + names[i]
}
}
introductions
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01212))_

```
let introductions = [],
names = ['Karl', 'Friedrich', 'Gauss'];
for (let i = 0; i < 3; i++) {
introductions[i] = (soAndSo) =>
`Hello, ${soAndSo}, my name is ${names[i]}`
}
introductions[1]('Raganwald')
//=> 'Hello, Raganwald, my name is Friedrich'
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01213))_

> This small error was a frequent cause of confusion, and in the days when there was no block-scoped let , programmers would need to know how to fake it, usually with an IIFE:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01214))_

```
var introductions = [],
names = ['Karl', 'Friedrich', 'Gauss'];
for (var i = 0; i < 3; i++) {
((i) => {
introductions[i] = (soAndSo) =>
`Hello, ${soAndSo}, my name is ${names[i]}`
}
})(i)
}
introductions[1]('Raganwald')
//=> 'Hello, Raganwald, my name is Friedrich'
```

## Copy on Write

- We've seen how to build lists with arrays and with linked lists. _(javascriptallonge.pdf (source-range-0e12e052-01220))_
- - When you take the rest of an array with destructuring ( [first, ...rest] ), you are given a copy of the elements of the array. _(javascriptallonge.pdf (source-range-0e12e052-01221))_
- - When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list. _(javascriptallonge.pdf (source-range-0e12e052-01222))_
- And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-0e12e052-01223))_
- And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-0e12e052-01223))_
- And therefore, modifications to the parent also modify the child, and modifications to the child also modify the parent. _(javascriptallonge.pdf (source-range-0e12e052-01224))_
- If we know that a list doesn't share any elements with another list, we can safely modify it. _(javascriptallonge.pdf (source-range-0e12e052-01227))_
- We'll end up reinventing reference counting and garbage collection. _(javascriptallonge.pdf (source-range-0e12e052-01227))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01218))_

> [Figure] (p.158)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01222, source-range-0e12e052-01224))_

> When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list. Whereas if you have a linked list, and you take it's 'rest,' your 'child' list shares its nodes with the 'parent' list. And therefore, modifications to the parent also modify the child, and modifications to the child also modify the parent.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01223))_

> The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01222))_

> When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01224))_

> Whereas if you have a linked list, and you take it's 'rest,' your 'child' list shares its nodes with the 'parent' list.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01225))_

> Let's confirm our understanding:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01226))_

```
const parentArray = [1, 2, 3];
const [aFirst, ...childArray] = parentArray;
parentArray[2] = "three";
childArray[0] = "two";
parentArray
//=> [1,2,"three"]
childArray
//=> ["two",3]
const EMPTY = { first: {}, rest: {} };
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
const childList = parentList.rest;
parentList.rest.rest.first = "three";
childList.first = "two";
parentList
//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\
{},"rest":{}}}}}
childList
//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}
```

### a few utilities

- The main difference is that array[index] = value evaluates to value , while set(index, value, list) evaluates to the modified list . _(javascriptallonge.pdf (source-range-0e12e052-01232))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01229))_

> before we go any further, let's write a few naïve list utilities so that we can work at a slightly higher level of abstraction:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01230))_

```
const copy = (node, head = null, tail = null) => {
if (node === EMPTY) {
return head;
}
else if (tail === null) {
const { first, rest } = node;
const newNode = { first, rest };
return copy(rest, newNode, newNode);
}
else {
const { first, rest } = node;
const newNode = { first, rest };
tail.rest = newNode;
return copy(node.rest, head, newNode);
}
}
const first = ({first, rest}) => first;
const rest = ({first, rest}) => rest;
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(rest(node), { first: first(node), rest: delayed });
const mapWith = (fn, node, delayed = EMPTY) =>
node === EMPTY
? reverse(delayed)
: mapWith(fn, rest(node), { first: fn(first(node)), rest: delayed });
const at = (index, list) =>
index === 0
? first(list)
: at(index - 1, rest(list));
const set = (index, value, list, originalList = list) =>
index === 0
? (list.first = value, originalList)
: set(index - 1, value, rest(list), originalList)
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01229))_

> before we go any further, let's write a few naïve list utilities so that we can work at a slightly higher level of abstraction:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01231))_

```
const childList = rest(parentList);
set(2, "three", parentList);
set(0, "two", childList);
parentList
//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\
{},"rest":{}}}}}
childList
//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}
```

#### copy-on-read

- Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-0e12e052-01234))_
- One strategy for avoiding problems is to be pessimistic . _(javascriptallonge.pdf (source-range-0e12e052-01234))_
- Thereafter, we can write to the parent or the copy of the child freely. _(javascriptallonge.pdf (source-range-0e12e052-01236))_
- This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. _(javascriptallonge.pdf (source-range-0e12e052-01236))_
- This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. _(javascriptallonge.pdf (source-range-0e12e052-01236))_
- As we expected, making a copy lets us modify the copy without interfering with the original. _(javascriptallonge.pdf (source-range-0e12e052-01237))_
- Sometimes we don't need to make a copy because we won't be modifying the list. _(javascriptallonge.pdf (source-range-0e12e052-01237))_
- Our mapWith function would be very expensive if we make a copy every time we call rest(node) . _(javascriptallonge.pdf (source-range-0e12e052-01237))_
- Sometimes we don't need to make a copy because we won't be modifying the list. _(javascriptallonge.pdf (source-range-0e12e052-01237))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01234, source-range-0e12e052-01236))_

> So back to the problem of structure sharing. One strategy for avoiding problems is to be pessimistic . Whenever we take the rest of a list, make a copy. This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01235))_

```
const rest = ({first, rest}) => copy(rest);
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
const childList = rest(parentList);
const newParentList = set(2, "three", parentList);
set(0, "two", childList);
parentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\
rest":{}}}}}
childList
//=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

#### copy-on-write

- But our new parent and child lists are copies that contain the desired modifications, without interfering with each other: _(javascriptallonge.pdf (source-range-0e12e052-01244))_
- And now functions like mapWith that make copies without modifying anything, work at full speed. _(javascriptallonge.pdf (source-range-0e12e052-01246))_
- This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' _(javascriptallonge.pdf (source-range-0e12e052-01247))_
- This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' _(javascriptallonge.pdf (source-range-0e12e052-01247))_
- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.Wikipedia 73 _(javascriptallonge.pdf (source-range-0e12e052-01248))_
- Like all strategies, it makes a tradeoff: It's much cheaper than pessimistically copying structures when you make an infrequent number of small changes, but if you tend to make a lot of changes to some that you aren't sharing, it's more expensive. _(javascriptallonge.pdf (source-range-0e12e052-01249))_
- Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-0e12e052-01250))_
- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. _(javascriptallonge.pdf (source-range-0e12e052-01250))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01240))_

> Why are we copying? In case we modify a child list. Ok, what if we do this: Make the copy when we know we are modifying the list. When do we know that? When we call set . We'll restore our original definition for rest , but change set :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01241))_

```
const rest = ({first, rest}) => rest;
const set = (index, value, list) =>
index === 0
? { first: value, rest: list.rest }
: { first: list.first, rest: set(index - 1, value, list.rest) };
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
const childList = rest(parentList);
const newParentList = set(2, "three", parentList);
const newChildList = set(0, "two", childList);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01242))_

> Our original parent and child lists remain unmodified:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01243))_

```
parentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{"first":{},"rest":\
{}}}}}
childList
//=> {"first":2,"rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01244))_

> But our new parent and child lists are copies that contain the desired modifications, without interfering with each other:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01245))_

```
newParentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\
rest":{}}}}}
newChildList
//=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

### Tortoises, Hares, and Teleporting Turtles

- It was, 'Write an algorithm to detect a loop in a linked list, in constant space.' _(javascriptallonge.pdf (source-range-0e12e052-01253))_
- This is the 'trick answer' to a question about finding a missing integer from a list, so I was trying the old, 'Transform this into a problem you've already solved 74 ' meta-algorithm. _(javascriptallonge.pdf (source-range-0e12e052-01255))_
- Eventually, I came up with something and tried it (In Java!) on my home PC. _(javascriptallonge.pdf (source-range-0e12e052-01256))_
- I then forgot about it for a while. _(javascriptallonge.pdf (source-range-0e12e052-01256))_
- You have two node references, and one traverses the list at twice the speed of the other. _(javascriptallonge.pdf (source-range-0e12e052-01260))_
- No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you'll detect the loop. _(javascriptallonge.pdf (source-range-0e12e052-01260))_
- No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you'll detect the loop. _(javascriptallonge.pdf (source-range-0e12e052-01260))_
- It seems to be faster under certain circumstances, depending on the size of the loop and the relative costs of certain operations. _(javascriptallonge.pdf (source-range-0e12e052-01263))_
- What's interesting about these two algorithms is that they both tangle two separate concerns: How to traverse a data structure, and what to do with the elements that you encounter. _(javascriptallonge.pdf (source-range-0e12e052-01264))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01256))_

> I went home and pondered the problem. I wanted to solve it. Eventually, I came up with something and tried it (In Java!) on my home PC. I sent him an email sharing my result, to demonstrate my ability to follow through. I then forgot about it for a while. Some time later, I was told that the correct solution was:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01257))_

```
const EMPTY = null;
const isEmpty = (node) => node === EMPTY;
const pair = (first, rest = EMPTY) => ({first, rest});
const list = (...elements) => {
const [first, ...rest] = elements;
return elements.length === 0
? EMPTY
: pair(first, list(...rest))
}
const forceAppend = (list1, list2) => {
if (isEmpty(list1)) {
return "FAIL!"
}
if (isEmpty(list1.rest)) {
list1.rest = list2;
}
else {
forceAppend(list1.rest, list2);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01256))_

> I went home and pondered the problem. I wanted to solve it. Eventually, I came up with something and tried it (In Java!) on my home PC. I sent him an email sharing my result, to demonstrate my ability to follow through. I then forgot about it for a while. Some time later, I was told that the correct solution was:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01259))_

```
}
}
const tortoiseAndHare = (aPair) => {
let tortoisePair = aPair,
harePair = aPair.rest;
while (true) {
if (isEmpty(tortoisePair) || isEmpty(harePair)) {
return false;
}
if (tortoisePair.first === harePair.first) {
return true;
}
harePair = harePair.rest;
if (isEmpty(harePair)) {
return false;
}
if (tortoisePair.first === harePair.first) {
return true;
}
tortoisePair = tortoisePair.rest;
harePair = harePair.rest;
}
};
const aList = list(1, 2, 3, 4, 5);
tortoiseAndHare(aList)
//=> false
forceAppend(aList, aList.rest.rest);
tortoiseAndHare(aList);
//=> true
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01261))_

> At the time, I couldn't think of any way to use hashing to solve the problem, so I gave up and tried to fit this into a powers-of-two algorithm. My first pass at it was clumsy, but it was roughly equivalent to this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01262))_

```
const teleportingTurtle = (list) => {
let speed = 1,
rabbit = list,
turtle = rabbit;
while (true) {
for (let i = 0; i <= speed; i += 1) {
rabbit = rabbit.rest;
if (rabbit == null) {
return false;
}
if (rabbit === turtle) {
return true;
}
}
turtle = rabbit;
speed *= 2;
}
return false;
};
const aList = list(1, 2, 3, 4, 5);
teleportingTurtle(aList)
//=> false
forceAppend(aList, aList.rest.rest);
teleportingTurtle(aList);
//=> true
```

### Functional Iterators

- But it still relies on foldArrayWith , so it can only sum arrays. _(javascriptallonge.pdf (source-range-0e12e052-01271))_
- The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. _(javascriptallonge.pdf (source-range-0e12e052-01271))_
- But it still relies on foldArrayWith , so it can only sum arrays. _(javascriptallonge.pdf (source-range-0e12e052-01271))_
- Well, we call arraySum with an array, and it has baked into it a method for traversing the array. _(javascriptallonge.pdf (source-range-0e12e052-01273))_
- Perhaps we could extract both of those things. _(javascriptallonge.pdf (source-range-0e12e052-01273))_
- What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . _(javascriptallonge.pdf (source-range-0e12e052-01275))_
- The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable. _(javascriptallonge.pdf (source-range-0e12e052-01275))_
- We've found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we've completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really). _(javascriptallonge.pdf (source-range-0e12e052-01278))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01267))_

> Let's consider a remarkably simple problem: Finding the sum of the elements of an array. In tailrecursive style, it looks like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01268))_

```
const arraySum = ([first, ...rest], accumulator = 0) =>
first === undefined
? accumulator
: arraySum(rest, first + accumulator)
arraySum([1, 4, 9, 16, 25])
//=> 55
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01269))_

> As we saw earlier, this entangles the mechanism of traversing the array with the business of summing the bits. So we can separate them using fold :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01270))_

```
const callLeft = (fn, ...args) =>
(...remainingArgs) =>
fn(...args, ...remainingArgs);
const foldArrayWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: fn(first, foldArrayWith(fn, terminalValue, rest));
const arraySum = callLeft(foldArrayWith, (a, b) => a + b, 0);
arraySum([1, 4, 9, 16, 25])
//=> 55
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01273))_

> Well, we call arraySum with an array, and it has baked into it a method for traversing the array. Perhaps we could extract both of those things. Let's rearrange our code a bit:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01274))_

```
const callRight = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
const foldArrayWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: fn(first, foldArrayWith(fn, terminalValue, rest));
const foldArray = (array) => callRight(foldArrayWith, array);
const sumFoldable = (folder) => folder((a, b) => a + b, 0);
sumFoldable(foldArray([1, 4, 9, 16, 25]))
//=> 55
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01276))_

> Here it is summing a tree of numbers:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01277))_

```
const callRight = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
const foldTreeWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: Array.isArray(first)
? fn(foldTreeWith(fn, terminalValue, first), foldTreeWith(fn, terminalValu\
e, rest))
: fn(first, foldTreeWith(fn, terminalValue, rest));
const foldTree = (tree) => callRight(foldTreeWith, tree);
const sumFoldable = (folder) => folder((a, b) => a + b, 0);
sumFoldable(foldTree([1, [4, [9, 16]], 25]))
//=> 55
```

#### iterating

- Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. _(javascriptallonge.pdf (source-range-0e12e052-01280))_
- Nevertheless, there is some value in being able to express some algorithms as iteration. _(javascriptallonge.pdf (source-range-0e12e052-01280))_
- JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. _(javascriptallonge.pdf (source-range-0e12e052-01281))_
- And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 . _(javascriptallonge.pdf (source-range-0e12e052-01283))_
- Notice that buried inside our loop, we have bound the names done and value . _(javascriptallonge.pdf (source-range-0e12e052-01286))_
- We can put those into a POJO (a Plain Old JavaScript Object). _(javascriptallonge.pdf (source-range-0e12e052-01286))_
- Notice that buried inside our loop, we have bound the names done and value . _(javascriptallonge.pdf (source-range-0e12e052-01286))_
- The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. _(javascriptallonge.pdf (source-range-0e12e052-01289))_
- Now this is something else. _(javascriptallonge.pdf (source-range-0e12e052-01289))_
- We can write a different iterator for a different data structure. _(javascriptallonge.pdf (source-range-0e12e052-01290))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01281))_

> JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. Summing the elements of an array can be accomplished with:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01282))_

```
const arraySum = (array) => {
let sum = 0;
for (let i = 0; i < array.length; ++i) {
sum += array[i];
}
return sum
}
arraySum([1, 4, 9, 16, 25])
//=> 55
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01284))_

> We can write this a slightly different way, using a while loop:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01285))_

```
const arraySum = (array) => {
let done,
sum = 0,
i = 0;
while ((done = i == array.length, !done)) {
const value = array[i++];
sum += value;
}
return sum
}
arraySum([1, 4, 9, 16, 25])
//=> 55
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01286))_

> Notice that buried inside our loop, we have bound the names done and value . We can put those into a POJO (a Plain Old JavaScript Object). It'll be a little awkward, but we'll be patient:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01287))_

```
const arraySum = (array) => {
let iter,
sum = 0,
index = 0;
while (
(eachIteration = {
done: index === array.length,
value: index < array.length ? array[index] : undefined
},
++index,
!eachIteration.done)
) {
sum += eachIteration.value;
}
return sum;
}
arraySum([1, 4, 9, 16, 25])
//=> 55
With this code, we make a POJO that has done and value keys. All the summing code needs to know
is to add eachIteration.value. Now we can extract the ickiness into a separate function:
const arrayIterator = (array) => {
let i = 0;
return () => {
const done = i === array.length;
return {
done,
value: done ? undefined : array[i++]
}
}
}
const iteratorSum = (iterator) => {
let eachIteration,
sum = 0;
while ((eachIteration = iterator(), !eachIteration.done)) {
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01286))_

> Notice that buried inside our loop, we have bound the names done and value . We can put those into a POJO (a Plain Old JavaScript Object). It'll be a little awkward, but we'll be patient:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01288))_

```
sum += eachIteration.value;
}
return sum;
}
iteratorSum(arrayIterator([1, 4, 9, 16, 25]))
//=> 55
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01290))_

> We can write a different iterator for a different data structure. Here's one for linked lists:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01291))_

```
const EMPTY = null;
const isEmpty = (node) => node === EMPTY;
const pair = (first, rest = EMPTY) => ({first, rest});
const list = (...elements) => {
const [first, ...rest] = elements;
return elements.length === 0
? EMPTY
: pair(first, list(...rest))
}
const print = (aPair) =>
isEmpty(aPair)
? ""
: `${aPair.first} ${print(aPair.rest)}`
const listIterator = (aPair) =>
() => {
const done = isEmpty(aPair);
if (done) {
return {done};
}
else {
const {first, rest} = aPair;
aPair = aPair.rest;
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01290))_

> We can write a different iterator for a different data structure. Here's one for linked lists:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01292))_

```
return { done, value: first }
}
}
const iteratorSum = (iterator) => {
let eachIteration,
sum = 0;;
while ((eachIteration = iterator(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
const aListIterator = listIterator(list(1, 4, 9, 16, 25));
iteratorSum(aListIterator)
//=> 55
```

#### unfolding and laziness

- When they iterate over an array or linked list, they are traversing something that is already there. _(javascriptallonge.pdf (source-range-0e12e052-01294))_
- A function that starts with a seed and expands it into a data structure is called an unfold . _(javascriptallonge.pdf (source-range-0e12e052-01298))_
- A function that starts with a seed and expands it into a data structure is called an unfold . _(javascriptallonge.pdf (source-range-0e12e052-01298))_
- We can start with take , an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-0e12e052-01302))_
- This business of going on forever has some drawbacks. _(javascriptallonge.pdf (source-range-0e12e052-01302))_
- We can start with take , an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-0e12e052-01302))_
- We'll need an iterator that produces odd numbers. _(javascriptallonge.pdf (source-range-0e12e052-01304))_
- Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions. _(javascriptallonge.pdf (source-range-0e12e052-01309))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01294))_

> Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let's consider the simplest example:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01295))_

```
const NumberIterator = (number = 0) =>
() => ({ done: false, value: number++ })
fromOne = NumberIterator(1);
fromOne().value;
//=> 1
fromOne().value;
//=> 2
fromOne().value;
//=> 3
fromOne().value;
//=> 4
fromOne().value;
//=> 5
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01297))_

```
const FibonacciIterator
= () => {
let previous = 0,
current = 1;
return () => {
const value = current;
[previous, current] = [current, current + previous];
return {done: false, value};
};
};
const fib = FibonacciIterator()
fib().value
//=> 1
fib().value
//=> 1
fib().value
//=> 2
fib().value
//=> 3
fib().value
//=> 5
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01299))_

> For starters, we can map an iterator, just like we map a collection:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01300))_

```
const mapIteratorWith = (fn, iterator) =>
() => {
const {done, value} = iterator();
return ({done, value: done ? undefined : fn(value)});
}
const squares = mapIteratorWith((x) => x * x, NumberIterator(1));
squares().value
//=> 1
squares().value
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01299))_

> For starters, we can map an iterator, just like we map a collection:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01301))_

```
//=> 4
squares().value
//=> 9
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01302))_

> This business of going on forever has some drawbacks. Let's introduce an idea: A function that takes an iterator and returns another iterator. We can start with take , an easy function that returns an iterator that only returns a fixed number of elements:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01303))_

```
const take = (iterator, numberToTake) => {
let count = 0;
return () => {
if (++count <= numberToTake) {
return iterator();
} else {
return {done: true};
}
};
};
const toArray = (iterator) => {
let eachIteration,
array = [];
while ((eachIteration = iterator(), !eachIteration.done)) {
array.push(eachIteration.value);
}
return array;
}
toArray(take(FibonacciIterator(), 5))
//=> [1, 1, 2, 3, 5]
toArray(take(squares, 5))
//=> [1, 4, 9, 16, 25]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01304))_

> How about the squares of the first five odd numbers? We'll need an iterator that produces odd numbers. We can write that directly:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01305))_

```
const odds = () => {
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01304))_

> How about the squares of the first five odd numbers? We'll need an iterator that produces odd numbers. We can write that directly:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01306))_

```
let number = 1;
return () => {
const value = number;
number += 2;
return {done: false, value};
}
}
const squareOf = callLeft(mapIteratorWith, (x) => x * x)
toArray(take(squareOf(odds()), 5))
//=> [1, 9, 25, 49, 81]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01307))_

> We could also write a filter for iterators to accompany our mapping function:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01308))_

```
const filterIteratorWith = (fn, iterator) =>
() => {
do {
const {done, value} = iterator();
} while (!done && !fn(value));
return {done, value};
}
const oddsOf = callLeft(filterIteratorWith, (n) => n % 2 === 1);
toArray(take(squareOf(oddsOf(NumberIterator(1))), 5))
//=> [1, 9, 25, 49, 81]
```

#### bonus

- In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-0e12e052-01311))_
- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. _(javascriptallonge.pdf (source-range-0e12e052-01311))_
- In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-0e12e052-01311))_
- This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. _(javascriptallonge.pdf (source-range-0e12e052-01314))_
- This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. _(javascriptallonge.pdf (source-range-0e12e052-01314))_
- If array was very large, and fn very slow, this would consume a lot of unnecessary time. _(javascriptallonge.pdf (source-range-0e12e052-01316))_
- And if fn had some sort of side-effect, the program could be buggy. _(javascriptallonge.pdf (source-range-0e12e052-01316))_
- JavaScript would apply fn to every element. _(javascriptallonge.pdf (source-range-0e12e052-01316))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01311, source-range-0e12e052-01314))_

> Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. In Smalltalk, for example, they are known as collect , select , and detect . This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01313))_

```
const firstInIteration = (fn, iterator) =>
take(filterIteratorWith(fn, iterator), 1);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01314))_

> This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01315))_

```
const firstInArray = (fn, array) =>
array.filter(fn)[0];
```

#### caveat

- One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. _(javascriptallonge.pdf (source-range-0e12e052-01318))_
- There are some important implications of stateful functions. _(javascriptallonge.pdf (source-range-0e12e052-01318))_
- Please note that unlike most of the other functions discussed in this book, iterators are stateful . _(javascriptallonge.pdf (source-range-0e12e052-01318))_
- Please note that unlike most of the other functions discussed in this book, iterators are stateful . _(javascriptallonge.pdf (source-range-0e12e052-01318))_
- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-0e12e052-01319))_

### Making Data Out Of Functions

- For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-0e12e052-01323))_
- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. _(javascriptallonge.pdf (source-range-0e12e052-01323))_
- For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-0e12e052-01323))_
- A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations. _(javascriptallonge.pdf (source-range-0e12e052-01325))_
- They searched for a radically simpler set of tools that could accomplish all of the same things. _(javascriptallonge.pdf (source-range-0e12e052-01325))_
- We can model lists just using functions. _(javascriptallonge.pdf (source-range-0e12e052-01326))_
- They established that arbitrary computations could be represented a small set of axiomatic components. _(javascriptallonge.pdf (source-range-0e12e052-01326))_
- For example, we don't need arrays to represent lists, or even POJOs to represent nodes in a linked list. _(javascriptallonge.pdf (source-range-0e12e052-01326))_
- For example, we don't need arrays to represent lists, or even POJOs to represent nodes in a linked list. _(javascriptallonge.pdf (source-range-0e12e052-01326))_
- The oscin.es 77 library contains code for all of the standard combinators and for experimenting using the standard notation. _(javascriptallonge.pdf (source-range-0e12e052-01328))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01321))_

> [Figure] (p.177)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01323))_

> In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01324))_

```
const EMPTY = {};
const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \
} } };
OneTwoThree.first
//=> 1
OneTwoThree.rest.first
//=> 2
OneTwoThree.rest.rest.first
//=> 3
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
length(OneTwoThree)
//=> 3
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01328))_

> The oscin.es 77 library contains code for all of the standard combinators and for experimenting using the standard notation.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01330))_

```text
76 http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422
77 http://oscin.es
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 76 | http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422 |
| 77 | http://oscin.es |

</details>

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01328))_

> The oscin.es 77 library contains code for all of the standard combinators and for experimenting using the standard notation.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01331))_

```
const K = (x) => (y) => x;
const I = (x) => (x);
const V = (x) => (y) => (z) => z(x)(y);
```

#### the kestrel and the idiot

- You give it a value, and it returns a constant function that gives that value. _(javascriptallonge.pdf (source-range-0e12e052-01333))_
- For example, (x) => 42 is a constant function that always evaluates to 42. _(javascriptallonge.pdf (source-range-0e12e052-01333))_
- The kestrel, or K , is a function that makes constant functions. _(javascriptallonge.pdf (source-range-0e12e052-01333))_
- A constant function is a function that always returns the same thing, no matter what you give it. _(javascriptallonge.pdf (source-range-0e12e052-01333))_
- For example, (x) => 42 is a constant function that always evaluates to 42. _(javascriptallonge.pdf (source-range-0e12e052-01333))_
- The identity function is a function that evaluates to whatever parameter you pass it. _(javascriptallonge.pdf (source-range-0e12e052-01336))_
- Given two values, we can say that K always returns the first value: K(x)(y) => x (that's not valid JavaScript, but it's essentially how it works). _(javascriptallonge.pdf (source-range-0e12e052-01339))_
- Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value. _(javascriptallonge.pdf (source-range-0e12e052-01347))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01335))_

```
const K = (x) => (y) => x;
const fortyTwo = K(42);
fortyTwo(6)
//=> 42
fortyTwo("Hello")
//=> 42
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01338))_

```
K(6)(7)
//=> 6
K(12)(24)
//=> 12
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01340))_

> Now, an interesting thing happens when we pass functions to each other. Consider K(I) . From what we just wrote, K(x)(y) => x So K(I)(x) => I . Makes sense. Now let's tack one more invocation on: What is K(I)(x)(y) ? If K(I)(x) => I , then K(I)(x)(y) === I(y) which is y .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01341))_

```
Therefore, K(I)(x)(y) => y:
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01340))_

> Now, an interesting thing happens when we pass functions to each other. Consider K(I) . From what we just wrote, K(x)(y) => x So K(I)(x) => I . Makes sense. Now let's tack one more invocation on: What is K(I)(x)(y) ? If K(I)(x) => I , then K(I)(x)(y) === I(y) which is y .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01342))_

```
K(I)(6)(7)
//=> 7
K(I)(12)(24)
//=> 24
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01344))_

```
K("primus")("secundus")
//=> "primus"
K(I)("primus")("secundus")
//=> "secundus"
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01345))_

> If we are not feeling particularly academic, we can name our functions:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01346))_

```
const first = K,
second = K(I);
first("primus")("secundus")
//=> "primus"
second("primus")("secundus")
//=> "secundus"
```

#### backwardness

- Our first and second functions are a little different than what most people are used to when we talk about functions that access data. _(javascriptallonge.pdf (source-range-0e12e052-01349))_
- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. _(javascriptallonge.pdf (source-range-0e12e052-01353))_
- So if we wanted to use them with a two-element array, we'd need to have a piece of code that calls some code. _(javascriptallonge.pdf (source-range-0e12e052-01354))_
- Our latin data structure is no longer a dumb data structure, it's a function. _(javascriptallonge.pdf (source-range-0e12e052-01357))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01349))_

> Our first and second functions are a little different than what most people are used to when we talk about functions that access data. If we represented a pair of values as an array, we'd write them like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01350))_

```
const first = ([first, second]) => first,
second = ([first, second]) => second;
const latin = ["primus", "secundus"];
first(latin)
//=> "primus"
second(latin)
//=> "secundus"
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01351))_

> Or if we were using a POJO, we'd write them like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01352))_

```
const first = ({first, second}) => first,
second = ({first, second}) => second;
const latin = {first: "primus", second: "secundus"};
first(latin)
//=> "primus"
second(latin)
//=> "secundus"
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01356))_

```
const first = K,
second = K(I);
const latin = (selector) => selector("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```

#### the vireo

- In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-0e12e052-01359))_
- Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data. _(javascriptallonge.pdf (source-range-0e12e052-01359))_
- For 'data' we access with K and K(I) , our 'structure' is the function (selector) => selector("primus")("secundus") . _(javascriptallonge.pdf (source-range-0e12e052-01360))_
- For consistency with the way combinators are written as functions taking just one parameter, we'll curry 78 the function: _(javascriptallonge.pdf (source-range-0e12e052-01362))_
- It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. _(javascriptallonge.pdf (source-range-0e12e052-01369))_
- It is known to most programmers as .tap . _(javascriptallonge.pdf (source-range-0e12e052-01369))_
- One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. _(javascriptallonge.pdf (source-range-0e12e052-01369))_
- As an aside, the Vireo is a little like JavaScript's .apply function. _(javascriptallonge.pdf (source-range-0e12e052-01369))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01360))_

> For 'data' we access with K and K(I) , our 'structure' is the function (selector) => selector("primus")("secundus") . Let's extract those into parameters:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01361))_

```
(first, second) => (selector) => selector(first)(second)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01362))_

> For consistency with the way combinators are written as functions taking just one parameter, we'll curry 78 the function:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01363))_

```
(first) => (second) => (selector) => selector(first)(second)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01364))_

> Let's try it, we'll use the word pair for the function that makes data (When we need to refer to a specific pair, we'll use the name aPair by default):

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01365))_

```
const first = K,
second = K(I),
pair = (first) => (second) => (selector) => selector(first)(second);
const latin = pair("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01364))_

> Let's try it, we'll use the word pair for the function that makes data (When we need to refer to a specific pair, we'll use the name aPair by default):

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01366))_

> If we change the names to x , y , and z , we get: (x) => (y) => (z) => z(x)(y) .

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01366))_

> It works! Now what is this pair function? If we change the names to x , y , and z , we get: (x) => (y) => (z) => z(x)(y) . That's the V combinator, the Vireo! So we can write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01368))_

```
const first = K,
second = K(I),
pair = V;
const latin = pair("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```

#### lists with functions as data

- Here's another look at linked lists using POJOs. _(javascriptallonge.pdf (source-range-0e12e052-01372))_
- Presto, we can use pure functions to represent a linked list . _(javascriptallonge.pdf (source-range-0e12e052-01380))_
- And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else. _(javascriptallonge.pdf (source-range-0e12e052-01380))_
- We used functions to replace arrays and POJOs, but we still use JavaScript's built-in operators to test for equality ( === ) and to branch ?: . _(javascriptallonge.pdf (source-range-0e12e052-01382))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01372))_

> Here's another look at linked lists using POJOs. We use the term rest instead of second , but it's otherwise identical to what we have above:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01373))_

```
const first = ({first, rest}) => first,
rest
= ({first, rest}) => rest,
pair = (first, rest) => ({first, rest}),
EMPTY = ({});
const l123 = pair(1, pair(2, pair(3, EMPTY)));
first(l123)
//=> 1
first(rest(l123))
//=> 2
first(rest(rest(l123)))
//=3
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01374))_

> We can write length and mapWith functions over it:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01375))_

```
const length = (aPair) =>
aPair === EMPTY
? 0
: 1 + length(rest(aPair));
length(l123)
//=> 3
const reverse = (aPair, delayed = EMPTY) =>
aPair === EMPTY
? delayed
: reverse(rest(aPair), pair(first(aPair), delayed));
const mapWith = (fn, aPair, delayed = EMPTY) =>
aPair === EMPTY
? reverse(delayed)
: mapWith(fn, rest(aPair), pair(fn(first(aPair)), delayed));
const doubled = mapWith((x) => x * 2, l123);
first(doubled)
//=> 2
first(rest(doubled))
//=> 4
first(rest(rest(doubled)))
//=> 6
Can we do the same with the linked lists we build out of functions? Yes:
const first = K,
rest
= K(I),
pair = V,
EMPTY = (() => {});
const l123 = pair(1)(pair(2)(pair(3)(EMPTY)));
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01374))_

> We can write length and mapWith functions over it:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01376))_

```
rest
= K(I),
pair = V,
EMPTY = (() => {});
const l123 = pair(1)(pair(
l123(first)
//=> 1
l123(rest)(first)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01374))_

> We can write length and mapWith functions over it:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01377))_

```
//=> 2
return l123(rest)(rest)(first)
//=> 3
We write them in a backwards way, but they seem to work. How about
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01379))_

```
const length = (aPair) =>
aPair === EMPTY
? 0
: 1 + length(aPair(rest));
length(l123)
//=> 3
And mapWith?
const reverse = (aPair, delayed = EMPTY) =>
aPair === EMPTY
? delayed
: reverse(aPair(rest), pair(aPair(first))(delayed));
const mapWith = (fn, aPair, delayed = EMPTY) =>
aPair === EMPTY
? reverse(delayed)
: mapWith(fn, aPair(rest), pair(fn(aPair(first)))(delayed));
const doubled = mapWith((x) => x * 2, l123)
doubled(first)
//=> 2
doubled(rest)(first)
//=> 4
doubled(rest)(rest)(first)
//=> 6
```

#### say 'please'

- This follows the philosophy we used with data structures: The function doing the work inspects the data structure. _(javascriptallonge.pdf (source-range-0e12e052-01384))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-0e12e052-01385))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-0e12e052-01385))_
- Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. _(javascriptallonge.pdf (source-range-0e12e052-01389))_
- We can write reverse and mapWith as well. _(javascriptallonge.pdf (source-range-0e12e052-01392))_
- We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else. _(javascriptallonge.pdf (source-range-0e12e052-01394))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01385))_

> We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. Here's length again:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01386))_

```
const length = (aPair) =>
aPair === EMPTY
? 0
: 1 + length(aPair(rest));
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01387))_

> Let's presume we are working with a slightly higher abstraction, we'll call it a list . Instead of writing length(list) and examining a list, we'll write something like:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01388))_

```
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(rest)))
);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01389))_

> Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. So let's disambiguate our names:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01390))_

```
const pairFirst = K,
pairRest
= K(I),
pair = V;
const first = (list) => list(
() => "ERROR: Can't take first of an empty list",
(aPair) => aPair(pairFirst)
);
const rest = (list) => list(
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01389))_

> Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. So let's disambiguate our names:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01391))_

```
() => "ERROR: Can't take first of an empty list",
(aPair) => aPair(pairRest)
);
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(pairRest)))
);
We’ll also write a handy list printer:
const print = (list) => list(
() => "",
(aPair) => `${aPair(pairFirst)} ${print(aPair(pairRest))}`
);
How would all this work? Let’s start with the obvious. What is an empty list?
const EMPTYLIST = (whenEmpty, unlessEmpty) => whenEmpty()
And what is a node of a list?
const node = (x) => (y) =>
(whenEmpty, unlessEmpty) => unlessEmpty(pair(x)(y));
Let’s try it:
const l123 = node(1)(node(2)(node(3)(EMPTYLIST)));
print(l123)
//=> 1 2 3
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01392))_

> We can write reverse and mapWith as well. We aren't being super-strict about emulating combinatory logic, we'll use default parameters:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01393))_

```
const reverse = (list, delayed = EMPTYLIST) => list(
() => delayed,
(aPair) => reverse(aPair(pairRest), node(aPair(pairFirst))(delayed))
);
print(reverse(l123));
//=> 3 2 1
const mapWith = (fn, list, delayed = EMPTYLIST) =>
list(
() => reverse(delayed),
(aPair) => mapWith(fn, aPair(pairRest), node(fn(aPair(pairFirst)))(delayed))
);
print(mapWith(x => x * x, reverse(l123)))
//=> 941
```

#### functions are not the real point

- You can establish that K and K(I) can represent true and false , model magnitudes with Church Numerals 79 or Surreal Numbers 80 , and build your way up to printing FizzBuzz. _(javascriptallonge.pdf (source-range-0e12e052-01396))_
- There are lots of similar texts explaining how to construct complex semantics out of functions. _(javascriptallonge.pdf (source-range-0e12e052-01396))_
- Functions are a fundamental building block of computation. _(javascriptallonge.pdf (source-range-0e12e052-01398))_
- They are 'axioms' of combinatory logic, and can be used to compute anything that JavaScript can compute. _(javascriptallonge.pdf (source-range-0e12e052-01398))_
- Knowing how to make a linked list out of functions is not really necessary for the working programmer. _(javascriptallonge.pdf (source-range-0e12e052-01399))_
- (Knowing that it can be done, on the other hand, is very important to understanding computer science.) _(javascriptallonge.pdf (source-range-0e12e052-01399))_
- However, that is not the interesting thing to note here. _(javascriptallonge.pdf (source-range-0e12e052-01399))_
- Practically speaking, languages like JavaScript already provide arrays with mapping and folding methods, choice operations, and other rich constructs. _(javascriptallonge.pdf (source-range-0e12e052-01399))_
- Knowing how to make a list out of just functions is a little like knowing that photons are the Gauge Bosons 81 of the electromagnetic force. _(javascriptallonge.pdf (source-range-0e12e052-01400))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01400))_

> Knowing how to make a list out of just functions is a little like knowing that photons are the Gauge Bosons 81 of the electromagnetic force. It's the QED of physics that underpins the Maxwell's Equations of programming. Deeply important, but not practical when you're building a bridge.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01401))_

```text
79 https://en.wikipedia.org/wiki/Church_encoding
81 https://en.wikipedia.org/wiki/Gauge_boson
80 https://en.wikipedia.org/wiki/Surreal_number
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 79 | https://en.wikipedia.org/wiki/Church_encoding |
| 81 | https://en.wikipedia.org/wiki/Gauge_boson |
| 80 | https://en.wikipedia.org/wiki/Surreal_number |

</details>

#### a return to backward thinking

- To make pairs work, we did things backwards , we passed the first and rest functions to the pair, and the pair called our function. _(javascriptallonge.pdf (source-range-0e12e052-01404))_
- We could have written a pair that stored its elements in an array, or a pair that stored its elements in a POJO. _(javascriptallonge.pdf (source-range-0e12e052-01405))_
- But we could have done something completely different. _(javascriptallonge.pdf (source-range-0e12e052-01405))_
- All we know is that we can pass the pair function a function of our own, at it will be called with the elements of the pair. _(javascriptallonge.pdf (source-range-0e12e052-01405))_
- The exact implementation of a pair is hidden from the code that uses a pair. _(javascriptallonge.pdf (source-range-0e12e052-01406))_
- This is a little gratuitous, but it makes the point: The code that uses the data doesn't reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. _(javascriptallonge.pdf (source-range-0e12e052-01408))_
- We're passing list what we want done with an empty list, and what we want done with a list that has at least one element. _(javascriptallonge.pdf (source-range-0e12e052-01411))_
- We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-0e12e052-01411))_
- We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-0e12e052-01411))_
- It presumes you can compare these things with the === operator. _(javascriptallonge.pdf (source-range-0e12e052-01414))_
- It presumes there is one canonical empty list value. _(javascriptallonge.pdf (source-range-0e12e052-01414))_
- We can fix this with an isEmpty function, but now we're pushing even more knowledge about the structure of lists into the code that uses them. _(javascriptallonge.pdf (source-range-0e12e052-01414))_
- This is a fundamental principle of good design. _(javascriptallonge.pdf (source-range-0e12e052-01415))_
- It is a tenet of Object-Oriented Programming, but it is not exclusive to OOP: We can and should design data structures to hide implementation information from the code that use them, whether we are working with functions, objects, or both. _(javascriptallonge.pdf (source-range-0e12e052-01415))_
- Having a list know itself whether it is empty hides implementation information from the code that uses lists. _(javascriptallonge.pdf (source-range-0e12e052-01415))_
- There are many tools for hiding implementation information, and we have now seen two particularly powerful patterns: _(javascriptallonge.pdf (source-range-0e12e052-01416))_
- - Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. _(javascriptallonge.pdf (source-range-0e12e052-01417))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01406))_

> The exact implementation of a pair is hidden from the code that uses a pair. Here, we'll prove it:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01407))_

```
const first = K,
second = K(I),
pair = (first) => (second) => {
const pojo = {first, second};
return (selector) => selector(pojo.first)(pojo.second);
};
const latin = pair("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01409, source-range-0e12e052-01412))_

> The same thing happens with our lists. Here's length for lists: We won't bother here, but it's easy to see how to swap our functions out and replace them with an array. Or a column in a database. This is fundamentally not the same thing as this code for the length of a linked list:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01410))_

```
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(pairRest)))
);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01412))_

> We won't bother here, but it's easy to see how to swap our functions out and replace them with an array. Or a column in a database. This is fundamentally not the same thing as this code for the length of a linked list:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01413))_

```
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
```

## Recipes with Data

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01420))_

> [Figure] (p.191)

#### Disclaimer

- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven't been discussed in the text to this point, such as methods and/or prototypes. _(javascriptallonge.pdf (source-range-0e12e052-01423))_
- The overall use of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-0e12e052-01423))_
- The overall use of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-0e12e052-01423))_
- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven't been discussed in the text to this point, such as methods and/or prototypes. _(javascriptallonge.pdf (source-range-0e12e052-01423))_

### mapWith

- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. _(javascriptallonge.pdf (source-range-0e12e052-01432))_
- For example, we might need a function to return the squares of an array. _(javascriptallonge.pdf (source-range-0e12e052-01432))_
- For example, we might need a function to return the squares of an array. _(javascriptallonge.pdf (source-range-0e12e052-01432))_
- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. _(javascriptallonge.pdf (source-range-0e12e052-01432))_
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. _(javascriptallonge.pdf (source-range-0e12e052-01435))_
- 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. _(javascriptallonge.pdf (source-range-0e12e052-01435))_
- But for the purposes of discussing ideas, we can use the same name twice in two different contexts. _(javascriptallonge.pdf (source-range-0e12e052-01435))_
- It's the same idea, after all. _(javascriptallonge.pdf (source-range-0e12e052-01435))_
- If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result: _(javascriptallonge.pdf (source-range-0e12e052-01437))_
- mapWith is a very convenient abstraction for a very common pattern. _(javascriptallonge.pdf (source-range-0e12e052-01439))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01425))_

> In JavaScript, arrays have a .map method. Map takes a function as an argument, and applies it to each of the elements of the array, then returns the results in another array. For example:

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01425))_

> In JavaScript, arrays have a .map method. Map takes a function as an argument, and applies it to each of the elements of the array, then returns the results in another array. For example:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01426))_

```
[1, 2, 3, 4, 5].map(x => x * x)
//=> [1, 4, 9, 16, 25]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01427))_

> We could write a function that behaves like the .map method if we wanted:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01428))_

```
const map = (list, fn) =>
list.map(fn);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01427, source-range-0e12e052-01432))_

> We could write a function that behaves like the .map method if we wanted: That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01430))_

```
const mapWith = (fn) => (list) => list.map(fn);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01432))_

> That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01433))_

```
const squaresOf = (list) =>
list.map(x => x * x);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01435, source-range-0e12e052-01437))_

> 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01436))_

```
const squaresOf = mapWith(n => n * n);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01437))_

> If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01438))_

```
const squaresOf = callRight(map, (n => n * n);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

### Flip

- What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. _(javascriptallonge.pdf (source-range-0e12e052-01457))_
- What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. _(javascriptallonge.pdf (source-range-0e12e052-01457))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01443))_

> We wrote mapWith like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01444))_

```
const mapWith = (fn) => (list) => list.map(fn);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01445))_

> Let's consider the case whether we have a map function of our own, perhaps from the allong.es 84 library, perhaps from Underscore 85 . We could write our function something like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01446))_

```
const mapWith = (fn) => (list) => map(list, fn);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01445))_

> Let's consider the case whether we have a map function of our own, perhaps from the allong.es 84 library, perhaps from Underscore 85 . We could write our function something like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01447))_

> You can see that if we simplify it:

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01447))_

> Looking at this, we see we're conflating two separate transformations. First, we're reversing the order of arguments. You can see that if we simplify it:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01448))_

```
const mapWith = (fn, list) => map(list, fn);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01449))_

> Second, we're 'currying' the function so that instead of defining a function that takes two arguments, it returns a function that takes the first argument and returns a function that takes the second argument and applies them both, like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01450))_

```
const mapper = (list) => (fn) => map(list, fn);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01451))_

> Let's return to the implementation of mapWith that relies on a map function rather than a method:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01452))_

```
const mapWith = (fn) => (list) => map(list, fn);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01453))_

> We're going to extract these two operations by refactoring our function to paramaterize map . The first step is to give our parameters generic names:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01454))_

```
const mapWith = (first) => (second) => map(second, first);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01453))_

> We're going to extract these two operations by refactoring our function to paramaterize map . The first step is to give our parameters generic names:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01456))_

```
const wrapper = (fn) =>
(first) => (second) => fn(second, first);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01457))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01458))_

```text
84 https://github.com/raganwald/allong.es
85 http://underscorejs.org
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 84 | https://github.com/raganwald/allong.es |
| 85 | http://underscorejs.org |

</details>

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01457))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01459))_

```
const flipAndCurry = (fn) =>
(first) => (second) => fn(second, first);
Sometimes you want to flip, but not curry:
const flip = (fn) =>
(first, second) => fn(second, first);
This is gold. Consider how we define mapWith now:
var mapWith = flipAndCurry(map);
Much nicer!
```

#### self-currying flip

- Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). _(javascriptallonge.pdf (source-range-0e12e052-01461))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01461))_

> Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01462))_

```
const flip = (fn) =>
function (first, second) {
if (arguments.length === 2) {
return fn(second, first);
}
else {
return function (second) {
return fn(second, first);
};
};
};
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01461))_

> Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01463))_

> Nowif we write mapWith = flip(map) , we can call mapWith(fn, list) or mapWith(fn)(list) , our choice.

#### flipping methods

- When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. _(javascriptallonge.pdf (source-range-0e12e052-01465))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01465))_

> When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. A small alteration gets the job done:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01466))_

```
const flipAndCurry = (fn) =>
(first) =>
function (second) {
return fn.call(this, second, first);
}
const flip = (fn) =>
function (first, second) {
return fn.call(this, second, first);
}
const flip = (fn) =>
function (first, second) {
if (arguments.length === 2) {
return fn.call(this, second, first);
}
else {
return function (second) {
return fn.call(this, second, first);
};
};
};
```

### Object.assign

- Both needs can be met with Object.assign , a standard function. _(javascriptallonge.pdf (source-range-0e12e052-01472))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01468))_

> It's very common to want to 'extend' an object by assigning properties to it:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01469))_

```
const inventory = {
apples: 12,
oranges: 12
};
inventory.bananas = 54;
inventory.pears = 24;
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01470))_

> It's also common to want to assign the properties of one object to another:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01471))_

```
for (let fruit in shipment) {
inventory[fruit] = shipment[fruit]
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01472))_

> Both needs can be met with Object.assign , a standard function. You can copy an object by extending an empty object:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01473))_

```
Object.assign({}, {
apples: 12,
oranges: 12
})
//=> { apples: 12, oranges: 12 }
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01474))_

> You can extend one object with another:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01475))_

```
const inventory = {
apples: 12,
oranges: 12
};
const shipment = {
bananas: 54,
pears: 24
}
Object.assign(inventory, shipment)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01474))_

> You can extend one object with another:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01476))_

```
//=> { apples: 12,
//
oranges: 12,
//
bananas: 54,
//
pears: 24 }
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01477))_

> oranges: 12, bananas: 54, And when we discuss prototypes, we will use Object.assign to turn this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01478))_

```
const Queue = function () {
this.array = [];
this.head = 0;
this.tail = -1
};
Queue.prototype.pushTail = function (value) {
// ...
};
Queue.prototype.pullHead = function () {
// ...
};
Queue.prototype.isEmpty = function () {
// ...
}
Into this:
const Queue = function () {
Object.assign(this, {
array: [],
head: 0,
tail: -1
})
};
Object.assign(Queue.prototype, {
pushTail (value) {
// ...
},
pullHead () {
// ...
},
isEmpty () {
// ...
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01477))_

> oranges: 12, bananas: 54, And when we discuss prototypes, we will use Object.assign to turn this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01479))_

```
Recipes with Data
}
});
```

### Why?

- It enables you to make recursive functions without needing to bind a function to a name in an environment. _(javascriptallonge.pdf (source-range-0e12e052-01484))_
- This has little practical utility in JavaScript, but in combinatory logic it's essential: With fixed-point combinators it's possible to compute everything computable without binding names. _(javascriptallonge.pdf (source-range-0e12e052-01484))_
- Well, besides all of the practical applications that combinators provide, there is this little thing called The joy of working things out. _(javascriptallonge.pdf (source-range-0e12e052-01485))_
- There are many explanations of the Y Combinator's mechanism on the internet, but resist the temptation to read any of them: Work it out for yourself. _(javascriptallonge.pdf (source-range-0e12e052-01486))_
- One tip is to use JavaScript to name things. _(javascriptallonge.pdf (source-range-0e12e052-01487))_
- Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-0e12e052-01489))_
- Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-0e12e052-01489))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01482))_

```
This is the canonical Y Combinator86:
const Y = (f) =>
( x => f(v => x(x)(v)) )(
x => f(v => x(x)(v))
);
You use it like this:
const factorial = Y(function (fac) {
return function (n) {
return (n == 0 ? 1 : n * fac(n - 1));
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01483))_

```
return function (n) {
return (n == 0 ? 1
}
});
factorial(5)
//=> 120
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01487))_

> One tip is to use JavaScript to name things. For example, you could start by writing:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01488))_

```
const Y = (f) => {
const something = x => f(v => x(x)(v));
return something(something);
};
```

## A Warm Cup: Basic Strings and Quasi-Literals

- Coffee and a Book An expression is any valid unit of code that resolves to a value.-Mozilla Development Network: Expressions and operators 87 _(javascriptallonge.pdf (source-range-0e12e052-01494))_
- For example, the escape sequence \n inserts a newline character in a string literal, like this: 'first line\nsecond line' . _(javascriptallonge.pdf (source-range-0e12e052-01495))_
- There are operators that can be used on strings. _(javascriptallonge.pdf (source-range-0e12e052-01496))_
- Writing is a big part of what makes us human, and strings are how JavaScript and most other languages represent writing. _(javascriptallonge.pdf (source-range-0e12e052-01498))_
- String manipulation is extremely common in programming. _(javascriptallonge.pdf (source-range-0e12e052-01498))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01493))_

> [Figure] (p.202)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01496))_

> There are operators that can be used on strings. The most common is + , it concatenates :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01497))_

```
'fu' + 'bar'
//=> 'fubar'
```

#### quasi-literals

- Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-0e12e052-01500))_
- A quasi-literal can contain an expression to be evaluated. _(javascriptallonge.pdf (source-range-0e12e052-01502))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-0e12e052-01502))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-0e12e052-01502))_
- Aquasi-literal is computationally equivalent to an expression using + . _(javascriptallonge.pdf (source-range-0e12e052-01505))_
- Quasi-literals are expressions that resemble their result. _(javascriptallonge.pdf (source-range-0e12e052-01508))_
- However, there is a big semantic difference between a quasi-literal and an expression. _(javascriptallonge.pdf (source-range-0e12e052-01508))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01502))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01501))_

```
`foobar`
//=> 'foobar'
`fizz` + `buzz`
//=> 'fizzbuzz'
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01503, source-range-0e12e052-01505))_

> For example: Aquasi-literal is computationally equivalent to an expression using + . So the above expression could also be written:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01504))_

```
`A popular number for nerds is ${40 + 2}`
//=> 'A popular number for nerds is 42'
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01505, source-range-0e12e052-01508))_

> Aquasi-literal is computationally equivalent to an expression using + . So the above expression could also be written: However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01507))_

```
'A popular number for nerds is ' + (40 + 2)
//=> 'A popular number for nerds is 42'
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01508))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01509))_

```
'A popular number for nerds is' + (40 + 2)
//=> 'A popular number for nerds is42'
```

#### evaluation time

- Like any other expression, quasi-literals are evaluated late , when that line or lines of code is evaluated. _(javascriptallonge.pdf (source-range-0e12e052-01511))_
- Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-0e12e052-01514))_
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. _(javascriptallonge.pdf (source-range-0e12e052-01514))_
- Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-0e12e052-01514))_
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. _(javascriptallonge.pdf (source-range-0e12e052-01514))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01513))_

```
const name = "Harry";
const greeting = (name) => `Hello my name is ${name}`;
greeting('Arthur Dent')
//=> 'Hello my name is Arthur Dent'
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01515))_

> This is exactly what we'd expect if we'd written it like this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01516))_

```
const greeting = (name) => 'Hello my name is ' + name;
greeting('Arthur Dent')
//=> 'Hello my name is Arthur Dent'
```

## Served by the Pot: Collections

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01518))_

> [Figure] (p.205)

### Iteration and Iterables

- But sometimes you want to open it up and do things with its contents. _(javascriptallonge.pdf (source-range-0e12e052-01523))_
- Many objects in JavaScript can model collections of things. _(javascriptallonge.pdf (source-range-0e12e052-01523))_
- Acting on the elements of a collection one at a time is called iterating over the contents , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-0e12e052-01525))_
- Acting on the elements of a collection one at a time is called iterating over the contents , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-0e12e052-01525))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01521))_

> [Figure] (p.206)

#### a look back at functional iterators

- We can do the same thing for objects. _(javascriptallonge.pdf (source-range-0e12e052-01527))_
- We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method: _(javascriptallonge.pdf (source-range-0e12e052-01536))_
- Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-0e12e052-01538))_
- If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. _(javascriptallonge.pdf (source-range-0e12e052-01538))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01527))_

> When discussing functions, we looked at the benefits of writing Functional Iterators. We can do the same thing for objects. Here's a stack that has its own functional iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01528))_

```
const Stack1 = () =>
({
array:[],
index: -1,
push (value) {
return this.array[this.index += 1] = value;
},
pop () {
const value = this.array[this.index];
this.array[this.index] = undefined;
if (this.index >= 0) {
this.index -= 1
}
return value
},
isEmpty () {
return this.index < 0
},
iterator () {
let iterationIndex = this.index;
return () => {
if (iterationIndex > this.index) {
iterationIndex = this.index;
}
if (iterationIndex < 0) {
return {done: true};
}
else {
return {done: false, value: this.array[iterationIndex--]}
}
}
}
});
const stack = Stack1();
stack.push("Greetings");
stack.push("to");
stack.push("you!")
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01527))_

> When discussing functions, we looked at the benefits of writing Functional Iterators. We can do the same thing for objects. Here's a stack that has its own functional iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01529))_

```
const iter = stack.iterator();
iter().value
//=> "you!"
iter().value
//=> "to"
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01531))_

```
The .iterator() method is defined with shorthand equivalent to iterator: function iterator()
{ ... }. Note that it uses the function keyword, so when we invoke it with stack.iterator(),
JavaScript sets this to the value of stack. But what about the function .iterator() returns? It is
defined with a fat arrow () => { ... }. What is the value of this within that function?
Since JavaScript doesn’t bind this within a fat arrow function, we follow the same rules of variable
scoping as any other variable name: We check in the environment enclosing the function. Although
the .iterator() method has returned, its environment is the one that encloses our () => { ...
} function, and that’s where this is bound to the value of stack.
Therefore, the iterator function returned by the .iterator() method has this bound to the stack
object, even though we call it with iter().
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01532))_

> And here's a sum function implemented as a fold over a functional iterator:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01533))_

```
const iteratorSum = (iterator) => {
let eachIteration,
sum = 0;
while ((eachIteration = iterator(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01534))_

> We can use it with our stack:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01535))_

```
const stack = Stack1();
stack.push(1);
stack.push(2);
stack.push(3);
iteratorSum(stack.iterator())
//=> 6
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01536))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01537))_

```
const collectionSum = (collection) => {
const iterator = collection.iterator();
let eachIteration,
sum = 0;
while ((eachIteration = iterator(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
collectionSum(stack)
//=> 6
```

#### iterator objects

- Iteration for functions and objects has been around for many, many decades. _(javascriptallonge.pdf (source-range-0e12e052-01541))_
- For simple linear collections like arrays, linked lists, stacks, and queues, functional iterators are the simplest and easiest way to implement iterators. _(javascriptallonge.pdf (source-range-0e12e052-01541))_
- The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-0e12e052-01542))_
- In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. _(javascriptallonge.pdf (source-range-0e12e052-01542))_
- The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-0e12e052-01542))_
- Fortunately, an iterator object is almost as simple as an iterator function. _(javascriptallonge.pdf (source-range-0e12e052-01543))_
- Instead of having a function that you call to get the next element, you have an object with a .next() method. _(javascriptallonge.pdf (source-range-0e12e052-01543))_

##### Like this:

- Now our .iterator() method is returning an iterator object. _(javascriptallonge.pdf (source-range-0e12e052-01547))_
- When working with objects, we do things the object way. _(javascriptallonge.pdf (source-range-0e12e052-01547))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01545))_

```
const Stack2 = () =>
({
array: [],
index: -1,
push (value) {
return this.array[this.index += 1] = value;
},
pop () {
const value = this.array[this.index];
this.array[this.index] = undefined;
if (this.index >= 0) {
this.index -= 1
}
return value
},
isEmpty () {
return this.index < 0
},
iterator () {
let iterationIndex = this.index;
return {
next () {
if (iterationIndex > this.index) {
iterationIndex = this.index;
}
if (iterationIndex < 0) {
return {done: true};
}
else {
return {done: false, value: this.array[iterationIndex--]}
}
}
}
}
});
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01546))_

```
const stack = Stack2();
stack.push(2000);
stack.push(10);
stack.push(5)
const collectionSum = (collection) => {
const iterator = collection.iterator();
let eachIteration,
sum = 0;
while ((eachIteration = iterator.next(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
collectionSum(stack)
//=> 2015
```

#### iterables

- People have been writing iterators since JavaScript was first released in the late 1990s. _(javascriptallonge.pdf (source-range-0e12e052-01549))_
- Since there was no particular standard way to do it, people used all sorts of methods, and their methods returned all sorts of things: Objects with various interfaces, functional iterators, you name it. _(javascriptallonge.pdf (source-range-0e12e052-01549))_
- Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator. _(javascriptallonge.pdf (source-range-0e12e052-01550))_
- So, when a standard way to write iterators was added to the JavaScript language, it didn't make sense to use a method like .iterator() for it: That would conflict with existing code. _(javascriptallonge.pdf (source-range-0e12e052-01550))_
- To ensure that the method would not conflict with any existing code, JavaScript provides a symbol . _(javascriptallonge.pdf (source-range-0e12e052-01551))_
- Symbols are a longstanding technique in programming going back to Lisp, where the GENSYM function generated… You guessed it… Symbols. _(javascriptallonge.pdf (source-range-0e12e052-01551))_
- Symbols are unique constants that are guaranteed not to conflict with existing strings. _(javascriptallonge.pdf (source-range-0e12e052-01551))_
- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-0e12e052-01552))_
- 88 You can read more about JavaScript symbols in Axel Rauschmayer's Symbols in ECMAScript 2015. _(javascriptallonge.pdf (source-range-0e12e052-01553))_
- Our stack does, so instead of binding the existing iterator method to the name iterator , we bind it to the Symbol.iterator . _(javascriptallonge.pdf (source-range-0e12e052-01554))_
- The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. _(javascriptallonge.pdf (source-range-0e12e052-01557))_
- ) can spread the elements of an array in an array literal or as parameters in a function invocation. _(javascriptallonge.pdf (source-range-0e12e052-01559))_
- Nowis the time to note that we can spread any iterable. _(javascriptallonge.pdf (source-range-0e12e052-01560))_
- That might be very wasteful for extremely large collections. _(javascriptallonge.pdf (source-range-0e12e052-01565))_
- For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-0e12e052-01565))_
- For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-0e12e052-01565))_
- And if we have an infinite collection, spreading is going to fail outright as we're about to see. _(javascriptallonge.pdf (source-range-0e12e052-01566))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01554))_

> Our stack does, so instead of binding the existing iterator method to the name iterator , we bind it to the Symbol.iterator . We'll do that using the [ ] syntax for using an expression as an object literal key:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01555))_

```
const Stack3 = () =>
({
array: [],
index: -1,
push (value) {
return this.array[this.index += 1] = value;
},
pop () {
const value = this.array[this.index];
this.array[this.index] = undefined;
if (this.index >= 0) {
this.index -= 1
}
return value
},
isEmpty () {
return this.index < 0
},
[Symbol.iterator] () {
let iterationIndex = this.index;
return {
next () {
if (iterationIndex > this.index) {
iterationIndex = this.index;
}
if (iterationIndex < 0) {
return {done: true};
}
else {
return {done: false, value: this.array[iterationIndex--]}
}
}
}
}
});
const stack = Stack3();
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01554))_

> Our stack does, so instead of binding the existing iterator method to the name iterator , we bind it to the Symbol.iterator . We'll do that using the [ ] syntax for using an expression as an object literal key:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01556))_

```
stack.push(2000);
stack.push(10);
stack.push(5)
const collectionSum = (collection) => {
const iterator = collection[Symbol.iterator]();
let eachIteration,
sum = 0;
while ((eachIteration = iterator.next(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
collectionSum(stack)
//=> 2015
Using [Symbol.iterator] instead of .iterator seems like adding an extra moving part for nothing.
Do we get anything in return?
Indeed we do. Behold the for...of loop:
const iterableSum = (iterable) => {
let sum = 0;
for (const num of iterable) {
sum += num;
}
return sum
}
iterableSum(stack)
//=> 2015
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01557))_

> The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01558))_

```
const EMPTY = {
isEmpty: () => true
};
const isEmpty = (node) => node === EMPTY;
const Pair1 = (first, rest = EMPTY) =>
({
first,
rest,
isEmpty () { return false },
[Symbol.iterator] () {
let currentPair = this;
return {
next () {
if (currentPair.isEmpty()) {
return {done: true}
}
else {
const value = currentPair.first;
currentPair = currentPair.rest;
return {done: false, value}
}
}
}
}
});
const list = (...elements) => {
const [first, ...rest] = elements;
return elements.length === 0
? EMPTY
: Pair1(first, list(...rest))
}
const someSquares = list(1, 4, 9, 16, 25);
iterableSum(someSquares)
//=> 55
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01560))_

> Nowis the time to note that we can spread any iterable. So we can spread the elements of an iterable into an array literal:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01561))_

```
['some squares', ...someSquares]
//=> ["some squares", 1, 4, 9, 16, 25]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01562))_

> And we can also spread the elements of an array literal into parameters:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01563))_

```
const firstAndSecondElement = (first, second) =>
({first, second})
firstAndSecondElement(...stack)
//=> {"first":5,"second":10}
```

#### iterables out to infinity

- There are useful things we can do with iterables representing an infinitely large collection. _(javascriptallonge.pdf (source-range-0e12e052-01570))_
- Attempting to spread an infinite iterable into an array is always going to fail. _(javascriptallonge.pdf (source-range-0e12e052-01572))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01568))_

> Iterables needn't represent finite collections:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01569))_

```
const Numbers = {
[Symbol.iterator] () {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01570))_

> There are useful things we can do with iterables representing an infinitely large collection. But let's point out what we can't do with them:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01571))_

```
['all the numbers', ...Numbers]
//=> infinite loop!
firstAndSecondElement(...Numbers)
//=> infinite loop!
```

#### ordered collections

- The iterables we're discussing represent ordered collections . _(javascriptallonge.pdf (source-range-0e12e052-01574))_
- One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. _(javascriptallonge.pdf (source-range-0e12e052-01574))_
- This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator] , and ensuring that our iterators start at the beginning and work forward. _(javascriptallonge.pdf (source-range-0e12e052-01576))_
- Iterables needn't represent ordered collections. _(javascriptallonge.pdf (source-range-0e12e052-01577))_
- Therefore, RandomNumbers is not an ordered collection. _(javascriptallonge.pdf (source-range-0e12e052-01579))_
- Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. _(javascriptallonge.pdf (source-range-0e12e052-01579))_
- Therefore, RandomNumbers is not an ordered collection. _(javascriptallonge.pdf (source-range-0e12e052-01579))_
- Right now, we're just looking at ordered collections. _(javascriptallonge.pdf (source-range-0e12e052-01580))_
- To reiterate (hah), an ordered collection represents a (possibly infinite) collection of elements that are in some order. _(javascriptallonge.pdf (source-range-0e12e052-01580))_
- Every time we get an iterator from an ordered collection, we start iterating from the beginning. _(javascriptallonge.pdf (source-range-0e12e052-01580))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01574))_

> The iterables we're discussing represent ordered collections . One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. For example:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01575))_

```
const abc = ["a", "b", "c"];
for (const i of abc) {
console.log(i)
}
//=>
a
b
c
for (const i of abc) {
console.log(i)
}
//=>
a
b
c
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01577, source-range-0e12e052-01579))_

> Iterables needn't represent ordered collections. We could make an infinite iterable representing random numbers: Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. Therefore, RandomNumbers is not an ordered collection.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01578))_

```
const RandomNumbers = {
[Symbol.iterator]: () =>
({
next () {
return {value: Math.random()};
}
})
}
for (const i of RandomNumbers) {
console.log(i)
}
//=>
0.494052127469331
0.835459444206208
0.1408337657339871
...
for (const i of RandomNumbers) {
console.log(i)
}
//=>
0.7845381607767195
0.4956772483419627
0.20259276474826038
...
```

#### operations on ordered collections

- Here's mapWith , it takes an ordered collection, and returns another ordered collection representing a mapping over the original: 89 _(javascriptallonge.pdf (source-range-0e12e052-01582))_
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. _(javascriptallonge.pdf (source-range-0e12e052-01583))_
- 89 Yes, we also used the name mapWith for working with ordinary collections elsewhere. _(javascriptallonge.pdf (source-range-0e12e052-01583))_
- But for the purposes of discussing ideas, we can use the same name twice in two different contexts. _(javascriptallonge.pdf (source-range-0e12e052-01583))_
- It's the same idea, after all. _(javascriptallonge.pdf (source-range-0e12e052-01583))_
- This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . _(javascriptallonge.pdf (source-range-0e12e052-01585))_
- An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order. _(javascriptallonge.pdf (source-range-0e12e052-01585))_
- Many operations on ordered collections return another ordered collection. _(javascriptallonge.pdf (source-range-0e12e052-01586))_
- Numbers is an ordered collection. _(javascriptallonge.pdf (source-range-0e12e052-01588))_
- That in turns means it executes const iterator = Numbers[Symbol.iterator](); every time we write for (const i of Evens) , and that means that iterator starts at the beginning of Numbers . _(javascriptallonge.pdf (source-range-0e12e052-01590))_
- That in turns means it executes const iterator = Numbers[Symbol.iterator](); every time we write for (const i of Evens) , and that means that iterator starts at the beginning of Numbers . _(javascriptallonge.pdf (source-range-0e12e052-01590))_
- Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. _(javascriptallonge.pdf (source-range-0e12e052-01591))_
- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. _(javascriptallonge.pdf (source-range-0e12e052-01591))_
- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. _(javascriptallonge.pdf (source-range-0e12e052-01591))_
- Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. _(javascriptallonge.pdf (source-range-0e12e052-01591))_
- Like mapWith , they preserve the ordered collection semantics of whatever you give them. _(javascriptallonge.pdf (source-range-0e12e052-01598))_
- Andhere's a computation performed using operations on ordered collections: We'll create an ordered collection of square numbers that end in one and are less than 1,000: _(javascriptallonge.pdf (source-range-0e12e052-01599))_
- As we expect from an ordered collection, each time we iterate over UpTo1000 , we begin at the beginning. _(javascriptallonge.pdf (source-range-0e12e052-01601))_
- For completeness, here are two more handy iterable functions. _(javascriptallonge.pdf (source-range-0e12e052-01602))_
- first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. _(javascriptallonge.pdf (source-range-0e12e052-01602))_
- like our other operations, rest preserves the ordered collection semantics of its argument. _(javascriptallonge.pdf (source-range-0e12e052-01604))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01583, source-range-0e12e052-01586))_

> 89 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. Many operations on ordered collections return another ordered collection. They do so by taking care to iterate over a result fresh

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01584))_

```
const mapWith = (fn, collection) =>
({
[Symbol.iterator] () {
const iterator = collection[Symbol.iterator]();
return {
next () {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : fn(value)});
}
}
}
});
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01586))_

> Many operations on ordered collections return another ordered collection. They do so by taking care to iterate over a result freshly every time we get an iterator for them. Consider this example for mapWith :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01587))_

```
const Evens = mapWith((x) => 2 * x, Numbers);
for (const i of Evens) {
console.log(i)
}
//=>
0
2
4
...
for (const i of Evens) {
console.log(i)
}
//=>
0
2
4
...
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01588, source-range-0e12e052-01590))_

> Numbers is an ordered collection. We invoke mapWith((x) => 2 * x, Numbers) and get Evens . Evens works just as if we'd written this: Every time we write for (const i of Evens) , JavaScript calls Evens[Symbol.iterator]() . That in turns means it executes const iterator = Numbers[Symbol.iterator](); every time we write for (const i of Evens) , and that means that iterator starts at the beginning of Numbers .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01589))_

```
const Evens =
{
[Symbol.iterator] () {
const iterator = Numbers[Symbol.iterator]();
return {
next () {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : 2 *value});
}
}
}
};
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01592))_

> Mind you, we can also map non-collection iterables, like RandomNumbers :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01593))_

```
const ZeroesToNines = mapWith((n) => Math.floor(10 * limit), RandomNumbers);
for (const i of ZeroesToNines) {
console.log(i)
}
//=>
5
1
9
...
for (const i of ZeroesToNines) {
console.log(i)
}
//=>
3
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01592))_

> Mind you, we can also map non-collection iterables, like RandomNumbers :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01594))_

```
6
1
...
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01592))_

> Mind you, we can also map non-collection iterables, like RandomNumbers :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01595))_

> mapWith can get a new iterator from RandomNumbers each time we iterate over ZeroesToNines , but if RandomNumbers doesn't behave like an ordered collection, that's not mapWith 's fault.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01596))_

> Here are two more operations on ordered collections, filterWith and untilWith :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01597))_

```
const filterWith = (fn, iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
return {
next () {
do {
const {done, value} = iterator.next();
} while (!done && !fn(value));
return {done, value};
}
}
}
});
const untilWith = (fn, iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
return {
next () {
let {done, value} = iterator.next();
done = done || fn(value);
return ({done, value: done ? undefined : value});
}
}
}
});
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01599))_

> Andhere's a computation performed using operations on ordered collections: We'll create an ordered collection of square numbers that end in one and are less than 1,000:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01600))_

```
const Squares = mapWith((x) => x * x, Numbers);
const EndWithOne = filterWith((x) => x % 10 === 1, Squares);
const UpTo1000 = untilWith((x) => (x > 1000), EndWithOne);
[...UpTo1000]
//=>
[1,81,121,361,441,841,961]
[...UpTo1000]
//=>
[1,81,121,361,441,841,961]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01602))_

> For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest] :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01603))_

```
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
const rest = (iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
iterator.next();
return iterator;
}
});
```

#### from

- No, of course not, we can do anything we like with them. _(javascriptallonge.pdf (source-range-0e12e052-01606))_
- One useful thing is to write a .from function that gathers an iterable into a particular collection type. _(javascriptallonge.pdf (source-range-0e12e052-01607))_
- As you recall, functions are mutable objects. _(javascriptallonge.pdf (source-range-0e12e052-01609))_
- And if we assign a function to a property, we've created a method. _(javascriptallonge.pdf (source-range-0e12e052-01609))_
- We can do the same with our own collections. _(javascriptallonge.pdf (source-range-0e12e052-01609))_
- And we can assign properties to functions with a . _(javascriptallonge.pdf (source-range-0e12e052-01609))_
- Nowwecan go 'end to end,' If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that: _(javascriptallonge.pdf (source-range-0e12e052-01612))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01607))_

> One useful thing is to write a .from function that gathers an iterable into a particular collection type. JavaScript's built-in Array class already has one:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01608))_

```
Array.from(UpTo1000)
//=> [1,81,121,361,441,841,961]
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01611))_

```
Stack3.from = function (iterable) {
const stack = this();
for (let element of iterable) {
stack.push(element);
}
return stack;
}
Pair1.from = (iterable) =>
(function iterationToList (iteration) {
const {done, value} = iteration.next();
return done ? EMPTY : Pair1(value, iterationToList(iteration));
})(iterable[Symbol.iterator]())
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01612))_

> Nowwecan go 'end to end,' If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01613))_

```
const numberList = Pair1.from(untilWith((x) => x > 10, Numbers));
Pair1.from(Squares)
//=> {"first":0,
"rest":{"first":1,
"rest":{"first":4,
"rest":{ ...
```

#### summary

- Iterable ordered collections can be iterated over or gathered into another collection. _(javascriptallonge.pdf (source-range-0e12e052-01615))_
- Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection from what we want to do with the elements of a collection. _(javascriptallonge.pdf (source-range-0e12e052-01615))_
- Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-0e12e052-01616))_

### Generating Iterables

- Iterables look cool, but then again, everything looks amazing when you're given cherry-picked examples. _(javascriptallonge.pdf (source-range-0e12e052-01620))_
- Iterables look cool, but then again, everything looks amazing when you're given cherry-picked examples. _(javascriptallonge.pdf (source-range-0e12e052-01620))_
- Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done. _(javascriptallonge.pdf (source-range-0e12e052-01621))_
- This seems blindingly obvious and simple. _(javascriptallonge.pdf (source-range-0e12e052-01622))_
- The Numbers iterable returns an object that updates a mutable variable, n , to deliver number after number. _(javascriptallonge.pdf (source-range-0e12e052-01624))_
- There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers. _(javascriptallonge.pdf (source-range-0e12e052-01625))_
- Then it waits for the next request. _(javascriptallonge.pdf (source-range-0e12e052-01625))_
- It waits until given a request, and then it returns exactly one item. _(javascriptallonge.pdf (source-range-0e12e052-01625))_
- Of course, when we have some code that makes a bunch of something, we don't usually write it like that. _(javascriptallonge.pdf (source-range-0e12e052-01626))_
- And magically, the numbers would pour forth. _(javascriptallonge.pdf (source-range-0e12e052-01628))_
- We would generate numbers. _(javascriptallonge.pdf (source-range-0e12e052-01628))_
- Well, there are some collections that are much easier to generate than to iterate over. _(javascriptallonge.pdf (source-range-0e12e052-01630))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01618))_

> [Figure] (p.224)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01621))_

> Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01622))_

> Iterators have to arrange its own state such that when you call them, they compute and return the next item.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01622))_

> Iterators have to arrange its own state such that when you call them, they compute and return the next item. This seems blindingly obvious and simple. If, for example, you want numbers, you write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01623))_

```
const Numbers = {
[Symbol.iterator]: () => {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
};
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01626))_

> Of course, when we have some code that makes a bunch of something, we don't usually write it like that. We usually just write something like:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01627))_

```
let n = 0;
while (true) {
console.log(n++)
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01628))_

> And magically, the numbers would pour forth. We would generate numbers. Let's put that beside the code for the iterator, minus the iterable scaffolding:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01629))_

```
// Iteration
let n = 0;
() =>
({done: false, value: n++})
// Generation
let n = 0;
while (true) {
console.log(n++)
}
```

#### recursive iterators

- Generators have to manage the exact same amount of state, but sometimes, it's much easier to manage that state in a generator. _(javascriptallonge.pdf (source-range-0e12e052-01632))_
- Iterators maintain state, that's what they do. _(javascriptallonge.pdf (source-range-0e12e052-01632))_
- elements that are not, themselves, iterable. _(javascriptallonge.pdf (source-range-0e12e052-01633))_
- For example, iterating over a tree. _(javascriptallonge.pdf (source-range-0e12e052-01633))_
- In essence, both the generation and iteration implementations have stacks, but the generation version's stack is implicit , while the iteration version's stack is explicit . _(javascriptallonge.pdf (source-range-0e12e052-01639))_
- If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next , we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. _(javascriptallonge.pdf (source-range-0e12e052-01639))_
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We're reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. _(javascriptallonge.pdf (source-range-0e12e052-01640))_
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We're reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. _(javascriptallonge.pdf (source-range-0e12e052-01640))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01632))_

> One of those cases is when we have to recursively enumerate something.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01633))_

> For example, iterating over a tree. Given an array that might contain arrays, let's say we want to generate all the 'leaf' elements, i.e. elements that are not, themselves, iterable.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01634))_

```
// Generation
const isIterable = (something) =>
!!something[Symbol.iterator];
const generate = (iterable) => {
for (let element of iterable) {
if (isIterable(element)) {
generate(element)
}
else {
console.log(element)
}
}
}
generate([1, [2, [3, 4], 5]])
//=>
1
2
3
4
5
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01636, source-range-0e12e052-01640))_

> Very simple. Now for the iteration version. We'll write a functional iterator to keep things simple, but it's easy to see the shape of the basic problem: A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We're reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01638))_

```
const isIterable = (something) =>
!!something[Symbol.iterator];
const treeIterator = (iterable) => {
const iterators = [ iterable[Symbol.iterator]() ];
return () => {
while (!!iterators[0]) {
const iterationResult = iterators[0].next();
if (iterationResult.done) {
iterators.shift();
}
else if (isIterable(iterationResult.value)) {
iterators.unshift(iterationResult.value[Symbol.iterator]());
}
else {
return iterationResult.value;
}
}
return;
}
}
const i = treeIterator([1, [2, [3, 4], 5]]);
let n;
while (n = i()) {
console.log(n)
}
//=>
1
2
3
4
5
```

#### state machines

- Some iterables can be modelled as state machines. _(javascriptallonge.pdf (source-range-0e12e052-01642))_
- - The first element of the fibonacci sequence is zero. _(javascriptallonge.pdf (source-range-0e12e052-01643))_
- - The second element of the fibonacci sequence is one. _(javascriptallonge.pdf (source-range-0e12e052-01644))_
- - Every subsequent element of the fibonacci sequence is the sum of the previous two elements. _(javascriptallonge.pdf (source-range-0e12e052-01645))_
- This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 : _(javascriptallonge.pdf (source-range-0e12e052-01649))_
- The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. _(javascriptallonge.pdf (source-range-0e12e052-01649))_
- This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 : _(javascriptallonge.pdf (source-range-0e12e052-01649))_
- The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. _(javascriptallonge.pdf (source-range-0e12e052-01649))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01646, source-range-0e12e052-01649))_

> Let's write a generator: The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01647))_

```
// Generation
const fibonacci = () => {
let a, b;
console.log(a = 0);
console.log(b = 1);
while (true) {
[a, b] = [b, a + b];
console.log(b);
}
}
fibonacci()
//=>
0
1
1
2
3
5
8
13
21
34
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01646, source-range-0e12e052-01649))_

> Let's write a generator: The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01648))_

```text
while (true) {
[a, b] = [b, a + b];
console.log(b);
}
}
fibonacci()
//=>
0
1
1
2
3
5
8
13
21
34
Served by the Pot: Collections
206
55
89
144
...
The thing to note here is that our fibonacci generator has three states: generating 0, generating
1, and generating everything after that. This isn’t a good fit for an iterator, because iterators have
one functional entry point and therefore, we’d have to represent our three states explicitly, perhaps
using a state pattern90:
We’ll keep it simple:
// Iteration
let a, b, state = 0;
const fibonacci = () => {
switch (state) {
case 0:
state = 1;
return a = 0;
case 1:
state = 2;
return b = 1;
case 2:
[a, b] = [b, a + b];
return b
}
};
while (true) {
console.log(fibonacci());
}
//=>
0
1
1
2
3
5
8
13
90https://en.wikipedia.org/wiki/State_pattern
Served by the Pot: Collections
207
21
34
55
89
144
...
Again, this is not particularly horrendous, but like the recursive example, we’re explicitly greenspun-
ning the natural linear state. In a generator, we write “do this, then this, then this.” In an iterator,
we have to wrap that up and explicitly keep track of what step we’re on.
So we see the same thing: The generation version has state, but it’s implicit in JavaScript’s linear
control flow. Whereas the iteration version must make that state explicit.
javascript’s generators
It would be very nice if we could sometimes write iterators as a .next() method that gets called, and
sometimes write out a generator. Given the title of this chapter, it is not a surprise that JavaScript
makes this possible.
We can write an iterator, but use a generation style of programming. An iterator written in a
generation style is called a generator. To write a generator, we write a function, but we make two
changes:
1. We declare the function using the function * syntax. Not a fat arrow. Not a plain function.
2. We don’t return values or output them to console.log. We “yield” values using the yield
keyword.
When we invoke the function, we get an iterator object back. Let’s start with the degenerate example,
the empty iterator:91
function * empty () {};
empty().next()
//=>
{"done":true}
When we invoke empty, we get an iterator with no elements. This makes sense, because empty never
yields anything. We call its .next() method, but it’s done immediately.
Generator functions can take an argument. Let’s use that to illustrate yield:
91We wrote a generator declaration. We can also write const empty = function * () {} to bind an anonymous generator to the empty keyword,
but we don’t need to do that here.
Served by the Pot: Collections
208
function * only (something) {
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 34 | Served by the Pot: Collections |
| 144 | The thing to note here is that our fibonacci generator has three states: generating 0, generating 1, and generating everything after that. This isn’t a good fit for an iterator, because iterators have one functional entry point and therefore, we’d have to represent our three states explicitly, perhaps using a state pattern90: We’ll keep it simple: // Iteration let a, b, state = 0; const fibonacci = () => { switch (state) { case 0: state = 1; return a = 0; case 1: state = 2; return b = 1; case 2: [a, b] = [b, a + b]; return b while (true) { console.log(fibonacci()); |
| 13 | 90https://en.wikipedia.org/wiki/State_pattern |
| 207 | Served by the Pot: Collections |
| 144 | Again, this is not particularly horrendous, but like the recursive example, we’re explicitly greenspun- ning the natural linear state. In a generator, we write “do this, then this, then this.” In an iterator, we have to wrap that up and explicitly keep track of what step we’re on. So we see the same thing: The generation version has state, but it’s implicit in JavaScript’s linear control flow. Whereas the iteration version must make that state explicit. javascript’s generators It would be very nice if we could sometimes write iterators as a.next() method that gets called, and sometimes write out a generator. Given the title of this chapter, it is not a surprise that JavaScript makes this possible. We can write an iterator, but use a generation style of programming. An iterator written in a generation style is called a generator. To write a generator, we write a function, but we make two changes: |
| 1 | We declare the function using the function * syntax. Not a fat arrow. Not a plain function. |
| 2 | We don’t return values or output them to console.log. We “yield” values using the yield keyword. When we invoke the function, we get an iterator object back. Let’s start with the degenerate example, the empty iterator:91 function * empty () {}; empty().next() {"done":true} When we invoke empty, we get an iterator with no elements. This makes sense, because empty never yields anything. We call its.next() method, but it’s done immediately. 91We wrote a generator declaration. We can also write const empty = function * () {} to bind an anonymous generator to the empty keyword, but we don’t need to do that here. |
| 208 | Generator functions can take an argument. Let’s use that to illustrate yield: Served by the Pot: Collections function * only (something) { |

</details>

##### We'll keep it simple:

- In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. _(javascriptallonge.pdf (source-range-0e12e052-01654))_
- Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. _(javascriptallonge.pdf (source-range-0e12e052-01654))_
- In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. _(javascriptallonge.pdf (source-range-0e12e052-01654))_
- So we see the same thing: The generation version has state, but it's implicit in JavaScript's linear control flow. _(javascriptallonge.pdf (source-range-0e12e052-01655))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01651))_

```
// Iteration
let a, b, state = 0;
const fibonacci = () => {
switch (state) {
case 0:
state = 1;
return a = 0;
case 1:
state = 2;
return b = 1;
case 2:
[a, b] = [b, a + b];
return b
}
};
while (true) {
console.log(fibonacci());
}
//=>
0
1
1
2
3
5
8
13
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01653))_

```
21
34
55
89
144
...
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01655))_

> Whereas the iteration version must make that state explicit.

#### javascript's generators

- Given the title of this chapter, it is not a surprise that JavaScript makes this possible. _(javascriptallonge.pdf (source-range-0e12e052-01657))_
- It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator. _(javascriptallonge.pdf (source-range-0e12e052-01657))_
- An iterator written in a generation style is called a generator . _(javascriptallonge.pdf (source-range-0e12e052-01658))_
- We can write an iterator, but use a generation style of programming. _(javascriptallonge.pdf (source-range-0e12e052-01658))_
- An iterator written in a generation style is called a generator . _(javascriptallonge.pdf (source-range-0e12e052-01658))_
- This makes sense, because empty never yields anything. _(javascriptallonge.pdf (source-range-0e12e052-01663))_
- This makes sense, because empty never yields anything. _(javascriptallonge.pdf (source-range-0e12e052-01663))_
- Generator functions can take an argument. _(javascriptallonge.pdf (source-range-0e12e052-01664))_
- Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-0e12e052-01667))_
- Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . _(javascriptallonge.pdf (source-range-0e12e052-01667))_
- Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-0e12e052-01667))_
- Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . _(javascriptallonge.pdf (source-range-0e12e052-01667))_
- It yields the value of something , and then it's done. _(javascriptallonge.pdf (source-range-0e12e052-01671))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01660, source-range-0e12e052-01663))_

> We don't return values or output them to console.log . We 'yield' values using the yield keyword. When we invoke empty , we get an iterator with no elements. This makes sense, because empty never yields anything. We call its .next() method, but it's done immediately.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01662))_

```
function * empty () {};
empty().next()
//=>
{"done":true}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01660))_

> We don't return values or output them to console.log . We 'yield' values using the yield keyword.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01663))_

> When we invoke empty , we get an iterator with no elements.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01665))_

> 91 Wewrote a generator declaration . We can also write const empty = function * () {} to bind an anonymous generator to the empty keyword, but we don't need to do that here.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01666))_

```
function * only (something) {
yield something;
};
only("you").next()
//=>
{"done":false, value: "you"}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01667))_

> Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01668))_

```
only("you").next()
//=>
{"done":false, value: "you"}
only("the lonely").next()
//=>
{"done":false, value: "the lonely"}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01669))_

> We can invoke the same iterator twice:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01670))_

```
const sixteen = only("sixteen");
sixteen.next()
//=>
{"done":false, value: "sixteen"}
sixteen.next()
//=>
{"done":true}
```

#### generators are coroutines

- This is where generators behave very, very differently from ordinary functions. _(javascriptallonge.pdf (source-range-0e12e052-01675))_
- - The iterator is in a nascent or 'newborn' state. _(javascriptallonge.pdf (source-range-0e12e052-01677))_
- - When we call interator.next() , the body of our generator begins to be evaluated. _(javascriptallonge.pdf (source-range-0e12e052-01678))_
- - The body of our generator runs until it returns, ends, or encounters a yield statement, which is yield 1; . _(javascriptallonge.pdf (source-range-0e12e052-01679))_
- - The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-0e12e052-01682))_
- - The iterator resumes execution from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-0e12e052-01683))_
- - The body of our generator runs until it returns, ends, or encounters the next yield statement, which is yield 2; . _(javascriptallonge.pdf (source-range-0e12e052-01684))_
- - The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-0e12e052-01687))_
- - The iterator resumes execution from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-0e12e052-01688))_
- - The body of our generator runs until it returns, ends, or encounters the next yield statement, which is yield 3; . _(javascriptallonge.pdf (source-range-0e12e052-01689))_
- - The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-0e12e052-01692))_
- - The iterator resumes execution from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-0e12e052-01693))_
- There are no more lines of code, so it ends. _(javascriptallonge.pdf (source-range-0e12e052-01694))_
- - The body of our generator runs until it returns, ends, or encounters the next yield statement. _(javascriptallonge.pdf (source-range-0e12e052-01694))_
- Coroutines are well-suited for implementing more familiar program components such as cooperative tasks, exceptions, event loop, iterators, infinite lists and pipes. _(javascriptallonge.pdf (source-range-0e12e052-01697))_
- Coroutines are computer program components that generalize subroutines for nonpreemptive multitasking, by allowing multiple entry points for suspending and resuming execution at certain locations. _(javascriptallonge.pdf (source-range-0e12e052-01697))_
- Coroutines are well-suited for implementing more familiar program components such as cooperative tasks, exceptions, event loop, iterators, infinite lists and pipes. _(javascriptallonge.pdf (source-range-0e12e052-01697))_
- The iterator is the producer, and the code that iterates over it is the consumer. _(javascriptallonge.pdf (source-range-0e12e052-01698))_
- With an iterator, we can call them the producer and the consumer . _(javascriptallonge.pdf (source-range-0e12e052-01698))_
- Of course, generators need not be implemented exactly as coroutines. _(javascriptallonge.pdf (source-range-0e12e052-01700))_
- For example, a 'transpiler' might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we'll see that later): _(javascriptallonge.pdf (source-range-0e12e052-01700))_
- For example, a 'transpiler' might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we'll see that later): _(javascriptallonge.pdf (source-range-0e12e052-01700))_
- But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next() , it runs until it returns, ends, or yields. _(javascriptallonge.pdf (source-range-0e12e052-01702))_
- If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-0e12e052-01702))_
- If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-0e12e052-01702))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01673))_

> Here's a generator that yields three numbers:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01674))_

```
const oneTwoThree = function * () {
yield 1;
yield 2;
yield 3;
};
oneTwoThree().next()
//=>
{"done":false, value: 1}
oneTwoThree().next()
//=>
{"done":false, value: 1}
oneTwoThree().next()
//=>
{"done":false, value: 1}
const iterator = oneTwoThree();
iterator.next()
//=>
{"done":false, value: 1}
iterator.next()
//=>
{"done":false, value: 2}
iterator.next()
//=>
{"done":false, value: 3}
iterator.next()
//=>
{"done":true}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01700))_

> Of course, generators need not be implemented exactly as coroutines. For example, a 'transpiler' might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we'll see that later):

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01701))_

```
const oneTwoThree = function () {
let state = 'newborn';
return {
next () {
switch (state) {
case 'newborn':
state = 1;
return {value: 1};
case 1:
state = 2;
return {value: 2}
case 2:
state = 3;
return {value: 3}
case 3:
return {done: true};
}
}
}
};
```

#### generators and iterables

- Our generator function oneTwoThree is not an iterator. _(javascriptallonge.pdf (source-range-0e12e052-01704))_
- We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call. _(javascriptallonge.pdf (source-range-0e12e052-01704))_
- Recalling the way we wrote ordered collections, we could make a collection that uses a generator function: _(javascriptallonge.pdf (source-range-0e12e052-01705))_
- As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3 . _(javascriptallonge.pdf (source-range-0e12e052-01705))_
- This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects: _(javascriptallonge.pdf (source-range-0e12e052-01708))_
- Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-0e12e052-01710))_
- This object declares a [Symbol.iterator] function that makes it iterable. _(javascriptallonge.pdf (source-range-0e12e052-01710))_
- Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-0e12e052-01710))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01704))_

> Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01705))_

> If we call our generator function more than once, we get new iterators.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01705))_

> If we call our generator function more than once, we get new iterators. As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3 . Recalling the way we wrote ordered collections, we could make a collection that uses a generator function:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01706))_

```
const ThreeNumbers = {
[Symbol.iterator]: function * () {
yield 1;
yield 2;
yield 3
}
}
for (const i of ThreeNumbers) {
console.log(i);
}
//=>
1
2
3
[...ThreeNumbers]
//=>
[1,2,3]
const iterator = ThreeNumbers[Symbol.iterator]();
iterator.next()
//=>
{"done":false, value: 1}
iterator.next()
//=>
{"done":false, value: 2}
iterator.next()
//=>
{"done":false, value: 3}
iterator.next()
//=>
{"done":true}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01705))_

> If we call our generator function more than once, we get new iterators. As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3 . Recalling the way we wrote ordered collections, we could make a collection that uses a generator function:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01707))_

```text
yield 3
}
}
for (const i of ThreeNumbers) {
console.log(i);
}
//=>
1
2
3
[...ThreeNumbers]
//=>
[1,2,3]
const iterator = ThreeNumbers[Symbol.iterator]();
iterator.next()
//=>
{"done":false, value: 1}
iterator.next()
//=>
{"done":false, value: 2}
iterator.next()
//=>
{"done":false, value: 3}
iterator.next()
//=>
{"done":true}
Now we can use it in a for...of loop, spread it into an array literal, or spread it into a function
invocation, because we have written an iterable that uses a generator to return an iterator from its
[Symbol.iterator] method.
This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing
Served by the Pot: Collections
213
generator methods for objects:
const ThreeNumbers = {
*[Symbol.iterator] () {
yield 1;
yield 2;
yield 3
}
}
This object declares a [Symbol.iterator] function that makes it iterable. Because it’s declared
*[Symbol.iterator], it’s a generator instead of an iterator.
So to summarize, ThreeNumbers is an object that we’ve made iterable, by way of writing a generator
method for [Symbol.iterator].
more generators
Generators can produce infinite streams of values:
const Numbers = {
*[Symbol.iterator] () {
let i = 0;
while (true) {
yield i++;
}
}
};
for (const i of Numbers) {
console.log(i);
}
//=>
0
1
2
3
4
5
6
7
Served by the Pot: Collections
214
8
9
10
...
Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we
wrote Fibonacci using explicit state:
const Fibonacci = {
[Symbol.iterator]: () => {
let a = 0, b = 1, state = 0;
return {
next: () => {
switch (state) {
case 0:
state = 1;
return {value: a};
case 1:
state = 2;
return {value: b};
case 2:
[a, b] = [b, a + b];
return {value: b};
}
}
}
}
};
for (let n of Fibonacci) {
console.log(n)
}
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 3 | [...ThreeNumbers] [1,2,3] const iterator = ThreeNumbers[Symbol.iterator](); iterator.next() {"done":false, value: 1} iterator.next() {"done":false, value: 2} iterator.next() {"done":false, value: 3} iterator.next() {"done":true} Now we can use it in a for...of loop, spread it into an array literal, or spread it into a function invocation, because we have written an iterable that uses a generator to return an iterator from its [Symbol.iterator] method. This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing |
| 213 | Served by the Pot: Collections generator methods for objects: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 This object declares a [Symbol.iterator] function that makes it iterable. Because it’s declared *[Symbol.iterator], it’s a generator instead of an iterator. So to summarize, ThreeNumbers is an object that we’ve made iterable, by way of writing a generator method for [Symbol.iterator]. more generators Generators can produce infinite streams of values: const Numbers = { *[Symbol.iterator] () { let i = 0; while (true) { yield i++; for (const i of Numbers) { console.log(i); |
| 7 | Served by the Pot: Collections |
| 10 | Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state: const Fibonacci = { [Symbol.iterator]: () => { let a = 0, b = 1, state = 0; return { next: () => { switch (state) { case 0: state = 1; return {value: a}; case 1: state = 2; return {value: b}; case 2: [a, b] = [b, a + b]; return {value: b}; for (let n of Fibonacci) { console.log(n) |

</details>

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01708, source-range-0e12e052-01710))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects: This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01709))_

```
const ThreeNumbers = {
*[Symbol.iterator] () {
yield 1;
yield 2;
yield 3
}
}
```

#### more generators

- Our OneTwoThree example used implicit state to output the numbers in sequence. _(javascriptallonge.pdf (source-range-0e12e052-01716))_
- And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own. _(javascriptallonge.pdf (source-range-0e12e052-01721))_
- We've writing a function that returns an iterator, but we used a generator to do it. _(javascriptallonge.pdf (source-range-0e12e052-01721))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01713, source-range-0e12e052-01716))_

> Generators can produce infinite streams of values: Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01714))_

```
const Numbers = {
*[Symbol.iterator] () {
let i = 0;
while (true) {
yield i++;
}
}
};
for (const i of Numbers) {
console.log(i);
}
//=>
0
1
2
3
4
5
6
7
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01713, source-range-0e12e052-01716))_

> Generators can produce infinite streams of values: Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01715))_

```
8
9
10
...
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01716))_

> Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01717))_

```
const Fibonacci = {
[Symbol.iterator]: () => {
let a = 0, b = 1, state = 0;
return {
next: () => {
switch (state) {
case 0:
state = 1;
return {value: a};
case 1:
state = 2;
return {value: b};
case 2:
[a, b] = [b, a + b];
return {value: b};
}
}
}
}
};
for (let n of Fibonacci) {
console.log(n)
}
//=>
0
1
1
2
3
5
8
13
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01716))_

> Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01718))_

```
21
34
55
89
144
...
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01719))_

> And here is the Fibonacci ordered collection, implemented with a generator method:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01720))_

```
const Fibonacci = {
*[Symbol.iterator] () {
let a, b;
yield a = 0;
yield b = 1;
while (true) {
[a, b] = [b, a + b]
yield b;
}
}
}
for (const i of Fibonacci) {
console.log(i);
}
//=>
0
1
1
2
3
5
8
13
21
34
55
89
144
...
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01722))_

> Of course, we could just as easily write a generator function for Fibonacci numbers:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01723))_

```
function * fibonacci () {
let a, b;
yield a = 0;
yield b = 1;
while (true) {
[a, b] = [b, a + b]
yield b;
}
}
for (const i of fibonacci()) {
console.log(i);
}
//=>
0
1
1
2
3
5
8
13
21
34
55
89
144
...
```

#### yielding iterables

- It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93 _(javascriptallonge.pdf (source-range-0e12e052-01727))_
- 93 There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. _(javascriptallonge.pdf (source-range-0e12e052-01728))_
- 93 There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. _(javascriptallonge.pdf (source-range-0e12e052-01728))_
- If e is not an iterable, yield e . _(javascriptallonge.pdf (source-range-0e12e052-01731))_
- Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. _(javascriptallonge.pdf (source-range-0e12e052-01731))_
- Things like arrays can be easily catenated, but append iterates lazily, so there's no need to construct intermediary results. _(javascriptallonge.pdf (source-range-0e12e052-01736))_
- Tucked inside of it is the same three-line idiom for yielding each element of an iterable. _(javascriptallonge.pdf (source-range-0e12e052-01737))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01725, source-range-0e12e052-01728))_

> Here's a first crack at a function that returns an iterable object for iterating over trees: 93 There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. But if you can write it as a simple generator, write it as a simple generator.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01726))_

```
const isIterable = (something) =>
!!something[Symbol.iterator];
const TreeIterable = (iterable) =>
({
[Symbol.iterator]: function * () {
for (const e of iterable) {
if (isIterable(e)) {
for (const ee of TreeIterable(e)) {
yield ee;
}
}
else {
yield e;
}
}
}
})
for (const i of TreeIterable([1, [2, [3, 4], 5]])) {
console.log(i);
}
//=>
1
2
3
4
5
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01725))_

> Here's a first crack at a function that returns an iterable object for iterating over trees:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01728))_

> But if you can write it as a simple generator, write it as a simple generator.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01728))_

> 93 There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. But if you can write it as a simple generator, write it as a simple generator.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01729))_

```
function * tree (iterable) {
for (const e of iterable) {
if (isIterable(e)) {
for (const ee of tree(e)) {
yield ee;
}
}
else {
yield e;
}
}
};
for (const i of tree([1, [2, [3, 4], 5]])) {
console.log(i);
}
//=>
1
2
3
4
5
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01732))_

> But while we're here, let's look at one bit of this code:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01733))_

```
for (const ee of tree(e)) {
yield ee;
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01734))_

> These three lines say, in essence, 'yield all the elements of TreeIterable(e) , in order. ' This comes up quite often when we have collections that are compounds, collections made from other collections. Consider this operation on iterables:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01735))_

```
function * append (...iterables) {
for (const iterable of iterables) {
for (const element of iterable) {
yield element;
}
}
}
const lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\
"]);
for (const word of lyrics) {
console.log(word);
}
//=>
a
b
c
one
two
three
do
re
me
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01737))_

> Tucked inside of it is the same three-line idiom for yielding each element of an iterable. There is an abbreviation for this, we can use yield * to yield all the elements of an iterable:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01738))_

```
function * append (...iterables) {
for (const iterable of iterables) {
yield * iterable;
}
}
const lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\
"]);
for (const word of lyrics) {
console.log(word);
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01737))_

> Tucked inside of it is the same three-line idiom for yielding each element of an iterable. There is an abbreviation for this, we can use yield * to yield all the elements of an iterable:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01739))_

```
//=>
a
b
c
one
two
thre
do
re
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01737))_

> Tucked inside of it is the same three-line idiom for yielding each element of an iterable. There is an abbreviation for this, we can use yield * to yield all the elements of an iterable:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01740))_

```
const isIterable = (something) =>
!!something[Symbol.iterator];
function * tree (iterable) {
for (const e of iterable) {
if (isIterable(e)) {
yield * tree(e);
}
else {
yield e;
}
}
};
for (const i of tree([1, [2, [3, 4
console.log(i);
}
//=>
1
2
3
4
5
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01741))_

```
three
do
re
me
yield * yields all of the elements of an iterable, in order. We can use it in tree, too:
const isIterable = (something) =>
!!something[Symbol.iterator];
function * tree (iterable) {
for (const e of iterable) {
if (isIterable(e)) {
yield * tree(e);
}
else {
yield e;
}
}
};
for (const i of tree([1, [2, [3, 4], 5]])) {
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01742))_

```text
else {
yield e;
}
}
};
for (const i of tree([1, [2, [3, 4], 5]])) {
console.log(i);
}
//=>
1
2
3
4
5
yield* is handy when writing generator functions that operate on or create iterables.
rewriting iterable operations
Now that we know about iterables, we can rewrite our iterable operations as generators. Instead of:
Served by the Pot: Collections
221
const mapWith = (fn, iterable) =>
({
[Symbol.iterator]: () => {
const iterator = iterable[Symbol.iterator]();
return {
next: () => {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : fn(value)});
}
}
}
});
We can write:
function * mapWith (fn, iterable) {
for (const element of iterable) {
yield fn(element);
}
}
No need to explicitly construct an object that has a [Symbol.iterator] method. No need to return
an object with a .next() method. No need to fool around with {done} or {value}, just yield values
until we’re done.
We can do the same thing with our other operations like filterWith and untilWith. Here’re our
iterable methods rewritten as generators:
function * mapWith(fn, iterable) {
for (const element of iterable) {
yield fn(element);
}
}
function * filterWith (fn, iterable) {
for (const element of iterable) {
if (!!fn(element)) yield element;
}
}
Served by the Pot: Collections
222
function * untilWith (fn, iterable) {
for (const element of iterable) {
if (fn(element)) break;
yield fn(element);
}
}
first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
function * rest (iterable) {
const iterator = iterable[Symbol.iterator]();
iterator.next();
yield * iterator;
}
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 5 | yield* is handy when writing generator functions that operate on or create iterables. rewriting iterable operations Now that we know about iterables, we can rewrite our iterable operations as generators. Instead of: |
| 221 | Served by the Pot: Collections const mapWith = (fn, iterable) => [Symbol.iterator]: () => { const iterator = iterable[Symbol.iterator](); return { next: () => { const {done, value} = iterator.next(); return ({done, value: done? undefined: fn(value)}); We can write: function * mapWith (fn, iterable) { for (const element of iterable) { yield fn(element); No need to explicitly construct an object that has a [Symbol.iterator] method. No need to return an object with a.next() method. No need to fool around with {done} or {value}, just yield values until we’re done. We can do the same thing with our other operations like filterWith and untilWith. Here’re our iterable methods rewritten as generators: function * mapWith(fn, iterable) { for (const element of iterable) { yield fn(element); function * filterWith (fn, iterable) { for (const element of iterable) { if (!!fn(element)) yield element; |
| 222 | Served by the Pot: Collections function * untilWith (fn, iterable) { for (const element of iterable) { if (fn(element)) break; yield fn(element); first works directly with iterators and remains unchanged, but rest can be rewritten as a generator: const first = (iterable) => iterable[Symbol.iterator]().next().value; function * rest (iterable) { const iterator = iterable[Symbol.iterator](); iterator.next(); yield * iterator; |

</details>

### rewriting iterable operations

- Now that we know about iterables, we can rewrite our iterable operations as generators. _(javascriptallonge.pdf (source-range-0e12e052-01744))_
- No need to return an object with a .next() method. _(javascriptallonge.pdf (source-range-0e12e052-01748))_
- No need to explicitly construct an object that has a [Symbol.iterator] method. _(javascriptallonge.pdf (source-range-0e12e052-01748))_
- We can do the same thing with our other operations like filterWith and untilWith . _(javascriptallonge.pdf (source-range-0e12e052-01749))_
- first works directly with iterators and remains unchanged, but rest can be rewritten as a generator: _(javascriptallonge.pdf (source-range-0e12e052-01752))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01744))_

> Now that we know about iterables, we can rewrite our iterable operations as generators. Instead of:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01745))_

```
const mapWith = (fn, iterable) =>
({
[Symbol.iterator]: () => {
const iterator = iterable[Symbol.iterator]();
return {
next: () => {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : fn(value)});
}
}
}
});
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01746))_

> We can write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01747))_

```
function * mapWith (fn, iterable) {
for (const element of iterable) {
yield fn(element);
}
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01749))_

> We can do the same thing with our other operations like filterWith and untilWith . Here're our iterable methods rewritten as generators:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01750))_

```
function * mapWith(fn, iterable) {
for (const element of iterable) {
yield fn(element);
}
}
function * filterWith (fn, iterable) {
for (const element of iterable) {
if (!!fn(element)) yield element;
}
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01749))_

> We can do the same thing with our other operations like filterWith and untilWith . Here're our iterable methods rewritten as generators:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01751))_

```
function * untilWith (fn, iterable) {
for (const element of iterable) {
if (fn(element)) break;
yield fn(element);
}
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01752))_

> first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01753))_

```
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
function * rest (iterable) {
const iterator = iterable[Symbol.iterator]();
iterator.next();
yield * iterator;
}
```

### Summary

- And we don't need to worry about wrapping our values in an object with .done and .value properties. _(javascriptallonge.pdf (source-range-0e12e052-01755))_
- Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns. _(javascriptallonge.pdf (source-range-0e12e052-01755))_
- A generator is a function that is defined with function * and uses yield (or yield * ) to generate values. _(javascriptallonge.pdf (source-range-0e12e052-01755))_
- This is especially useful for making iterables. _(javascriptallonge.pdf (source-range-0e12e052-01756))_

## Lazy and Eager Collections

- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack _(javascriptallonge.pdf (source-range-0e12e052-01759))_
- If we wanted to flatten collections to arrays, we wrote a .toArray method for each type of collection. _(javascriptallonge.pdf (source-range-0e12e052-01760))_
- in the older style of object-oriented programming, we built 'fat' objects. _(javascriptallonge.pdf (source-range-0e12e052-01760))_
- Each collection knew how to map itself ( .map ), how to fold itself ( .reduce ), how to filter itself ( .filter ) and how to find one element within itself ( .find ). _(javascriptallonge.pdf (source-range-0e12e052-01760))_
- We tell ourselves that, well, a collection ought to know how to map itself. _(javascriptallonge.pdf (source-range-0e12e052-01761))_
- Some methods are only added to a few collections, some are added to all. _(javascriptallonge.pdf (source-range-0e12e052-01761))_
- Some methods are only added to a few collections, some are added to all. _(javascriptallonge.pdf (source-range-0e12e052-01761))_
- But we end up recreating the same bits of code in each .map method we create, in each .reduce method we create, in each .filter method we create, and in each .find method. _(javascriptallonge.pdf (source-range-0e12e052-01762))_
- That's a sign that we should work at a higher level of abstraction, and working with iterables is that higher level of abstraction. _(javascriptallonge.pdf (source-range-0e12e052-01762))_
- Each one has its own variation, but the overall form is identical. _(javascriptallonge.pdf (source-range-0e12e052-01762))_
- This 'fat object' style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don't need for the collection to handle every single detail. _(javascriptallonge.pdf (source-range-0e12e052-01763))_
- That would be like saying that when we ask a bank teller for some cash, they personally print every bank note. _(javascriptallonge.pdf (source-range-0e12e052-01763))_

### implementing methods with iteration

- Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. _(javascriptallonge.pdf (source-range-0e12e052-01765))_
- And they should know how to accomplish the desired result, but they should do so by delegating as much of the work as possible to operations like mapWith . _(javascriptallonge.pdf (source-range-0e12e052-01765))_
- And if we want to create convenience methods, we can reuse common pieces. _(javascriptallonge.pdf (source-range-0e12e052-01766))_
- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack. _(javascriptallonge.pdf (source-range-0e12e052-01766))_
- For simplicity, we'll show how to mix it into Numbers and Pair . _(javascriptallonge.pdf (source-range-0e12e052-01772))_
- To use LazyCollection , we mix it into an any iterable object. _(javascriptallonge.pdf (source-range-0e12e052-01772))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01767))_

> Here is LazyCollection , a mixin we can use with any ordered collection that is also an iterable:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01768))_

```
const extend = function (consumer, ...providers) {
for (let i = 0; i < providers.length; ++i) {
const provider = providers[i];
for (let key in provider) {
if (provider.hasOwnProperty(key)) {
consumer[key] = provider[key]
}
}
}
return consumer
};
const LazyCollection = {
map(fn) {
return Object.assign({
[Symbol.iterator]: () => {
const iterator = this[Symbol.iterator]();
return {
next: () => {
const {
done, value
} = iterator.next();
return ({
done, value: done ? undefined : fn(value)
});
}
}
}
}, LazyCollection);
},
reduce(fn, seed) {
const iterator = this[Symbol.iterator]();
let iterationResult,
accumulator = seed;
while ((iterationResult = iterator.next(), !iterationResult.done)) {
accumulator = fn(accumulator, iterationResult.value);
}
return accumulator;
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01767))_

> Here is LazyCollection , a mixin we can use with any ordered collection that is also an iterable:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01769))_

```
},
filter(fn) {
return Object.assign({
[Symbol.iterator]: () => {
const iterator = this[Symbol.iterator]();
return {
next: () => {
do {
const {
done, value
} = iterator.next();
} while (!done && !fn(value));
return {
done, value
};
}
}
}
}, LazyCollection)
},
find(fn) {
return Object.assign({
[Symbol.iterator]: () => {
const iterator = this[Symbol.iterator]();
return {
next: () => {
let {
done, value
} = iterator.next();
done = done || fn(value);
return ({
done, value: done ? undefined : value
});
}
}
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01767))_

> Here is LazyCollection , a mixin we can use with any ordered collection that is also an iterable:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01770))_

```
}, LazyCollection)
},
until(fn) {
return Object.assign({
[Symbol.iterator]: () => {
const iterator = this[Symbol.iterator]();
return {
next: () => {
let {
done, value
} = iterator.next();
done = done || fn(value);
return ({
done, value: done ? undefined : value
});
}
}
}
}, LazyCollection)
},
first() {
return this[Symbol.iterator]().next().value;
},
rest() {
return Object.assign({
[Symbol.iterator]: () => {
const iterator = this[Symbol.iterator]();
iterator.next();
return iterator;
}
}, LazyCollection);
},
take(numberToTake) {
return Object.assign({
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01771))_

```
[Symbol.iterator]: () => {
const iterator = this[Symbol.iterator]();
let remainingElements = numberToTake;
return {
next: () => {
let {
done, value
} = iterator.next();
done = done || remainingElements-- <= 0;
return ({
done, value: done ? undefined : value
});
}
}
}
}, LazyCollection);
}
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01772))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01773))_

```
const Numbers = Object.assign({
[Symbol.iterator]: () => {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
}, LazyCollection);
// Pair, a/k/a linked lists
const EMPTY = {
isEmpty: () => true
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01772))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01774))_

```
};
const isEmpty = (node) => node === EMPTY;
const Pair = (car, cdr = EMPTY) =>
Object.assign({
car,
cdr,
isEmpty: () => false,
[Symbol.iterator]: function () {
let currentPair = this;
return {
next: () => {
if (currentPair.isEmpty()) {
return {done: true}
}
else {
const value = currentPair.car;
currentPair = currentPair.cdr;
return {done: false, value}
}
}
}
}
}, LazyCollection);
Pair.from = (iterable) =>
(function iterationToList (iteration) {
const {done, value} = iteration.next();
return done ? EMPTY : Pair(value, iterationToList(iteration));
})(iterable[Symbol.iterator]());
// Stack
const Stack = () =>
Object.assign({
array: [],
index: -1,
push: function (value) {
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01772))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01775))_

```
return this.array[this.index += 1] = value;
},
pop: function () {
const value = this.array[this.index];
this.array[this.index] = undefined;
if (this.index >= 0) {
this.index -= 1
}
return value
},
isEmpty: function () {
return this.index < 0
},
[Symbol.iterator]: function () {
let iterationIndex = this.index;
return {
next: () => {
if (iterationIndex > this.index) {
iterationIndex = this.index;
}
if (iterationIndex < 0) {
return {done: true};
}
else {
return {done: false, value: this.array[iterationIndex--]}
}
}
}
}
}, LazyCollection);
Stack.from = function (iterable) {
const stack = this();
for (let element of iterable) {
stack.push(element);
}
return stack;
}
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01776))_

```
// Pair and Stack in action
Stack.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.first()
//=> 100
Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.reduce((seed, element) => seed + element, 0)
```

### lazy collection operations

- But it can be an excellent strategy for efficiency in algorithms. _(javascriptallonge.pdf (source-range-0e12e052-01779))_
- And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. _(javascriptallonge.pdf (source-range-0e12e052-01782))_
- And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. _(javascriptallonge.pdf (source-range-0e12e052-01782))_
- Thus, calling .map.filter.reduce produces two temporary arrays that are discarded when .reduce performs its final computation. _(javascriptallonge.pdf (source-range-0e12e052-01783))_
- Thus, calling .map.filter.reduce produces two temporary arrays that are discarded when .reduce performs its final computation. _(javascriptallonge.pdf (source-range-0e12e052-01783))_
- They produce small iterable objects that refer back to the original iteration. _(javascriptallonge.pdf (source-range-0e12e052-01784))_
- Whereas the .map and .filter methods on Pair work with iterators. _(javascriptallonge.pdf (source-range-0e12e052-01784))_
- It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. _(javascriptallonge.pdf (source-range-0e12e052-01787))_
- Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array. _(javascriptallonge.pdf (source-range-0e12e052-01787))_
- This expression begins with a stack containing 30 elements. _(javascriptallonge.pdf (source-range-0e12e052-01787))_
- Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack's elements, and it only needs to square two of those elements, 29 and 28 , to return the answer. _(javascriptallonge.pdf (source-range-0e12e052-01788))_
- Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack's elements, and it only needs to square two of those elements, 29 and 28 , to return the answer. _(javascriptallonge.pdf (source-range-0e12e052-01788))_
- This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections. _(javascriptallonge.pdf (source-range-0e12e052-01796))_
- If we mutate a collection after taking an iterable, we might get an unexpected result. _(javascriptallonge.pdf (source-range-0e12e052-01796))_
- If we mutate a collection after taking an iterable, we might get an unexpected result. _(javascriptallonge.pdf (source-range-0e12e052-01796))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01780, source-range-0e12e052-01782))_

> Here's an example. Compare these two: Both expressions evaluate to 220 . And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01781))_

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.reduce((seed, element) => seed + element, 0)
Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.reduce((seed, element) => seed + element, 0)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01782))_

> Both expressions evaluate to 220 . And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01784))_

> When working with very large collections and many operations, this can be important.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01782))_

> Both expressions evaluate to 220 . And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01785))_

> The effect is even more pronounced when we use methods like first , until , or take :

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01785, source-range-0e12e052-01788))_

> The effect is even more pronounced when we use methods like first , until , or take : Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack's elements, and it only needs to square two of those elements, 29 and 28 , to return the answer.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01786))_

```
Stack.from([ 0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.first()
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01789))_

> We can confirm this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01790))_

```
Stack.from([ 0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
.map((x) => {
console.log(`squaring ${x}`);
return x * x
})
.filter((x) => {
console.log(`filtering ${x}`);
return x % 2 == 0
})
.first()
//=>
squaring 29
filtering 841
squaring 28
filtering 784
784
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01789))_

> We can confirm this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01791))_

> If we write the almost identical thing with an array, we get a different behaviour:

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01791))_

> If we write the almost identical thing with an array, we get a different behaviour:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01792))_

```
[ 0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
.reverse()
.map((x) => {
console.log(`squaring ${x}`);
return x * x
})
.filter((x) => {
console.log(`filtering ${x}`);
return x % 2 == 0
})[0]
//=>
squaring 0
squaring 1
squaring 2
squaring 3
...
squaring 28
squaring 29
filtering 0
filtering 1
filtering 4
...
filtering 784
filtering 841
784
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01794, source-range-0e12e052-01796))_

> You recall we briefly touched on the idea of infinite collections? Let's make iterable numbers. They have to be lazy, otherwise we couldn't write things like: Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of im

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01795))_

```
const Numbers = Object.assign({
[Symbol.iterator]: () => {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
}, LazyCollection);
const firstCubeOver1234 =
Numbers
.map((x) => x * x * x)
.filter((x) => x > 1234)
.first()
//=> 1331
```

### eager collections

- We can make an eager collection out of any collection that is gatherable , meaning it has a .from method: _(javascriptallonge.pdf (source-range-0e12e052-01798))_
- We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs: _(javascriptallonge.pdf (source-range-0e12e052-01802))_
- Here is our Pair implementation. _(javascriptallonge.pdf (source-range-0e12e052-01802))_
- Pair is gatherable, because it implements .from() . _(javascriptallonge.pdf (source-range-0e12e052-01802))_
- Pair is gatherable, because it implements .from() . _(javascriptallonge.pdf (source-range-0e12e052-01802))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01798))_

> An eager collection, like an array, returns a collection of its own type from each of the methods. We can make an eager collection out of any collection that is gatherable , meaning it has a .from method:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01799))_

```
const extend = function (consumer, ...providers) {
for (let i = 0; i < providers.length; ++i) {
const provider = providers[i];
for (let key in provider) {
if (provider.hasOwnProperty(key)) {
consumer[key] = provider[key]
}
}
}
return consumer
};
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01798, source-range-0e12e052-01802))_

> An eager collection, like an array, returns a collection of its own type from each of the methods. We can make an eager collection out of any collection that is gatherable , meaning it has a .from method: Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01800))_

```
const EagerCollection = (gatherable) =>
({
map(fn) {
const
original = this;
return gatherable.from(
(function* () {
for (let element of original) {
yield fn(element);
}
})()
);
},
reduce(fn, seed) {
let accumulator = seed;
for(let element of this) {
accumulator = fn(accumulator, element);
}
return accumulator;
},
filter(fn) {
const original = this;
return gatherable.from(
(function* () {
for (let element of original) {
if (fn(element)) yield element;
}
})()
);
},
find(fn) {
for (let element of this) {
if (fn(element)) return element;
}
},
until(fn) {
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01798, source-range-0e12e052-01802))_

> An eager collection, like an array, returns a collection of its own type from each of the methods. We can make an eager collection out of any collection that is gatherable , meaning it has a .from method: Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01801))_

```
const original = this;
return gatherable.from(
(function* () {
for (let element of original) {
if (fn(element)) break;
yield element;
}
})()
);
},
first() {
return this[Symbol.iterator]().next().value;
},
rest() {
const iteration = this[Symbol.iterator]();
iteration.next();
return gatherable.from(
(function* () {
yield * iteration;
})()
);
return gatherable.from(iterable);
},
take(numberToTake) {
const original = this;
let numberRemaining = numberToTake;
return gatherable.from(
(function* () {
for (let element of original) {
if (numberRemaining-- <= 0) break;
yield element;
}
})()
);
}
});
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01802))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01803))_

```
const EMPTY = {
isEmpty: () => true
};
const isEmpty = (node) => node === EMPTY;
const Pair = (car, cdr = EMPTY) =>
Object.assign({
car,
cdr,
isEmpty: () => false,
[Symbol.iterator]: function () {
let currentPair = this;
return {
next: () => {
if (currentPair.isEmpty()) {
return {done: true}
}
else {
const value = currentPair.car;
currentPair = currentPair.cdr;
return {done: false, value}
}
}
}
}
}, EagerCollection(Pair));
Pair.from = (iterable) =>
(function iterationToList (iteration) {
const {done, value} = iteration.next();
return done ? EMPTY : Pair(value, iterationToList(iteration));
})(iterable[Symbol.iterator]());
Pair.from([1, 2, 3, 4, 5]).map(x => x * 2)
//=>
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01802))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01804))_

```
{"car": 2,
"cdr": {"car": 4,
"cdr": {"car": 6,
"cdr": {"car": 8,
"cdr": {"car": 10,
"cdr": {}
}
}
}
}
}
```

## Interlude: The Carpenter Interviews for a Job

### the problem

- Despite his experience and industry longevity, the Carpenter did not mind being asked to demonstrate that he was, in fact, the person described on the resumé. _(javascriptallonge.pdf (source-range-0e12e052-01809))_
- After some small talk, Christine explained that they liked to ask candidates to whiteboard some code. _(javascriptallonge.pdf (source-range-0e12e052-01809))_
- After some small talk, Christine explained that they liked to ask candidates to whiteboard some code. _(javascriptallonge.pdf (source-range-0e12e052-01809))_
- Many companies use white-boarding code as an excuse to have a technical conversation with a candidate, and The Carpenter felt that being asked to whiteboard code was an excuse to have a technical conversation with a future colleague. _(javascriptallonge.pdf (source-range-0e12e052-01810))_
- Each move consists of moving the chequer one square in the direction of the arrow in the square it occupies. _(javascriptallonge.pdf (source-range-0e12e052-01814))_
- A chequer is placed randomly on the checkerboard. _(javascriptallonge.pdf (source-range-0e12e052-01814))_
- The problem is this: The game board is hidden from us. _(javascriptallonge.pdf (source-range-0e12e052-01815))_
- Your code should not presume anything about the game-board's size or contents, only that it is given an arrow every time though the while loop. _(javascriptallonge.pdf (source-range-0e12e052-01817))_
- Your code should not presume anything about the game-board's size or contents, only that it is given an arrow every time though the while loop. _(javascriptallonge.pdf (source-range-0e12e052-01817))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01810))_

> Many companies use white-boarding code as an excuse to have a technical conversation with a candidate, and The Carpenter felt that being asked to whiteboard code was an excuse to have a technical conversation with a future colleague. 'Win, win' he thought to himself.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01812))_

> [Figure] (p.262)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01813))_

> Christine intoned the question, as if by rote:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01814))_

> If the arrow should cause the chequer to move off the edge of the board, the game halts.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01815))_

> The problem is this: The game board is hidden from us. A player moves the chequer, following the rules. As the player moves the chequer, they calls out the direction of movement, e.g. '↑, →, ↑, ↓, ↑, →…' Write an algorithm that will determine whether the game halts, strictly from the called out directions, in finite time and space.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01817))_

> You may use babeljs.io 95 , or ES6Fiddle 96 to check your work.

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01819))_

> Christine quickly scribbled on the whiteboard:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01820))_

```
const Game = (size = 8) => {
// initialize the board
const board = [];
for (let i = 0; i < size; ++i) {
board[i] = [];
for (let j = 0; j < size; ++j) {
board[i][j] = '￿￿￿￿'[Math.floor(Math.random() * 4)];
}
}
// initialize the position
let initialPosition = [
2 + Math.floor(Math.random() * (size - 4)),
2 + Math.floor(Math.random() * (size - 4))
];
// ???
let [x, y] = initialPosition;
const MOVE = {
"￿": ([x, y]) => [x - 1, y],
"￿": ([x, y]) => [x + 1, y],
"￿": ([x, y]) => [x, y - 1],
"￿": ([x, y]) => [x, y + 1]
};
while (x >= 0 && y >=0 && x < size && y < size) {
const arrow = board[x][y];
// ???
[x, y] = MOVE[arrow]([x, y]);
}
// ???
};
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01819))_

> Christine quickly scribbled on the whiteboard:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01821))_

```text
95 http://babeljs.io
96 http://www.es6fiddle.net
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 95 | http://babeljs.io |
| 96 | http://www.es6fiddle.net |

</details>

### the carpenter's solution

- He then coached subsequent candidates to give polished answers to the company's pet technical questions. _(javascriptallonge.pdf (source-range-0e12e052-01824))_
- The Carpenter was not surprised at the problem. _(javascriptallonge.pdf (source-range-0e12e052-01824))_
- He then coached subsequent candidates to give polished answers to the company's pet technical questions. _(javascriptallonge.pdf (source-range-0e12e052-01824))_
- Bob had, in fact, warned The Carpenter that 'Thing' liked to ask either or both of two questions: Determine how to detect a loop in a linked list, and determine whether the chequerboard game would halt. _(javascriptallonge.pdf (source-range-0e12e052-01826))_
- To save time, The Carpenter had prepared the same answer for both questions. _(javascriptallonge.pdf (source-range-0e12e052-01826))_
- The Carpenter coughed softly, then began. _(javascriptallonge.pdf (source-range-0e12e052-01827))_
- I'll refactor a touch to make things clearer, for example I'll extract the board to make it easier to test:' _(javascriptallonge.pdf (source-range-0e12e052-01827))_
- The Carpenter coughed softly, then began. _(javascriptallonge.pdf (source-range-0e12e052-01827))_
- I'll refactor a touch to make things clearer, for example I'll extract the board to make it easier to test:' _(javascriptallonge.pdf (source-range-0e12e052-01827))_
- A statefulMap is a lazy map that preserves state from iteration to iteration. _(javascriptallonge.pdf (source-range-0e12e052-01830))_
- That's what we need, because we need to know the current position to map each move to the next position.' _(javascriptallonge.pdf (source-range-0e12e052-01830))_
- That's what we need, because we need to know the current position to map each move to the next position.' _(javascriptallonge.pdf (source-range-0e12e052-01830))_
- Detecting whether the game terminates is equivalent to detecting whether the graph contains a cycle.' _(javascriptallonge.pdf (source-range-0e12e052-01837))_
- I approached this question in that spirit. _(javascriptallonge.pdf (source-range-0e12e052-01840))_
- The question was, Given a linked list, detect whether it contains a cycle. _(javascriptallonge.pdf (source-range-0e12e052-01842))_
- I have never forgotten the question, or the general form of the solution. _(javascriptallonge.pdf (source-range-0e12e052-01842))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01827, source-range-0e12e052-01830))_

> The Carpenter coughed softly, then began. 'To begin with, I'll transform a game into an iterable that generates arrows, using the 'Starman' notation for generators. I'll refactor a touch to make things clearer, for example I'll extract the board to make it easier to test:' 'Now that we have an iterable, we can transform the iterable of arrows into an iterable of positions.' The Carpenter sketched quickly. 'We want to take the arrows and convert them to positions. For that, we'll map the Game ite

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01828))_

```
const MOVE = {
"￿": ([x, y]) => [x - 1, y],
"￿": ([x, y]) => [x + 1, y],
"￿": ([x, y]) => [x, y + 1],
"￿": ([x, y]) => [x, y - 1]
};
const Board = (size = 8) => {
// initialize the board
const board = [];
for (let i = 0; i < size; ++i) {
board[i] = [];
for (let j = 0; j < size; ++j) {
board[i][j] = '￿￿￿￿'[Math.floor(Math.random() * 4)];
}
}
// initialize the position
const position = [
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01827, source-range-0e12e052-01830))_

> The Carpenter coughed softly, then began. 'To begin with, I'll transform a game into an iterable that generates arrows, using the 'Starman' notation for generators. I'll refactor a touch to make things clearer, for example I'll extract the board to make it easier to test:' 'Now that we have an iterable, we can transform the iterable of arrows into an iterable of positions.' The Carpenter sketched quickly. 'We want to take the arrows and convert them to positions. For that, we'll map the Game ite

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01829))_

```
Math.floor(Math.random() * size),
Math.floor(Math.random() * size)
];
return {board, position};
};
const Game = ({board, position}) => {
const size = board[0].length;
return ({
*[Symbol.iterator] () {
let [x, y] = position;
while (x >= 0 && y >=0 && x < size && y < size) {
const direction = board[y][x];
yield direction;
[x, y] = MOVE[direction]([x, y]);
}
}
});
};
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01831))_

> 'This is a standard idiom we can obtain from libraries, we don't reinvent the wheel. I'll show it here for clarity:'

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01832))_

```
const statefulMapWith = (fn, seed, iterable) =>
({
*[Symbol.iterator] () {
let value,
state = seed;
for (let element of iterable) {
[state, value] = fn(state, element);
yield value;
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01831))_

> 'This is a standard idiom we can obtain from libraries, we don't reinvent the wheel. I'll show it here for clarity:'

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01833))_

```
}
}
});
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01835))_

```
const positionsOf = (game) =>
statefulMapWith(
(position, direction) => {
const [x, y] =
MOVE[direction](position);
position = [x, y];
return [position, `x: ${x}, y: ${y}`];
},
[0, 0],
game);
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01836))_

> The Carpenter reflected. 'Having turned our game loop into an iterable, we can now see that our problem of whether the game terminates is isomorphic to the problem of detecting whether the positions given ever repeat themselves: If the chequer ever returns to a position it has previously visited, it will cycle endlessly. '

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01838))_

> [Figure] (p.267)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01840))_

> 'There's an old joke that a mathematician is someone who will take a five-minute problem, then spend an hour proving it is equivalent to another problem they have already solved. I approached this question in that spirit. Now that we have created an iterable of values that can be compared with === , I can show you this function:'

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01841))_

```
const tortoiseAndHare = (iterable) => {
const hare = iterable[Symbol.iterator]();
let hareResult = (hare.next(), hare.next());
for (let tortoiseValue of iterable) {
hareResult = hare.next();
if (hareResult.done) {
return false;
}
if (tortoiseValue === hareResult.value) {
return true;
}
hareResult = hare.next();
if (hareResult.done) {
return false;
}
if (tortoiseValue === hareResult.value) {
return true;
}
}
return false;
};
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01846))_

```
const terminates = (game) =>
tortoiseAndHare(positionsOf(game))
const test = [
["￿","￿","￿","￿"],
["￿","￿","￿","￿"],
["￿","￿","￿","￿"],
["￿","￿","￿","￿"]
];
terminates(Game({board: test, position: [0, 0]}))
//=> false
terminates(Game({board: test, position: [3, 0]}))
//=> true
terminates(Game({board: test, position: [0, 3]}))
//=> false
terminates(Game({board: test, position: [3, 3]}))
//=> false
```

### the aftermath

- This type of solution provided an excellent opportunity to explore lazy versus eager evaluation, the performance of iterators versus native iteration, single responsibility design, and many other rich topics. _(javascriptallonge.pdf (source-range-0e12e052-01849))_
- The Carpenter sat down and waited. _(javascriptallonge.pdf (source-range-0e12e052-01849))_
- The Carpenter was confident that although nobody would write this exact code in production, prospective employers would also recognize that nobody would try to detect whether a chequer game terminates in production, either. _(javascriptallonge.pdf (source-range-0e12e052-01850))_
- Christine looked at the solution on the board, frowned, and glanced at the clock on the wall. _(javascriptallonge.pdf (source-range-0e12e052-01851))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01857))_

> [Figure] (p.270)

### after another drink

- A few drinks later, The Carpenter was telling his Thing story and an engineer named Kidu introduced themself. _(javascriptallonge.pdf (source-range-0e12e052-01859))_
- I had a look at the code you left on the whiteboard. _(javascriptallonge.pdf (source-range-0e12e052-01861))_
- Whereas the problem as stated involves a single stream of directions. _(javascriptallonge.pdf (source-range-0e12e052-01862))_
- Whereas the problem as stated involves a single stream of directions. _(javascriptallonge.pdf (source-range-0e12e052-01862))_
- There's no benefit to constant space if finite space is sufficient. _(javascriptallonge.pdf (source-range-0e12e052-01865))_
- The Carpenter stared at Kidu's solution. _(javascriptallonge.pdf (source-range-0e12e052-01867))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01864))_

```
// implements Teleporting Tortoise
// cycle detection algorithm.
const hasCycle = (iterable) => {
let iterator = iterable[Symbol.iterator](),
teleportDistance = 1;
while (true) {
let {value, done} = iterator.next(),
tortoise = value;
if (done) return false;
for (let i = 0; i < teleportDistance; ++i) {
let {value, done} = iterator.next(),
hare = value;
if (done) return false;
if (tortoise === hare) return true;
}
teleportDistance *= 2;
}
return false;
};
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01866))_

```
const hasCycle = (orderedCollection) => {
const visited = new Set();
for (let element of orderedCollection) {
if (visited.has(element)) {
return true;
}
visited.add(element);
}
return false;
};
```

## Interactive Generators

- We saw how to use them for recursive unfolds and state machines. _(javascriptallonge.pdf (source-range-0e12e052-01869))_
- But there are other times we want to build functions that maintain implicit state. _(javascriptallonge.pdf (source-range-0e12e052-01869))_
- We used generators to build iterators that maintain implicit state. _(javascriptallonge.pdf (source-range-0e12e052-01869))_
- The moves a player makes are a stream of values, just like the contents of an array can be consider a stream of values. _(javascriptallonge.pdf (source-range-0e12e052-01872))_
- But of course, iterating over a stream of moves requires us to wait for the game to be over so we know what moves were made. _(javascriptallonge.pdf (source-range-0e12e052-01872))_
- Consider, for example, the moves in a game. _(javascriptallonge.pdf (source-range-0e12e052-01872))_
- The first player will always be o , and they will always place their chequer in the top-left corner, coincidentally numbered o : _(javascriptallonge.pdf (source-range-0e12e052-01874))_
- x has six possible moves, but they are really just two choices: 3 and anything else: _(javascriptallonge.pdf (source-range-0e12e052-01883))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01869))_

> We used generators to build iterators that maintain implicit state. We saw how to use them for recursive unfolds and state machines. But there are other times we want to build functions that maintain implicit state. Let's start by looking at a very simple example of a function that can be written statefully.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01870))_

> [Figure] (p.273)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01874))_

> The first player will always be o , and they will always place their chequer in the top-left corner, coincidentally numbered o :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01876))_

> [Figure] (p.274)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01877))_

> The second player has five possible moves if we ignore reflections:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01878))_

> [Figure] (p.274)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01879))_

> Let's consider move 1 . That produces this board:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01880))_

> [Figure] (p.274)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01881))_

> We will always play into position 6 :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01882))_

> [Figure] (p.274)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01883))_

> x has six possible moves, but they are really just two choices: 3 and anything else:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01884))_

> [Figure] (p.274)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01885))_

> For 2 , 4 , 5 , 7 , or 8 , we play 3 and win. But if x moves 3 , we play 8 :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01886))_

> [Figure] (p.275)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01887))_

> x now has three significant moves: 4 , 7 , and anything else:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01888))_

> [Figure] (p.275)

### representing naughts and crosses as a stateless function

- We could plays naughts and crosses as a stateless function. _(javascriptallonge.pdf (source-range-0e12e052-01891))_
- We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. _(javascriptallonge.pdf (source-range-0e12e052-01891))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01891))_

> We could plays naughts and crosses as a stateless function. We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. For example, the entry for:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01892))_

> [Figure] (p.275)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01893))_

> Would be 8 , producing:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01894))_

> [Figure] (p.275)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01895))_

> And the entry for:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01896))_

> [Figure] (p.276)

#### Would be 3 , producing:

- We can encode the board in several different ways. _(javascriptallonge.pdf (source-range-0e12e052-01899))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01898))_

> [Figure] (p.276)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01900))_

> Let's use an array. So this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01901))_

> [Figure] (p.276)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01902))_

> Will be represented as:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01903))_

> [Figure] (p.276)

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01905))_

> [Figure] (p.277)

#### Will be represented as:

- We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. _(javascriptallonge.pdf (source-range-0e12e052-01908))_
- We can use a POJO to make a map from positions to moves. _(javascriptallonge.pdf (source-range-0e12e052-01908))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01907))_

```
[
'o', 'x', ' ',
'x', ' ', ' ',
'o', ' ', ' '
]
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01908))_

> We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01909))_

```
const moveLookupTable = {
[[
' ', ' ', ' ',
' ', ' ', ' ',
' ', ' ', ' '
]]: 0,
[[
'o', 'x', ' ',
' ', ' ', ' ',
' ', ' ', ' '
]]: 6,
[[
'o', 'x', 'x',
' ', ' ', ' ',
'o', ' ', ' '
]]: 3,
[[
'o', 'x', ' ',
'x', ' ', ' ',
'o', ' ', ' '
]]: 8,
[[
'o', 'x', ' ',
' ', 'x', ' ',
'o', ' ', ' '
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01908))_

> We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01910))_

```
]]: 3,
[[
'o', 'x', ' ',
' ', ' ', 'x',
'o', ' ', ' '
]]: 3,
[[
'o', 'x', ' ',
' ', ' ', ' ',
'o', 'x', ' '
]]: 3,
[[
'o', 'x', ' ',
' ', ' ', ' ',
'o', ' ', 'x'
]]: 3
// ...
};
```

#### We get:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01912))_

```
{
"o,x, , , , , , , ":6,
"o,x,x, , , ,o, , ":3,
"o,x, ,x, , ,o, , ":8,
"o,x, , ,x, ,o, , ":3,
"o,x, , , ,x,o, , ":3,
"o,x, , , , ,o,x, ":3,
"o,x, , , , ,o, ,x":3
}
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01913))_

> And if we want to look up what move to make, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01914))_

```
moveLookupTable[[
'o', 'x', ' ',
' ', ' ', ' ',
'o', 'x', ' '
]]
//=> 3
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01915))_

> And from there, a stateless function to play naughts-and-crosses is trivial:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01916))_

```
statelessNaughtsAndCrosses([
'o', 'x', ' ',
' ', ' ', ' ',
'o', 'x', ' '
])
//=> 3
```

### representing naughts and crosses as a stateful function

- Our 'API' will work like this: When we want a new game, we'll call a function that will return a game function, We'll call the game function repeatedly, passing our moves, and get the opponent's moves from it. _(javascriptallonge.pdf (source-range-0e12e052-01918))_
- In that case, we need a stateful function. _(javascriptallonge.pdf (source-range-0e12e052-01918))_
- The state is encoded entirely in data. _(javascriptallonge.pdf (source-range-0e12e052-01924))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01920))_

```
const aNaughtsAndCrossesGame = statefulNaughtsAndCrosses();
// our opponent makes the first move
aNaughtsAndCrossesGame()
//=> 0
// then we move, and get its next move back
aNaughtsAndCrossesGame(1)
//=> 6
// then we move, and get its next move back
aNaughtsAndCrossesGame(4)
//=> 3
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01921))_

> We can build this out of our statelessNaughtsAndCrosses function:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01922))_

```
const statefulNaughtsAndCrosses = () => {
const state = [
' ', ' ', ' ',
' ', ' ', ' ',
' ', ' ', ' '
];
return (x = false) => {
if (x) {
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01921))_

> We can build this out of our statelessNaughtsAndCrosses function:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01923))_

```
if (state[x] === ' ') {
state[x] = 'x';
}
else throw "occupied!"
}
let o = moveLookupTable[state];
state[o] = 'o';
return o;
}
};
const aNaughtsAndCrossesGame = statefulNaughtsAndCrosses();
// our opponent makes the first move
aNaughtsAndCrossesGame()
//=> 0
// then we move, and get its next move back
aNaughtsAndCrossesGame(1)
//=> 6
// then we move, and get its next move back
aNaughtsAndCrossesGame(4)
//=> 3
```

### this seems familiar

- Sometimes there is a state machine that is naturally represented implicitly in JavaScript's control flow rather than explicitly in data. _(javascriptallonge.pdf (source-range-0e12e052-01926))_
- When we looked at generators, we saw that some iterators are inherently stateful, but sometimes it is awkward to represent them in a fully stateless fashion. _(javascriptallonge.pdf (source-range-0e12e052-01926))_
- A game like this is absolutely a state machine, and we've explicitly coded those states into the lookup table. _(javascriptallonge.pdf (source-range-0e12e052-01927))_
- If we were in full control of the interaction, it would be easy to encode the game play as a decision tree instead of as a lookup table. _(javascriptallonge.pdf (source-range-0e12e052-01928))_
- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. _(javascriptallonge.pdf (source-range-0e12e052-01930))_
- But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree. _(javascriptallonge.pdf (source-range-0e12e052-01930))_
- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. _(javascriptallonge.pdf (source-range-0e12e052-01930))_
- With iterators, we wrote a generator function using function * , and then used yield to yield values while maintaining the implicit state of the generator's control flow. _(javascriptallonge.pdf (source-range-0e12e052-01931))_
- With iterators, we wrote a generator function using function * , and then used yield to yield values while maintaining the implicit state of the generator's control flow. _(javascriptallonge.pdf (source-range-0e12e052-01931))_
- But the first glance is deceptive, because we only see what we've seen so far. _(javascriptallonge.pdf (source-range-0e12e052-01932))_
- But the first glance is deceptive, because we only see what we've seen so far. _(javascriptallonge.pdf (source-range-0e12e052-01932))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01928, source-range-0e12e052-01930))_

> If we were in full control of the interaction, it would be easy to encode the game play as a decision tree instead of as a lookup table. For example, we could do this in a browser: Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01929))_

```
function browserNaughtsAndCrosses () {
const x1 = parseInt(prompt('o plays 0, where does x play?'));
switch (x1) {
case 1:
const x2 = parseInt(prompt('o plays 6, where does x play?'));
switch (x2) {
case 2:
case 4:
case 5:
case 7:
case 8:
alert('o plays 3');
break;
case 3:
const x3 = parseInt(prompt('o plays 8, where does x play?'));
switch (x3) {
case 2:
case 5:
case 7:
alert('o plays 4');
break;
case 4:
alert('o plays 7');
break;
}
}
break;
// ...
}
}
```

#### interactive generators

- So far, we have called iterators (and generators) with .next() . _(javascriptallonge.pdf (source-range-0e12e052-01934))_
- Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. _(javascriptallonge.pdf (source-range-0e12e052-01937))_
- If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1).value //=> 6 aNaughtsAndCrossesGame.next(3).value //=> 8 aNaughtsAndCrossesGame.next(7).value //=> 4 _(javascriptallonge.pdf (source-range-0e12e052-01937))_
- Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. _(javascriptallonge.pdf (source-range-0e12e052-01937))_
- If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1).value //=> 6 aNaughtsAndCrossesGame.next(3).value //=> 8 aNaughtsAndCrossesGame.next(7).value //=> 4 _(javascriptallonge.pdf (source-range-0e12e052-01937))_
- It isn't a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. _(javascriptallonge.pdf (source-range-0e12e052-01938))_
- But the generator function allows us to maintain state implicitly. _(javascriptallonge.pdf (source-range-0e12e052-01939))_
- And sometimes, we want to use implicit state instead of explicitly storing state in our data. _(javascriptallonge.pdf (source-range-0e12e052-01939))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01934, source-range-0e12e052-01937))_

> So far, we have called iterators (and generators) with .next() . But what if we pass a value to .next() ? If we could do that, a generator function that played naughts and crosses would look like this: Served by the Pot: Collections 260 } } break ; // ... } } const aNaughtsAndCrossesGame = generatorNaughtsAndCrosses(); We can then get the first move by calling .next() . Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the 

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01936))_

```
function* generatorNaughtsAndCrosses () {
const x1 = yield 0;
switch (x1) {
case 1:
const x2 = yield 6;
switch (x2) {
case 2:
case 4:
case 5:
case 7:
case 8:
yield 3;
break;
case 3:
const x3 = yield 8;
switch (x3) {
case 2:
case 5:
case 7:
yield 4;
break;
case 4:
yield 7;
break;
```

#### summary

- We have looked at generators as ways of making iterators over static collections, where state is modelled implicitly in control flow. _(javascriptallonge.pdf (source-range-0e12e052-01941))_
- Again, the salient difference is that an 'interactive' generator is stateful, and it embodies its state in its control flow. _(javascriptallonge.pdf (source-range-0e12e052-01942))_

### Basic Operations on Iterables

- Here are the operations we've defined on Iterables. _(javascriptallonge.pdf (source-range-0e12e052-01944))_

#### operations that transform one iterable into another

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01946))_

```
function * mapWith(fn, iterable) {
for (const element of iterable) {
yield fn(element);
}
}
function * mapAllWith (fn, iterable) {
for (const element of iterable) {
yield * fn(element);
}
}
function * filterWith (fn, iterable) {
for (const element of iterable) {
if (!!fn(element)) yield element;
}
}
function * compact (iterable) {
for (const element of iterable) {
if (element != null) yield element;
}
}
function * untilWith (fn, iterable) {
for (const element of iterable) {
if (fn(element)) break;
yield fn(element);
}
}
function * rest (iterable) {
const iterator = iterable[Symbol.iterator]();
iterator.next();
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01947))_

```
yield * iterator;
}
function * take (numberToTake, iterable) {
const iterator = iterable[Symbol.iterator]();
for (let i = 0; i < numberToTake; ++i) {
const { done, value } = iterator.next();
if (!done) yield value;
}
}
```

#### operations that compose two or more iterables into an iterable

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01949))_

```
function * zip (...iterables) {
const iterators = iterables.map(i => i[Symbol.iterator]());
while (true) {
const pairs = iterators.map(j => j.next()),
dones = pairs.map(p => p.done),
values = pairs.map(p => p.value);
if (dones.indexOf(true) >= 0) break;
yield values;
}
};
function * zipWith (zipper, ...iterables) {
const iterators = iterables.map(i => i[Symbol.iterator]());
while (true) {
const pairs = iterators.map(j => j.next()),
dones = pairs.map(p => p.done),
values = pairs.map(p => p.value);
if (dones.indexOf(true) >= 0) break;
yield zipper(...values);
}
};
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01950))_

> Note: zip is also the following special case of zipWith :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01951))_

```
const zip = callFirst(zipWith, (...values) => values);
```

#### operations that transform an iterable into a value

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01953))_

```
const reduceWith = (fn, seed, iterable) => {
let accumulator = seed;
for (const element of iterable) {
accumulator = fn(accumulator, element);
}
return accumulator;
};
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
```

#### memoizing an iterable

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01955))_

```
function memoize (generator) {
const memos = {},
iterators = {};
return function * (...args) {
const key = JSON.stringify(args);
let i = 0;
if (memos[key] == null) {
memos[key] = [];
iterators[key] = generator(...args);
}
while (true) {
if (i < memos[key].length) {
yield memos[key][i++];
}
else {
const { done, value } = iterators[key].next();
if (done) {
return;
} else {
yield memos[key][i++] = value;
```

## The Golden Crema: Appendices and Afterwords

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01958))_

> [Figure] (p.288)

### How to run the examples

- At the time this book was written, ECMAScript 2015 was not yet widely available. _(javascriptallonge.pdf (source-range-0e12e052-01961))_
- Traceur and Babel are both transpilers , they work by parsing ECMAScript 2015 code, then emitting valid ECMAScript-5 code that produces the same semantics. _(javascriptallonge.pdf (source-range-0e12e052-01961))_
- All of the examples in this book were tested using either Google Traceur Compiler 100 , Babel 101 , or both. _(javascriptallonge.pdf (source-range-0e12e052-01961))_
- Traceur and Babel are both transpilers , they work by parsing ECMAScript 2015 code, then emitting valid ECMAScript-5 code that produces the same semantics. _(javascriptallonge.pdf (source-range-0e12e052-01961))_
- Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. _(javascriptallonge.pdf (source-range-0e12e052-01972))_
- To see the result of your expressions, you may have to use the console in your web browser. _(javascriptallonge.pdf (source-range-0e12e052-01972))_
- And 4 would appear in your browser's development console. _(javascriptallonge.pdf (source-range-0e12e052-01977))_
- The care and feeding of node and npm are beyond the scope of this book, but both tools offer clear instructions for those who have already installed node . _(javascriptallonge.pdf (source-range-0e12e052-01978))_
- You can also install the transpilers on your development system and use them with Node 102 on the command line 103 . _(javascriptallonge.pdf (source-range-0e12e052-01978))_

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01962))_

> For example, this ECMAScript 2015 code:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01963))_

```
const before = (decoration) =>
(method) =>
function () {
decoration.apply(this, arguments);
return method.apply(this, arguments)
};
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01964))_

> Is translated into this ECMAScript-5 code:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01965))_

```
"use strict"
var before = function (decoration) {
return function (method) {
return function () {
decoration.apply(this, arguments);
return method.apply(this, arguments);
};
};
};
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01966))_

> The Babel 'try it out' page

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01967))_

> [Figure] (p.289)

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01968, source-range-0e12e052-01972))_

> If we make it even more idiomatic, we could write: Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01970))_

```
100https://github.com
101http://babeljs.io/
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01968, source-range-0e12e052-01972))_

> If we make it even more idiomatic, we could write: Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01971))_

```
const before = (decoration) =>
(method) =>
function (...args) {
decoration.apply(this, args);
return method.apply(this, args)
};
And it would be “transpiled” into:
var before = function (decoration) {
return function (method) {
return function () {
for (let _len = arguments.length, args = Array(_len), _key = 0; _key < _le\
n; _key++) {
args[_key] = arguments[_key];
}
decoration.apply(this, args);
return method.apply(this, args);
};
};
};
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01973))_

> So instead of just writing:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01974))_

```
(() => 2 + 2)()
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01975))_

> And having 4 displayed, you'd need to write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01976))_

```
console.log(
(() => 2 + 2)()
)
```

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01978))_

> You can also install the transpilers on your development system and use them with Node 102 on the command line 103 . The care and feeding of node and npm are beyond the scope of this book, but both tools offer clear instructions for those who have already installed node .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01979))_

```text
102 http://nodejs.org/
103 https://en.wikipedia.org/wiki/REPL
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 102 | http://nodejs.org/ |
| 103 | https://en.wikipedia.org/wiki/REPL |

</details>

### Thanks!

#### Daniel Friedman and Matthias Felleisen

- But where The Little Schemer's primary focus is recursion, JavaScript Allongé's primary focus is functions as first-class values . _(javascriptallonge.pdf (source-range-0e12e052-01984))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01982))_

> [Figure] (p.291)

#### Richard Feynman

- Richard Feynman's QED 105 wasanother inspiration: A book that explains Quantum Electrodynamics and the 'Sum of the Histories' methodology using the simple expedient of explaining how light reflects off a mirror, and showing how most of the things we think are happening-such as light travelling on a straight line, the angle of reflection equalling the angle of refraction, or that a beam of light only interacts with a small portion of the mirror, or that it reflects off a plane-are all wrong. _(javascriptallonge.pdf (source-range-0e12e052-01989))_
- Richard Feynman's QED 105 wasanother inspiration: A book that explains Quantum Electrodynamics and the 'Sum of the Histories' methodology using the simple expedient of explaining how light reflects off a mirror, and showing how most of the things we think are happening-such as light travelling on a straight line, the angle of reflection equalling the angle of refraction, or that a beam of light only interacts with a small portion of the mirror, or that it reflects off a plane-are all wrong. _(javascriptallonge.pdf (source-range-0e12e052-01989))_

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01987))_

> [Figure] (p.292)

### Copyright Notice

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01992))_

> The original words in this book are (c) 2012-2015, Reginald Braithwaite. All rights reserved.

#### images

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-02007))_

```text
106 http://www.flickr.com/photos/trumpetca/
http://creativecommons.org/licenses/by/2.0/deed.en
107 http://www.flickr.com/photos/avlxyz/4907262046 108 http://creativecommons.org/licenses/by-sa/2.0/deed.en 109 http://www.flickr.com/photos/digitalcolony/5054568279/ 110 http://creativecommons.org/licenses/by-sa/2.0/deed.en 111 http://www.flickr.com/photos/everydaylifemodern/1353570874/ 112 http://creativecommons.org/licenses/by-nd/2.0/deed.en 113 http://www.flickr.com/photos/everydaylifemodern/434299813/ 114 http://creativecommons.org/licenses/by-nd/2.0/deed.en 115 http://www.flickr.com/photos/the_rev/2295096211/ 116 http://creativecommons.org/licenses/by/2.0/deed.en 117 http://www.flickr.com/photos/thedigitelmyr/6199419022/ 118 http://creativecommons.org/licenses/by-sa/2.0/deed.en 119 http://www.flickr.com/photos/sagamiono/4391542823/ 120 http://creativecommons.org/licenses/by-sa/2.0/deed.en 121 http://www.flickr.com/photos/digitalcolony/3924227011/ 122 http://creativecommons.org/licenses/by-sa/2.0/deed.en 123 http://www.flickr.com/photos/15481483@N06/6231443466/ 124 http://creativecommons.org/licenses/by-sa/2.0/deed.en 125 http://www.flickr.com/photos/tjgfernandes/2785677276/ 126 http://creativecommons.org/licenses/by/2.0/deed.en 127 http://www.flickr.com/photos/kirstenloza/4805716699/ 128 http://creativecommons.org/licenses/by/2.0/deed.en 129 http://www.flickr.com/photos/jenny-pics/5053954146/ 130
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 106 | http://www.flickr.com/photos/trumpetca/ http://creativecommons.org/licenses/by/2.0/deed.en |
| 107 | http://www.flickr.com/photos/avlxyz/4907262046 |
| 108 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 109 | http://www.flickr.com/photos/digitalcolony/5054568279/ |
| 110 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 111 | http://www.flickr.com/photos/everydaylifemodern/1353570874/ |
| 112 | http://creativecommons.org/licenses/by-nd/2.0/deed.en |
| 113 | http://www.flickr.com/photos/everydaylifemodern/434299813/ |
| 114 | http://creativecommons.org/licenses/by-nd/2.0/deed.en |
| 115 | http://www.flickr.com/photos/the_rev/2295096211/ |
| 116 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 117 | http://www.flickr.com/photos/thedigitelmyr/6199419022/ |
| 118 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 119 | http://www.flickr.com/photos/sagamiono/4391542823/ |
| 120 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 121 | http://www.flickr.com/photos/digitalcolony/3924227011/ |
| 122 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 123 | http://www.flickr.com/photos/15481483@N06/6231443466/ |
| 124 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 125 | http://www.flickr.com/photos/tjgfernandes/2785677276/ |
| 126 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 127 | http://www.flickr.com/photos/kirstenloza/4805716699/ |
| 128 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 129 | http://www.flickr.com/photos/jenny-pics/5053954146/ 130 |

</details>

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-02024))_

```
131http://www.flickr.com/photos/33388953@N04/4017985434/
132http://creativecommons.org/licenses/by/2.0/deed.en
133http://www.flickr.com/photos/tangysd/5953453156/
134http://creativecommons.org/licenses/by-sa/2.0/deed.en
135http://www.flickr.com/photos/digitalcolony/4000837035/
136http://creativecommons.org/licenses/by-sa/2.0/deed.en
137http://www.flickr.com/photos/digitalcolony/4309812256/
138http://creativecommons.org/licenses/by-sa/2.0/deed.en
139http://www.flickr.com/photos/bike/3237859728/
140http://creativecommons.org/licenses/by-sa/2.0/deed.en
141http://www.flickr.com/photos/lacerabbit/2102801319/
142http://creativecommons.org/licenses/by-nd/2.0/deed.en
143http://www.flickr.com/photos/nalundgaard/4785922266/
144http://creativecommons.org/licenses/by-sa/2.0/deed.en
145http://www.flickr.com/photos/paulmccoubrie/6828131856/
146http://creativecommons.org/licenses/by-nd/2.0/deed.en
147http://www.flickr.com/photos/mikecogh/7676649034/
148http://creativecommons.org/licenses/by-sa/2.0/deed.en
149http://www.flickr.com/photos/yellowskyphotography/5641003165/
150http://creativecommons.org/licenses/by-sa/2.0/deed.en
151http://www.flickr.com/photos/andynash/6204253236/
152http://creativecommons.org/licenses/by-sa/2.0/deed.en
153http://www.flickr.com/photos/28705377@N04/5306009552/
154http://creativecommons.org/licenses/by/2.0/deed.en
155http://www.flickr.com/photos/shavejonathan/2343081208/
156http://creativecommons.org/licenses/by/2.0/deed.en
157http://www.flickr.com/photos/ilovememphis/7103931235/
158http://creativecommons.org/licenses/by-nd/2.0/deed.en
159http://www.flickr.com/photos/mikecogh/7561440544/
160http://creativecommons.org/licenses/by-sa/2.0/deed.en
161http://www.flickr.com/photos/dtownsend/6171015997/
162http://creativecommons org/licenses/by-sa/2 0/deed en
```

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-02041))_

```text
163 http://www.flickr.com/photos/93425126@N00/313053257/ 164 http://creativecommons.org/licenses/by-sa/2.0/deed.en 165 http://www.flickr.com/photos/digitalcolony/2833809436/ 166 http://creativecommons.org/licenses/by-sa/2.0/deed.en 167 http://www.flickr.com/photos/citizenhelder/5006498068/ 168 http://creativecommons.org/licenses/by/2.0/deed.en 169 http://www.flickr.com/photos/joncrel/237026246/ 170 http://creativecommons.org/licenses/by-nd/2.0/deed.en 171 http://www.flickr.com/photos/nalundgaard/3163852170/ 172 http://creativecommons.org/licenses/by-sa/2.0/deed.en 173 http://www.flickr.com/photos/47000103@N05/6525288841/ 174 http://creativecommons.org/licenses/by-sa/2.0/deed.en 175 http://www.flickr.com/photos/lotzman/978418891/ 176 http://creativecommons.org/licenses/by/2.0/deed.en 177 http://www.flickr.com/photos/kk/sets/72157626168201654/with/5484839102/ 178 http://creativecommons.org/licenses/by-sa/2.0/deed.en 179 https://www.flickr.com/photos/kellan/434503323 180 http://creativecommons.org/licenses/by/2.0/deed.en 181 https://www.flickr.com/photos/whitneyinchicago/3835218626 182 http://creativecommons.org/licenses/by/2.0/deed.en 183 https://www.flickr.com/photos/sankarshan/5165312159 184 http://creativecommons.org/licenses/by-sa/2.0/deed.en 185 https://www.flickr.com/photos/candy-s/7619358284 186 https://www.flickr.com/photos/candy-s/ 187 http://creativecommons.org/licenses/by/2.0/deed.en 188 https://www.flickr.com/photos/lorentey/22193876 189 https://www.flickr.com/photos/lorentey/ 190 http://creativecommons.org/licenses/by/2.0/deed.en 191 https://www.flickr.com/photos/kk/5484876862 192 http://creativecommons.org/licenses/by-sa/2.0/deed.en 193 https://www.flickr.com/photos/f_mafra/2956649121 194
http://creativecommons.org/licenses/by-sa/2.0/deed.en
coffee pots 195 (c) 2009 Jonas Forth Some rights reserved 196 .
5 Barrel Roaster 197 (c) 2013 David Lytle Some rights reserved 198 .
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 163 | http://www.flickr.com/photos/93425126@N00/313053257/ |
| 164 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 165 | http://www.flickr.com/photos/digitalcolony/2833809436/ |
| 166 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 167 | http://www.flickr.com/photos/citizenhelder/5006498068/ |
| 168 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 169 | http://www.flickr.com/photos/joncrel/237026246/ |
| 170 | http://creativecommons.org/licenses/by-nd/2.0/deed.en |
| 171 | http://www.flickr.com/photos/nalundgaard/3163852170/ |
| 172 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 173 | http://www.flickr.com/photos/47000103@N05/6525288841/ |
| 174 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 175 | http://www.flickr.com/photos/lotzman/978418891/ |
| 176 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 177 | http://www.flickr.com/photos/kk/sets/72157626168201654/with/5484839102/ |
| 178 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 179 | https://www.flickr.com/photos/kellan/434503323 |
| 180 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 181 | https://www.flickr.com/photos/whitneyinchicago/3835218626 |
| 182 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 183 | https://www.flickr.com/photos/sankarshan/5165312159 |
| 184 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 185 | https://www.flickr.com/photos/candy-s/7619358284 |
| 186 | https://www.flickr.com/photos/candy-s/ |
| 187 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 188 | https://www.flickr.com/photos/lorentey/22193876 |
| 189 | https://www.flickr.com/photos/lorentey/ |
| 190 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 191 | https://www.flickr.com/photos/kk/5484876862 |
| 192 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 193 | https://www.flickr.com/photos/f_mafra/2956649121 194 http://creativecommons.org/licenses/by-sa/2.0/deed.en coffee pots 195 (c) 2009 Jonas Forth Some rights reserved 196. |
| 5 | Barrel Roaster 197 (c) 2013 David Lytle Some rights reserved 198. |

</details>

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-02053))_

```text
195 https://www.flickr.com/photos/jforth/3360599750/
197 https://www.flickr.com/photos/dlytle/8720139854
196 http://creativecommons.org/licenses/by-nd/2.0/deed.en
198 http://creativecommons.org/licenses/by/2.0/deed.en
200 http://creativecommons.org/licenses/by-nd/2.0/deed.en
199 https://www.flickr.com/photos/joebehr/5504285781
201 https://www.flickr.com/photos/adders/8372085101
203 https://www.flickr.com/photos/digitalcolony/2843767532
202 http://creativecommons.org/licenses/by-nd/2.0/deed.en
204 http://creativecommons.org/licenses/by-sa/2.0/deed.en
206 http://creativecommons.org/licenses/by/2.0/deed.en
205 https://www.flickr.com/photos/arisvrakas/4217869291
207 https://www.flickr.com/photos/vscript/8708520929
209 https://www.flickr.com/photos/peterme/1271652
208 http://creativecommons.org/licenses/by/2.0/deed.en
210 http://creativecommons.org/licenses/by-sa/2.0/deed.en
212 http://creativecommons.org/licenses/by/2.0/deed.en
211 https://www.flickr.com/photos/renaud-camus/6165559492
213 https://www.flickr.com/photos/cyclonebill/2606398721
215 https://www.flickr.com/photos/tillwe/8154272083
214 http://creativecommons.org/licenses/by-sa/2.0/deed.en
216 http://creativecommons.org/licenses/by-sa/2.0/deed.en
218 http://creativecommons.org/licenses/by/2.0/deed.en
217 https://www.flickr.com/photos/peddhapati/11671457605
219 https://www.flickr.com/photos/mjaysplanet/8416343475
220 http://creativecommons.org/licenses/by-sa/2.0/deed.en
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 195 | https://www.flickr.com/photos/jforth/3360599750/ |
| 197 | https://www.flickr.com/photos/dlytle/8720139854 |
| 196 | http://creativecommons.org/licenses/by-nd/2.0/deed.en |
| 198 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 200 | http://creativecommons.org/licenses/by-nd/2.0/deed.en |
| 199 | https://www.flickr.com/photos/joebehr/5504285781 |
| 201 | https://www.flickr.com/photos/adders/8372085101 |
| 203 | https://www.flickr.com/photos/digitalcolony/2843767532 |
| 202 | http://creativecommons.org/licenses/by-nd/2.0/deed.en |
| 204 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 206 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 205 | https://www.flickr.com/photos/arisvrakas/4217869291 |
| 207 | https://www.flickr.com/photos/vscript/8708520929 |
| 209 | https://www.flickr.com/photos/peterme/1271652 |
| 208 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 210 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 212 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 211 | https://www.flickr.com/photos/renaud-camus/6165559492 |
| 213 | https://www.flickr.com/photos/cyclonebill/2606398721 |
| 215 | https://www.flickr.com/photos/tillwe/8154272083 |
| 214 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 216 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 218 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 217 | https://www.flickr.com/photos/peddhapati/11671457605 |
| 219 | https://www.flickr.com/photos/mjaysplanet/8416343475 |
| 220 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |

</details>

### About The Author

- When he's not shipping JavaScript, Ruby, CoffeeScript and Java applications scaling out to millions of users, Reg 'Raganwald' Braithwaite has authored libraries 221 for JavaScript, CoffeeScript, and Ruby programming such as Allong.es, Method Combinators, Katy, JQuery Combinators, YouAreDaChef, andand, and others. _(javascriptallonge.pdf (source-range-0e12e052-02055))_
- When he's not shipping JavaScript, Ruby, CoffeeScript and Java applications scaling out to millions of users, Reg 'Raganwald' Braithwaite has authored libraries 221 for JavaScript, CoffeeScript, and Ruby programming such as Allong.es, Method Combinators, Katy, JQuery Combinators, YouAreDaChef, andand, and others. _(javascriptallonge.pdf (source-range-0e12e052-02055))_

#### contact

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-02059))_

> [Figure] (p.297)

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-02061))_

```text
221 http://github.com/raganwald
223 http://braythwayt.com
222 http://raganwald
224 https://twitter.com/raganwald
225 mailto:reg@braythwayt.com
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 221 | http://github.com/raganwald |
| 223 | http://braythwayt.com |
| 222 | http://raganwald |
| 224 | https://twitter.com/raganwald |
| 225 | mailto:reg@braythwayt.com |

</details>

## Source review

### Needs review

- Like adding a splash of water to whiskey, the small dilution releases more of the complex flavours in the mouth. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00014))_
- This achieves approximately the same ratio of oils to water as the dilution method, but also releases a different mix of flavours due to the longer extraction. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00015))_
- 'The important thing is that neither method of preparation should use so much water as to result in a sickly, pale ghost of Espresso. Moderation in all things.' — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00016))_
- JavaScript Allongé teaches you how to handle complex code, and it also teaches you how to simplify code without dumbing it down. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00021))_
- And presto, rest collects the rest of the arguments without a lot of malarky involving slicing arguments . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00040))_
- Thus, the focus on things like writing decorators. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00045))_
- But there's more to it than that . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00045))_
- And these techniques dovetail nicely with Allongé's focus on composing entities and working with functions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00047))_
- It introduces iterators and generators. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00048))_
- Thus, the 'six' edition introduces classes and mixins. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00048))_
- It introduces the notion of implementing private properties with symbols. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00048))_
- We just call some of those functions constructors, others decorators, others functional mixins, and yet others, policies. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00049))_
- From functions flow many ideas, from decorators to methods to delegation to mixins, and onwards in so many fruitful directions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00054))_
- There are reasons why the second form is more flexible, especially when used in combination with partial application, but does that outweigh the benefit of having an entire codebase do everything consistently the first way or the second way? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00063))_
- JavaScript Allongé introduces new aspects of programming with functions in each chapter, explaining exactly how JavaScript works. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00067))_
- This upgrade became ECMAScript 5. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00072))_
- - Better syntax for features that already exist (e.g. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00075))_
- For example: classes and modules. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00075))_
- - New functionality in the standard library. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00076))_
- - Completely new features. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00080))_
- For example: Generators, proxies and WeakMaps. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00080))_
- Having written books myself, I know the pain of soliciting and receiving feedback. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00086))_
- Besides, there's really no risk at all . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00095))_
- Say you hand the barista a café Cubano. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00103))_
- Is this an expression? A value? Neither? Or both? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00106))_
- In JavaScript, we test whether two values are identical with the === operator, and whether they are not identical with the !== operator: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00117))_
- And then you're shown another cup of coffee. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00119))_
- Well, JavaScript's third and fourth possibilities cover that. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00124))_
- So what kinds of values might be the same type and have the same contents, but not be considered identical to JavaScript? Let's meet a data structure that is very common in contemporary programming languages, the Array (other languages sometimes call it a List or a Vector). — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00133))_
- An array looks like this: [1, 2, 3] . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00134))_
- Most programmers never encounter the limit on the magnitude of an integer. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00149))_
- In a sense, they behave like little functions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00162))_
- There are lots and lots more operators that can be used with numbers, including bitwise operators like | and & that allow you to operate directly on a number's binary representation, and a number of other operators that perform assignment or logical comparison that we will look at later. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00166))_
- Which kind are functions? Let's try them out and see. For reasons of appeasing the JavaScript parser, we'll enclose our functions in parentheses: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00179))_
- Here's how we apply a function to some values in JavaScript: Let's say that fn_expr is an expression that when evaluated, produces a function. Let's call the arguments args . Here's how to apply a function to some arguments: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00184))_
- Since we aren't giving it any arguments, we'll simply write () after the expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00186))_
- If not… Welcome to the ALGOL family of programming languages! — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00188))_
- It evaluates to the same thing, 0 . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00201))_
- It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00203))_
- So, this is a valid function: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00213))_
- - By evaluating a function that doesn't return a value (() => {})() , and; — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00229))_
- There's a third way, with JavaScript's void operator. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00231))_
- Something like: { statement 1 ; statement 2 ; statement 3 ; ... — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00239))_
- Statements belong inside blocks and only inside blocks. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00251))_
- We'll see a few more of these later. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00251))_
- Some languages simplify this by making everything an expression, but JavaScript maintains this distinction, so when learning JavaScript we also learn about statements like function declarations, for loops, if statements, and so forth. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00251))_
- Secondary school mathematics discusses this. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00266))_
- Use them in the body, of course. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00271))_
- It's a function for calculating the circumference of a circle given the diameter. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00273))_
- To apply a function with an argument (or arguments), we put the argument (or arguments) within the parentheses, like this: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00274))_
- 22 The Argument Sketch from 'Monty Python's Previous Record' and 'Monty Python's Instant Record Collection' — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00277))_
- A return statement accepts any valid JavaScript expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00283))_
- We'll see below that while JavaScript always calls by value, the notion of a 'value' has additional subtlety. But before we do, let's look at variables. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00291))_
- Arguments and variables work the same way whether we're talking about (x) => (y) => x or just plain (x) => x . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00297))_
- - JavaScript parses this whole thing as an expression made up of several sub-expressions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00303))_
- - Another, 2 , evaluates to the number 2. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00306))_
- - JavaScript now evaluates applying the function to the argument 2 . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00307))_
- And with that, we're ready to look at closures . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00321))_
- When we combine our knowledge of value types, reference types, arguments, and closures, we'll understand why this function always evaluates to true no matter what argument 26 you apply it to: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00321))_
- NaN in JavaScript behaves a lot like NULL in SQL. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00323))_
- Given ( some function )( some argument ) , we know that we apply the function to the argument, create an environment, bind the value of the argument to the name, and evaluate the function's expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00327))_
- The environment belonging to the function with signature (x) => ... — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00329))_
- Now let's enjoy a relaxed Allongé before we continue! — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00336))_
- has a free variable, but the entire expression refers to (x) => ... — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00343))_
- And now you can guess how we evaluate ((y) => x)(2) in the environment {y: 2, '..': {x: 1, ...}} . The variable x isn't in (y) => ... 's immediate environment, but it is in its parent's environment, so it evaluates to 1 and that's what ((y) => x)(2) returns even though it ended up ignoring its own a — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00352))_
- Only you call it with (1)(2)(3) instead of (1, 2, 3) . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00360))_
- JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00368))_
- But before we do so, there's one final question: Where does the ancestry start? If there's no other code in a file, what is (x) => x 's parent environment? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00374))_
- Create an environment for them, of course. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00376))_
- Sometimes, programmers wish to avoid this. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00376))_
- The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': global environment }} . As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code  — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00378))_
- (diameter) => diameter * 3.14159265 What is this '3.14159265' number? PI 28 , obviously. We'd like to name it so that we can write something like: (diameter) => diameter * PI — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00382))_
- What do we put inside our new function that binds 3.14159265 to the name PI when evaluated? Our circumference function, of course: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00385))_
- 'Exposes' naming PI first, and we have to look inside to find out why we care. So, should we should always write this? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00403))_
- Every time we invoke the outer function, we'll invoke the inner function. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00405))_
- And we could use it like this: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00412))_
- Even better, it puts the symbol (like PI ) close to the value ( 3.14159265 ). — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00417))_
- The const keyword introduces one or more bindings in the block that encloses it. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00417))_
- It doesn't incur the cost of a function invocation. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00417))_
- It works just as we want. Instead of: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00419))_
- That emphasizes one of the things JavaScript gets really, really right: Functions as 'first class entities. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00428))_
- For readability, most people put one binding per line: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00429))_
- Let's back up and reconsider how closures work. What happens if we use parameters to bind two different values to the same name? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00444))_
- And we know that functions create environments. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00459))_
- Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00470))_
- We say that when we bind a variable using a parameter inside another binding, the inner binding shadows the outer binding. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00472))_
- So what about const . Does it work the same way? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00473))_
- Yes, names bound with const shadow enclosing bindings just like parameters. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00475))_
- That's why we made all these IIFEs. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00476))_
- Ah! const statements don't just shadow values bound within the environments created by functions, they shadow values bound within environments created by blocks! — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00479))_
- This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function's scope. In that case, we'd see things like this: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00480))_
- Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00484))_
- By default, JavaScript permits us to rebind new values to names bound with a parameter. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00486))_
- The line n = n -2; rebinds a new value to the name n . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00489))_
- Let's get right to it. This code does not name a function: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00494))_
- It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00496))_
- - We introduce a function with the function keyword. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00504))_
- This still does not name a function, but as we noted above, functions written with the function keyword have an optional 'something else.' Could that 'something else' name a function? Yes, of course. 33 — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00513))_
- In this book we are not examining JavaScript's tooling such as debuggers baked into browsers, but we will note that when you are navigating call stacks in all modern tools, the function's binding name is ignored but its actual name is displayed, so naming functions is very useful even if they don't  — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00521))_
- As we've seen, JavaScript functions take values as arguments and return values. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00552))_
- Higher-order functions dominate JavaScript Allongé . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00555))_
- But before we go on, we'll talk about some specific types of higher-order functions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00555))_
- Let's start with a useful combinator: Most programmers call it Compose , although the logicians call it the B combinator or 'Bluebird.' Here is the typical 37 programming implementation: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00559))_
- You'll find lots more perusing the recipes in this book. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00561))_
- You'll see other function decorators in the recipes, like once and maybe. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00573))_
- When you look at functions within functions in JavaScript, there's a bit of a 'spaghetti code' look to it. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00575))_
- We don't want to fool around writing _. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00589))_
- We'll discuss mapWith again. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00594))_
- Wegeneralized composition with the compose combinator. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00598))_
- Although arguments looks like an array, it isn't an array: It's more like an object 43 that happens to bind some values to properties with names that look like integers starting with zero: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00605))_
- It's the same idea, after all. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00623))_
- Now our inner function binds arguments[0] every time it is invoked, so we get the same result as if we'd written function (column) { return column * column } . — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00625))_
- - Expression bodies evaluate to the value of the expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00639))_
- - Function application creates a scope. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00643))_
- 'Unary' is a function decorator that modifies the number of arguments a function takes: Unary takes any function and turns it into a function taking exactly one argument. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00663))_
- JavaScript's map actually calls each function with three arguments: The element, the index of the element in the array, and the array itself. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00666))_
- However, that's not the whole story. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00666))_
- In that example, it looks exactly like the mapping function you'll find in most languages: You pass it a function, and it calls the function with one argument, the element of the array. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00666))_
- It takes an optional radix argument. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00671))_
- It takes a value and returns a function that always returns the value, but if you pass it a function, it executes the function for side-effects. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00682))_
- tap('espresso')((it) => { console.log(`Our drink is ' ${ it } '`) }); //=> Our drink is 'espresso' 'espresso' It's easy to turn off: tap('espresso')(); //=> 'espresso' Libraries like Underscore 49 use a version of tap that is 'uncurried:' _.tap('espresso', (it) => console.log(`Our drink is ' ${ it } — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00683))_
- And if we wish it to do nothing at all, We can write either tap('espresso')() or tap('espresso', null) — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00687))_
- It's also useful for working with object and instance methods. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00688))_
- As a bonus, maybe plays very nicely with instance methods, we'll discuss those later: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00701))_
- You pass it a function, and you get a function back. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00707))_
- It seems some people will only try blind dating once. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00709))_
- It accepts a coach, a captain, and an arbitrary number of players. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00714))_
- 53 Another history lesson. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00722))_
- We've seen operators that act on numeric values, like + and % . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00748))_
- is a unary prefix operator that negates its argument. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00754))_
- , && , and || , but we've said nothing about expressions or about passing other values. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00758))_
- We'll look at those presently. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00758))_
- We'll look at them in a moment, but first, we'll look at one more operator. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00762))_
- It's the only operator that takes three arguments. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00763))_
- 54 We will not discuss JavaScript's numeric behaviour in much depth in this book, but the most important thing to know is that it implements the IEEE Standard for Floating-Point Arithmetic (IEEE 754), a technical standard for floating-point computation established in 1985 by the Institute of Electri — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00764))_
- Our logical operators ! — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00771))_
- is the way we write 'is truthy' in JavaScript. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00774))_
- - && evaluates its left-hand expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00776))_
- -If its left-hand expression evaluates to something falsy, && returns the value of its lefthand expression without evaluating its right-hand expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00777))_
- -If its left-hand expression evaluates to something truthy, && evaluates its right-hand expression and returns the value of the right-hand expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00778))_
- - || evaluates its left-hand expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00779))_
- -If its left-hand expression evaluates to something truthy, || returns the value of its lefthand expression without evaluating its right-hand expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00780))_
- -If its left-hand expression evaluates to something false, || evaluates its right-hand expression and returns the value of the right-hand expression. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00781))_
- In JavaScript, && and || aren't boolean logical operators in the logical sense. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00784))_
- If n === 0 , JavaScript does not evaluate (n !== 1 && even(n -2)) . This is very important! Imagine that JavaScript evaluated both sides of the || operator before determining its value. n === 0 would be true. What about (n !== 1 && even(n -2)) ? Well, it would evaluate even(n 2) , or even(-2) — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00790))_
- and so on and so forth until JavaScript throws up its hands and runs out of stack space. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00791))_
- But that's not what happens. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00792))_
- It's best to think of || and && as control-flow operators. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00793))_
- This leads to the infinite recursion we fear. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00797))_
- is a logical operator, it always returns true or false . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00803))_
- We saw how to construct an array literal using [ , expressions, , and ] . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00835))_
- Some other languages call them first and butFirst , or head and tail . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00849))_
- operation as a 'gather,' following Kyle Simpson's example. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00849))_
- to place the elements of an array inside another array. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00854))_
- who] = ["duck feet", "tiger tail"]; And if there aren't any items to assign with ... — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00862))_
- Some languages support multiple return values: A function can return several things at once, like a value and an error code. This can easily be emulated in JavaScript with destructuring: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00865))_
- It is very much like an array literal. And consider how we bind values to parameter names: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00870))_
- It looks like destructuring. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00872))_
- It acts like destructuring. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00872))_
- Gathering works with parameters! — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00874))_
- We gather the rest of the parameters. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00875))_
- Armed with our definition of an empty list and with what we've already learned, we can build a great many functions that operate on arrays. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00891))_
- First, we pick what we call a terminal case . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00893))_
- But we don't know the length of rest . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00895))_
- 'Recursion' sometimes seems like an elaborate party trick. There's even a joke about this: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00900))_
- They find a bunsen burner, a sparker, a tap, an empty beaker, a stand, and a card with the instructions 'boil water.' — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00901))_
- The engineers light the burner immediately. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00903))_
- Recursive algorithms follow the 'divide and conquer' strategy for solving a problem: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00904))_
- It's very useful and simple to understand. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00910))_
- We already know how to divide arrays into smaller pieces. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00911))_
- Wecanwrite it out using a ternary operator. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00927))_
- With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00930))_
- - Given the terminal case of an empty list, we return a 0 instead of an empty list, and; — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00933))_
- - We catenate the square of each element to the result of applying sumSquares to the rest of the elements. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00934))_
- Let's rewrite mapWith so that we can use it to sum squares. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00935))_
- Let's look at how. Here's our extremely simple mapWith function again: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00949))_
- The first two don't return anything, they don't matter. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00964))_
- This lengthDelaysWork function calls itself in tail position. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00974))_
- But while we're doing that, it's annoying to remember to call it with a zero. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-00974))_
- Wesawearlier that destructuring parameters works the same way as destructuring assignment. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01006))_
- Much slower than the built-in .map method for arrays. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01014))_
- Every time we call mapWith , we're calling [...prepend, fn(first)] . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01015))_
- Worse, the JavaScript Engine actually copies the elements from prepend into the new array one at a time. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01016))_
- So here's a question: If this is such a slow approach, why do some examples of 'functional' algorithms work this exact way? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01020))_
- Notice that though JavaScript displays our list as if it is composed of arrays nested within each other like Russian Dolls, in reality the arrays refer to each other with references, so [1,[2,[3,[4,[5,null]]]]] is actually more like: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01035))_
- But what about the rest of the list? cdr does the trick: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01040))_
- Again, it's just extracting a reference from a cons cell, it's very fast. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01042))_
- In Lisp, it's blazingly fast because it happens in hardware. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01042))_
- Getting back to JavaScript now, when we write [first, ...rest] to gather or spread arrays, we're emulating the semantics of car and cdr , but not the implementation. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01044))_
- If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01049))_
- In addition to the extra fetches to dereference pointers, pointer chasing suffers from cache misses. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01050))_
- All containers can contain any value, including functions or other containers, like a fat arrow function: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01080))_
- Just as we saw with arrays, we can write destructuring assignments with literal object syntax. So, we can write: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01090))_
- Well, well, well. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01109))_
- Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01111))_
- Their identities stay the same, but not their structure. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01116))_
- JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01133))_
- Languages like Haskell 70 don't permit mutation at all. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01137))_
- of a list: We aren't making a new list, we're using some of the old list. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01142))_
- So back to avoiding mutation. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01146))_
- In general, it's easier to reason about data that doesn't change. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01146))_
- Consider our copy algorithm. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01148))_
- By default, JavaScript permits us to rebind new values to names bound with a parameter. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01158))_
- The line n = n -2; rebinds a new value to the name n . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01160))_
- We took the time to carefully examine what happens with bindings in environments. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01165))_
- However, if we don't shadow age with let , reassigning within the block changes the original: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01171))_
- It then rebinds the name in that environment. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01173))_
- Some programmers dislike deliberately shadowing variables. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01175))_
- If you buy that argument, the way that shadowing works in JavaScript exists to protect us from accidentally shadowing a variable when we move code around. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01175))_
- Well, parameters bind names. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01184))_
- Named function expressions bind names. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01184))_
- So that's five different ways so far. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01184))_
- Function declarations bind names. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01184))_
- It's just different enough to present a source of confusion. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01186))_
- But of course, it's not exactly like let . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01186))_
- JavaScript hoists the declaration, but not the assignment. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01193))_
- It looks a lot like the for loop in C. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01198))_
- About 30 seconds later Gauss gave him the answer. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01201))_
- Of course Gauss came up with the answer about 20 times faster than the other kids. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01201))_
- So far, so good. Hey, remember that functions in JavaScript are values? Let's get fancy! — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01204))_
- Again, so far, so good. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01206))_
- That's not what we want at all. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01210))_
- Now we're creating a new inner parameter, i and binding it to the value of the outer i . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01215))_
- And therefore, modifications to the parent also modify the child, and modifications to the child also modify the parent. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01224))_
- before we go any further, let's write a few naïve list utilities so that we can work at a slightly higher level of abstraction: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01229))_
- Our new at and set functions behave similarly to array[index] and array[index] = value . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01232))_
- So back to the problem of structure sharing. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01234))_
- There's also a bug: What happens when we modify the first element of a list? But before we fix that, let's try being lazy about copying. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01238))_
- In case we modify a child list. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01240))_
- I'm not particularly surprised that I couldn't think up an answer in a few minutes at the time. And to the interviewer's credit, he didn't terminate the interview on the spot, he asked me to describe the kinds of things going through my head. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01254))_
- I then forgot about it for a while. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01256))_
- I sent him an email sharing my result, to demonstrate my ability to follow through. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01256))_
- At the time, I couldn't think of any way to use hashing to solve the problem, so I gave up and tried to fit this into a powers-of-two algorithm. My first pass at it was clumsy, but it was roughly equivalent to this: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01261))_
- In Functional Iterators, we'll investigate one pattern for separating these concerns. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01264))_
- Let's consider a remarkably simple problem: Finding the sum of the elements of an array. In tailrecursive style, it looks like this: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01267))_
- As we saw earlier, this entangles the mechanism of traversing the array with the business of summing the bits. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01269))_
- What happens when we want to sum a tree of numbers? Or a linked list of numbers? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01272))_
- Once again, we're mixing the code for iterating over an array with the code for calculating a sum. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01283))_
- We haven't written anything that finds the first element of an iteration that meets a certain criteria. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01312))_
- So as you traverse the new decorator, you're changing the state of the original! — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01318))_
- To Mock a Mockingbird 76 established the metaphor of songbirds for the combinators, and ever since then logicians have called the K combinator a 'kestrel,' the B combinator a 'bluebird,' and so forth. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01327))_
- Let's start with some of the building blocks of combinatory logic, the K, I, and V combinators, nicknamed the 'Kestrel', the 'Idiot Bird', and the 'Vireo:' — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01329))_
- Very simple, but useful. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01336))_
- Now we'll take it one more step forward: Passing a value to K gets a function back, and passing a value to that function gets us a value. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01336))_
- Now, an interesting thing happens when we pass functions to each other. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01340))_
- From what we just wrote, K(x)(y) => x So K(I)(x) => I . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01340))_
- Given two values, K(I) always returns the second value. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01343))_
- You pass the data to these functions, and they extract it. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01353))_
- But the first and second we built out of K and I don't work that way. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01354))_
- You call them and pass them the bits, and they choose what to return. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01354))_
- And instead of passing latin to first or second , we pass first or second to latin . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01357))_
- It's exactly backwards of the way we write functions that operate on data. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01357))_
- For arrays, we'd write cons = (first, second) => [first, second] . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01359))_
- We'd better try it out to check. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01370))_
- Armed with nothing more than K , I , and V , we can make a little data structure that holds two values, the cons cell of Lisp and the node of a linked list. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01370))_
- Without arrays, and without objects, just with functions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01370))_
- But without building our way up to something insane like writing a JavaScript interpreter using JavaScript functions and no other data structures, let's take things another step in a slightly different direction. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01381))_
- Instead of writing length(list) and examining a list, we'll write something like: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01387))_
- Deeply important, but not practical when you're building a bridge. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01400))_
- It's the QED of physics that underpins the Maxwell's Equations of programming. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01400))_
- So what is interesting about this? What nags at our brain as we're falling asleep after working our way through this? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01402))_
- The same thing happens with our lists. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01409))_
- We won't bother here, but it's easy to see how to swap our functions out and replace them with an array. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01412))_
- The line node === EMPTY presumes a lot of things. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01414))_
- - And instead of testing some property of an entity and making a choice of our own with ?: (or if ), pass the entity the work we want done for each case and let it test itself. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01418))_
- This recipe isn't for map : It's for mapWith , a function that wraps around map and turns any other function into a mapper. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01429))_
- mapWith differs from map in two ways. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01431))_
- It also 'curries' the function: Instead of taking two arguments, it takes one argument and returns a function that takes another argument. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01431))_
- It reverses the arguments, taking the function first and the list second. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01431))_
- It's the same idea, after all. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01435))_
- Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01439))_
- Let's consider the case whether we have a map function of our own, perhaps from the allong.es 84 library, perhaps from Underscore 85 . We could write our function something like this: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01445))_
- First, we're reversing the order of arguments. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01447))_
- Looking at this, we see we're conflating two separate transformations. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01447))_
- Second, we're 'currying' the function so that instead of defining a function that takes two arguments, it returns a function that takes the first argument and returns a function that takes the second argument and applies them both, like this: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01449))_
- Let's return to the implementation of mapWith that relies on a map function rather than a method: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01451))_
- Assigning properties from one object to another (also called 'cloning' or 'shallow copying') is a basic building block that we will later use to implement more advanced paradigms like mixins. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01480))_
- Use it as an excuse to get familiar with your environment's debugging facility. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01486))_
- Work things out for yourself! — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01490))_
- For example, the escape sequence \n inserts a newline character in a string literal, like this: 'first line\nsecond line' . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01495))_
- Quasi-literals go much further. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01502))_
- Sometimes you just want to move the box around. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01523))_
- Things like 'put a label on every bag of coffee in this box,' Or, 'Open the box, take out the bags of decaf, and make a new box with just the decaf.' Or, 'go through the bags in this box, and take out the first one marked 'Espresso' that contains at least 454 grams of beans.' — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01524))_
- The way we've written .iterator as a method, each object knows how to return an iterator for itself. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01530))_
- We can use it with our stack: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01534))_
- We just ask the object for an iterator, and work on the iterator. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01538))_
- And there's one more thing: You recall that the spread operator ( ... — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01559))_
- One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01565))_
- It's the same idea, after all. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01583))_
- We invoke mapWith((x) => 2 * x, Numbers) and get Evens . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01588))_
- Every time we write for (const i of Evens) , JavaScript calls Evens[Symbol.iterator]() . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01590))_
- So we call it a collection operation . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01591))_
- The Numbers iterable returns an object that updates a mutable variable, n , to deliver number after number. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01624))_
- Then it waits for the next request. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01625))_
- It waits until given a request, and then it returns exactly one item. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01625))_
- Well, we've written our iterator as a server . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01625))_
- They're of approximately equal complexity. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01630))_
- For example, iterating over a tree. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01633))_
- else {
console.log(element)
}
}
}
generate([1, [2, [3, 4], 5]])
//=>
1
2
3
4
5
Very simple. Now for the iteration version. We’ll write a functional iterator to keep things simple,
but it’s easy to see the shape of the basic problem: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01635))_
- Now for the iteration version. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01636))_
- We'll write a functional iterator to keep things simple, but it's easy to see the shape of the basic problem: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01636))_
- Not a fat arrow. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01659))_
- We 'yield' values using the yield keyword. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01660))_
- - We don't return values or output them to console.log . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01660))_
- Whenweinvokethe function, we get an iterator object back. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01661))_
- We call its .next() method, but it's done immediately. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01663))_
- 91 Wewrote a generator declaration . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01665))_
- It yields the value of something , and then it's done. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01671))_
- - We call oneTwoThree() and get an iterator. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01676))_
- - The iterator suspends its execution . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01680))_
- - The iterator wraps 1 in {done: false, value: 1} and returns that from the call to .next() . — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01681))_
- - The iterator suspends its execution . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01685))_
- - The iterator wraps 2 in {done: false, value: 2} and returns that from the call to .next() . — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01686))_
- - The iterator suspends its execution . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01690))_
- - The iterator wraps 3 in {done: false, value: 3} and returns that from the call to .next() . — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01691))_
- - The iterator returns {done: true} from the call to .next() , and every call to this iterator's .next() method will return {done: true} from now on. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01695))_
- When the consumer calls .next() , it 'suspends' and the producer starts running. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01698))_
- When the producer yields a value, the producer suspends and the consumer starts running, taking the value from the result of calling .next() . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01698))_
- It's a function that returns an iterator when we invoke it. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01704))_
- Of course, we could just as easily write a generator function for Fibonacci numbers: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01722))_
- Here's a first crack at a function that returns an iterable object for iterating over trees: — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01725))_
- We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01727))_
- else {
yield e;
}
}
};
for (const i of tree([1, [2, [3, 4], 5]])) {
console.log(i);
}
//=>
1
2
3
4
5
We take advantage of the for...of loop in a plain and direct way: For each element e, if it is iterable,
treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01730))_
- These three lines say, in essence, 'yield all the elements of TreeIterable(e) , in order. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01734))_
- append iterates over a collection of iterables, one element at a time. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01736))_
- Tucked inside of it is the same three-line idiom for yielding each element of an iterable. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01737))_
- The operations on iterables are tremendously valuable, but let's reiterate why we care: In JavaScript, we build single-responsibility objects, and single-responsibility functions, and we compose these together to build more full-featured objects and algorithms. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01758))_
- Each collection knew how to map itself ( .map ), how to fold itself ( .reduce ), how to filter itself ( .filter ) and how to find one element within itself ( .find ). — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01760))_
- But our objects grow fatter and fatter. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01761))_
- Both expressions evaluate to 220 . — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01782))_
- But it's still illustrative to dissect something important: Array's .map and .filter methods gather their results into new arrays. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01783))_
- Whereas the .map and .filter methods on Pair work with iterators. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01784))_
- This reduces the memory footprint. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01784))_
- Arrays copy-on-read, so every time we perform a map or filter, we get a new array and perform all the computations. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01793))_
- You recall we briefly touched on the idea of infinite collections? Let's make iterable numbers. They have to be lazy, otherwise we couldn't write things like: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01794))_
- Balanced against their flexibility, our 'lazy collections' use structure sharing. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01796))_
- 'The Carpenter' was a JavaScript programmer, well-known for a meticulous attention to detail and love for hand-crafted, exquisitely joined code. The Carpenter normally worked through personal referrals, but from time to time a recruiter would slip through his screen. One such recruiter was Bob Pliss — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01806))_
- Plissken lined up a technical interview with a well-funded startup in San Francisco. The Carpenter arrived early for his meeting with 'Thing Software,' and was shown to conference room 13. A few minutes later, he was joined by one of the company's developers, Christine. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01807))_
- On each square, we randomly place an arrow pointing to one of its four sides. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01814))_
- Consider a finite checkerboard of unknown size. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01814))_
- As the player moves the chequer, they calls out the direction of movement, e.g. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01815))_
- A player moves the chequer, following the rules. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01815))_
- 'What,' Christine asked, 'Do you write in place of the three // ??? placeholders to determine whether the game halts?' — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01822))_
- And just as companies often pick a problem that gives them broad latitude for discussing alternate approaches and determining that depth of a candidate's experience, The Carpenter liked to sketch out solutions that provided an opportunity to judge the interviewer's experience and provide an easy exc — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01825))_
- For that, we'll map the Game iterable to positions. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01830))_
- 'This is a standard idiom we can obtain from libraries, we don't reinvent the wheel. I'll show it here for clarity:' — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01831))_
- 'Armed with this, it's straightforward to map an iterable of directions to an iterable of strings representing positions:' — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01834))_
- The Carpenter reflected. 'Having turned our game loop into an iterable, we can now see that our problem of whether the game terminates is isomorphic to the problem of detecting whether the positions given ever repeat themselves: If the chequer ever returns to a position it has previously visited, it — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01836))_
- 'This is, of course, the most common solution, it is Floyd's cycle-finding algorithm 97 , although there is some academic dispute as to whether Robert Floyd actually discovered it or was misattributed by Knuth.' — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01843))_
- It also cleanly separates the mechanics of the game from the algorithm for detecting cycles in a graph.' — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01847))_
- 'We at the Thing Software company are very grateful you made some time to visit with us, but alas, that is all the time we have today. If we wish to talk to you further, we'll be in touch.' — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01852))_
- The Carpenter never did hear back from them, but the next day there was an email containing a generous contract from Friends of Ghosts ('FOG'), a codename for a stealth startup doing interesting work, and the Thing interview was forgotten. — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01853))_
- Some time later, The Carpenter ran into Bob Plissken at a local technology meet-up. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01854))_
- The Carpenter smiled. 'I forgot about them, it's been a while. So, do They Live?' — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01855))_
- You're essentially calling for the player to clone themselves and call out the directions in parallel.' — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01862))_
- The Carpenter thought about this for a moment. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01863))_
- Consider, for example, the moves in a game. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01872))_
- To save space, we'll ignore rotations and reflections, and we'll model the first player's moves as a stream. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01873))_
- Let's consider move 1 . That produces this board: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01879))_
- For 2 , 4 , 5 , 7 , or 8 , we play 3 and win. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01885))_
- If x plays 4 , we play 7 and win. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01889))_
- If x plays anything else, including 7 , we play 4 and win. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01889))_
- We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01891))_
- Let's use an array. So this: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01900))_
- Our statelessNaughtsAndCrosses function pushes the work of tracking the game's state onto us, the player. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01918))_
- We've done almost the exact same thing here with our naughts and crosses game. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01927))_
- However, our solution inverts the control. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01931))_
- We aren't calling our function with moves, it's calling us. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01931))_
- Canwedothesamethinghere?Atfirst glance, no. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01932))_
- If it was possible, how would it work? — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01935))_
- Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn't call us. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01938))_
- Is translated into this ECMAScript-5 code: — _unextracted: segment carries subject matter but no structured claim was recovered_ _(javascriptallonge.pdf (source-range-0e12e052-01964))_
- He writes about programming on 'Raganwald 222 ,' as well as general-purpose ruminations on 'Braythwayt Dot Com 223 '. — _fragmentary: no subject/predicate region recovered_ _(javascriptallonge.pdf (source-range-0e12e052-02056))_

### Disposition counts

- non-claim: 313
