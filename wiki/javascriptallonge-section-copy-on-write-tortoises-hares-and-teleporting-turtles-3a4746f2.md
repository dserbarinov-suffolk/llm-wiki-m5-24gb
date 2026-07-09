---
page_id: javascriptallonge-section-copy-on-write-tortoises-hares-and-teleporting-turtles-3a4746f2
page_kind: source
summary: Copy on Write / Tortoises, Hares, and Teleporting Turtles: 12 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-write-tortoises-hares-and-teleporting-turtles-3a4746f2@a0a750ef3df513406f6f5384e5f4030f
---

# Copy on Write / Tortoises, Hares, and Teleporting Turtles

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-copy-on-write-a-few-utilities-7b82367a]] - previous source section: Copy on Write / a few utilities
- [[javascriptallonge-section-copy-on-write-functional-iterators-74724e0a]] - next source section: Copy on Write / Functional Iterators

### Source structure

- [[javascriptallonge-section-copy-on-write-d081f846]] - broader source section: Copy on Write

### Recipes

- [[javascriptallonge-recipe-tortoises-hares-and-teleporting-turtles]] - recipe pattern: Tortoises, Hares, and Teleporting Turtles

## Statements

- A good long while ago (The First Age of Internet Startups), someone asked me one of those pet algorithm questions. It was, 'Write an algorithm to detect a loop in a linked list, in constant space.' _(javascriptallonge.pdf (source-range-c98ab3e6-01233))_
- I think I told him that I was trying to figure out if I could adapt a hashing algorithm such as XORing everything together. This is the 'trick answer' to a question about finding a missing integer from a list, so I was trying the old, 'Transform this into a problem you've already solved 74 ' meta-algorithm. We moved on from there, and he didn't reveal the 'solution.' _(javascriptallonge.pdf (source-range-c98ab3e6-01235))_
- I went home and pondered the problem. I wanted to solve it. Eventually, I came up with something and tried it (In Java!) on my home PC. I sent him an email sharing my result, to demonstrate my ability to follow through. I then forgot about it for a while. Some time later, I was told that the correct solution was: _(javascriptallonge.pdf (source-range-c98ab3e6-01236))_
- This algorithm is called 'The Tortoise and the Hare,' and was discovered by Robert Floyd in the 1960s. You have two node references, and one traverses the list at twice the speed of the other. No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you'll detect the loop. _(javascriptallonge.pdf (source-range-c98ab3e6-01240))_
- Years later, I came across a discussion of this algorithm, The Tale of the Teleporting Turtle 75 . It seems to be faster under certain circumstances, depending on the size of the loop and the relative costs of certain operations. _(javascriptallonge.pdf (source-range-c98ab3e6-01243))_
- What's interesting about these two algorithms is that they both tangle two separate concerns: How to traverse a data structure, and what to do with the elements that you encounter. In Functional Iterators, we'll investigate one pattern for separating these concerns. _(javascriptallonge.pdf (source-range-c98ab3e6-01244))_
- I then forgot about it for a while. _(javascriptallonge.pdf (source-range-c98ab3e6-01236))_
- No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you'll detect the loop. _(javascriptallonge.pdf (source-range-c98ab3e6-01240))_
