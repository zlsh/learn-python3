#！/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['value1','value2','value3']
ret = 20;
print('please enter your number')
ret = input()

if int(ret) >= 20:
	classmates.append('value4')
	print(classmates) 

	classmates.insert(1,'luoshuhan')
	print(classmates) 

	classmates.pop()
	print(classmates) 

	classmates.pop(1)
	print(classmates) 
else:	
	tuples = ('a','b',['A','B'])
	tuples[2][0] = 'my'
	tuples[2][1] = 'tuple'
	print(tuples)

sum = 0  
for x in range(101):
	sum = sum + x
print(sum)

n1 = 255
n2 = 1000
print(str(hex(n1)))
print(str(hex(n2)))