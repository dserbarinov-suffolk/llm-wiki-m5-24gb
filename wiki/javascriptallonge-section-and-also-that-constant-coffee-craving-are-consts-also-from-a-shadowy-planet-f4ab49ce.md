---
page_id: javascriptallonge-section-and-also-that-constant-coffee-craving-are-consts-also-from-a-shadowy-planet-f4ab49ce
page_kind: source
summary: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: 32 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-that-constant-coffee-craving-are-consts-also-from-a-shadowy-planet-f4ab49ce@b927da53d618a3f8271089658554f06b
---

# And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-that-constant-coffee-craving-ac9d9918]] - broader source section: And also: / That Constant Coffee Craving
- [[javascriptallonge-section-and-also-that-constant-coffee-craving-const-and-lexical-scope-326031a2]] - previous source section: And also: / That Constant Coffee Craving / const and lexical scope
- [[javascriptallonge-section-and-also-that-constant-coffee-craving-rebinding-145a514e]] - next source section: And also: / That Constant Coffee Craving / rebinding

## Statements

- We just saw that values bound with const use lexical scope, just like values bound with parameters. They are looked up in the environment where they are declared. And we know that functions create environments. Parameters are declared when we create functions, so it makes sense that parameters are bound to environments created when we invoke functions. _(javascriptallonge.pdf (source-range-0e12e052-00459))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. So where are const variables bound? In the function environment? Or in an environment corresponding to the block? _(javascriptallonge.pdf (source-range-0e12e052-00460))_
- We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-0e12e052-00461))_
- And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the 'outer' environment? Let's rewrite things slightly differently: _(javascriptallonge.pdf (source-range-0e12e052-00468))_
- Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . Does that binding 'overwrite' the outer one? Will our function return 6 or 6.2831853 ? This is a book, you've already scanned ahead, so you know that the answer is no , the inner binding does not overwrite the outer binding: _(javascriptallonge.pdf (source-range-0e12e052-00470))_
- We say that when we bind a variable using a parameter inside another binding, the inner binding shadows the outer binding. It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-0e12e052-00472))_
- Parameters are only bound when we invoke a function. That's why we made all these IIFEs. But const statements can appear inside blocks. What happens when we use a const inside of a block? We'll need a gratuitous block. We've seen if statements, what could be more gratuitous than: _(javascriptallonge.pdf (source-range-0e12e052-00476))_
- Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it. _(javascriptallonge.pdf (source-range-0e12e052-00484))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. _(javascriptallonge.pdf (source-range-0e12e052-00460))_
- Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . _(javascriptallonge.pdf (source-range-0e12e052-00470))_
- We say that when we bind a variable using a parameter inside another binding, the inner binding shadows the outer binding. _(javascriptallonge.pdf (source-range-0e12e052-00472))_
- It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-0e12e052-00472))_
- Parameters are only bound when we invoke a function. _(javascriptallonge.pdf (source-range-0e12e052-00476))_
- But const statements can appear inside blocks. _(javascriptallonge.pdf (source-range-0e12e052-00476))_
- This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. _(javascriptallonge.pdf (source-range-0e12e052-00484))_
- Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it. _(javascriptallonge.pdf (source-range-0e12e052-00484))_
