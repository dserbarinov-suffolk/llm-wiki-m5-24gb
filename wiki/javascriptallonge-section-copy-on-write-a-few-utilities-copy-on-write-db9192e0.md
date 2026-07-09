---
page_id: javascriptallonge-section-copy-on-write-a-few-utilities-copy-on-write-db9192e0
page_kind: source
summary: Copy on Write / a few utilities / copy-on-write: 11 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-write-a-few-utilities-copy-on-write-db9192e0@35ee3abc0ab185782bc27fa63ba3aa64
---

# Copy on Write / a few utilities / copy-on-write

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-copy-on-write-a-few-utilities-copy-on-read-2d301e7a]] - previous source section: Copy on Write / a few utilities / copy-on-read

### Source structure

- [[javascriptallonge-section-copy-on-write-a-few-utilities-7b82367a]] - broader source section: Copy on Write / a few utilities

### Recipes

- [[javascriptallonge-recipe-copy-on-write]] - recipe pattern: copy-on-write

### Topics

- [[javascriptallonge-copy-write]] - topic hub: opens the topic page for Copy Write

## Statements

- But our new parent and child lists are copies that contain the desired modifications, without interfering with each other: _(javascriptallonge.pdf (source-range-c98ab3e6-01224))_
- And now functions like mapWith that make copies without modifying anything, work at full speed. _(javascriptallonge.pdf (source-range-c98ab3e6-01226))_
- This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' _(javascriptallonge.pdf (source-range-c98ab3e6-01227))_
- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.Wikipedia 73 _(javascriptallonge.pdf (source-range-c98ab3e6-01228))_
- Like all strategies, it makes a tradeoff: It's much cheaper than pessimistically copying structures when you make an infrequent number of small changes, but if you tend to make a lot of changes to some that you aren't sharing, it's more expensive. _(javascriptallonge.pdf (source-range-c98ab3e6-01229))_
- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-c98ab3e6-01230))_
- This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' _(javascriptallonge.pdf (source-range-c98ab3e6-01227))_
