---
category: source
summary: Generating Iterables from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.224-245
updated: 2026-06-18
domain: javascriptallonge
category_path: source-sections
source_id: javascriptallonge.pdf
---

# Generating Iterables

This page summarizes Chapter 6, "Generating Iterables" from *JavaScript Allongé* (raw/javascriptallonge.pdf p.224-245). It discusses how iterables work in JavaScript and compares generating values with iteration.

## Key Concepts

- **Iterables** are objects that implement the `[Symbol.iterator]` method, allowing them to be iterated over using `for...of` loops.
- **Iterators** are objects that have a `next()` method, which returns the next value in a sequence.
- **Generators** are a special kind of function that allows for easier state management and can be used to generate values dynamically.
- **Recursive iterators** can be used to traverse complex data structures like trees, but they often require explicit stack management.
- **State machines** can be modeled using iterators, but they may require more complex state management compared to generators.

## Examples

### Generating Numbers

```javascript
const Numbers = { [Symbol.iterator]: () => {
  let n = 0;
  return { next: () => ({ done: false, value: n++ }) }
};
```

This code defines an iterable `Numbers` that generates numbers sequentially.

### Recursive Iteration

```javascript
const isIterable = (something) => !!something[Symbol.iterator];

const generate = (iterable) => {
  for (let element of iterable) {
    if (isIterable(element)) {
      generate(element);
    } else {
      console.log(element);
    }
  }
};

generate([1, [2, [3, 4], 5]]);
```

This function recursively generates and logs all leaf elements from a nested array.

### Iteration Version of Recursive Traversal

```javascript
const isIterable = (something) => !!something[Symbol.iterator];

const treeIterator = (iterable) => {
  const iterators = [ iterable[Symbol.iterator]() ];
  return () => {
    while (!!iterators[0]) {
      const iterationResult = iterators[0].next();
      if (iterationResult.done) {
        iterators.shift();
      } else if (isIterable(iterationResult.value)) {
        iterators.unshift(iterationResult.value[Symbol.iterator]());
      } else {
        return iterationResult.value;
      }
    }
    return;
  };
};

const i = treeIterator([1, [2, [3, 4], 5]]);
let n;
while (n = i()) {
  console.log(n);
}
```

This code implements an explicit stack to manage recursive iteration over a nested array.

### Fibonacci Sequence with Generator

```javascript
const fibonacci = () => {
  let a, b;
  console.log(a = 0);
  console.log(b = 1);
  while (true) {
    [a, b] = [b, a + b];
    console.log(b);
  }
};

fibonacci();
```

This generator produces the Fibonacci sequence dynamically.

### Fibonacci Sequence with Iterator

```javascript
let a, b, state = 0;

const fibonacci = () => {
  switch (state) {
    case 0: state = 1; return a = 0;
    case 1: state = 2; return b = 1;
    case 2: [a, b] = [b, a + b]; return b;
  }
};

while (true) {
  console.log(fibonacci());
}
```

This iterator explicitly manages the state of the Fibonacci sequence.

## Key Takeaways

- Generators are often easier to use for generating values compared to implementing iterators manually.
- Recursive iteration can be complex and may require explicit stack management, while generators can implicitly manage recursion.
- State management in iterators can become complex, especially for state machines like the Fibonacci sequence.

## References

- *JavaScript Allongé* (raw/javascriptallonge.pdf p.224-245)
- [State Pattern](https://en.wikipedia.org/wiki/State_pattern)
