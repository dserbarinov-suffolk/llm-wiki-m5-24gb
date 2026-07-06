---
page_id: javascriptallonge-section-interactive-generators-21aeba33
page_kind: source
summary: Interactive Generators: 70 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-interactive-generators-21aeba33@dae01f1bed88a1a273f0e1fc960d4e11
---

# Interactive Generators

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-interlude-the-carpenter-interviews-for-a-job-4a7d7995]] - previous source section: Interlude: The Carpenter Interviews for a Job
- [[javascriptallonge-section-the-golden-crema-appendices-and-afterwords-86b691f6]] - next source section: The Golden Crema: Appendices and Afterwords

### Source structure

- [[javascriptallonge-section-interactive-generators-basic-operations-on-iterables-9269edcc]] - narrower source section: Interactive Generators / Basic Operations on Iterables
- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateful-function-2e75ec69]] - narrower source section: Interactive Generators / representing naughts and crosses as a stateful function
- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-45305bce]] - narrower source section: Interactive Generators / representing naughts and crosses as a stateless function
- [[javascriptallonge-section-interactive-generators-this-seems-familiar-dc5208f1]] - narrower source section: Interactive Generators / this seems familiar

### Topics

- [[javascriptallonge-interactive-generator]] - topic hub: opens the topic page for Interactive Generator

## Statements

- We used generators to build iterators that maintain implicit state. We saw how to use them for recursive unfolds and state machines. But there are other times we want to build functions that maintain implicit state. Let's start by looking at a very simple example of a function that can be written statefully. _(javascriptallonge.pdf (source-range-c98ab3e6-01869))_
- Consider, for example, the moves in a game. The moves a player makes are a stream of values, just like the contents of an array can be consider a stream of values. But of course, iterating over a stream of moves requires us to wait for the game to be over so we know what moves were made. _(javascriptallonge.pdf (source-range-c98ab3e6-01872))_
- The first player will always be o , and they will always place their chequer in the top-left corner, coincidentally numbered o : _(javascriptallonge.pdf (source-range-c98ab3e6-01874))_
- x has six possible moves, but they are really just two choices: 3 and anything else: _(javascriptallonge.pdf (source-range-c98ab3e6-01883))_
- Consider, for example, the moves in a game. _(javascriptallonge.pdf (source-range-c98ab3e6-01872))_

## Statements by subsection

### Interactive Generators / representing naughts and crosses as a stateless function

- We could plays naughts and crosses as a stateless function. We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. For example, the entry for: _(javascriptallonge.pdf (source-range-c98ab3e6-01891))_
- We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. _(javascriptallonge.pdf (source-range-c98ab3e6-01891))_

### Interactive Generators / representing naughts and crosses as a stateless function / Would be 3 , producing:

- We can encode the board in several different ways. We could use multiline strings with formatting just as we've written it here, but it is a design smell to couple presentation with modelling. Our function should be just as useful on a teletype as it would be backing a DOM game that uses a table, or a browser game that draws on Canvas. _(javascriptallonge.pdf (source-range-c98ab3e6-01899))_

### Interactive Generators / representing naughts and crosses as a stateless function / Will be represented as:

- We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write: _(javascriptallonge.pdf (source-range-c98ab3e6-01908))_

### Interactive Generators / representing naughts and crosses as a stateful function

- Our statelessNaughtsAndCrosses function pushes the work of tracking the game's state onto us, the player. What if we want to exchange moves with the function? In that case, we need a stateful function. Our 'API' will work like this: When we want a new game, we'll call a function that will return a game function, We'll call the game function repeatedly, passing our moves, and get the opponent's moves from it. _(javascriptallonge.pdf (source-range-c98ab3e6-01918))_
- Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data. _(javascriptallonge.pdf (source-range-c98ab3e6-01924))_

### Interactive Generators / this seems familiar

- When we looked at generators, we saw that some iterators are inherently stateful, but sometimes it is awkward to represent them in a fully stateless fashion. Sometimes there is a state machine that is naturally represented implicitly in JavaScript's control flow rather than explicitly in data. _(javascriptallonge.pdf (source-range-c98ab3e6-01926))_
- We've done almost the exact same thing here with our naughts and crosses game. A game like this is absolutely a state machine, and we've explicitly coded those states into the lookup table. Which leads us to wonder: Is there a way to encode those states implicitly , in JavaScript control flow? _(javascriptallonge.pdf (source-range-c98ab3e6-01927))_
- If we were in full control of the interaction, it would be easy to encode the game play as a decision tree instead of as a lookup table. For example, we could do this in a browser: _(javascriptallonge.pdf (source-range-c98ab3e6-01928))_
- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree. _(javascriptallonge.pdf (source-range-c98ab3e6-01930))_
- However, our solution inverts the control. We aren't calling our function with moves, it's calling us. With iterators, we wrote a generator function using function * , and then used yield to yield values while maintaining the implicit state of the generator's control flow. _(javascriptallonge.pdf (source-range-c98ab3e6-01931))_
- Canwedothesamethinghere?Atfirst glance, no. How do we get the player's moves to the generator function? But the first glance is deceptive, because we only see what we've seen so far. Let's see how it would actually work. _(javascriptallonge.pdf (source-range-c98ab3e6-01932))_
- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. _(javascriptallonge.pdf (source-range-c98ab3e6-01930))_
- With iterators, we wrote a generator function using function * , and then used yield to yield values while maintaining the implicit state of the generator's control flow. _(javascriptallonge.pdf (source-range-c98ab3e6-01931))_
- But the first glance is deceptive, because we only see what we've seen so far. _(javascriptallonge.pdf (source-range-c98ab3e6-01932))_

### Interactive Generators / this seems familiar / interactive generators

- So far, we have called iterators (and generators) with .next() . But what if we pass a value to .next() ? If we could do that, a generator function that played naughts and crosses would look like this: _(javascriptallonge.pdf (source-range-c98ab3e6-01934))_
- Served by the Pot: Collections 260 } } break ; // ... } } const aNaughtsAndCrossesGame = generatorNaughtsAndCrosses(); We can then get the first move by calling .next() . Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1).value //=> 6 aNaughtsAndCrossesGame.next(3).value //=> 8 aNaughtsAndCrossesGame.next(7).value //=> 4 _(javascriptallonge.pdf (source-range-c98ab3e6-01937))_
- Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn't call us. It isn't a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. _(javascriptallonge.pdf (source-range-c98ab3e6-01938))_
- But the generator function allows us to maintain state implicitly. And sometimes, we want to use implicit state instead of explicitly storing state in our data. _(javascriptallonge.pdf (source-range-c98ab3e6-01939))_
- If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1).value //=> 6 aNaughtsAndCrossesGame.next(3).value //=> 8 aNaughtsAndCrossesGame.next(7).value //=> 4 _(javascriptallonge.pdf (source-range-c98ab3e6-01937))_
- Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. _(javascriptallonge.pdf (source-range-c98ab3e6-01937))_

### Interactive Generators / this seems familiar / summary

- We have looked at generators as ways of making iterators over static collections, where state is modelled implicitly in control flow. But as we see here, it's also possible to use a generator interactively, passing values in and receiving a value in return, just like an ordinary function. _(javascriptallonge.pdf (source-range-c98ab3e6-01941))_
- Again, the salient difference is that an 'interactive' generator is stateful, and it embodies its state in its control flow. _(javascriptallonge.pdf (source-range-c98ab3e6-01942))_

### Interactive Generators / Basic Operations on Iterables

- Here are the operations we've defined on Iterables. As discussed, they preserve the collection semantics of the iterable they are given: _(javascriptallonge.pdf (source-range-c98ab3e6-01944))_
