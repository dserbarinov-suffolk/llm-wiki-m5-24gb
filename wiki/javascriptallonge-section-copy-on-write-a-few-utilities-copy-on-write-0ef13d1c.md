---
page_id: javascriptallonge-section-copy-on-write-a-few-utilities-copy-on-write-0ef13d1c
page_kind: source
summary: Copy on Write / a few utilities / copy-on-write: 11 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-write-a-few-utilities-copy-on-write-0ef13d1c@436e01329ab1440be890fa3e8014f844
---

# Copy on Write / a few utilities / copy-on-write

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-copy-on-write-a-few-utilities-copy-on-read-aa66973b]] - previous source section: Copy on Write / a few utilities / copy-on-read

### Source structure

- [[javascriptallonge-section-copy-on-write-a-few-utilities-a7dc3b9f]] - broader source section: Copy on Write / a few utilities

### Topics

- [[javascriptallonge-copy-write]] - topic hub: opens the topic page for Copy Write

## Statements

- But our new parent and child lists are copies that contain the desired modifications, without interfering with each other: _(javascriptallonge.pdf (source-range-c98ab3e6-01244))_
- And now functions like mapWith that make copies without modifying anything, work at full speed. _(javascriptallonge.pdf (source-range-c98ab3e6-01246))_
- This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' _(javascriptallonge.pdf (source-range-c98ab3e6-01247))_
- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.Wikipedia 73 _(javascriptallonge.pdf (source-range-c98ab3e6-01248))_
- Like all strategies, it makes a tradeoff: It's much cheaper than pessimistically copying structures when you make an infrequent number of small changes, but if you tend to make a lot of changes to some that you aren't sharing, it's more expensive. _(javascriptallonge.pdf (source-range-c98ab3e6-01249))_
- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-c98ab3e6-01250))_
- This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' _(javascriptallonge.pdf (source-range-c98ab3e6-01247))_
