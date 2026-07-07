---
page_id: javascriptallonge-section-composing-and-decomposing-data-self-similarity-ea23a471
page_kind: source
summary: Composing and Decomposing Data / Self-Similarity: 28 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-self-similarity-ea23a471@8d4ccf563f73431964a6c7c313e1730f
---

# Composing and Decomposing Data / Self-Similarity

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-2a38bfc8]] - previous source section: Composing and Decomposing Data / Arrays and Destructuring Arguments
- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-b4311a56]] - next source section: Composing and Decomposing Data / Tail Calls (and Default Arguments)

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-99b4771a]] - broader source section: Composing and Decomposing Data
- [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-folding-be06a8d2]] - narrower source section: Composing and Decomposing Data / Self-Similarity / folding
- [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-linear-recursion-fad0c717]] - narrower source section: Composing and Decomposing Data / Self-Similarity / linear recursion
- [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-mapping-bf63b383]] - narrower source section: Composing and Decomposing Data / Self-Similarity / mapping

## Statements

- Recursion is the root of computation since it trades description for time.-Alan Perlis, Epigrams in Programming 60 _(javascriptallonge.pdf (source-range-c98ab3e6-00863))_
- In Arrays and Destructuring Arguments, we worked with the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-c98ab3e6-00864))_
- We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-c98ab3e6-00865))_
- Let's be more specific. Some data structures, like lists, can obviously be seen as a collection of items. Some are empty, some have three items, some forty-two, some contain numbers, some contain strings, some a mixture of elements, there are all kinds of lists. _(javascriptallonge.pdf (source-range-c98ab3e6-00866))_
- Let's convert our rules to array literals. The first rule is simple: [] is a list. How about the second rule? We can express that using a spread. Given an element e and a list list , [e, ...list] is a list. We can test this manually by building up a list: _(javascriptallonge.pdf (source-range-c98ab3e6-00870))_
- Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists: _(javascriptallonge.pdf (source-range-c98ab3e6-00872))_
- Armed with our definition of an empty list and with what we've already learned, we can build a great many functions that operate on arrays. We know that we can get the length of an array using its .length . But as an exercise, how would we write a length function using just what we have already? _(javascriptallonge.pdf (source-range-c98ab3e6-00877))_
- 61 Well, actually, this does not work for arrays that contain undefined as a value, but we are not going to see that in our examples. A more robust implementation would be (array) => array.length === 0 , but we are doing backflips to keep this within a very small and contrived playground. _(javascriptallonge.pdf (source-range-c98ab3e6-00878))_
- We need something for when the array isn't empty. If an array is not empty, and we break it into two pieces, first and rest , the length of our array is going to be length(first) + length(rest) . Well, the length of first is 1 , there's just one element at the front. But we don't know the length of rest . If only there was a function we could call… Like length ! _(javascriptallonge.pdf (source-range-c98ab3e6-00881))_
- Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-c98ab3e6-00884))_
- If only there was a function we could call… Like length ! _(javascriptallonge.pdf (source-range-c98ab3e6-00881))_
- This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-c98ab3e6-00884))_

## Statements by subsection

### Composing and Decomposing Data / Self-Similarity / summary

- Linear recursion is a basic building block of algorithms. Its basic form parallels the way linear data structures like lists are constructed: This helps make it understandable. Its specialized cases of mapping and folding are especially useful and can be used to build other functions. And finally, while folding is a special case of linear recursion, mapping is a special case of folding. _(javascriptallonge.pdf (source-range-c98ab3e6-00932))_
