---
page_id: javascriptallonge-return-to-backward-thinking
page_kind: concept
summary: topic-concept: 27 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_2433b10f56f8ad1b@241b2f40d37d741fa88ca86893b80793
---

# a return to backward thinking

Source: [[javascriptallonge]]

## Statements

- To make pairs work, we did things backwards , we passed the first and rest functions to the pair, and the pair called our function. (javascriptallonge.pdf p.189)
- But we could have done something completely different. (javascriptallonge.pdf p.189)
- All we know is that we can pass the pair function a function of our own, at it will be called with the elements of the pair. (javascriptallonge.pdf p.189)
- We could have written a pair that stored its elements in an array, or a pair that stored its elements in a POJO. (javascriptallonge.pdf p.189)
- The exact implementation of a pair is hidden from the code that uses a pair. (javascriptallonge.pdf p.189)
- This is a little gratuitous, but it makes the point: The code that uses the data doesn't reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. (javascriptallonge.pdf p.189)
- We're passing list what we want done with an empty list, and what we want done with a list that has at least one element. (javascriptallonge.pdf p.189)
- We then ask list to do it, and provide a way for list to call the code we pass in. (javascriptallonge.pdf p.189)
- We can fix this with an isEmpty function, but now we're pushing even more knowledge about the structure of lists into the code that uses them. (javascriptallonge.pdf p.190)
- It presumes there is one canonical empty list value. (javascriptallonge.pdf p.190)
- It presumes you can compare these things with the === operator. (javascriptallonge.pdf p.190)
- This is a fundamental principle of good design. (javascriptallonge.pdf p.190)
- Having a list know itself whether it is empty hides implementation information from the code that uses lists. (javascriptallonge.pdf p.190)
- It is a tenet of Object-Oriented Programming, but it is not exclusive to OOP: We can and should design data structures to hide implementation information from the code that use them, whether we are working with functions, objects, or both. (javascriptallonge.pdf p.190)
- There are many tools for hiding implementation information, and we have now seen two particularly powerful patterns:. (javascriptallonge.pdf p.190)
- Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. (javascriptallonge.pdf p.190)

## Rules

- But we could have done something completely different. (javascriptallonge.pdf p.189)
- All we know is that we can pass the pair function a function of our own, at it will be called with the elements of the pair. (javascriptallonge.pdf p.189)
- We could have written a pair that stored its elements in an array, or a pair that stored its elements in a POJO. (javascriptallonge.pdf p.189)
- We can fix this with an isEmpty function, but now we're pushing even more knowledge about the structure of lists into the code that uses them. (javascriptallonge.pdf p.190)
- It presumes there is one canonical empty list value. (javascriptallonge.pdf p.190)
- It presumes you can compare these things with the === operator. (javascriptallonge.pdf p.190)
- It is a tenet of Object-Oriented Programming, but it is not exclusive to OOP: We can and should design data structures to hide implementation information from the code that use them, whether we are working with functions, objects, or both. (javascriptallonge.pdf p.190)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

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

<a id="atom-2"></a>
**Atom:** code block

```
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(pairRest)))
);
```

<a id="atom-3"></a>
**Atom:** code block

```
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
```


## Related pages

- [[javascriptallonge-functions-are-not-the-real-point]] - contextualizes: source-supported topic dependency
