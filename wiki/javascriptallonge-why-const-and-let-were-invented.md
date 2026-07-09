---
page_id: javascriptallonge-why-const-and-let-were-invented
page_kind: concept
summary: topic-concept: 13 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_6dec1904ea3d9de4@f7fbafc4f2686c29f63d6c7c3d8f6a53
---

# why const and let were invented

Source: [[javascriptallonge]]

## Statements

- For nearly twenty years, variables were declared with var (not counting parameters and function declarations, of course). (javascriptallonge.pdf p.154)
- However, its functional scope was a problem. (javascriptallonge.pdf p.154)
- We haven't looked at it yet, but JavaScript provides a for loop for your iterating pleasure and convenience. (javascriptallonge.pdf p.154)
- Hopefully, you can think of a faster way to calculate this sum. (javascriptallonge.pdf p.154)
- 72 And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. (javascriptallonge.pdf p.154)
- 72 There is a well known story about Karl Friedrich Gauss when he was in elementary school. (javascriptallonge.pdf p.154)
- The other kids were adding the numbers like this: 1 + 2 + 3 + . (javascriptallonge.pdf p.154)
- But Gauss rearranged the numbers to add them like this: (1 + 100) + (2 + 99) + (3 + 98) + . (javascriptallonge.pdf p.154)
- There are 50 pairs of numbers, so the answer is 50*101 = 5050. (javascriptallonge.pdf p.154)
- If you notice every pair of numbers adds up to 101. (javascriptallonge.pdf p.154)

## Rules

- Hopefully, you can think of a faster way to calculate this sum. (javascriptallonge.pdf p.154)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
var sum = 0;
for (var i = 1; i <= 100; i++) {
sum = sum + i
}
sum
#=> 5050
```


## Related pages

- [[javascriptallonge-mixing-let-and-const]] - contextualizes: source-supported topic dependency
