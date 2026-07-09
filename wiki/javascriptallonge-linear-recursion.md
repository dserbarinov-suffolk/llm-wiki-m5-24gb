---
page_id: javascriptallonge-linear-recursion
page_kind: concept
summary: linear recursion: 19 accepted assertion(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_72ee3054bba39f38@2d0737af4659f016f951604e74e6dab0
---

# linear recursion

Source: [[javascriptallonge]]

## Statements

- When promising students are trying to choose between pure mathematics and applied engineering, they are given a two-part aptitude test. (javascriptallonge.pdf p.111)
- In the first part, they are led to a laboratory bench and told to follow the instructions printed on the card. (javascriptallonge.pdf p.111)
- Of course, all the students know what to do : They fill the beaker with water, place the stand on the burner and the beaker on the stand, then they turn the burner on and use the sparker to ignite the flame. (javascriptallonge.pdf p.112)
- After a bit the water boils, and they turn off the burner and are lead to a second bench. (javascriptallonge.pdf p.112)
- Once again, there is a card that reads, 'boil water.' But this time, the beaker is on the stand over the burner, as left behind by the previous student. (javascriptallonge.pdf p.112)
- Whereas the mathematicians take the beaker off the stand and empty it, thus reducing the situation to a problem they have already solved. (javascriptallonge.pdf p.112)
- There is more to recursive solutions that simply functions that invoke themselves. (javascriptallonge.pdf p.112)
- When all small problems have been solved, compose the solutions into one big solution. (javascriptallonge.pdf p.112)
- The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. (javascriptallonge.pdf p.112)
- Our solutions are a little simpler in that we don't really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. (javascriptallonge.pdf p.112)
- This simpler form of 'divide and conquer' is called linear recursion . (javascriptallonge.pdf p.112)
- Sometimes we want to flatten an array, that is , an array of arrays needs to be turned into one array of elements that aren't arrays. (javascriptallonge.pdf p.112)
- We need a test for the terminal case. (javascriptallonge.pdf p.112)
- Whereas if an element is an array, we'll flatten it and put it together with the rest of our solution. (javascriptallonge.pdf p.112)
- The usual 'terminal case' will be that flattening an empty array will produce an empty array. (javascriptallonge.pdf p.112)
- The next terminal case is that if an element isn't an array, we don't flatten it, and can put it together with the rest of our solution directly. (javascriptallonge.pdf p.112)
- 62 flatten is a very simple unfold, a function that takes a seed value and turns it into an array. (javascriptallonge.pdf p.112)
- Unfolds can be thought of a 'path' through a data structure, and flattening a tree is equivalent to a depth-first traverse. (javascriptallonge.pdf p.112)
- Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions. (javascriptallonge.pdf p.113)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
Array.isArray("foo")
//=> false
Array.isArray(["foo"])
//=> true
```

<a id="atom-2"></a>
**Atom:** code block

```
const flatten = ([first, ...rest]) => {
if (first === undefined) {
return [];
}
else if (!Array.isArray(first)) {
return [first, ...flatten(rest)];
}
else {
return [...flatten(first), ...flatten(rest)];
}
}
flatten(["foo", [3, 4, []]])
//=> ["foo",3,4]
```
