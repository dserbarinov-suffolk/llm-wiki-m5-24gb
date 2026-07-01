---
page_id: javascriptallonge-section-and-also-variables-and-bindings-baf19230
page_kind: source
summary: And also: / variables and bindings: 20 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-variables-and-bindings-baf19230@0cc58f972024a0ee4868ed2117892ac2
---

# And also: / variables and bindings

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-0e29dfba]] - broader source section: And also:
- [[javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-1153c61b]] - previous source section: And also: / Ah. I'd Like to Have an Argument, Please. 22
- [[javascriptallonge-section-and-also-call-by-sharing-db439a98]] - next source section: And also: / call by sharing

## Statements

- Right now everything looks simple and straightforward, and we can move on to talk about arguments in more detail. And we're going to work our way up from (diameter) => diameter * 3.14159265 to functions like: _(javascriptallonge.pdf (source-range-0e12e052-00293))_
- (x) => (y) => x just looks crazy, as if we are learning English as a second language and the teacher promises us that soon we will be using words like antidisestablishmentarianism . Besides a desire to use long words to sound impressive, this is not going to seem attractive until we find ourselves wanting to discuss the role of the Church of England in 19th century British politics. _(javascriptallonge.pdf (source-range-0e12e052-00295))_
- But there's another reason for learning the word antidisestablishmentarianism : We might learn how prefixes and postfixes work in English grammar. It's the same thing with (x) => (y) => x . It has a certain important meaning in its own right, and it's also an excellent excuse to learn about functions that make functions, environments, variables, and more. _(javascriptallonge.pdf (source-range-0e12e052-00296))_
- In order to talk about how this works, we should agree on a few terms (you may already know them, but let's check-in together and 'synchronize our dictionaries'). The first x , the one in (x) => ... , is an argument . The y in function (y) ... is another argument. The second x , the one in => x , is not an argument, it's an expression referring to a variable . Arguments and variables work the same way whether we're talking about (x) => (y) => x or just plain (x) => x . _(javascriptallonge.pdf (source-range-0e12e052-00297))_
- Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. An environment is a (possibly empty) dictionary that maps variables to values by name. The x in the expression that we call a 'variable' is itself an expression that is evaluated by looking up the value in the environment. _(javascriptallonge.pdf (source-range-0e12e052-00298))_
- 24 We said that you can't apply a function to an expression. You can apply a function to one or more functions. Functions are values! This has interesting applications, and they will be explored much more thoroughly in Functions That Are Applied to Functions. _(javascriptallonge.pdf (source-range-0e12e052-00299))_
- How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dictionary for each argument. So when we write: _(javascriptallonge.pdf (source-range-0e12e052-00300))_
- The value '2' is bound to the name 'x' in the environment. _(javascriptallonge.pdf (source-range-0e12e052-00309))_
- The expression 'x' (the right side of the function) is evaluated within the environment we just created. _(javascriptallonge.pdf (source-range-0e12e052-00310))_
- The value of a variable when evaluated in an environment is the value bound to the variable's name in that environment, which is '2' _(javascriptallonge.pdf (source-range-0e12e052-00311))_
- When we talk about environments, we'll use an unsurprising syntax 25 for showing their bindings: {x: 2, ...} . meaning, that the environment is a dictionary, and that the value 2 is bound to the name x , and that there might be other stuff in that dictionary we aren't discussing right now. _(javascriptallonge.pdf (source-range-0e12e052-00313))_
- Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. _(javascriptallonge.pdf (source-range-0e12e052-00298))_
- - The expression 'x' (the right side of the function) is evaluated within the environment we just created. _(javascriptallonge.pdf (source-range-0e12e052-00310))_
