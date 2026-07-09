---
page_id: javascriptallonge-representing-naughts-and-crosses-as-a-stateful-function
page_kind: concept
summary: topic-concept: 7 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_bd24fee2cbabc0db@1c68c9441d4eb684444c8a16f1ae8aff
---

# representing naughts and crosses as a stateful function

Source: [[javascriptallonge]]

## Statements

- Our 'API' will work like this: When we want a new game, we'll call a function that will return a game function, We'll call the game function repeatedly, passing our moves, and get the opponent's moves from it. (javascriptallonge.pdf p.279)
- In that case, we need a stateful function. (javascriptallonge.pdf p.279)
- The state is encoded entirely in data. (javascriptallonge.pdf p.280)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

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

<a id="atom-2"></a>
**Atom:** code block

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

<a id="atom-3"></a>
**Atom:** code block

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


## Related pages

- [[javascriptallonge-this-seems-familiar]] - contextualizes: source-supported topic dependency
