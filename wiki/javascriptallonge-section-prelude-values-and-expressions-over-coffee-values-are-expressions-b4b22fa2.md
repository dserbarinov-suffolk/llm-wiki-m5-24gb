---
page_id: javascriptallonge-section-prelude-values-and-expressions-over-coffee-values-are-expressions-b4b22fa2
page_kind: source
summary: Prelude: Values and Expressions over Coffee / values are expressions: 30 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-prelude-values-and-expressions-over-coffee-values-are-expressions-b4b22fa2@4b1f3f58a3dae8b0579d057f9b00d568
---

# Prelude: Values and Expressions over Coffee / values are expressions

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-prelude-values-and-expressions-over-coffee-value-types-cb5b0b74]] - next source section: Prelude: Values and Expressions over Coffee / value types

### Source structure

- [[javascriptallonge-section-prelude-values-and-expressions-over-coffee-9ed49287]] - broader source section: Prelude: Values and Expressions over Coffee

### Recipes

- [[javascriptallonge-recipe-values-are-expressions]] - recipe pattern: values are expressions

## Statements

- All values are expressions. Say you hand the barista a café Cubano. Yup, you hand over a cup with some coffee infused through partially caramelized sugar. You say, 'I want one of these.' The barista is no fool, she gives it straight back to you, and you get exactly what you want. Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). _(javascriptallonge.pdf (source-range-c98ab3e6-00099))_
- The answer is, this is both an expression and a value. 10 The way you can tell that it's both is very easy: When you type it into JavaScript, you get the same thing back, just like our café Cubano: _(javascriptallonge.pdf (source-range-c98ab3e6-00103))_
- All values are expressions. That's easy! Are there any other kinds of expressions? Sure! let's go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let's hand over some ground coffee plus some boiling water. _(javascriptallonge.pdf (source-range-c98ab3e6-00105))_
- Astute readers will realize we're omitting something. Congratulations! Take a sip of espresso. We'll get to that in a moment. _(javascriptallonge.pdf (source-range-c98ab3e6-00106))_
- Now the barista gives us back an espresso. And if we hand over the espresso, we get the espresso right back. So, boiling water plus ground coffee is an expression, but it isn't a value. 11 Boiling water is a value. Ground coffee is a value. Espresso is a value. Boiling water plus ground coffee is an expression. _(javascriptallonge.pdf (source-range-c98ab3e6-00107))_
- First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types . For example, the string "2" is not the same thing as the number 2 . Strings and numbers are different types, so strings and numbers are never identical: _(javascriptallonge.pdf (source-range-c98ab3e6-00116))_
- Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 . _(javascriptallonge.pdf (source-range-c98ab3e6-00118))_
- Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). _(javascriptallonge.pdf (source-range-c98ab3e6-00099))_
- And then you're shown another cup of coffee. _(javascriptallonge.pdf (source-range-c98ab3e6-00115))_
- For example, the string "2" is not the same thing as the number 2 . _(javascriptallonge.pdf (source-range-c98ab3e6-00116))_
- This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 . _(javascriptallonge.pdf (source-range-c98ab3e6-00118))_

## Technical atoms

### Technical frame 1: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00105))_

> All values are expressions. That's easy! Are there any other kinds of expressions? Sure! let's go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let's hand over some ground coffee plus some boiling water.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00104))_

<a id="atom-technical-atom-b864e01d2b117c1e"></a>
```
42
//=> 42
```

### Technical frame 2: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00106))_

> Astute readers will realize we're omitting something. Congratulations! Take a sip of espresso. We'll get to that in a moment.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00107))_

<a id="atom-technical-atom-fe6c24dbca825fef"></a>
> And if we hand over the espresso, we get the espresso right back.
