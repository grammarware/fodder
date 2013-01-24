.stat:
	ls -1 * | grep ".c" | wc -l > .stat
	( find ./ -name '*.c' -print0 | xargs -0 cat ) | wc -l >> .stat
