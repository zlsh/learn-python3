#-*- coding: utf-8 -*-

'a test module'

__author__ = 'luoshuhan'

import sys
#导入sys模块后，就有了变量sys指向该模块，利用sys这个变量，可以访问sys模块的所有功能

def hellolsh():
	args = sys.argv
	if len(args)==1:
		print('Hello,luoshuhan!')
	elif len(args)==2:
		print('Hello, %s' % args[1])
	else:
		print('Too many arguments!')
if __name__ =='__main__':
	hellolsh()