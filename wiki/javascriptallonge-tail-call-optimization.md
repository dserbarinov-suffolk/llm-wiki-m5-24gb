---
page_id: javascriptallonge-tail-call-optimization
page_kind: concept
summary: topic-concept: 18 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_5727a692f5bce3a2@10619f0425653ebfde01335d8ce2d547
---

# tail-call optimization

Source: [[javascriptallonge]]

## Statements

- A'tail-call' occurs when a function's last act is to invoke another function, and then return whatever the other function returns. (javascriptallonge.pdf p.119)
- This is a tail-call, because it invokes another function and returns its result. (javascriptallonge.pdf p.119)
- It isn't going to do any more work, so it can throw its existing stack frame away. (javascriptallonge.pdf p.119)
- There are three places it returns. (javascriptallonge.pdf p.119)
- This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. (javascriptallonge.pdf p.119)
- But the third is fn.apply(this, args) . (javascriptallonge.pdf p.119)
- And in fact, it does exactly that: It throws the stack frame away, and does not consume extra memory when making a maybe -wrapped call. (javascriptallonge.pdf p.119)
- This is a very important characteristic of JavaScript: If a function makes a call in tail position, JavaScript optimizes away the function call overhead and stack space. (javascriptallonge.pdf p.119)
- That is excellent, but one wrapping is not a big deal. (javascriptallonge.pdf p.119)
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) . (javascriptallonge.pdf p.119)
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length , the other happens after the recursive call. (javascriptallonge.pdf p.119)

## Rules

- It isn't going to do any more work, so it can throw its existing stack frame away. (javascriptallonge.pdf p.119)
- This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. (javascriptallonge.pdf p.119)
- And in fact, it does exactly that: It throws the stack frame away, and does not consume extra memory when making a maybe -wrapped call. (javascriptallonge.pdf p.119)
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length , the other happens after the recursive call. (javascriptallonge.pdf p.119)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

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

<a id="atom-2"></a>
**Atom:** code block

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: 1 + length(rest);
```


## Related pages

- [[javascriptallonge-converting-non-tail-calls-to-tail-calls]] - contextualizes: source-supported topic dependency
