---
page_id: javascriptallonge-section-that-constant-coffee-craving-const-and-lexical-scope-bbfe0b3d
page_kind: source
summary: That Constant Coffee Craving / const and lexical scope: 13 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-that-constant-coffee-craving-const-and-lexical-scope-bbfe0b3d@9ecd7f4e258c20405854f14db570b936
---

# That Constant Coffee Craving / const and lexical scope

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-that-constant-coffee-craving-nested-blocks-f1c29f4e]] - previous source section: That Constant Coffee Craving / nested blocks
- [[javascriptallonge-section-that-constant-coffee-craving-are-consts-also-from-a-shadowy-planet-12b08c07]] - next source section: That Constant Coffee Craving / are consts also from a shadowy planet?

### Source structure

- [[javascriptallonge-section-that-constant-coffee-craving-614e2fd3]] - broader source section: That Constant Coffee Craving

## Statements

- This seems very straightforward, but alas, there are some semantics of binding names that we need to understand if we're to place const anywhere we like. The first thing to ask ourselves is, what happens if we use const to bind two different values to the 'same' name? _(javascriptallonge.pdf (source-range-c98ab3e6-00433))_
- It's more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we've elided. We can use any expression in there, and that expression can invoke diameter_fn . For example: _(javascriptallonge.pdf (source-range-c98ab3e6-00437))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn . _(javascriptallonge.pdf (source-range-c98ab3e6-00439))_
- This is called lexical scoping 31 , because we can discover where a name is bound by looking at the source code for the program. We can see that PI is bound in an environment surrounding (diameter) => diameter * PI , we don't need to know where diameter_fn is invoked. _(javascriptallonge.pdf (source-range-c98ab3e6-00440))_
- Although we have bound 3 to PI in the environment surrounding diameter_fn(2) , the value that counts is 3.14159265 , the value we bound to PI in the environment surrounding (diameter) ⇒ diameter * PI. _(javascriptallonge.pdf (source-range-c98ab3e6-00443))_
- That much we can carefully work out from the way closures work. Does const work the same way? Let's find out: _(javascriptallonge.pdf (source-range-c98ab3e6-00444))_
- Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-c98ab3e6-00447))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn . _(javascriptallonge.pdf (source-range-c98ab3e6-00439))_
