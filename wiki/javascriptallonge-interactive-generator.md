---
page_id: javascriptallonge-interactive-generator
page_kind: concept
summary: Interactive Generators: 31 statement(s) and 10 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-interactive-generator@f760c35a335f7d939f8c04cc0d5927a9
---

# Interactive Generators

What [[javascriptallonge]] covers about interactive generators:

## Statements

### Interactive Generators

- We used generators to build iterators that maintain implicit state. We saw how to use them for recursive unfolds and state machines. But there are other times we want to build functions that maintain implicit state. Let's start by looking at a very simple example of a function that can be written statefully. _(javascriptallonge.pdf (source-range-c98ab3e6-01840))_

- Consider, for example, the moves in a game. The moves a player makes are a stream of values, just like the contents of an array can be consider a stream of values. But of course, iterating over a stream of moves requires us to wait for the game to be over so we know what moves were made. _(javascriptallonge.pdf (source-range-c98ab3e6-01842))_

- The first player will always be o , and they will always place their chequer in the top-left corner, coincidentally numbered o : _(javascriptallonge.pdf (source-range-c98ab3e6-01844))_

- x has six possible moves, but they are really just two choices: 3 and anything else: _(javascriptallonge.pdf (source-range-c98ab3e6-01849))_

### Interactive Generators / representing naughts and crosses as a stateless function

- We could plays naughts and crosses as a stateless function. We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. For example, the entry for: _(javascriptallonge.pdf (source-range-c98ab3e6-01854))_

### Interactive Generators / representing naughts and crosses as a stateless function / Would be 3 , producing:

- We can encode the board in several different ways. We could use multiline strings with formatting just as we've written it here, but it is a design smell to couple presentation with modelling. Our function should be just as useful on a teletype as it would be backing a DOM game that uses a table, or a browser game that draws on Canvas. _(javascriptallonge.pdf (source-range-c98ab3e6-01858))_

### Interactive Generators / representing naughts and crosses as a stateless function / Will be represented as:

- We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write: _(javascriptallonge.pdf (source-range-c98ab3e6-01864))_

### Interactive Generators / representing naughts and crosses as a stateful function

- Our statelessNaughtsAndCrosses function pushes the work of tracking the game's state onto us, the player. What if we want to exchange moves with the function? In that case, we need a stateful function. Our 'API' will work like this: When we want a new game, we'll call a function that will return a game function, We'll call the game function repeatedly, passing our moves, and get the opponent's moves from it. _(javascriptallonge.pdf (source-range-c98ab3e6-01874))_

- Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data. _(javascriptallonge.pdf (source-range-c98ab3e6-01880))_

### Interactive Generators / this seems familiar

- When we looked at generators, we saw that some iterators are inherently stateful, but sometimes it is awkward to represent them in a fully stateless fashion. Sometimes there is a state machine that is naturally represented implicitly in JavaScript's control flow rather than explicitly in data. _(javascriptallonge.pdf (source-range-c98ab3e6-01882))_

- We've done almost the exact same thing here with our naughts and crosses game. A game like this is absolutely a state machine, and we've explicitly coded those states into the lookup table. Which leads us to wonder: Is there a way to encode those states implicitly , in JavaScript control flow? _(javascriptallonge.pdf (source-range-c98ab3e6-01883))_

- If we were in full control of the interaction, it would be easy to encode the game play as a decision tree instead of as a lookup table. For example, we could do this in a browser: _(javascriptallonge.pdf (source-range-c98ab3e6-01884))_

- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree. _(javascriptallonge.pdf (source-range-c98ab3e6-01886))_

- However, our solution inverts the control. We aren't calling our function with moves, it's calling us. With iterators, we wrote a generator function using function * , and then used yield to yield values while maintaining the implicit state of the generator's control flow. _(javascriptallonge.pdf (source-range-c98ab3e6-01887))_

- Canwedothesamethinghere?Atfirst glance, no. How do we get the player's moves to the generator function? But the first glance is deceptive, because we only see what we've seen so far. Let's see how it would actually work. _(javascriptallonge.pdf (source-range-c98ab3e6-01888))_

### Interactive Generators / this seems familiar / interactive generators

- So far, we have called iterators (and generators) with .next() . But what if we pass a value to .next() ? If we could do that, a generator function that played naughts and crosses would look like this: _(javascriptallonge.pdf (source-range-c98ab3e6-01890))_

- Served by the Pot: Collections 260 } } break ; // ... } } const aNaughtsAndCrossesGame = generatorNaughtsAndCrosses(); We can then get the first move by calling .next() . Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1).value //=> 6 aNaughtsAndCrossesGame.next(3).value //=> 8 aNaughtsAndCrossesGame.next(7).value //=> 4 _(javascriptallonge.pdf (source-range-c98ab3e6-01893))_

- Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn't call us. It isn't a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. _(javascriptallonge.pdf (source-range-c98ab3e6-01894))_

- But the generator function allows us to maintain state implicitly. And sometimes, we want to use implicit state instead of explicitly storing state in our data. _(javascriptallonge.pdf (source-range-c98ab3e6-01895))_

### Interactive Generators / this seems familiar / summary

- We have looked at generators as ways of making iterators over static collections, where state is modelled implicitly in control flow. But as we see here, it's also possible to use a generator interactively, passing values in and receiving a value in return, just like an ordinary function. _(javascriptallonge.pdf (source-range-c98ab3e6-01897))_

- Again, the salient difference is that an 'interactive' generator is stateful, and it embodies its state in its control flow. _(javascriptallonge.pdf (source-range-c98ab3e6-01898))_

### Interactive Generators / Basic Operations on Iterables

- Here are the operations we've defined on Iterables. As discussed, they preserve the collection semantics of the iterable they are given: _(javascriptallonge.pdf (source-range-c98ab3e6-01900))_


## Technical atoms

### Technical frame 1: Interactive Generators / representing naughts and crosses as a stateless function / Will be represented as:

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01864))_

> We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01863))_

<a id="atom-technical-atom-d38dbc26a4407691"></a>
```
[
'o', 'x', ' ',
'x', ' ', ' ',
'o', ' ', ' '
]
```

### Technical frame 2: Interactive Generators / representing naughts and crosses as a stateless function / Will be represented as:

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01864))_

> We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01865))_

<a id="atom-technical-atom-718d04c176db03f9"></a>
```
const moveLookupTable = {
[[
' ', ' ', ' ',
' ', ' ', ' ',
' ', ' ', ' '
]]: 0,
[[
'o', 'x', ' ',
' ', ' ', ' ',
' ', ' ', ' '
]]: 6,
[[
'o', 'x', 'x',
' ', ' ', ' ',
'o', ' ', ' '
]]: 3,
[[
'o', 'x', ' ',
'x', ' ', ' ',
'o', ' ', ' '
]]: 8,
[[
'o', 'x', ' ',
' ', 'x', ' ',
'o', ' ', ' '
```

### Technical frame 3: Interactive Generators / representing naughts and crosses as a stateless function / Will be represented as:

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01864))_

> We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01866))_

<a id="atom-technical-atom-051504ff8036c61a"></a>
```
]]: 3,
[[
'o', 'x', ' ',
' ', ' ', 'x',
'o', ' ', ' '
]]: 3,
[[
'o', 'x', ' ',
' ', ' ', ' ',
'o', 'x', ' '
]]: 3,
[[
'o', 'x', ' ',
' ', ' ', ' ',
'o', ' ', 'x'
]]: 3
// ...
};
```

### Technical frame 4: Interactive Generators / representing naughts and crosses as a stateful function

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01880))_

> Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01876))_

<a id="atom-technical-atom-61be599b8f60219b"></a>
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

### Technical frame 5: Interactive Generators / representing naughts and crosses as a stateful function

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01880))_

> Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01878))_

<a id="atom-technical-atom-8427aaaf8ddcd159"></a>
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

### Technical frame 6: Interactive Generators / representing naughts and crosses as a stateful function

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01880))_

> Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01879))_

<a id="atom-technical-atom-a480fca1427874e0"></a>
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

### Technical frame 7: Interactive Generators / this seems familiar

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01886))_

> Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01885))_

<a id="atom-technical-atom-92ff13fcae05707f"></a>
```
function browserNaughtsAndCrosses () {
const x1 = parseInt(prompt('o plays 0, where does x play?'));
switch (x1) {
case 1:
const x2 = parseInt(prompt('o plays 6, where does x play?'));
switch (x2) {
case 2:
case 4:
case 5:
case 7:
case 8:
alert('o plays 3');
break;
case 3:
const x3 = parseInt(prompt('o plays 8, where does x play?'));
switch (x3) {
case 2:
case 5:
case 7:
alert('o plays 4');
break;
case 4:
alert('o plays 7');
break;
}
}
break;
// ...
}
}
```

### Technical frame 8: Interactive Generators / this seems familiar / interactive generators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01893))_

> Served by the Pot: Collections 260 } } break ; // ... } } const aNaughtsAndCrossesGame = generatorNaughtsAndCrosses(); We can then get the first move by calling .next() . Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1)

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01892))_

<a id="atom-technical-atom-03b137678eb4ca24"></a>
```
function* generatorNaughtsAndCrosses () {
const x1 = yield 0;
switch (x1) {
case 1:
const x2 = yield 6;
switch (x2) {
case 2:
case 4:
case 5:
case 7:
case 8:
yield 3;
break;
case 3:
const x3 = yield 8;
switch (x3) {
case 2:
case 5:
case 7:
yield 4;
break;
case 4:
yield 7;
break;
```

### Technical atom 9

<a id="atom-technical-atom-d315e55c465ae657"></a>

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01869))_

> And if we want to look up what move to make, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01870))_

```
moveLookupTable[[
'o', 'x', ' ',
' ', ' ', ' ',
'o', 'x', ' '
]]
//=> 3
```

### Technical atom 10

<a id="atom-technical-atom-807e66e77775b368"></a>

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01871))_

> And from there, a stateless function to play naughts-and-crosses is trivial:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01872))_

```
statelessNaughtsAndCrosses([
'o', 'x', ' ',
' ', ' ', ' ',
'o', 'x', ' '
])
//=> 3
```


## Related pages

### Source structure

- [[javascriptallonge-section-interactive-generators-c6339bc5]] - source section: Interactive Generators shares source evidence from Interactive Generators: We used generators to build iterators that maintain implicit state. We saw how to use them for recursive unfolds and state machines. But there are other times we wan ... [truncated]; Interactive Generators shares technical record from Interactive Generators / representing naughts and crosses as a stateless function / Will be represented as:: [ 'o', 'x', ' ', 'x', ' ', ' ', 'o', ' ', ' ' ] (31 shared statement(s), 10 shared atom(s))
- [[javascriptallonge-section-interactive-generators-this-seems-familiar-interactive-generators-0e36e551]] - source section: Interactive Generators / this seems familiar / interactive generators shares source evidence from Interactive Generators / this seems familiar / interactive generators: So far, we have called iterators (and generators) with .next() . But what if we pass a value to .next() ? If we could do that, a generator function that played naugh ... [truncated]; Interactive Generators / this seems familiar / interactive generators shares technical record from Interactive Generators / this seems familiar / interactive generators: function* generatorNaughtsAndCrosses () { const x1 = yield 0; switch (x1) { case 1: const x2 = yield 6; switch (x2) { case 2: case 4: case 5: case 7: case 8: yield 3 ... [truncated] (6 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateful-function-94951f68]] - source section: Interactive Generators / representing naughts and crosses as a stateful function
- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-e2c2d97f]] - source section: Interactive Generators / representing naughts and crosses as a stateless function
- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-will-be-represen-66494cc9]] - source section: Interactive Generators / representing naughts and crosses as a stateless function / Will be represented as:
- [[javascriptallonge-section-interactive-generators-this-seems-familiar-ca8bdeb5]] - source section: Interactive Generators / this seems familiar

### Shared technical atoms

- [[javascriptallonge-collection]] - shared statements and technical atoms: Collection shares source evidence from Interactive Generators / this seems familiar / interactive generators: Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn't call us. It isn't a collection, it has no mea ... [truncated]; Collection shares technical record from Interactive Generators / this seems familiar / interactive generators: function* generatorNaughtsAndCrosses () { const x1 = yield 0; switch (x1) { case 1: const x2 = yield 6; switch (x2) { case 2: case 4: case 5: case 7: case 8: yield 3 ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-cross-stateless-function]] - shared statements and technical atoms: Cross Stateless Function shares source evidence from Interactive Generators / representing naughts and crosses as a stateless function: We could plays naughts and crosses as a stateless function. We encode each position of the board in some fashion, and then we build a dictionary from positions to mo ... [truncated]; Cross Stateless Function shares technical record from Interactive Generators / representing naughts and crosses as a stateless function / We get:: statelessNaughtsAndCrosses([ 'o', 'x', ' ', ' ', ' ', ' ', 'o', 'x', ' ' ]) //=> 3 (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements and technical atoms: Iterator shares source evidence from Interactive Generators / this seems familiar: However, our solution inverts the control. We aren't calling our function with moves, it's calling us. With iterators, we wrote a generator function using function * ... [truncated]; Iterator shares technical record from Interactive Generators / this seems familiar / interactive generators: function* generatorNaughtsAndCrosses () { const x1 = yield 0; switch (x1) { case 1: const x2 = yield 6; switch (x2) { case 2: case 4: case 5: case 7: case 8: yield 3 ... [truncated] (1 shared statement(s), 1 shared atom(s))

### Shared claims

- [[javascriptallonge-cross-stateful-function]] - shared statements: Cross Stateful Function shares source evidence from Interactive Generators / representing naughts and crosses as a stateful function: Our statelessNaughtsAndCrosses function pushes the work of tracking the game's state onto us, the player. What if we want to exchange moves with the function? In tha ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
