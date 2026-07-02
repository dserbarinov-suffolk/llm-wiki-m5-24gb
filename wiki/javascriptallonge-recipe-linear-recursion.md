---
page_id: javascriptallonge-recipe-linear-recursion
page_kind: recipe
summary: linear recursion: reusable source-backed pattern with 19 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: linear-recursion
projection_coverage: recipe-javascriptallonge-recipe-linear-recursion@1859035567f8a60f3b7ae1c422a2da77
---

# linear recursion

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-linear-recursion-4f6c918d]].
- Evidence roles: decision, procedure, explanation, definition, constraint, example.

## Applicability And Rationale

- When promising students are trying to choose between pure mathematics and applied engineering, they are given a two-part aptitude test. _(javascriptallonge.pdf (source-range-0e12e052-00901))_
- In the first part, they are led to a laboratory bench and told to follow the instructions printed on the card. _(javascriptallonge.pdf (source-range-0e12e052-00901))_
- After a bit the water boils, and they turn off the burner and are lead to a second bench. _(javascriptallonge.pdf (source-range-0e12e052-00902))_
- Of course, all the students know what to do: They fill the beaker with water, place the stand on the burner and the beaker on the stand, then they turn the burner on and use the sparker to ignite the flame. _(javascriptallonge.pdf (source-range-0e12e052-00902))_
- Once again, there is a card that reads, 'boil water.' But this time, the beaker is on the stand over the burner, as left behind by the previous student. _(javascriptallonge.pdf (source-range-0e12e052-00903))_
- Whereas the mathematicians take the beaker off the stand and empty it, thus reducing the situation to a problem they have already solved. _(javascriptallonge.pdf (source-range-0e12e052-00903))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00912)_

```
Array.isArray("foo")
//=> false
Array.isArray(["foo"])
//=> true
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00916)_

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

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-linear-recursion-4f6c918d]]
