---
category: source
summary: Mutation from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.141-157
updated: 2026-06-18
domain: javascriptallonge
category_path: source-sections
source_id: javascriptallonge.pdf
---

## Mutation

In JavaScript, arrays and objects can mutate. Their identities remain the same, but their structure changes. For example:

- You can reassign values in arrays using `[] =`: 
  ```javascript
  const oneTwoThree = [1, 2, 3];
  oneTwoThree[0] = 'one'; // => ['one', 2, 3]
  ```
- You can add values to arrays using `[] =`: 
  ```javascript
  const oneTwoThree = [1, 2, 3];
  oneTwoThree[3] = 'four'; // => [1, 2, 3, 'four']
  ```
- You can add properties to objects: 
  ```javascript
  const name = {firstName: 'Leonard', lastName: 'Braithwaite'};
  name.middleName = 'Austin'; // => { firstName: 'Leonard', lastName: 'Braithwaite', middleName: 'Austin' }
  ```

### Mutation and Aliases

When two bindings refer to the same value, mutating one affects the other. For example:

```javascript
const allHallowsEve = [2012, 10, 31];
(function (halloween) {
  halloween[0] = 2013;
})(allHallowsEve);
// allHallowsEve => [2013, 10, 31]
```

This shows that mutation changes the shared value, unlike rebinding which does not.

### Mutation and Data Structures

Mutation can simplify algorithms but makes them harder to reason about. Some developers are liberal with mutation during construction and conservative during consumption.

For example, in linked lists, mutation can be used during construction but avoided afterward to prevent unintended side effects. However, in arrays, destructuring creates a copy, so mutation of the copy does not affect the original.

```javascript
const OneToFive = [1, 2, 3, 4, 5];
const [a, b, ...ThreeToFive] = OneToFive;
ThreeToFive[0] = 'three'; // OneToFive remains [1, 2, 3, 4, 5]
```

This highlights the trade-off between performance and safety when using mutation.

### Avoiding Mutation

Avoiding mutation can lead to easier reasoning about data. Immutable data does not require copying operations when passed to functions or used in computations. However, mutation can be more efficient in certain cases, like linked lists, where structure sharing is possible.

This section is based on: (raw/javascriptallonge.pdf p.141-157)
