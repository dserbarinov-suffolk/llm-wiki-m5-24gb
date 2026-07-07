---
page_id: javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-is-not-pattern-m-27d4b226
page_kind: source
summary: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching: 12 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-is-not-pattern-m-27d4b226@acfe9acebb352cc3fbd585fc6c16b55e
---

# Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-gathering-1b2d594b]] - previous source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-and-return-value-0323454e]] - next source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring and return values

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-2a38bfc8]] - broader source section: Composing and Decomposing Data / Arrays and Destructuring Arguments

## Statements

- Some other languages have something called pattern matching , where you can write something like a destructuring assignment, and the language decides whether the 'patterns' matches at all. If it does, assignments are made where appropriate. _(javascriptallonge.pdf (source-range-c98ab3e6-00842))_
- That match would fail because the array doesn't have an element to assign to what . But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. Therefore: _(javascriptallonge.pdf (source-range-c98ab3e6-00845))_
- From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-c98ab3e6-00849))_
- That match would fail because the array doesn't have an element to assign to what . _(javascriptallonge.pdf (source-range-c98ab3e6-00845))_
- This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-c98ab3e6-00849))_
