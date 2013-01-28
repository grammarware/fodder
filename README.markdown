Fodder
======

Fodder for feeding grammarware: a multi-license open source project collecting source code files that can be used for testing grammar-based tools (parsers, compilers, interpreters, mappers, type checkers, validators, etc).

Repositories used:
* [mono](https://github.com/mono/mono)
* [SignalR](http://github.com/SignalR/SignalR)
* [Nancy](https://github.com/NancyFx/Nancy)
* [ServiceStack](https://github.com/ServiceStack/ServiceStack)
* [kernel](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux.git;a=summary)

The information is collected by git-pulling entire repositories and sorting the files afterwards, so mining their history is also enabled (with `--follow`), if one desires it. No distinction is made between various dialects/versions of each language. No documentation and build information is preserved. If you want something to work on well-defined systems, it is a good idea to search elsewhere. If you need to quickly check whether your tool that claims to work on language X, breaks if faced with thousands of files in language X, be my guest.

The structure of the repo is language/project/files - when a project is connected, its structure gets flattened with the path info preserved but all slashes, backslashes and other funny symbols replaced by underscores for the sake of easy processing afterwards. Each project dir has a README file explaining its source and licensing. For detailed license info, look for LICENSE files in each directory.

Statistics so far (counted brutally by `ls`, `cat` and `wc -l`:
* C: 55077 files, 15425647 LOC
* C#: 28792 files, 4712395 LOC
