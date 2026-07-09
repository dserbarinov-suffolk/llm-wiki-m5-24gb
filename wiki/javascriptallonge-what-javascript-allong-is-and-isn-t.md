---
page_id: javascriptallonge-what-javascript-allong-is-and-isn-t
page_kind: concept
summary: What JavaScript Allongé is. And isn't.: 17 accepted assertion(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_655357ca4ec385d5@b3d2366902de28071ff6666b761031e3
---

# What JavaScript Allongé is. And isn't.

Source: [[javascriptallonge]]

## Statements

- JavaScript Allongé is a book about programming with functions. (javascriptallonge.pdf p.10)
- The intention is to improve the way we think about programs. (javascriptallonge.pdf p.10)
- The focus in this book on the underlying ideas, what we might call the fundamentals, and how they combine to form new ideas. (javascriptallonge.pdf p.10)
- There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others. (javascriptallonge.pdf p.10)
- But while JavaScript Allongé attempts to be provocative, it is not prescriptive . (javascriptallonge.pdf p.10)
- Software development is a complex field. (javascriptallonge.pdf p.10)
- People often say that software should be written for people to read. (javascriptallonge.pdf p.10)
- For example, business software written in-house has a very different set of requirements than a library written to be publicly distributed as open-source. (javascriptallonge.pdf p.10)
- If a particular codebase is written with lots of helper functions that place the subject first, like this:. (javascriptallonge.pdf p.11)
- Choices in software development must also consider the question of consistency. (javascriptallonge.pdf p.11)
- Then it can be jarring to add new helpers written that place the verb first, like this:. (javascriptallonge.pdf p.11)
- The use of linters 1 makes checking for certain types of undesirable code very cheap. (javascriptallonge.pdf p.11)
- Finally, choices in software development cannot ignore the tooling that is used to create and maintain software. (javascriptallonge.pdf p.11)
- Continuous integration encourages the creation of software in tandem with and factored to facilitate the creation of automated test suites. (javascriptallonge.pdf p.11)
- The use of source-code control systems with integrated diffing rewards making certain types of focused changes. (javascriptallonge.pdf p.11)
- Debuggers encourage the use of functions with explicit or implicit names. (javascriptallonge.pdf p.11)
- JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn't a book about practicing, it's a book about thinking. (javascriptallonge.pdf p.11)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const mapWith = (iterable, fn) =>
({
[Symbol.iterator]: function* () {
for (let element of iterable) {
yield fn(element);
}
}
});
```

<a id="atom-2"></a>
**Atom:** code block

```
const filterWith = (fn, iterable) =>
({
[Symbol.iterator]: function* () {
for (let element of iterable) {
if (!!fn(element)) yield element;
}
}
});
```
