---
page_id: javascriptallonge-section-interactive-generators-this-seems-familiar-ca8bdeb5
page_kind: source
summary: Interactive Generators / this seems familiar: 14 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-interactive-generators-this-seems-familiar-ca8bdeb5@5d5ceaca29b7435ff219208e98315180
---

# Interactive Generators / this seems familiar

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateful-function-94951f68]] - previous source section: Interactive Generators / representing naughts and crosses as a stateful function
- [[javascriptallonge-section-interactive-generators-basic-operations-on-iterables-540cf505]] - next source section: Interactive Generators / Basic Operations on Iterables

### Source structure

- [[javascriptallonge-section-interactive-generators-c6339bc5]] - broader source section: Interactive Generators
- [[javascriptallonge-section-interactive-generators-this-seems-familiar-interactive-generators-0e36e551]] - narrower source section: Interactive Generators / this seems familiar / interactive generators

## Statements

- When we looked at generators, we saw that some iterators are inherently stateful, but sometimes it is awkward to represent them in a fully stateless fashion. Sometimes there is a state machine that is naturally represented implicitly in JavaScript's control flow rather than explicitly in data. _(javascriptallonge.pdf (source-range-c98ab3e6-01882))_
- We've done almost the exact same thing here with our naughts and crosses game. A game like this is absolutely a state machine, and we've explicitly coded those states into the lookup table. Which leads us to wonder: Is there a way to encode those states implicitly , in JavaScript control flow? _(javascriptallonge.pdf (source-range-c98ab3e6-01883))_
- If we were in full control of the interaction, it would be easy to encode the game play as a decision tree instead of as a lookup table. For example, we could do this in a browser: _(javascriptallonge.pdf (source-range-c98ab3e6-01884))_
- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree. _(javascriptallonge.pdf (source-range-c98ab3e6-01886))_
- However, our solution inverts the control. We aren't calling our function with moves, it's calling us. With iterators, we wrote a generator function using function * , and then used yield to yield values while maintaining the implicit state of the generator's control flow. _(javascriptallonge.pdf (source-range-c98ab3e6-01887))_
- Canwedothesamethinghere?Atfirst glance, no. How do we get the player's moves to the generator function? But the first glance is deceptive, because we only see what we've seen so far. Let's see how it would actually work. _(javascriptallonge.pdf (source-range-c98ab3e6-01888))_
- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. _(javascriptallonge.pdf (source-range-c98ab3e6-01886))_
- With iterators, we wrote a generator function using function * , and then used yield to yield values while maintaining the implicit state of the generator's control flow. _(javascriptallonge.pdf (source-range-c98ab3e6-01887))_
- But the first glance is deceptive, because we only see what we've seen so far. _(javascriptallonge.pdf (source-range-c98ab3e6-01888))_

## Statements by subsection

### Interactive Generators / this seems familiar / summary

- We have looked at generators as ways of making iterators over static collections, where state is modelled implicitly in control flow. But as we see here, it's also possible to use a generator interactively, passing values in and receiving a value in return, just like an ordinary function. _(javascriptallonge.pdf (source-range-c98ab3e6-01897))_
- Again, the salient difference is that an 'interactive' generator is stateful, and it embodies its state in its control flow. _(javascriptallonge.pdf (source-range-c98ab3e6-01898))_
