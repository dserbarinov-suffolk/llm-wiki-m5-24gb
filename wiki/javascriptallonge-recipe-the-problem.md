---
page_id: javascriptallonge-recipe-the-problem
page_kind: recipe
summary: the problem: reusable source-backed pattern with 7 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: the-problem
projection_coverage: recipe-javascriptallonge-recipe-the-problem@9377cc50f535b29ef622b37d8a7b550d
---

# the problem

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-interlude-the-carpenter-interviews-for-a-job-the-problem-2249ceea]].
- Evidence roles: decision, constraint, explanation, structured-state, example.

## Applicability And Rationale

- Despite his experience and industry longevity, the Carpenter did not mind being asked to demonstrate that he was, in fact, the person described on the resumé. _(javascriptallonge.pdf (source-range-c98ab3e6-01783))_
- After some small talk, Christine explained that they liked to ask candidates to whiteboard some code. _(javascriptallonge.pdf (source-range-c98ab3e6-01783))_
- Many companies use white-boarding code as an excuse to have a technical conversation with a candidate, and The Carpenter felt that being asked to whiteboard code was an excuse to have a technical conversation with a future colleague. _(javascriptallonge.pdf (source-range-c98ab3e6-01784))_
- A chequer is placed randomly on the checkerboard. _(javascriptallonge.pdf (source-range-c98ab3e6-01787))_
- Each move consists of moving the chequer one square in the direction of the arrow in the square it occupies. _(javascriptallonge.pdf (source-range-c98ab3e6-01787))_
- The problem is this: The game board is hidden from us. _(javascriptallonge.pdf (source-range-c98ab3e6-01788))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01793)_

```
const Game = (size = 8) => {
// initialize the board
const board = [];
for (let i = 0; i < size; ++i) {
board[i] = [];
for (let j = 0; j < size; ++j) {
board[i][j] = '￿￿￿￿'[Math.floor(Math.random() * 4)];
}
}
// initialize the position
let initialPosition = [
2 + Math.floor(Math.random() * (size - 4)),
2 + Math.floor(Math.random() * (size - 4))
];
// ???
let [x, y] = initialPosition;
const MOVE = {
"￿": ([x, y]) => [x - 1, y],
"￿": ([x, y]) => [x + 1, y],
"￿": ([x, y]) => [x, y - 1],
"￿": ([x, y]) => [x, y + 1]
};
while (x >= 0 && y >=0 && x < size && y < size) {
const arrow = board[x][y];
// ???
[x, y] = MOVE[arrow]([x, y]);
}
// ???
};
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-interlude-the-carpenter-interviews-for-a-job-the-problem-2249ceea]]
