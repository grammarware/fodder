#!/usr/bin/python

f = open('files.lst','r')
sh = open('cleanup.sh','w')
sh.write("#!/bin/sh\n\n")
cx = 0
for line in map(lambda x:x.strip(),f.readlines()):
	cx += 1
	ffr = line.replace(' ','\ ').replace('`','\`')
	fft = line.replace('./','').replace('/','_').replace('.','_').replace(' ','_').replace('`','_')
	if fft.endswith('_h'):
		fft = fft[:-2]+'.h'
	else:
		print 'Unexpected extension in',fft
	sh.write('git mv '+ffr+' c/kernel/'+fft+'\n')
	if cx % 100 == 0:
		sh.write('echo %i files moved.\n' % cx)
f.close()
sh.close()

