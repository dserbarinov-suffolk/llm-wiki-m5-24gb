---
page_id: javascriptallonge-section-recipes-with-data-4b3e2c99
page_kind: source
summary: Recipes with Data: 14 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-data-4b3e2c99@dbe59d7f7f8aff452fe83dd516b8b5c2
---

# Recipes with Data

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-copy-on-write-d081f846]] - previous source section: Copy on Write
- [[javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-519b0d4d]] - next source section: A Warm Cup: Basic Strings and Quasi-Literals

### Source structure

- [[javascriptallonge-section-recipes-with-data-flip-b1a8ea8d]] - narrower source section: Recipes with Data / Flip
- [[javascriptallonge-section-recipes-with-data-mapwith-202c0d4f]] - narrower source section: Recipes with Data / mapWith
- [[javascriptallonge-section-recipes-with-data-object-assign-8d8e0e13]] - narrower source section: Recipes with Data / Object.assign

## Statements by subsection

### Recipes with Data / Disclaimer

- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven't been discussed in the text to this point, such as methods and/or prototypes. The overall use of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-c98ab3e6-01401))_
- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven't been discussed in the text to this point, such as methods and/or prototypes. _(javascriptallonge.pdf (source-range-c98ab3e6-01401))_
- The overall use of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-c98ab3e6-01401))_

### Recipes with Data / Why?

- Why? It enables you to make recursive functions without needing to bind a function to a name in an environment. This has little practical utility in JavaScript, but in combinatory logic it's essential: With fixed-point combinators it's possible to compute everything computable without binding names. _(javascriptallonge.pdf (source-range-c98ab3e6-01462))_
- So again, why include the recipe? Well, besides all of the practical applications that combinators provide, there is this little thing called The joy of working things out. _(javascriptallonge.pdf (source-range-c98ab3e6-01463))_
- There are many explanations of the Y Combinator's mechanism on the internet, but resist the temptation to read any of them: Work it out for yourself. Use it as an excuse to get familiar with your environment's debugging facility. _(javascriptallonge.pdf (source-range-c98ab3e6-01464))_
- One tip is to use JavaScript to name things. For example, you could start by writing: _(javascriptallonge.pdf (source-range-c98ab3e6-01465))_
- What is this something and how does it work? Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-c98ab3e6-01467))_
- Another friendly tip: Change some of the fat arrow functions inside of it into named function expressions to help you decipher stack traces. _(javascriptallonge.pdf (source-range-c98ab3e6-01467))_

## Technical atoms

### Technical frame 1: Recipes with Data / Flip

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01435))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01436))_

<a id="atom-technical-atom-890a831292ffdfc1"></a>
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
