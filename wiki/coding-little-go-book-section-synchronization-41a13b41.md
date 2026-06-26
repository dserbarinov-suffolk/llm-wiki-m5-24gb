---
page_id: coding-little-go-book-section-synchronization-41a13b41
page_kind: source
summary: Synchronization: 30 source-backed entries and 5 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-synchronization-41a13b41@85e4059f5f56961985a364653bec3d56
---

# Synchronization

From [[coding-little-go-book]].

## Statements

- To help with this problem, Go provides channels . _(coding_little_go_book.pdf (source-range-810ce361-00408))_
- Creating goroutines is trivial, and they are so cheap that we can start many; however, concurrent code needs to be coordinated. _(coding_little_go_book.pdf (source-range-810ce361-00408))_
- Writing concurrent code requires that you pay specific attention to where and how you read and write values. _(coding_little_go_book.pdf (source-range-810ce361-00409))_
- However, the reality is that the behavior is undefined. _(coding_little_go_book.pdf (source-range-810ce361-00413))_
- Because we potentially have multiple (two in this case) goroutines writing to the same variable, counter , at the same time. _(coding_little_go_book.pdf (source-range-810ce361-00413))_
- If you think the output is 1, 2, ... _(coding_little_go_book.pdf (source-range-810ce361-00413))_
- Because we potentially have multiple (two in this case) goroutines writing to the same variable, counter , at the same time. _(coding_little_go_book.pdf (source-range-810ce361-00413))_
- If you run this example, you'll see that very often the numbers are printed in a weird order, and/or numbers are duplicated/missing. _(coding_little_go_book.pdf (source-range-810ce361-00414))_
- There are worse possibilities too, such as system crashes or accessing an arbitrary piece of data and incrementing it! _(coding_little_go_book.pdf (source-range-810ce361-00414))_
- There are worse possibilities too, such as system crashes or accessing an arbitrary piece of data and incrementing it! _(coding_little_go_book.pdf (source-range-810ce361-00414))_
- The only concurrent thing you can safely do to a variable is to read from it. _(coding_little_go_book.pdf (source-range-810ce361-00415))_
- You can have as many readers as you want, but writes need to be synchronized. _(coding_little_go_book.pdf (source-range-810ce361-00415))_
- There are various ways to do this, including using some truly atomic operations that rely on special CPU instructions. _(coding_little_go_book.pdf (source-range-810ce361-00415))_
- The only concurrent thing you can safely do to a variable is to read from it. _(coding_little_go_book.pdf (source-range-810ce361-00415))_
- The reason we simply define our lock as lock sync.Mutex is because the default value of a sync.Mutex is unlocked. _(coding_little_go_book.pdf (source-range-810ce361-00417))_
- The reason we simply define our lock as lock sync.Mutex is because the default value of a sync.Mutex is unlocked. _(coding_little_go_book.pdf (source-range-810ce361-00417))_
- We generally want fine locks; else, we end up with a ten-lane highway that suddenly turns into a one-lane road. _(coding_little_go_book.pdf (source-range-810ce361-00418))_
- While it might be tempting to use coarse locks (locks that cover a large amount of code), that undermines the very reason we're doing concurrent programming in the first place. _(coding_little_go_book.pdf (source-range-810ce361-00418))_
- First of all, it isn't always so obvious what code needs to be protected. _(coding_little_go_book.pdf (source-range-810ce361-00418))_
- The example above is deceptive. _(coding_little_go_book.pdf (source-range-810ce361-00418))_
- With a single lock, this isn't a problem, but if you're using two or more locks around the same code, it's dangerously easy to have situations where goroutineA holds lockA but needs access to lockB, while goroutineB holds lockB but needs access to lockA. _(coding_little_go_book.pdf (source-range-810ce361-00419))_
- The other problem has to do with deadlocks. _(coding_little_go_book.pdf (source-range-810ce361-00419))_
- This isn't as dangerous as a multi-lock deadlock (because those are really tough to spot), but just so you can see what happens, try running: _(coding_little_go_book.pdf (source-range-810ce361-00420))_
- It actually is possible to deadlock with a single lock, if we forget to release it. _(coding_little_go_book.pdf (source-range-810ce361-00420))_
- This isn't as dangerous as a multi-lock deadlock (because those are really tough to spot), but just so you can see what happens, try running: _(coding_little_go_book.pdf (source-range-810ce361-00420))_

## Technical atoms

> In some ways, it's like programming without a garbage collector -- it requires that you think about your data from a new angle, always watchful for possible danger.
_(source: coding_little_go_book.pdf (source-range-810ce361-00409))_

```
package main import ( "fmt" "time" ) var counter	=	0 func main()	{ for i	:=	0;	i	<	20;	i++	{ go incr()
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00410))_

```
} time.Sleep(time.Millisecond	*	10) } func incr()	{ counter++ fmt.Println(counter) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00411))_

```
package main import ( "fmt" "time" "sync" ) var ( counter	=	0 lock	sync.Mutex ) func main()	{ for i	:=	0;	i	<	20;	i++	{ go incr() } time.Sleep(time.Millisecond	*	10) } func incr()	{ lock.Lock() defer lock.Unlock() counter++ fmt.Println(counter) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00416))_

> There's a whole class of serious bugs that can arise when doing concurrent programming.
_(source: coding_little_go_book.pdf (source-range-810ce361-00418))_
