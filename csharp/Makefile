.stat:
	ls -1 * | grep ".cs" | wc -l > .stat
	( find ./ -name '*.cs' -print0 | xargs -0 cat ) | wc -l >> .stat
