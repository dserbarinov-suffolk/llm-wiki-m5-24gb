---
page_id: javascriptallonge-this-seems-familiar
page_kind: concept
summary: topic-concept: 11 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_43911e662849abbc@0690998c4c921f7fe9db0f180b211f92
---

# this seems familiar

Source: [[javascriptallonge]]

## Statements

- Sometimes there is a state machine that is naturally represented implicitly in JavaScript's control flow rather than explicitly in data. (javascriptallonge.pdf p.280)
- When we looked at generators, we saw that some iterators are inherently stateful, but sometimes it is awkward to represent them in a fully stateless fashion. (javascriptallonge.pdf p.280)
- A game like this is absolutely a state machine, and we've explicitly coded those states into the lookup table. (javascriptallonge.pdf p.280)
- If we were in full control of the interaction, it would be easy to encode the game play as a decision tree instead of as a lookup table. (javascriptallonge.pdf p.280)
- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. (javascriptallonge.pdf p.281)
- But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree. (javascriptallonge.pdf p.281)
- With iterators, we wrote a generator function using function * , and then used yield to yield values while maintaining the implicit state of the generator's control flow. (javascriptallonge.pdf p.281-282)
- But the first glance is deceptive, because we only see what we've seen so far. (javascriptallonge.pdf p.282)

## Rules

- But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree. (javascriptallonge.pdf p.281)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

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


## Related pages

- [[javascriptallonge-representing-naughts-and-crosses-as-a-stateful-function]] - contextualizes: source-supported topic dependency
