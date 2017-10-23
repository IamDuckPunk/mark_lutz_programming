import os, sys


print('my os.getcwd =>', os.getcwd())
for line in sys.path[:3]:
    print('my sys.path =>', line)

#print('my os.getcwd() =>', sys.path[:6])
input('type to quit')
