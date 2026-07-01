---
page_id: javascriptallonge-interactive-generator
page_kind: concept
summary: Interactive Generators: 31 statement(s) and 17 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-interactive-generator@c485eebe180c7f75efb20f1543116ee1
---

# Interactive Generators

What [[javascriptallonge]] covers about interactive generators:

## Statements

### Interactive Generators

- We used generators to build iterators that maintain implicit state. We saw how to use them for recursive unfolds and state machines. But there are other times we want to build functions that maintain implicit state. Let's start by looking at a very simple example of a function that can be written statefully. _(javascriptallonge.pdf (source-range-0e12e052-01869))_

- Consider, for example, the moves in a game. The moves a player makes are a stream of values, just like the contents of an array can be consider a stream of values. But of course, iterating over a stream of moves requires us to wait for the game to be over so we know what moves were made. _(javascriptallonge.pdf (source-range-0e12e052-01872))_

- The first player will always be o , and they will always place their chequer in the top-left corner, coincidentally numbered o : _(javascriptallonge.pdf (source-range-0e12e052-01874))_

- x has six possible moves, but they are really just two choices: 3 and anything else: _(javascriptallonge.pdf (source-range-0e12e052-01883))_

### Interactive Generators / representing naughts and crosses as a stateless function

- We could plays naughts and crosses as a stateless function. We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. For example, the entry for: _(javascriptallonge.pdf (source-range-0e12e052-01891))_

### Interactive Generators / representing naughts and crosses as a stateless function / Would be 3 , producing:

- We can encode the board in several different ways. We could use multiline strings with formatting just as we've written it here, but it is a design smell to couple presentation with modelling. Our function should be just as useful on a teletype as it would be backing a DOM game that uses a table, or a browser game that draws on Canvas. _(javascriptallonge.pdf (source-range-0e12e052-01899))_

### Interactive Generators / representing naughts and crosses as a stateless function / Will be represented as:

- We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write: _(javascriptallonge.pdf (source-range-0e12e052-01908))_

### Interactive Generators / representing naughts and crosses as a stateful function

- Our statelessNaughtsAndCrosses function pushes the work of tracking the game's state onto us, the player. What if we want to exchange moves with the function? In that case, we need a stateful function. Our 'API' will work like this: When we want a new game, we'll call a function that will return a game function, We'll call the game function repeatedly, passing our moves, and get the opponent's moves from it. _(javascriptallonge.pdf (source-range-0e12e052-01918))_

- Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data. _(javascriptallonge.pdf (source-range-0e12e052-01924))_

### Interactive Generators / this seems familiar

- When we looked at generators, we saw that some iterators are inherently stateful, but sometimes it is awkward to represent them in a fully stateless fashion. Sometimes there is a state machine that is naturally represented implicitly in JavaScript's control flow rather than explicitly in data. _(javascriptallonge.pdf (source-range-0e12e052-01926))_

- We've done almost the exact same thing here with our naughts and crosses game. A game like this is absolutely a state machine, and we've explicitly coded those states into the lookup table. Which leads us to wonder: Is there a way to encode those states implicitly , in JavaScript control flow? _(javascriptallonge.pdf (source-range-0e12e052-01927))_

- If we were in full control of the interaction, it would be easy to encode the game play as a decision tree instead of as a lookup table. For example, we could do this in a browser: _(javascriptallonge.pdf (source-range-0e12e052-01928))_

- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree. _(javascriptallonge.pdf (source-range-0e12e052-01930))_

- However, our solution inverts the control. We aren't calling our function with moves, it's calling us. With iterators, we wrote a generator function using function * , and then used yield to yield values while maintaining the implicit state of the generator's control flow. _(javascriptallonge.pdf (source-range-0e12e052-01931))_

- Canwedothesamethinghere?Atfirst glance, no. How do we get the player's moves to the generator function? But the first glance is deceptive, because we only see what we've seen so far. Let's see how it would actually work. _(javascriptallonge.pdf (source-range-0e12e052-01932))_

### Interactive Generators / this seems familiar / interactive generators

- So far, we have called iterators (and generators) with .next() . But what if we pass a value to .next() ? If we could do that, a generator function that played naughts and crosses would look like this: _(javascriptallonge.pdf (source-range-0e12e052-01934))_

- Served by the Pot: Collections 260 } } break ; // ... } } const aNaughtsAndCrossesGame = generatorNaughtsAndCrosses(); We can then get the first move by calling .next() . Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1).value //=> 6 aNaughtsAndCrossesGame.next(3).value //=> 8 aNaughtsAndCrossesGame.next(7).value //=> 4 _(javascriptallonge.pdf (source-range-0e12e052-01937))_

- Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn't call us. It isn't a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. _(javascriptallonge.pdf (source-range-0e12e052-01938))_

- But the generator function allows us to maintain state implicitly. And sometimes, we want to use implicit state instead of explicitly storing state in our data. _(javascriptallonge.pdf (source-range-0e12e052-01939))_

### Interactive Generators / this seems familiar / summary

- We have looked at generators as ways of making iterators over static collections, where state is modelled implicitly in control flow. But as we see here, it's also possible to use a generator interactively, passing values in and receiving a value in return, just like an ordinary function. _(javascriptallonge.pdf (source-range-0e12e052-01941))_

- Again, the salient difference is that an 'interactive' generator is stateful, and it embodies its state in its control flow. _(javascriptallonge.pdf (source-range-0e12e052-01942))_

### Interactive Generators / Basic Operations on Iterables

- Here are the operations we've defined on Iterables. As discussed, they preserve the collection semantics of the iterable they are given: _(javascriptallonge.pdf (source-range-0e12e052-01944))_


## Technical atoms

### Technical frame 1: Interactive Generators / representing naughts and crosses as a stateless function / Will be represented as:

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01908))_

> We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01907))_

```
[
'o', 'x', ' ',
'x', ' ', ' ',
'o', ' ', ' '
]
```

### Technical frame 2: Interactive Generators / representing naughts and crosses as a stateless function / Will be represented as:

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01908))_

> We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01909))_

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01908))_

> We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01910))_

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

### Technical frame 4: Interactive Generators / representing naughts and crosses as a stateless function / We get:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01912))_

```
{
"o,x, , , , , , , ":6,
"o,x,x, , , ,o, , ":3,
"o,x, ,x, , ,o, , ":8,
"o,x, , ,x, ,o, , ":3,
"o,x, , , ,x,o, , ":3,
"o,x, , , , ,o,x, ":3,
"o,x, , , , ,o, ,x":3
}
```

### Technical frame 5: Interactive Generators / representing naughts and crosses as a stateless function / We get:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01914))_

```
moveLookupTable[[
'o', 'x', ' ',
' ', ' ', ' ',
'o', 'x', ' '
]]
//=> 3
```

### Technical frame 6: Interactive Generators / representing naughts and crosses as a stateless function / We get:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01916))_

```
statelessNaughtsAndCrosses([
'o', 'x', ' ',
' ', ' ', ' ',
'o', 'x', ' '
])
//=> 3
```

### Technical frame 7: Interactive Generators / representing naughts and crosses as a stateful function

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01924))_

> Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01920))_

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

### Technical frame 8: Interactive Generators / representing naughts and crosses as a stateful function

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01924))_

> Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01922))_

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

### Technical frame 9: Interactive Generators / representing naughts and crosses as a stateful function

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01924))_

> Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01923))_

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

### Technical frame 10: Interactive Generators / this seems familiar

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01930))_

> Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01929))_

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

### Technical frame 11: Interactive Generators / this seems familiar / interactive generators

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01937))_

> Served by the Pot: Collections 260 } } break ; // ... } } const aNaughtsAndCrossesGame = generatorNaughtsAndCrosses(); We can then get the first move by calling .next() . Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1)

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01936))_

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

### Technical frame 12: Interactive Generators / Basic Operations on Iterables / operations that transform one iterable into another

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01946))_

```
function * mapWith(fn, iterable) {
for (const element of iterable) {
yield fn(element);
}
}
function * mapAllWith (fn, iterable) {
for (const element of iterable) {
yield * fn(element);
}
}
function * filterWith (fn, iterable) {
for (const element of iterable) {
if (!!fn(element)) yield element;
}
}
function * compact (iterable) {
for (const element of iterable) {
if (element != null) yield element;
}
}
function * untilWith (fn, iterable) {
for (const element of iterable) {
if (fn(element)) break;
yield fn(element);
}
}
function * rest (iterable) {
const iterator = iterable[Symbol.iterator]();
iterator.next();
```

### Technical frame 13: Interactive Generators / Basic Operations on Iterables / operations that transform one iterable into another

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01947))_

```
yield * iterator;
}
function * take (numberToTake, iterable) {
const iterator = iterable[Symbol.iterator]();
for (let i = 0; i < numberToTake; ++i) {
const { done, value } = iterator.next();
if (!done) yield value;
}
}
```

### Technical frame 14: Interactive Generators / Basic Operations on Iterables / operations that compose two or more iterables into an iterable

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01949))_

```
function * zip (...iterables) {
const iterators = iterables.map(i => i[Symbol.iterator]());
while (true) {
const pairs = iterators.map(j => j.next()),
dones = pairs.map(p => p.done),
values = pairs.map(p => p.value);
if (dones.indexOf(true) >= 0) break;
yield values;
}
};
function * zipWith (zipper, ...iterables) {
const iterators = iterables.map(i => i[Symbol.iterator]());
while (true) {
const pairs = iterators.map(j => j.next()),
dones = pairs.map(p => p.done),
values = pairs.map(p => p.value);
if (dones.indexOf(true) >= 0) break;
yield zipper(...values);
}
};
```

### Technical frame 15: Interactive Generators / Basic Operations on Iterables / operations that compose two or more iterables into an iterable

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01951))_

```
const zip = callFirst(zipWith, (...values) => values);
```

### Technical frame 16: Interactive Generators / Basic Operations on Iterables / operations that transform an iterable into a value

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01953))_

```
const reduceWith = (fn, seed, iterable) => {
let accumulator = seed;
for (const element of iterable) {
accumulator = fn(accumulator, element);
}
return accumulator;
};
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
```

### Technical frame 17: Interactive Generators / Basic Operations on Iterables / memoizing an iterable

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01955))_

```
function memoize (generator) {
const memos = {},
iterators = {};
return function * (...args) {
const key = JSON.stringify(args);
let i = 0;
if (memos[key] == null) {
memos[key] = [];
iterators[key] = generator(...args);
}
while (true) {
if (i < memos[key].length) {
yield memos[key][i++];
}
else {
const { done, value } = iterators[key].next();
if (done) {
return;
} else {
yield memos[key][i++] = value;
```


## Related pages

- [[javascriptallonge-collection]] - shared statements and technical atoms: Collection shares source evidence from Interactive Generators / this seems familiar / interactive generators: Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn't call us. It isn't a collection, it has no mea ... [truncated]; Collection shares technical record from Interactive Generators / this seems familiar / interactive generators: function* generatorNaughtsAndCrosses () { const x1 = yield 0; switch (x1) { case 1: const x2 = yield 6; switch (x2) { case 2: case 4: case 5: case 7: case 8: yield 3 ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-cross-stateless-function]] - shared statements and technical atoms: Cross Stateless Function shares source evidence from Interactive Generators / representing naughts and crosses as a stateless function: We could plays naughts and crosses as a stateless function. We encode each position of the board in some fashion, and then we build a dictionary from positions to mo ... [truncated]; Cross Stateless Function shares technical record from Interactive Generators / representing naughts and crosses as a stateless function / We get:: statelessNaughtsAndCrosses([ 'o', 'x', ' ', ' ', ' ', ' ', 'o', 'x', ' ' ]) //=> 3 (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements and technical atoms: Iterator shares source evidence from Interactive Generators / this seems familiar: However, our solution inverts the control. We aren't calling our function with moves, it's calling us. With iterators, we wrote a generator function using function * ... [truncated]; Iterator shares technical record from Interactive Generators / this seems familiar / interactive generators: function* generatorNaughtsAndCrosses () { const x1 = yield 0; switch (x1) { case 1: const x2 = yield 6; switch (x2) { case 2: case 4: case 5: case 7: case 8: yield 3 ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-cross-stateful-function]] - shared statements: Cross Stateful Function shares source evidence from Interactive Generators / representing naughts and crosses as a stateful function: Our statelessNaughtsAndCrosses function pushes the work of tracking the game's state onto us, the player. What if we want to exchange moves with the function? In tha ... [truncated] (1 shared statement(s))
- [[javascriptallonge-section-interactive-generators-a0db0ac4]] - source section: Interactive Generators shares source evidence from Interactive Generators: We used generators to build iterators that maintain implicit state. We saw how to use them for recursive unfolds and state machines. But there are other times we wan ... [truncated]; Interactive Generators shares technical record from Interactive Generators / representing naughts and crosses as a stateless function / Will be represented as:: [ 'o', 'x', ' ', 'x', ' ', ' ', 'o', ' ', ' ' ] (31 shared statement(s), 17 shared atom(s))
- [[javascriptallonge-section-interactive-generators-this-seems-familiar-interactive-generators-3de32faa]] - source section: Interactive Generators / this seems familiar / interactive generators shares source evidence from Interactive Generators / this seems familiar / interactive generators: So far, we have called iterators (and generators) with .next() . But what if we pass a value to .next() ? If we could do that, a generator function that played naugh ... [truncated]; Interactive Generators / this seems familiar / interactive generators shares technical record from Interactive Generators / this seems familiar / interactive generators: function* generatorNaughtsAndCrosses () { const x1 = yield 0; switch (x1) { case 1: const x2 = yield 6; switch (x2) { case 2: case 4: case 5: case 7: case 8: yield 3 ... [truncated] (6 shared statement(s), 1 shared atom(s))

## Source

- [[javascriptallonge]]
