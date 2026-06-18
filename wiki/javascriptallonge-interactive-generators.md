---
category: source
summary: Interactive Generators from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.273-292
updated: 2026-06-18
domain: javascriptallonge
category_path: source-sections
source_id: javascriptallonge.pdf
---

## Interactive Generators

This page summarizes Chapter 5.2, "Interactive Generators" from *JavaScript Allonge* (raw/javascriptallonge.pdf p.273-292). The chapter discusses how to use generators to build stateful functions for interactive scenarios like games.

### Key Concepts
- **Stateful Functions**: Functions that maintain implicit state, such as a game state, through closures.
- **Naughts and Crosses (Tic-Tac-Toe)**: Used as an example to demonstrate stateful functions, where the game state is tracked internally and moves are made based on a lookup table.
- **Stateless vs. Stateful Functions**: A stateless function requires the player to track the state, while a stateful function encapsulates the state within the function itself.

### Example: Stateful Naughts and Crosses
The chapter provides an implementation of a stateful function for playing naughts and crosses. The function maintains the game state internally and returns the opponent's next move when provided with a player's move.

### Code Snippet
```javascript
const statefulNaughtsAndCrosses = () => {
  const state = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '];
  return (x = false) => {
    if (x) {
      if (state[x] === ' ') {
        state[x] = 'x';
      } else {
        throw "occupied!";
      }
    }
    let o = moveLookupTable[state];
    state[o] = 'o';
    return o;
  };
};
```

### Related Pages
- [[javascriptallonge-recipes-with-basic-functions]]
- [[generator]]
- [[iterable]]
- [[javascriptallonge-chapter-5]]
