---
page_id: javascriptallonge-variables-and-bindings
page_kind: concept
summary: topic-concept: 21 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_10d97b4dfed97019@18b1530ce6a192cc72f21a933414343e
---

# variables and bindings

Source: [[javascriptallonge]]

## Procedure

- Right now everything looks simple and straightforward, and we can move on to talk about arguments in more detail. (javascriptallonge.pdf p.41)
- Besides a desire to use long words to sound impressive, this is not going to seem attractive until we find ourselves wanting to discuss the role of the Church of England in 19th century British politics. (javascriptallonge.pdf p.41)
- But there's another reason for learning the word antidisestablishmentarianism : We might learn how prefixes and postfixes work in English grammar. (javascriptallonge.pdf p.41)
- It has a certain important meaning in its own right, and it's also an excellent excuse to learn about functions that make functions, environments, variables, and more. (javascriptallonge.pdf p.41)
- The second x , the one in => x , is not an argument, it's an expression referring to a variable . (javascriptallonge.pdf p.41)
- Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. (javascriptallonge.pdf p.41)
- This has interesting applications, and they will be explored much more thoroughly in Functions That Are Applied to Functions. (javascriptallonge.pdf p.41)
- 24 We said that you can 't apply a function to an expression. (javascriptallonge.pdf p.41)
- You can apply a function to one or more functions. (javascriptallonge.pdf p.41)
- When you apply the function to the arguments, an entry is placed in the dictionary for each argument. (javascriptallonge.pdf p.42)
- Well for arguments, that is very simple. (javascriptallonge.pdf p.42)
- The value '2' is bound to the name 'x' in the environment. (javascriptallonge.pdf p.42)
- The expression 'x' (the right side of the function) is evaluated within the environment we just created. (javascriptallonge.pdf p.42)
- The value of a variable when evaluated in an environment is the value bound to the variable's name in that environment, which is '2'. (javascriptallonge.pdf p.42)
- meaning, that the environment is a dictionary, and that the value 2 is bound to the name x , and that there might be other stuff in that dictionary we aren't discussing right now. (javascriptallonge.pdf p.42)

## Required tables and formulas

<a id="atom-1"></a>
**Atom:** formula

```
One sub-expression, (x) => x evaluates to a function.
```


## Rules and exceptions

- Right now everything looks simple and straightforward, and we can move on to talk about arguments in more detail. (javascriptallonge.pdf p.41)
- 24 We said that you can 't apply a function to an expression. (javascriptallonge.pdf p.41)
- You can apply a function to one or more functions. (javascriptallonge.pdf p.41)

## Related pages

- [[javascriptallonge-ah-i-d-like-to-have-an-argument-please-22]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-call-by-sharing]] - contextualizes: source-supported topic dependency
