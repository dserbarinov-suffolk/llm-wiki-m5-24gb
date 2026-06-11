---
category: concept
summary: JavaScript pattern for gathering arguments from the left
sources: javascriptallonge.pdf
updated: 2026-06-11
---

Left-variadic functions gather excess arguments into the leftmost parameter. Implemented via `leftVariadic` decorator:

```javascript
const leftVariadic = (fn) => (...args) => {
  const gathered = args.slice(0, args.length - fn.length + 1);
  const spread = args.slice(args.length - fn.length + 1);
  return fn.apply(this, [gathered].concat(spread));
};

const butLastAndLast = leftVariadic((butLast, last) => [butLast, last]);
butLastAndLast('why','hello','there','little','droid')
//=> [['why','hello','there','little'], 'droid']
```

Contrasts with right-variadic functions that gather from the end. See [[javascriptallonge-recipes-with-basic-functions]] (raw/javascriptallonge.pdf p.79-93).
