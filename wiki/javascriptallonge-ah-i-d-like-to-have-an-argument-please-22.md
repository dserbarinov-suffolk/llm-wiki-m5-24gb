---
page_id: javascriptallonge-ah-i-d-like-to-have-an-argument-please-22
page_kind: concept
summary: Ah. I'd Like to Have an Argument, Please. 22: 8 accepted assertion(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_e5a28d9d003dd1ef@84841874cede700b8960a6e158255bbf
---

# Ah. I'd Like to Have an Argument, Please. 22

Source: [[javascriptallonge]]

## Statements

- We haven't even said what an argument is , only that our functions don't have any. (javascriptallonge.pdf p.39)
- Up to now, we've looked at functions without arguments. (javascriptallonge.pdf p.39)
- Most programmers are perfectly familiar with arguments (often called 'parameters'). (javascriptallonge.pdf p.39)
- So you know what they are , and I know that you know what they are, but please be patient with the explanation!. (javascriptallonge.pdf p.39)
- This function has one argument, room , and an empty body. (javascriptallonge.pdf p.39)
- I'm sure you are perfectly comfortable with the idea that this function has two arguments, room , and board . (javascriptallonge.pdf p.39)
- I read that aloud as 'When applied to a value representing the diameter, this function returns the diameter times 3.14159265.'. (javascriptallonge.pdf p.39)
- You won't be surprised to see how to write and apply a function to two arguments:. (javascriptallonge.pdf p.39)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
(room) => {}
```

<a id="atom-2"></a>
**Atom:** code block

```
(room, board) => {}
```

<a id="atom-3"></a>
**Atom:** code block

```
(diameter) => diameter * 3.14159265
```

<a id="atom-4"></a>
**Atom:** code block

```
((diameter) => diameter * 3.14159265)(2)
//=> 6.2831853
```

<a id="atom-5"></a>
**Atom:** code block

```
((room, board) => room + board)(800, 150)
//=> 950
```
