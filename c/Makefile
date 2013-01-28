.stat:
	ls -1 * > allfiles
	expr `grep -c ".c" allfiles` + `grep -c ".h" allfiles` > .stat
	( find ./ -name '*.h' -print0 | xargs -0 cat ) | wc -l >> .stat
	rm allfiles
