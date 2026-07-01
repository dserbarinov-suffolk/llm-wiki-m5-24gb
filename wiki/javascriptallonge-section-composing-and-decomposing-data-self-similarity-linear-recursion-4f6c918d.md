---
page_id: javascriptallonge-section-composing-and-decomposing-data-self-similarity-linear-recursion-4f6c918d
page_kind: source
summary: Composing and Decomposing Data / Self-Similarity / linear recursion: 28 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-self-similarity-linear-recursion-4f6c918d@a1bd920953e31b995561cc0631f2a1d7
---

# Composing and Decomposing Data / Self-Similarity / linear recursion

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-4cbf7d4f]] - broader source section: Composing and Decomposing Data / Self-Similarity
- [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-mapping-c68b0f1d]] - next source section: Composing and Decomposing Data / Self-Similarity / mapping

## Statements

- When promising students are trying to choose between pure mathematics and applied engineering, they are given a two-part aptitude test. In the first part, they are led to a laboratory bench and told to follow the instructions printed on the card. They find a bunsen burner, a sparker, a tap, an empty beaker, a stand, and a card with the instructions 'boil water.' _(javascriptallonge.pdf (source-range-0e12e052-00901))_
- Of course, all the students know what to do: They fill the beaker with water, place the stand on the burner and the beaker on the stand, then they turn the burner on and use the sparker to ignite the flame. After a bit the water boils, and they turn off the burner and are lead to a second bench. _(javascriptallonge.pdf (source-range-0e12e052-00902))_
- Once again, there is a card that reads, 'boil water.' But this time, the beaker is on the stand over the burner, as left behind by the previous student. The engineers light the burner immediately. Whereas the mathematicians take the beaker off the stand and empty it, thus reducing the situation to a problem they have already solved. _(javascriptallonge.pdf (source-range-0e12e052-00903))_
- There is more to recursive solutions that simply functions that invoke themselves. Recursive algorithms follow the 'divide and conquer' strategy for solving a problem: _(javascriptallonge.pdf (source-range-0e12e052-00904))_
- When all small problems have been solved, compose the solutions into one big solution _(javascriptallonge.pdf (source-range-0e12e052-00908))_
- The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. Our solutions are a little simpler in that we don't really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. _(javascriptallonge.pdf (source-range-0e12e052-00909))_
- This simpler form of 'divide and conquer' is called linear recursion . It's very useful and simple to understand. Let's take another example. Sometimes we want to flatten an array, that is, an array of arrays needs to be turned into one array of elements that aren't arrays. 62 _(javascriptallonge.pdf (source-range-0e12e052-00910))_
- We already know how to divide arrays into smaller pieces. How do we decide whether a smaller problem is solvable? We need a test for the terminal case. Happily, there is something along these lines provided for us: _(javascriptallonge.pdf (source-range-0e12e052-00911))_
- The usual 'terminal case' will be that flattening an empty array will produce an empty array. The next terminal case is that if an element isn't an array, we don't flatten it, and can put it together with the rest of our solution directly. Whereas if an element is an array, we'll flatten it and put it together with the rest of our solution. _(javascriptallonge.pdf (source-range-0e12e052-00913))_
- 62 flatten is a very simple unfold, a function that takes a seed value and turns it into an array. Unfolds can be thought of a 'path' through a data structure, and flattening a tree is equivalent to a depth-first traverse. _(javascriptallonge.pdf (source-range-0e12e052-00915))_
- Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions. _(javascriptallonge.pdf (source-range-0e12e052-00917))_
- After a bit the water boils, and they turn off the burner and are lead to a second bench. _(javascriptallonge.pdf (source-range-0e12e052-00902))_
- Of course, all the students know what to do: They fill the beaker with water, place the stand on the burner and the beaker on the stand, then they turn the burner on and use the sparker to ignite the flame. _(javascriptallonge.pdf (source-range-0e12e052-00902))_
- Whereas the mathematicians take the beaker off the stand and empty it, thus reducing the situation to a problem they have already solved. _(javascriptallonge.pdf (source-range-0e12e052-00903))_
- Our solutions are a little simpler in that we don't really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. _(javascriptallonge.pdf (source-range-0e12e052-00909))_
- The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. _(javascriptallonge.pdf (source-range-0e12e052-00909))_
- This simpler form of 'divide and conquer' is called linear recursion . _(javascriptallonge.pdf (source-range-0e12e052-00910))_
- Whereas if an element is an array, we'll flatten it and put it together with the rest of our solution. _(javascriptallonge.pdf (source-range-0e12e052-00913))_
