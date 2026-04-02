#! /usr/bin/python

# Exampe python script
# another comment
# CTRL +/

import sys

# argv is part of the sys module
# argument vector a.k.a the list of parameters or inputs to the program
# print

argc = len(sys.argv)
print(argc)

if argc > 3:
 #   print('Too many args')
    print('Please try again')

else:
    where = 'world'
    print("Hello", where)

print('Goodbye from ' + sys.argv[0])
print('Goodbye from' , sys.argv[0])
print('one','two','three', sep="!!!")




