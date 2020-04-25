#!/usr/bin/python3
import my_pkg

what = input("Select menu : 1)conversion 2)union/intersection 3)exit?")
while True:
	if what=='1':
		binnum =int(input("input binary number : "))
		
		d = my_pkg.bin_to_others.bin_dec(binnum)
		o = my_pkg.bin_to_others.bin_oct(d)
		x = my_pkg.bin_to_others.bin_hex(d)
		print("OCT > "+o)
		print("DEC > "+d)
		print("HEX > "+x)

	elif what=='2':
		list1 = input("1st list: ")
		list2 = input("2nd list: ")
		set1 = set()
		set2 = set()
		
		for i in range(0, len(list1)):
			if list1[i].isnumeric()==True:
				set1.add(int(list1[i]))

		for i in range(0, len(list2)):
			if list2[i].isnumeric()==True:
				set2.add(int(list2[i]))
		
		list1 = my_pkg.list_set.union(set1, set2)
		list2 = my_pkg.list_set.intersection(set1, set2)

		list1=list(list1)
		list2 = list(list2)

		for i in range(0, len(list1)):
			list1[i] = int(list1[i])

		for i in range(0, len(list2)):
			list2[i] = int(list2[i])
		sorted(list1)
		sorted(list2)

		print("=> union ", end="")
		print(list1)
		print("=> intersection ", end='')
		print(list2)

	elif what=='3':
		print("exit the program...")
		break
	
	what = input("Select menu : 1)conversion 2)union/intersection 3)exit?")

