---
page_id: javascriptallonge-carpenter-s-solution
page_kind: concept
summary: the carpenter's solution: 12 accepted assertion(s) and 7 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_1cd0b0b915ba47e1@4817238ff039f8dbd7c149429599ea48
---

# the carpenter's solution

Source: [[javascriptallonge]]

## Statements

- He then coached subsequent candidates to give polished answers to the company's pet technical questions. (javascriptallonge.pdf p.264)
- The Carpenter was not surprised at the problem. (javascriptallonge.pdf p.264)
- To save time, The Carpenter had prepared the same answer for both questions. (javascriptallonge.pdf p.264)
- Bob had , in fact, warned The Carpenter that 'Thing' liked to ask either or both of two questions: Determine how to detect a loop in a linked list, and determine whether the chequerboard game would halt. (javascriptallonge.pdf p.264)
- I'll refactor a touch to make things clearer, for example I'll extract the board to make it easier to test:'. (javascriptallonge.pdf p.264)
- The Carpenter coughed softly, then began. (javascriptallonge.pdf p.264)
- A statefulMap is a lazy map that preserves state from iteration to iteration. (javascriptallonge.pdf p.265)
- That's what we need , because we need to know the current position to map each move to the next position.'. (javascriptallonge.pdf p.265)
- Detecting whether the game terminates is equivalent to detecting whether the graph contains a cycle.'. (javascriptallonge.pdf p.266)
- I approached this question in that spirit. (javascriptallonge.pdf p.267)
- The question was , Given a linked list, detect whether it contains a cycle. (javascriptallonge.pdf p.268)
- I have never forgotten the question, or the general form of the solution. (javascriptallonge.pdf p.268)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const MOVE = {
"￿": ([x, y]) => [x - 1, y],
"￿": ([x, y]) => [x + 1, y],
"￿": ([x, y]) => [x, y + 1],
"￿": ([x, y]) => [x, y - 1]
};
const Board = (size = 8) => {
// initialize the board
const board = [];
for (let i = 0; i < size; ++i) {
board[i] = [];
for (let j = 0; j < size; ++j) {
board[i][j] = '￿￿￿￿'[Math.floor(Math.random() * 4)];
}
}
// initialize the position
const position = [
```

<a id="atom-2"></a>
**Atom:** code block

```
Math.floor(Math.random() * size),
Math.floor(Math.random() * size)
];
return {board, position};
};
const Game = ({board, position}) => {
const size = board[0].length;
return ({
*[Symbol.iterator] () {
let [x, y] = position;
while (x >= 0 && y >=0 && x < size && y < size) {
const direction = board[y][x];
yield direction;
[x, y] = MOVE[direction]([x, y]);
}
}
});
};
```

<a id="atom-3"></a>
**Atom:** code block

```
const statefulMapWith = (fn, seed, iterable) =>
({
*[Symbol.iterator] () {
let value,
state = seed;
for (let element of iterable) {
[state, value] = fn(state, element);
yield value;
```

<a id="atom-4"></a>
**Atom:** code block

```
}
}
});
```

<a id="atom-5"></a>
**Atom:** code block

```
const positionsOf = (game) =>
statefulMapWith(
(position, direction) => {
const [x, y] =
MOVE[direction](position);
position = [x, y];
return [position, `x: ${x}, y: ${y}`];
},
[0, 0],
game);
```

<a id="atom-6"></a>
**Atom:** code block

```
const tortoiseAndHare = (iterable) => {
const hare = iterable[Symbol.iterator]();
let hareResult = (hare.next(), hare.next());
for (let tortoiseValue of iterable) {
hareResult = hare.next();
if (hareResult.done) {
return false;
}
if (tortoiseValue === hareResult.value) {
return true;
}
hareResult = hare.next();
if (hareResult.done) {
return false;
}
if (tortoiseValue === hareResult.value) {
return true;
}
}
return false;
};
```

<a id="atom-7"></a>
**Atom:** code block

```
const terminates = (game) =>
tortoiseAndHare(positionsOf(game))
const test = [
["￿","￿","￿","￿"],
["￿","￿","￿","￿"],
["￿","￿","￿","￿"],
["￿","￿","￿","￿"]
];
terminates(Game({board: test, position: [0, 0]}))
//=> false
terminates(Game({board: test, position: [3, 0]}))
//=> true
terminates(Game({board: test, position: [0, 3]}))
//=> false
terminates(Game({board: test, position: [3, 3]}))
//=> false
```
