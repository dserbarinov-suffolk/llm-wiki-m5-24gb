---
page_id: javascriptallonge-a-few-utilities-through-copy-on-write
page_kind: source
summary: a few utilities through copy-on-write from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.159-161, raw/javascriptallonge.pdf p.161-161, raw/javascriptallonge.pdf p.162-163
updated: 2026-06-20
domain: javascriptallonge
category_path: source-sections
source_id: javascriptallonge.pdf
---

## Source record

Source record for [[javascriptallonge-a-few-utilities-through-copy-on-write]]. (raw/javascriptallonge.pdf)

## Key supported claims

- Copy-on-write is a strategy where a copy of shared information is made only when a change is attempted, ensuring modifications are isolated to the private copy. (raw/javascriptallonge.pdf)
- The main difference is that array[index] = value evaluates to value, while set(index, value, list) evaluates to the modified list. (raw/javascriptallonge.pdf)
- The 'copy-on-read' strategy involves making a copy when reading a child of the list to allow free modification of the parent or the copy. (raw/javascriptallonge.pdf)
- The mapWith function would be very expensive if a copy is made every time rest(node) is called. (raw/javascriptallonge.pdf)
