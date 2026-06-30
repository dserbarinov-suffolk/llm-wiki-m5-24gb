---
page_id: javascriptallonge-section-interactive-generators-this-seems-familiar-4e1f58a1
page_kind: source
summary: Interactive Generators / this seems familiar: 23 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-interactive-generators-this-seems-familiar-4e1f58a1@2f88eb31a13668c24dffc11ec6659e36
---

# Interactive Generators / this seems familiar

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-interactive-generators-a0db0ac4]] - broader source section: Interactive Generators
- [[javascriptallonge-section-interactive-generators-this-seems-familiar-interactive-generators-3de32faa]] - narrower source section: Interactive Generators / this seems familiar / interactive generators
- [[javascriptallonge-section-interactive-generators-this-seems-familiar-summary-46445b98]] - narrower source section: Interactive Generators / this seems familiar / summary
- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateful-function-50fe6464]] - previous source section: Interactive Generators / representing naughts and crosses as a stateful function
- [[javascriptallonge-section-interactive-generators-basic-operations-on-iterables-e1c8a49e]] - next source section: Interactive Generators / Basic Operations on Iterables

## Statements

- When we looked at generators, we saw that some iterators are inherently stateful, but sometimes it is awkward to represent them in a fully stateless fashion. Sometimes there is a state machine that is naturally represented implicitly in JavaScript's control flow rather than explicitly in data. _(javascriptallonge.pdf (source-range-0e12e052-01926))_
- We've done almost the exact same thing here with our naughts and crosses game. A game like this is absolutely a state machine, and we've explicitly coded those states into the lookup table. Which leads us to wonder: Is there a way to encode those states implicitly , in JavaScript control flow? _(javascriptallonge.pdf (source-range-0e12e052-01927))_
- If we were in full control of the interaction, it would be easy to encode the game play as a decision tree instead of as a lookup table. For example, we could do this in a browser: _(javascriptallonge.pdf (source-range-0e12e052-01928))_
- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree. _(javascriptallonge.pdf (source-range-0e12e052-01930))_
- However, our solution inverts the control. We aren't calling our function with moves, it's calling us. With iterators, we wrote a generator function using function * , and then used yield to yield values while maintaining the implicit state of the generator's control flow. _(javascriptallonge.pdf (source-range-0e12e052-01931))_
- Canwedothesamethinghere?Atfirst glance, no. How do we get the player's moves to the generator function? But the first glance is deceptive, because we only see what we've seen so far. Let's see how it would actually work. _(javascriptallonge.pdf (source-range-0e12e052-01932))_
- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. _(javascriptallonge.pdf (source-range-0e12e052-01930))_
- With iterators, we wrote a generator function using function * , and then used yield to yield values while maintaining the implicit state of the generator's control flow. _(javascriptallonge.pdf (source-range-0e12e052-01931))_
- But the first glance is deceptive, because we only see what we've seen so far. _(javascriptallonge.pdf (source-range-0e12e052-01932))_

## Statements by subsection

### Interactive Generators / this seems familiar / interactive generators

- So far, we have called iterators (and generators) with .next() . But what if we pass a value to .next() ? If we could do that, a generator function that played naughts and crosses would look like this: _(javascriptallonge.pdf (source-range-0e12e052-01934))_
- Served by the Pot: Collections 260 } } break ; // ... } } const aNaughtsAndCrossesGame = generatorNaughtsAndCrosses(); We can then get the first move by calling .next() . Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1).value //=> 6 aNaughtsAndCrossesGame.next(3).value //=> 8 aNaughtsAndCrossesGame.next(7).value //=> 4 _(javascriptallonge.pdf (source-range-0e12e052-01937))_
- Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn't call us. It isn't a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. _(javascriptallonge.pdf (source-range-0e12e052-01938))_
- But the generator function allows us to maintain state implicitly. And sometimes, we want to use implicit state instead of explicitly storing state in our data. _(javascriptallonge.pdf (source-range-0e12e052-01939))_
- Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. _(javascriptallonge.pdf (source-range-0e12e052-01937))_
- If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1).value //=> 6 aNaughtsAndCrossesGame.next(3).value //=> 8 aNaughtsAndCrossesGame.next(7).value //=> 4 _(javascriptallonge.pdf (source-range-0e12e052-01937))_

### Interactive Generators / this seems familiar / summary

- We have looked at generators as ways of making iterators over static collections, where state is modelled implicitly in control flow. But as we see here, it's also possible to use a generator interactively, passing values in and receiving a value in return, just like an ordinary function. _(javascriptallonge.pdf (source-range-0e12e052-01941))_
- Again, the salient difference is that an 'interactive' generator is stateful, and it embodies its state in its control flow. _(javascriptallonge.pdf (source-range-0e12e052-01942))_
