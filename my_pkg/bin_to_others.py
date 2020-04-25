#!/usr/bin/python3

def bin_oct(x):
	return format(int(x), 'o')

def bin_dec(x):
	pos = 0
	x=str(x)
	decnum=0
	for i in range(len(x)-1, -1, -1):
		if x[i]=='1':
			decnum+=1<<pos
		#	print(i, decnum, pos)
		pos+=1
	return str(decnum)

def bin_hex(x):
	return format(int(x), 'X')
