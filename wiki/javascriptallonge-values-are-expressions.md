---
page_id: javascriptallonge-values-are-expressions
page_kind: concept
summary: topic-concept: 22 supported fragment(s) and 0 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_507f6603d88b129b@c5f2fc9aedf5c97c803500e7b504e72d
---

# values are expressions

Source: [[javascriptallonge]]

## Procedure

- All values are expressions. (javascriptallonge.pdf p.19)
- You say, 'I want one of these.' The barista is no fool, she gives it straight back to you, and you get exactly what you want. (javascriptallonge.pdf p.19)
- Yup, you hand over a cup with some coffee infused through partially caramelized sugar. (javascriptallonge.pdf p.19)
- Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). (javascriptallonge.pdf p.19)
- The answer is , this is both an expression and a value. (javascriptallonge.pdf p.19)
- All values are expressions. (javascriptallonge.pdf p.19)
- Instead of handing over the finished coffee, we can hand over the ingredients. (javascriptallonge.pdf p.19)
- Astute readers will realize we're omitting something. (javascriptallonge.pdf p.19)
- Ground coffee is a value. (javascriptallonge.pdf p.19)
- Boiling water plus ground coffee is an expression. (javascriptallonge.pdf p.19)
- 11 Boiling water is a value. (javascriptallonge.pdf p.19)
- So, boiling water plus ground coffee is an expression, but it isn't a value. (javascriptallonge.pdf p.19)
- One is a demitasse, the other a mug. (javascriptallonge.pdf p.21)
- This corresponds to comparing two things in JavaScript that have different types . (javascriptallonge.pdf p.21)
- First, sometimes, the cups are of different kinds. (javascriptallonge.pdf p.21)
- For example, the string "2" is not the same thing as the number 2 . (javascriptallonge.pdf p.21)
- This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 . (javascriptallonge.pdf p.21)
- One holds a single, one a double. (javascriptallonge.pdf p.21)

## Required tables and formulas

<a id="atom-1"></a>
**Atom:** table

```text
10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' and so does the computer.
11 In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values.
```

<a id="atom-2"></a>
**Atom:** table

```text
2 In JavaScript, we test whether two values are identical with the operator, and whether they are === not identical with the operator: !== 2 === 2 //=> true 'hello' !== 'goodbye' //=> true How does work, exactly? Imagine that you’re shown a cup of coffee. And then you’re shown === another cup of coffee. Are the two cups “identical?” In JavaScript, there are four possibilities: First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types. For example, the string "2" is not the same thing as the number 2. Strings and numbers are different types, so strings and numbers are never identical:
2 === '2' //=> false true !== 'true' //=> true Second, sometimes, the cups are of the same type–perhaps two espresso cups–but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2. true === false //=> false
2 !== 5 //=> true 'two' === 'five' //=> false What if the cups are of the same type and the contents are the same? Well, JavaScript’s third and fourth possibilities cover that. Prelude: Values and Expressions over Coffee xvii value types Third, some types of cups have no distinguishing marks on them. If they are the same kind of cup, and they hold the same contents, we have no way to tell the difference between them. This is the case with the strings, numbers, and booleans we have seen so far.
2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably. We haven’t encountered the fourth possibility yet. Stretching the metaphor somewhat, some types of cups have a serial number on the bottom. So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them. Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d’Italia reference types So what kinds of values might be the same type and have the same contents, but not be considered identical to JavaScript? Let’s meet a data structure that is very common in contemporary programming languages, the Array (other languages sometimes call it a List or a Vector). Prelude: Values and Expressions over Coffee xviii An array looks like this: [1, 2, 3]. This is an expression, and you can combine [] with other expressions. Go wild with things like: [2-1, 2, 2+1] [1, 1+1, 1+1+1] Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of is identical to every other value of 42? Try these for yourself: 42 [2-1, 2, 2+1] === [1,2,3] [1,2,3] === [1, 2, 3] [1, 2, 3] === [1, 2, 3] How about that! When you type or any of its variations, you are typing an expression [1, 2, 3] that generates its own unique array that is not identical to any other array, even if that other array also looks like 3]. It’s as if JavaScript is generating new cups of coffee with serial numbers [1, 2, on the bottom. They look the same, but if you examine them with ===, you see that they are different. Every time you evaluate an expression (including typing something in) to create an array, you’re creating a new, distinct value even if it appears to be the same as some other array value. As we’ll see, this is true of many other kinds of values, including functions, the main subject of this book.
```


## Rules and exceptions

- Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). (javascriptallonge.pdf p.19)
- Instead of handing over the finished coffee, we can hand over the ingredients. (javascriptallonge.pdf p.19)
