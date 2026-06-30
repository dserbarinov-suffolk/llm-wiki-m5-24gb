---
page_id: javascriptallonge-coffee
page_kind: concept
summary: Coffee: 5 statement(s) and 5 atom(s) from raw/javascriptallonge.pdf.
page_family: broad-topic
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-coffee@850676f6b4948e62722f3e1f2248c09d
---

# Coffee

What [[javascriptallonge]] covers about coffee:

## Statements

### Prelude: Values and Expressions over Coffee / values are expressions

- All values are expressions. Say you hand the barista a café Cubano. Yup, you hand over a cup with some coffee infused through partially caramelized sugar. You say, 'I want one of these.' The barista is no fool, she gives it straight back to you, and you get exactly what you want. Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). _(javascriptallonge.pdf (source-range-0e12e052-00103))_

- Now the barista gives us back an espresso. And if we hand over the espresso, we get the espresso right back. So, boiling water plus ground coffee is an expression, but it isn't a value. 11 Boiling water is a value. Ground coffee is a value. Espresso is a value. Boiling water plus ground coffee is an expression. _(javascriptallonge.pdf (source-range-0e12e052-00111))_

### A Warm Cup: Basic Strings and Quasi-Literals

- Coffee and a Book An expression is any valid unit of code that resolves to a value.-Mozilla Development Network: Expressions and operators 87 _(javascriptallonge.pdf (source-range-0e12e052-01494))_


## Technical atoms

### Technical frame 1: Prelude: Values and Expressions over Coffee

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00101))_

```text
Prelude: Values and Expressions over Coffee
The following material is extremely basic, however like most stories, the best way to begin is to start at the very beginning.
Imagine we are visiting our favourite coffee shop. They will make for you just about any drink you desire, from a short, intense espresso ristretto through a dry cappuccino, up to those coffee-flavoured desert concoctions featuring various concentrated syrups and milks. (You tolerate the existence of sugary drinks because they provide a sufficient profit margin to the establishment to finance your hanging out there all day using their WiFi and ordering a $3 drink every few hours.)
You express your order at one end of their counter, the folks behind the counter perform their magic, and deliver the coffee you value at the other end. This is exactly how the JavaScript environment works for the purpose of this book. We are going to dispense with web servers, browsers and other complexities and deal with this simple model: You give the computer an expression 8 , and it returns a value 9 , just as you express your wishes to a barista and receive a coffee in return.
8 https://en.wikipedia.org/wiki/Expression_
9 https://en.wikipedia.org/wiki/Value_
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 8 | https://en.wikipedia.org/wiki/Expression_ |
| 9 | https://en.wikipedia.org/wiki/Value_ |

</details>

### Technical frame 2: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00110))_

> Astute readers will realize we're omitting something. Congratulations! Take a sip of espresso. We'll get to that in a moment.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00111))_

> And if we hand over the espresso, we get the espresso right back.

### Technical frame 3: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00122))_

> Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00114))_

```text
10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' and so does the computer.
11 In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 10 | Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' and so does the computer. |
| 11 | In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values. |

</details>

### Technical frame 4: Prelude: Values and Expressions over Coffee / values are expressions

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00122))_

> Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00116))_

```text
2 In JavaScript, we test whether two values are identical with the operator, and whether they are === not identical with the operator: !== 2 === 2 //=> true 'hello' !== 'goodbye' //=> true How does work, exactly? Imagine that you’re shown a cup of coffee. And then you’re shown === another cup of coffee. Are the two cups “identical?” In JavaScript, there are four possibilities: First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types. For example, the string "2" is not the same thing as the number 2. Strings and numbers are different types, so strings and numbers are never identical:
2 === '2' //=> false true !== 'true' //=> true Second, sometimes, the cups are of the same type–perhaps two espresso cups–but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2. true === false //=> false
2 !== 5 //=> true 'two' === 'five' //=> false What if the cups are of the same type and the contents are the same? Well, JavaScript’s third and fourth possibilities cover that. Prelude: Values and Expressions over Coffee xvii value types Third, some types of cups have no distinguishing marks on them. If they are the same kind of cup, and they hold the same contents, we have no way to tell the difference between them. This is the case with the strings, numbers, and booleans we have seen so far.
2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably. We haven’t encountered the fourth possibility yet. Stretching the metaphor somewhat, some types of cups have a serial number on the bottom. So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them. Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d’Italia reference types So what kinds of values might be the same type and have the same contents, but not be considered identical to JavaScript? Let’s meet a data structure that is very common in contemporary programming languages, the Array (other languages sometimes call it a List or a Vector). Prelude: Values and Expressions over Coffee xviii An array looks like this: [1, 2, 3]. This is an expression, and you can combine [] with other expressions. Go wild with things like: [2-1, 2, 2+1] [1, 1+1, 1+1+1] Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of is identical to every other value of 42? Try these for yourself: 42 [2-1, 2, 2+1] === [1,2,3] [1,2,3] === [1, 2, 3] [1, 2, 3] === [1, 2, 3] How about that! When you type or any of its variations, you are typing an expression [1, 2, 3] that generates its own unique array that is not identical to any other array, even if that other array also looks like 3]. It’s as if JavaScript is generating new cups of coffee with serial numbers [1, 2, on the bottom. They look the same, but if you examine them with ===, you see that they are different. Every time you evaluate an expression (including typing something in) to create an array, you’re creating a new, distinct value even if it appears to be the same as some other array value. As we’ll see, this is true of many other kinds of values, including functions, the main subject of this book.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 2 | In JavaScript, we test whether two values are identical with the operator, and whether they are === not identical with the operator:!== 2 === 2 //=> true 'hello'!== 'goodbye' //=> true How does work, exactly? Imagine that you’re shown a cup of coffee. And then you’re shown === another cup of coffee. Are the two cups “identical?” In JavaScript, there are four possibilities: First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types. For example, the string "2" is not the same thing as the number 2. Strings and numbers are different types, so strings and numbers are never identical: |
| 2 | === '2' //=> false true!== 'true' //=> true Second, sometimes, the cups are of the same type–perhaps two espresso cups–but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2. true === false //=> false 2!== 5 //=> true 'two' === 'five' //=> false What if the cups are of the same type and the contents are the same? Well, JavaScript’s third and fourth possibilities cover that. Prelude: Values and Expressions over Coffee xvii value types Third, some types of cups have no distinguishing marks on them. If they are the same kind of cup, and they hold the same contents, we have no way to tell the difference between them. This is the case with the strings, numbers, and booleans we have seen so far. |
| 2 | + 2 === 4 //=> true (2 + 2 === 4) === (2!== 5) //=> true Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably. We haven’t encountered the fourth possibility yet. Stretching the metaphor somewhat, some types of cups have a serial number on the bottom. So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them. Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d’Italia reference types So what kinds of values might be the same type and have the same contents, but not be considered identical to JavaScript? Let’s meet a data structure that is very common in contemporary programming languages, the Array (other languages sometimes call it a List or a Vector). Prelude: Values and Expressions over Coffee xviii An array looks like this: [1, 2, 3]. This is an expression, and you can combine [] with other expressions. Go wild with things like: [2-1, 2, 2+1] [1, 1+1, 1+1+1] Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of is identical to every other value of 42? Try these for yourself: 42 [2-1, 2, 2+1] === [1,2,3] [1,2,3] === [1, 2, 3] [1, 2, 3] === [1, 2, 3] How about that! When you type or any of its variations, you are typing an expression [1, 2, 3] that generates its own unique array that is not identical to any other array, even if that other array also looks like 3]. It’s as if JavaScript is generating new cups of coffee with serial numbers [1, 2, on the bottom. They look the same, but if you examine them with ===, you see that they are different. Every time you evaluate an expression (including typing something in) to create an array, you’re creating a new, distinct value even if it appears to be the same as some other array value. As we’ll see, this is true of many other kinds of values, including functions, the main subject of this book. |

</details>

### Technical frame 5: The Golden Crema: Appendices and Afterwords / Copyright Notice / images

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-02041))_

```text
163 http://www.flickr.com/photos/93425126@N00/313053257/ 164 http://creativecommons.org/licenses/by-sa/2.0/deed.en 165 http://www.flickr.com/photos/digitalcolony/2833809436/ 166 http://creativecommons.org/licenses/by-sa/2.0/deed.en 167 http://www.flickr.com/photos/citizenhelder/5006498068/ 168 http://creativecommons.org/licenses/by/2.0/deed.en 169 http://www.flickr.com/photos/joncrel/237026246/ 170 http://creativecommons.org/licenses/by-nd/2.0/deed.en 171 http://www.flickr.com/photos/nalundgaard/3163852170/ 172 http://creativecommons.org/licenses/by-sa/2.0/deed.en 173 http://www.flickr.com/photos/47000103@N05/6525288841/ 174 http://creativecommons.org/licenses/by-sa/2.0/deed.en 175 http://www.flickr.com/photos/lotzman/978418891/ 176 http://creativecommons.org/licenses/by/2.0/deed.en 177 http://www.flickr.com/photos/kk/sets/72157626168201654/with/5484839102/ 178 http://creativecommons.org/licenses/by-sa/2.0/deed.en 179 https://www.flickr.com/photos/kellan/434503323 180 http://creativecommons.org/licenses/by/2.0/deed.en 181 https://www.flickr.com/photos/whitneyinchicago/3835218626 182 http://creativecommons.org/licenses/by/2.0/deed.en 183 https://www.flickr.com/photos/sankarshan/5165312159 184 http://creativecommons.org/licenses/by-sa/2.0/deed.en 185 https://www.flickr.com/photos/candy-s/7619358284 186 https://www.flickr.com/photos/candy-s/ 187 http://creativecommons.org/licenses/by/2.0/deed.en 188 https://www.flickr.com/photos/lorentey/22193876 189 https://www.flickr.com/photos/lorentey/ 190 http://creativecommons.org/licenses/by/2.0/deed.en 191 https://www.flickr.com/photos/kk/5484876862 192 http://creativecommons.org/licenses/by-sa/2.0/deed.en 193 https://www.flickr.com/photos/f_mafra/2956649121 194
http://creativecommons.org/licenses/by-sa/2.0/deed.en
coffee pots 195 (c) 2009 Jonas Forth Some rights reserved 196 .
5 Barrel Roaster 197 (c) 2013 David Lytle Some rights reserved 198 .
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 163 | http://www.flickr.com/photos/93425126@N00/313053257/ |
| 164 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 165 | http://www.flickr.com/photos/digitalcolony/2833809436/ |
| 166 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 167 | http://www.flickr.com/photos/citizenhelder/5006498068/ |
| 168 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 169 | http://www.flickr.com/photos/joncrel/237026246/ |
| 170 | http://creativecommons.org/licenses/by-nd/2.0/deed.en |
| 171 | http://www.flickr.com/photos/nalundgaard/3163852170/ |
| 172 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 173 | http://www.flickr.com/photos/47000103@N05/6525288841/ |
| 174 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 175 | http://www.flickr.com/photos/lotzman/978418891/ |
| 176 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 177 | http://www.flickr.com/photos/kk/sets/72157626168201654/with/5484839102/ |
| 178 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 179 | https://www.flickr.com/photos/kellan/434503323 |
| 180 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 181 | https://www.flickr.com/photos/whitneyinchicago/3835218626 |
| 182 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 183 | https://www.flickr.com/photos/sankarshan/5165312159 |
| 184 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 185 | https://www.flickr.com/photos/candy-s/7619358284 |
| 186 | https://www.flickr.com/photos/candy-s/ |
| 187 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 188 | https://www.flickr.com/photos/lorentey/22193876 |
| 189 | https://www.flickr.com/photos/lorentey/ |
| 190 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 191 | https://www.flickr.com/photos/kk/5484876862 |
| 192 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 193 | https://www.flickr.com/photos/f_mafra/2956649121 194 http://creativecommons.org/licenses/by-sa/2.0/deed.en coffee pots 195 (c) 2009 Jonas Forth Some rights reserved 196. |
| 5 | Barrel Roaster 197 (c) 2013 David Lytle Some rights reserved 198. |

</details>


## Related pages

- [[javascriptallonge-expression-coffee]] - narrower topic: Expression Coffee shares source evidence from Prelude: Values and Expressions over Coffee / values are expressions: Now the barista gives us back an espresso. And if we hand over the espresso, we get the espresso right back. So, boiling water plus ground coffee is an expression, b ... [truncated]; Expression Coffee shares technical record from Prelude: Values and Expressions over Coffee / values are expressions: And if we hand over the espresso, we get the espresso right back. (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms: Expression shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: Coffee and a Book An expression is any valid unit of code that resolves to a value.-Mozilla Development Network: Expressions and operators 87; Expression shares technical record from Prelude: Values and Expressions over Coffee: Prelude: Values and Expressions over Coffee The following material is extremely basic, however like most stories, the best way to begin is to start at the very begin ... [truncated] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Prelude: Values and Expressions over Coffee / values are expressions: 10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' ... [truncated] (2 shared atom(s))
- [[javascriptallonge-string]] - shared technical atoms: String shares technical record from Prelude: Values and Expressions over Coffee / values are expressions: 2 In JavaScript, we test whether two values are identical with the operator, and whether they are === not identical with the operator: !== 2 === 2 //=> true 'hello' ... [truncated] (1 shared atom(s))
- [[javascriptallonge-type]] - shared technical atoms: Type shares technical record from Prelude: Values and Expressions over Coffee / values are expressions: 2 In JavaScript, we test whether two values are identical with the operator, and whether they are === not identical with the operator: !== 2 === 2 //=> true 'hello' ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
