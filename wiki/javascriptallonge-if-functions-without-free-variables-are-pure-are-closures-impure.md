---
page_id: javascriptallonge-if-functions-without-free-variables-are-pure-are-closures-impure
page_kind: concept
summary: topic-concept: 25 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_95c171106b1915f6@66ddeabe0b628f05ff7e0f67f72e369b
---

# if functions without free variables are pure, are closures impure?

Source: [[javascriptallonge]]

## Statements

- 27 A free variable is one that is not bound within the function. (javascriptallonge.pdf p.45)
- Since the function (y) => x doesn't have an argument named x , the variable x isn't bound in this function, which makes it 'free.'. (javascriptallonge.pdf p.45)
- It contains a free variable , x . (javascriptallonge.pdf p.45)
- Now that we know that variables used in a function are either bound or free, we can bifurcate functions into those with free variables and those without:. (javascriptallonge.pdf p.45)
- Functions containing no free variables are called pure functions . (javascriptallonge.pdf p.45)
- Functions containing one or more free variables are called closures . (javascriptallonge.pdf p.45)
- Pure functions are easiest to understand. (javascriptallonge.pdf p.45)
- They always mean the same thing wherever you use them. (javascriptallonge.pdf p.45)
- The second doesn't have any free variables, because its only variable is bound. (javascriptallonge.pdf p.45)
- The first function doesn't have any variables, therefore doesn't have any free variables. (javascriptallonge.pdf p.45)
- The third one is actually two functions, one inside the other. (javascriptallonge.pdf p.45)
- , and it doesn't have a free variable: The only variable anywhere in its body is x , which is certainly bound within (x) => .. (javascriptallonge.pdf p.45)
- From this, we learn something: A pure function can contain a closure. (javascriptallonge.pdf p.45)
- If you can 't, give your reasoning for why it's impossible. (javascriptallonge.pdf p.45)
- Using only what we've learned so far, attempt to compose a closure that contains a pure function. (javascriptallonge.pdf p.45)
- If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . (javascriptallonge.pdf p.45)
- We can 't say what it will do with argument (2) without understanding the magic for evaluating the free variable x . (javascriptallonge.pdf p.45)
- 27 You may also hear the term 'non-local variable.' Both are correct. (javascriptallonge.pdf p.45)

## Rules

- Now that we know that variables used in a function are either bound or free, we can bifurcate functions into those with free variables and those without:. (javascriptallonge.pdf p.45)
- From this, we learn something: A pure function can contain a closure. (javascriptallonge.pdf p.45)
- If you can 't, give your reasoning for why it's impossible. (javascriptallonge.pdf p.45)
- We can 't say what it will do with argument (2) without understanding the magic for evaluating the free variable x . (javascriptallonge.pdf p.45)
- 27 You may also hear the term 'non-local variable.' Both are correct. (javascriptallonge.pdf p.45)

## Technical atoms

<a id="atom-1"></a>
**Atom:** rule

```
If pure functions can contain closures, can a closure contain a pure function?
```


## Related pages

- [[javascriptallonge-it-s-always-the-environment]] - contextualizes: source-supported topic dependency
