---
page_id: javascriptallonge-section-picking-the-bean-choice-and-truthiness-d2a76f30
page_kind: source
summary: Picking the Bean: Choice and Truthiness: 9 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-picking-the-bean-choice-and-truthiness-d2a76f30@bb17d3679ec89d2f51c19f6f58c76fff
---

# Picking the Bean: Choice and Truthiness

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-recipes-with-basic-functions-d7445960]] - previous source section: Recipes with Basic Functions
- [[javascriptallonge-section-composing-and-decomposing-data-99b4771a]] - next source section: Composing and Decomposing Data

### Source structure

- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-and-are-control-flow-operators-c8371217]] - narrower source section: Picking the Bean: Choice and Truthiness / || and && are control-flow operators
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-function-parameters-are-eager-699c4c1b]] - narrower source section: Picking the Bean: Choice and Truthiness / function parameters are eager
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-operators-44549e80]] - narrower source section: Picking the Bean: Choice and Truthiness / truthiness and operators
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-the-ternary-operator-b715a907]] - narrower source section: Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

## Statements

- We've seen operators that act on numeric values, like + and % . In addition to numbers, we often need to represent a much more basic idea of truth or falsehood. Is this array empty? Does this person have a middle name? Is this user logged in? _(javascriptallonge.pdf (source-range-c98ab3e6-00735))_
- true and false are value types. All values of true are === all other values of true. We can see that is the case by looking at some operators we can perform on boolean values, ! , && , and || . To being with, ! is a unary prefix operator that negates its argument. So: _(javascriptallonge.pdf (source-range-c98ab3e6-00741))_
- Now, note well: We have said what happens if you pass boolean values to ! , && , and || , but we've said nothing about expressions or about passing other values. We'll look at those presently. _(javascriptallonge.pdf (source-range-c98ab3e6-00745))_

## Statements by subsection

### Picking the Bean: Choice and Truthiness / summary

- Logical operators are based on truthiness and falsiness, not the strict values true and false . _(javascriptallonge.pdf (source-range-c98ab3e6-00789))_
- The ternary operator ( ?: ), || , and && are control flow operators, they do not always return true or false , and they have short-cut semantics. _(javascriptallonge.pdf (source-range-c98ab3e6-00791))_
- Function invocation uses eager evaluation, so if we need to roll our own control-flow semantics, we pass it functions, not expressions. _(javascriptallonge.pdf (source-range-c98ab3e6-00792))_
