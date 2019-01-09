#! /usr/bin/env python3

import re

'''
name = input("Enter file:")
try:
	handle = open(name)
except:
	print('File Name not valid')	
	quit()
	
re_sum = 0
for line in handle:
	line = line.rstrip()
	lst = re.findall('[0-9]+', line)
	if len(lst) > 0:
		for value in lst:
			re_sum = re_sum + int(value)
print(re_sum)

'''

data = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
url = re.findall('href="(.+)"', data)
print(url)



#Z:\learning\python\coursera\regex_sum_27486.txt	