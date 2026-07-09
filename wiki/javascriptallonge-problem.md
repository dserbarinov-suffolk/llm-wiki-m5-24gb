---
page_id: javascriptallonge-problem
page_kind: concept
summary: the problem: 7 accepted assertion(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_dee345fa6af3e0b9@a66bfd911a99818bc22976bbb14f88ed
---

# the problem

Source: [[javascriptallonge]]

## Statements

- Despite his experience and industry longevity, the Carpenter did not mind being asked to demonstrate that he was, in fact, the person described on the resumé. (javascriptallonge.pdf p.261)
- After some small talk, Christine explained that they liked to ask candidates to whiteboard some code. (javascriptallonge.pdf p.261)
- Many companies use white-boarding code as an excuse to have a technical conversation with a candidate, and The Carpenter felt that being asked to whiteboard code was an excuse to have a technical conversation with a future colleague. (javascriptallonge.pdf p.261)
- A chequer is placed randomly on the checkerboard. (javascriptallonge.pdf p.262)
- Each move consists of moving the chequer one square in the direction of the arrow in the square it occupies. (javascriptallonge.pdf p.262)
- The problem is this: The game board is hidden from us. (javascriptallonge.pdf p.262)
- Your code should not presume anything about the game-board's size or contents, only that it is given an arrow every time though the while loop. (javascriptallonge.pdf p.262-263)

## Technical atoms

<a id="atom-1"></a>
**Atom:** rule

```
If the arrow should cause the chequer to move off the edge of the board, the game halts.
```

<a id="atom-2"></a>
**Atom:** rule

```
You may use babeljs.io 95 , or ES6Fiddle 96 to check your work.
```

<a id="atom-3"></a>
**Atom:** code block

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

<a id="atom-4"></a>
**Atom:** table

```text
95 http://babeljs.io
96 http://www.es6fiddle.net
```
