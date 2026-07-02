---
page_id: javascriptallonge-recipe-representing-naughts-and-crosses-as-a-stateful-function
page_kind: recipe
summary: representing naughts and crosses as a stateful function: reusable source-backed pattern with 3 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: representing-naughts-and-crosses-as-a-stateful-function
projection_coverage: recipe-javascriptallonge-recipe-representing-naughts-and-crosses-as-a-stateful-function@9d214395291b1cacd80b84941c8c77dc
---

# representing naughts and crosses as a stateful function

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateful-function-50fe6464]].
- Evidence roles: decision, example.

## Applicability And Rationale

- Our 'API' will work like this: When we want a new game, we'll call a function that will return a game function, We'll call the game function repeatedly, passing our moves, and get the opponent's moves from it. _(javascriptallonge.pdf (source-range-0e12e052-01918))_
- In that case, we need a stateful function. _(javascriptallonge.pdf (source-range-0e12e052-01918))_
- The state is encoded entirely in data. _(javascriptallonge.pdf (source-range-0e12e052-01924))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01920)_

```
const aNaughtsAndCrossesGame = statefulNaughtsAndCrosses();
// our opponent makes the first move
aNaughtsAndCrossesGame()
//=> 0
// then we move, and get its next move back
aNaughtsAndCrossesGame(1)
//=> 6
// then we move, and get its next move back
aNaughtsAndCrossesGame(4)
//=> 3
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01922)_

```
const statefulNaughtsAndCrosses = () => {
const state = [
' ', ' ', ' ',
' ', ' ', ' ',
' ', ' ', ' '
];
return (x = false) => {
if (x) {
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01923)_

```
if (state[x] === ' ') {
state[x] = 'x';
}
else throw "occupied!"
}
let o = moveLookupTable[state];
state[o] = 'o';
return o;
}
};
const aNaughtsAndCrossesGame = statefulNaughtsAndCrosses();
// our opponent makes the first move
aNaughtsAndCrossesGame()
//=> 0
// then we move, and get its next move back
aNaughtsAndCrossesGame(1)
//=> 6
// then we move, and get its next move back
aNaughtsAndCrossesGame(4)
//=> 3
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateful-function-50fe6464]]
