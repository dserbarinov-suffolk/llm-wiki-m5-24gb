---
page_id: javascriptallonge-statement
page_kind: concept
summary: Statement: 6 statement(s) and 8 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-statement@5e8bc6a15603f3ca56cf31fe66a39ba3
---

# Statement

What [[javascriptallonge]] covers about statement:

## Statements

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / a quick summary of functions and bodies

- One of the important possible statements is a return statement. A return statement accepts any valid JavaScript expression. _(javascriptallonge.pdf (source-range-c98ab3e6-00274))_

### That Constant Coffee Craving / nested blocks

- The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like: _(javascriptallonge.pdf (source-range-c98ab3e6-00427))_

### That Constant Coffee Craving / are consts also from a shadowy planet?

- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. So where are const variables bound? In the function environment? Or in an environment corresponding to the block? _(javascriptallonge.pdf (source-range-c98ab3e6-00450))_

- Parameters are only bound when we invoke a function. That's why we made all these IIFEs. But const statements can appear inside blocks. What happens when we use a const inside of a block? We'll need a gratuitous block. We've seen if statements, what could be more gratuitous than: _(javascriptallonge.pdf (source-range-c98ab3e6-00466))_

### Summary / Functions

- Blocks also create scopes if const statements are within them. _(javascriptallonge.pdf (source-range-c98ab3e6-00633))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

- The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do the same thing with more than one element: _(javascriptallonge.pdf (source-range-c98ab3e6-00827))_


## Technical atoms

### Technical frame 1: That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00427))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00424))_

<a id="atom-technical-atom-ef73fd8cc79e6d6c"></a>
```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else
return !even(x - 1);
}
return even(n)
}
```

### Technical frame 2: That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00431))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00428))_

<a id="atom-technical-atom-dbc87a43c0709132"></a>
```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else {
const odd = (y) => !even(y);
return odd(x - 1);
}
```

### Technical frame 3: That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00431))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00430))_

<a id="atom-technical-atom-fef472217bf6fc04"></a>
```
//=> true
```

### Technical frame 4: That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00474))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00468))_

<a id="atom-technical-atom-c164dd0fd5dca0c5"></a>
```
})(2)
//=> 6.2831853
```

### Technical frame 5: That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00474))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00471))_

<a id="atom-technical-atom-e84da0d8c3993eab"></a>
```
((diameter) => {
const PI = 3.14159265;
if (true) {
const PI = 3;
}
return diameter * PI;
})(2)
//=> would return 6 if const had function scope
```

### Technical frame 6: That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00474))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00473))_

<a id="atom-technical-atom-bc18138dffce4c0f"></a>
```
((diameter) => {
if (true) {
const PI = 3.14159265;
}
return diameter * PI;
})(2)
//=> would return 6.2831853 if const had function scope
```

### Technical frame 7: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00827))_

> The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do the same thing with more than one element:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00826))_

<a id="atom-technical-atom-52b3dbb7f1aa6d3b"></a>
```
const unwrap = (wrapped) => {
const [something] = wrapped;
return something;
}
unwrap(["present"])
//=> "present"
```

### Technical frame 8: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00829))_

> We could do the same thing with (name) => name[1] , but destructuring is code that resembles the data it consumes, a valuable coding style.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00828))_

<a id="atom-technical-atom-34f749726f38e3e4"></a>
```
const surname = (name) => {
const [first, last] = name;
return last;
}
surname(["Reginald", "Braithwaite"])
//=> "Braithwaite"
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from That Constant Coffee Craving / nested blocks: (n) => { const even = (x) => { if (x === 0) return true; else { const odd = (y) => !even(y); return odd(x - 1); } (2 shared atom(s))
- [[javascriptallonge-array]] - shared statements and technical atoms: Array shares source evidence from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays: The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do ... [truncated]; Array shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays: const surname = (name) => { const [first, last] = name; return last; } surname(["Reginald", "Braithwaite"]) //=> "Braithwaite" (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-parameter]] - shared technical atoms: Parameter shares technical record from That Constant Coffee Craving / are consts also from a shadowy planet?: })(2) //=> 6.2831853 (1 shared atom(s))

### Shared claims

- [[javascriptallonge-scope]] - shared statements: Scope shares source evidence from Summary / Functions: Blocks also create scopes if const statements are within them. (1 shared statement(s))

## Source

- [[javascriptallonge]]
