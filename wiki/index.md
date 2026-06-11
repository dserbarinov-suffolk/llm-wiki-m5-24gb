# Index

One entry per page: `- [[page-name]] — one-line summary`. Maintained
automatically by the harness on every page write. See `SCHEMA.md`.

## Sources
- [[antikythera-mechanism]] — The oldest known analog computer, an ancient Greek device for tracking astronomical events.
- [[javascriptallonge-as-little-as-possible-about-functions-but-no-less]] — JavaScript functions as values, reference types, and function application mechanics (pages 30-43).
- [[javascriptallonge-chapter-5]] — Explains JavaScript's const keyword, lexical scoping, and function binding patterns like IIFEs.
- [[javascriptallonge-closures-and-scope]] — JavaScript closures, scope chains, pure functions, and environment hierarchy (pages 44-48).
- [[javascriptallonge-composing-and-decomposing-data]] — JavaScript arrays, array literals, destructuring, gathering, and control-flow semantics in function parameters.
- [[javascriptallonge-copy-on-write]] — Explains copy-on-write strategy for linked lists vs arrays, structure sharing, and trade-offs with copy-on-read. Includes code examples and the tortoise-and-hare loop detection algorithm.
- [[javascriptallonge-forewords-to-the-first-edition]] — Forewords to the first edition of JavaScript Allongé by Michael Fogus and Matthew Knox, discussing the Leanpub model and book content.
- [[javascriptallonge-frontend]] — Front matter of JavaScript Allongé, including prefaces, table of contents, and author information.
- [[javascriptallonge-garbage-garbage-everywhere]] — Analysis of JavaScript array recursion inefficiency, comparison to Lisp's linked lists, and object-based cons cell implementations. sources: raw/javascriptallonge.pdf p.126-140
- [[javascriptallonge-making-data-out-of-functions]] — Explores using combinators (K, I, V) and functions to create data structures like lists and pairs, avoiding arrays/objects. Introduces mapWith and flip functions.
- [[javascriptallonge-mutation]] — JavaScript mutation mechanics: array/object mutation, aliases, const/let reassignment, and var pitfalls (pages 141-157).
- [[javascriptallonge-naming-functions]] — JavaScript function naming conventions, declarations, and combinators (pages 62-78).
- [[javascriptallonge-object-assign]] — JavaScript Object.assign method for shallow cloning and merging objects (pages 198-205).
- [[javascriptallonge-picking-the-bean-choice-and-truthiness]] — JavaScript's truthiness, logical operators (!, &&, ||), ternary operator, and control-flow semantics explained with examples.
- [[javascriptallonge-recipes-with-basic-functions]] — JavaScript functional programming recipes: partial application, unary functions, tap, maybe, once, and left-variadic functions.

## Entities
- [[archimedes]] — Ancient Greek mathematician and engineer, known for inventions like the Archimedean screw and principles of buoyancy.
- [[axel-rauschmayer]] — Author of "Exploring ES6" and foreword for JavaScript Allongé's Six Edition.
- [[corinth]] — Ancient Greek city-state in the Peloponnese, known for its strategic location and historical significance.
- [[javascript]] — JavaScript features including closures, scope chains, and global environment isolation.
- [[matthew-knox]] — Software developer and author who praised JavaScript Allongé's exploration of JavaScript's depth.
- [[michael-fogus]] — Software developer and author known for advocating functional programming.
- [[nan]] — JavaScript value representing an invalid or undefined numerical result.
- [[node-js]] — JavaScript runtime environment for server-side and CLI applications.
- [[reg-raganwald-braithwaite]] — Author of JavaScript Allongé and other programming books.
- [[syracuse]] — Ancient Greek city-state in Sicily, renowned as the birthplace of Archimedes and a center of engineering.
- [[undefined]] — JavaScript value representing the absence of a defined value; distinct from SQL NULL.

## Concepts
- [[array-destructuring]] — Array destructuring creates a copy of elements, unlike linked list structure sharing which references the same nodes. See (raw/javascriptallonge.pdf p.158-176) for copy-on-write strategies.
- [[arrays]] — JavaScript arrays allow mutation via element reassignment even with `const`, and destructuring creates copies (unlike linked lists).
- [[call-by-value]] — JavaScript's evaluation strategy where arguments are evaluated before passing, with reference types sharing values (call-by-sharing).
- [[combinator]] — Combinators like K (Kestrel), I (Idiot Bird), and V (Vireo) enable creating functions that manipulate data without arrays/objects. Used in functional programming for data structure creation.
- [[const]] — JavaScript's block-scoped variable declaration that prevents reassignment but allows shadowing in nested blocks.
- [[ecmascript-2015]] — ECMAScript 2015 (ES6) language features and their impact on JavaScript.
- [[floating-point-numbers]] — JavaScript's representation of real numbers using IEEE 754 standard, with precision limitations.
- [[function]] — JavaScript functions, pure functions, closures, and declaration hoisting.
- [[function-decorator]] — Higher-order functions that modify or wrap another function's behavior.
- [[functional-data-structures]] — Functional data structures use closures and higher-order functions to represent lists, pairs, and other structures without arrays/objects. Key example: using combinator V to create data.
- [[functional-iterators]] — Functional iterators separate traversal from operations, enabling lazy evaluation and composition. See (raw/javascriptallonge.pdf p.158-176) for implementation examples.
- [[functional-programming]] — Functional programming concepts including closures and scope chains in JavaScript.
- [[leanpub]] — A publishing platform enabling iterative book development with reader feedback.
- [[left-variadic-functions]] — JavaScript pattern for gathering arguments from the left
- [[lexical-scoping]] — JavaScript's mechanism for resolving variable names based on their position in the source code, rather than runtime context.
- [[linked-lists]] — JavaScript linked lists use structure sharing, where mutation of one alias affects all shared nodes. Contrast with array destructuring which creates copies. See (raw/javascriptallonge.pdf p.158-176) for copy-on-write strategies.
- [[logical-operators]] — JavaScript's logical operators (!, &&, ||) operate on truthiness, not strict booleans, with short-circuit evaluation.
- [[mapping]] — Applying a function to each element of a data structure.
- [[mapwith-and-flip]] — mapWith curries functions for data transformation, while flip reverses argument order. Both enable functional programming patterns in JavaScript.
- [[object-assign]] — JavaScript's Object.assign() method for shallow cloning and merging objects.
- [[object-destructuring]] — JavaScript object destructuring syntax and examples, including compact method syntax. sources: raw/javascriptallonge.pdf p.126-140
- [[partial-application]] — Function technique to fix arguments in JavaScript
- [[quasi-literals]] — JavaScript template strings with backticks and interpolation using ${expression}.
- [[reference-types]] — Non-primitive data types in JavaScript compared by reference identity.
- [[saros-cycle]] — An 18-year astronomical period used to predict recurring solar and lunar eclipses.
- [[ternary-operator]] — JavaScript's ternary operator (?) is a control-flow expression that evaluates a condition and returns one of two values.
- [[tortoise-and-hare-algorithm]] — Algorithm to detect loops in linked lists using two pointers (tortoise and hare). See (raw/javascriptallonge.pdf p.158-176) for implementation details.
- [[truthiness]] — JavaScript's truthiness determines behavior of logical operators and conditionals, with falsy values including false, null, undefined, NaN, 0, and empty string.
- [[unary-functions]] — Decorator to enforce single-argument functions in JavaScript
- [[value-types]] — Primitive data types in JavaScript compared by value equality.

## Syntheses
- [[wiki-health]] — Wiki health report from the latest lint pass (2026-06-10).
