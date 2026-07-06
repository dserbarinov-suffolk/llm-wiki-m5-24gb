---
page_id: javascriptallonge-cross-stateless-function
page_kind: concept
summary: Cross Stateless Function: 1 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-cross-stateless-function@4542738d7c202b34330e7a94b552a757
---

# Cross Stateless Function

What [[javascriptallonge]] covers about cross stateless function:

## Statements

### Interactive Generators / representing naughts and crosses as a stateless function

- We could plays naughts and crosses as a stateless function. We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. For example, the entry for: _(javascriptallonge.pdf (source-range-c98ab3e6-01891))_


## Technical atoms

### Technical atom 1

<a id="atom-technical-atom-e8bd210dde564a7c"></a>

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01915))_

> And from there, a stateless function to play naughts-and-crosses is trivial:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01916))_

```
statelessNaughtsAndCrosses([
'o', 'x', ' ',
' ', ' ', ' ',
'o', 'x', ' '
])
//=> 3
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-interactive-generator]] - shared statements and technical atoms: Interactive Generators shares source evidence from Interactive Generators / representing naughts and crosses as a stateless function: We could plays naughts and crosses as a stateless function. We encode each position of the board in some fashion, and then we build a dictionary from positions to mo ... [truncated]; Interactive Generators shares technical record from Interactive Generators / representing naughts and crosses as a stateless function / We get:: statelessNaughtsAndCrosses([ 'o', 'x', ' ', ' ', ' ', ' ', 'o', 'x', ' ' ]) //=> 3 (1 shared statement(s), 1 shared atom(s))

## Source

- [[javascriptallonge]]
