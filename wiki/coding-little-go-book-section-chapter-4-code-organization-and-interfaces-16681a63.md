---
page_id: coding-little-go-book-section-chapter-4-code-organization-and-interfaces-16681a63
page_kind: source
summary: Chapter 4 - Code Organization and Interfaces: 85 source-backed entries and 1 atom(s) from raw/coding_little_go_book.pdf.
page_family: section-reference
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-4-code-organization-and-interfaces-16681a63@3cc980db7aeca8c75f5b2aba711073e3
---

# Chapter 4 - Code Organization and Interfaces

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-57d2c239]] - narrower source section: Chapter 4 - Code Organization and Interfaces / Packages
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-interfaces-ee136513]] - narrower source section: Chapter 4 - Code Organization and Interfaces / Interfaces
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-before-you-continue-75e8df25]] - narrower source section: Chapter 4 - Code Organization and Interfaces / Before You Continue
- [[coding-little-go-book-section-chapter-3-maps-arrays-and-slices-4800f0d1]] - previous source section: Chapter 3 - Maps, Arrays and Slices
- [[coding-little-go-book-section-chapter-5-tidbits-e7a41f7c]] - next source section: Chapter 5 - Tidbits

## Statements by subsection

### Chapter 4 - Code Organization and Interfaces / Packages

- Notice that the name of the package is the same as the name of the folder. Also, obviously, we aren't actually accessing the database. We're just using this as an example to show how to organize code. _(coding_little_go_book.pdf (source-range-23d24eb1-00277))_
- Now, create a file called pricecheck.go inside of the main shopping folder. Its content is: _(coding_little_go_book.pdf (source-range-23d24eb1-00278))_
- It's tempting to think that importing shopping/db is somehow special because we're inside the shopping package/folder already. In reality, you're importing $GOPATH/src/shopping/db , which means you could just as easily import test/db so long as you had a package named db inside of your workspace's src/test folder. _(coding_little_go_book.pdf (source-range-23d24eb1-00280))_
- If you're building a package, you don't need anything more than what we've seen. To build an executable, you still need a main . The way I prefer to do this is to create a subfolder called main inside of shopping with a file called main.go and the following content: _(coding_little_go_book.pdf (source-range-23d24eb1-00281))_
- Now, create a file called pricecheck.go inside of the main shopping folder. _(coding_little_go_book.pdf (source-range-23d24eb1-00278))_
- It's tempting to think that importing shopping/db is somehow special because we're inside the shopping package/folder already. _(coding_little_go_book.pdf (source-range-23d24eb1-00280))_
- The way I prefer to do this is to create a subfolder called main inside of shopping with a file called main.go and the following content: _(coding_little_go_book.pdf (source-range-23d24eb1-00281))_

### Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports

- As you start writing more complex systems, you're bound to run into cyclical imports. This happens when package A imports package B but package B imports package A (either directly or indirectly through another package). This is something the compiler won't allow. _(coding_little_go_book.pdf (source-range-23d24eb1-00286))_
- If you try to run the code, you'll get a couple of errors from db/db.go about Item being undefined. This makes sense. Item no longer exists in the db package; it's been moved to the shopping package. We need to change shopping/db/db.go to: _(coding_little_go_book.pdf (source-range-23d24eb1-00290))_
- pricecheck.go will still import shopping/db , but db.go will now import shopping/models instead of shopping , thus breaking the cycle. Since we moved the shared Item structure to shopping/models/item.go , we need to change shopping/db/db.go to reference the Item structure from models package: _(coding_little_go_book.pdf (source-range-23d24eb1-00295))_
- You'll often need to share more than just models , so you might have other similar folders named utilities and such. The important rule about these shared packages is that they shouldn't import anything from the shopping package or any sub-packages. In a few sections, we'll look at interfaces which can help us untangle these types of dependencies. _(coding_little_go_book.pdf (source-range-23d24eb1-00297))_
- pricecheck.go will still import shopping/db , but db.go will now import shopping/models instead of shopping , thus breaking the cycle. _(coding_little_go_book.pdf (source-range-23d24eb1-00295))_

### Chapter 4 - Code Organization and Interfaces / Packages / Visibility

- Go uses a simple rule to define what types and functions are visible outside of a package. If the name of the type or function starts with an uppercase letter, it's visible. If it starts with a lowercase letter, it isn't. _(coding_little_go_book.pdf (source-range-23d24eb1-00299))_
- This also applies to structure fields. If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. _(coding_little_go_book.pdf (source-range-23d24eb1-00300))_
- it could be called via models.NewItem() . But if the function was named newItem , we wouldn't be able to access it from a different package. _(coding_little_go_book.pdf (source-range-23d24eb1-00303))_
- If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. _(coding_little_go_book.pdf (source-range-23d24eb1-00300))_

### Chapter 4 - Code Organization and Interfaces / Packages / Package Management

- The go command we've been using to run and build has a get subcommand which is used to fetch third-party libraries. go get supports various protocols but for this example, we'll be getting a library from Github, meaning, you'll need git installed on your computer. _(coding_little_go_book.pdf (source-range-23d24eb1-00306))_
- Assuming you already have git installed, from a shell/command prompt, enter: _(coding_little_go_book.pdf (source-range-23d24eb1-00307))_
- go get fetches the remote files and stores them in your workspace. Go ahead and check your $GOPATH/src . In addition to the shopping project that we created, you'll now see a github.com folder. Within, you'll see a mattn folder which contains a go-sqlite3 folder. _(coding_little_go_book.pdf (source-range-23d24eb1-00309))_
- We just talked about how to import packages that live in our workspace. To use our newly gotten go-sqlite3 package, we'd import it like so: _(coding_little_go_book.pdf (source-range-23d24eb1-00310))_
- Within, you'll see a mattn folder which contains a go-sqlite3 folder. _(coding_little_go_book.pdf (source-range-23d24eb1-00309))_

### Chapter 4 - Code Organization and Interfaces / Packages / Dependency Management

- go get has a couple of other tricks up its sleeve. If we go get within a project, it'll scan all the files, looking for imports to third-party libraries and will download them. In a way, our own source code becomes a Gemfile or package.json . _(coding_little_go_book.pdf (source-range-23d24eb1-00314))_
- Eventually, you might find go get inadequate. For one thing, there's no way to specify a revision, it always points to the master/head/trunk/default. This is an even larger problem if you have two projects needing different versions of the same library. _(coding_little_go_book.pdf (source-range-23d24eb1-00316))_
- To solve this, you can use a third-party dependency management tool. They are still young, but two promising ones are goop and godep. A more complete list is available at the go-wiki. _(coding_little_go_book.pdf (source-range-23d24eb1-00317))_

### Chapter 4 - Code Organization and Interfaces / Interfaces

- Interfaces are types that define a contract but not an implementation. Here's an example: _(coding_little_go_book.pdf (source-range-23d24eb1-00319))_
- You might be wondering what purpose this could possibly serve. Interfaces help decouple your code from specific implementations. For example, we might have various types of loggers: _(coding_little_go_book.pdf (source-range-23d24eb1-00321))_
- Yet by programming against the interface, rather than these concrete implementations, we can easily change (and test) which we use without any impact to our code. _(coding_little_go_book.pdf (source-range-23d24eb1-00323))_
- In a language like C# or Java, we have to be explicit when a class implements an interface: In Go, this happens implicitly. If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . This cuts down on the verboseness of using interfaces: } public class ConsoleLogger : Logger { public void Logger(message string) { Console.WriteLine(message) } } type ConsoleLogger struct {} (l ConsoleLogger) Log(message string) { _(coding_little_go_book.pdf (source-range-23d24eb1-00327))_
- It also tends to promote small and focused interfaces. The standard library is full of interfaces. The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . If you write a function that expects a parameter that you'll only be calling Close() on, you absolutely should accept an io.Closer rather than whatever concrete type you're using. _(coding_little_go_book.pdf (source-range-23d24eb1-00329))_
- Interfaces can also participate in composition. And, interfaces themselves can be composed of other interfaces. For example, io.ReadCloser is an interface composed of the io.Reader interface as well as the io.Closer interface. _(coding_little_go_book.pdf (source-range-23d24eb1-00330))_
- Finally, interfaces are commonly used to avoid cyclical imports. Since they don't have implementations, they'll have limited dependencies. _(coding_little_go_book.pdf (source-range-23d24eb1-00331))_
- If your structure has a function name Log with a string parameter and no return value, then it can be used as a Logger . _(coding_little_go_book.pdf (source-range-23d24eb1-00327))_
- If you write a function that expects a parameter that you'll only be calling Close() on, you absolutely should accept an io.Closer rather than whatever concrete type you're using. _(coding_little_go_book.pdf (source-range-23d24eb1-00329))_
- The io package has a handful of popular ones such as io.Reader , io.Writer , and io.Closer . _(coding_little_go_book.pdf (source-range-23d24eb1-00329))_
- For example, io.ReadCloser is an interface composed of the io.Reader interface as well as the io.Closer interface. _(coding_little_go_book.pdf (source-range-23d24eb1-00330))_
- Since they don't have implementations, they'll have limited dependencies. _(coding_little_go_book.pdf (source-range-23d24eb1-00331))_

### Chapter 4 - Code Organization and Interfaces / Before You Continue

- Ultimately, how you structure your code around Go's workspace is something that you'll only feel comfortable with after you've written a couple of non-trivial projects. What's most important for you to remember is the tight relationship between package names and your directory structure (not just within a project, but within the entire workspace). _(coding_little_go_book.pdf (source-range-23d24eb1-00333))_
- The way Go handles visibility of types is straightforward and effective. It's also consistent. There are a few things we haven't looked at, such as constants and global variables but rest assured, their visibility is determined by the same naming rule. _(coding_little_go_book.pdf (source-range-23d24eb1-00334))_
- Finally, if you're new to interfaces, it might take some time before you get a feel for them. However, the first time you see a function that expects something like io.Reader , you'll find yourself thanking the author for not demanding more than he or she needed. _(coding_little_go_book.pdf (source-range-23d24eb1-00335))_
- What's most important for you to remember is the tight relationship between package names and your directory structure (not just within a project, but within the entire workspace). _(coding_little_go_book.pdf (source-range-23d24eb1-00333))_
- Ultimately, how you structure your code around Go's workspace is something that you'll only feel comfortable with after you've written a couple of non-trivial projects. _(coding_little_go_book.pdf (source-range-23d24eb1-00333))_
- There are a few things we haven't looked at, such as constants and global variables but rest assured, their visibility is determined by the same naming rule. _(coding_little_go_book.pdf (source-range-23d24eb1-00334))_

## Technical atoms

### Technical frame 1: Chapter 4 - Code Organization and Interfaces / Interfaces

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00323))_

> Yet by programming against the interface, rather than these concrete implementations, we can easily change (and test) which we use without any impact to our code.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00322))_

```
type SqlLogger struct { ... }
type ConsoleLogger struct { ... }
type FileLogger struct { ... }
```
