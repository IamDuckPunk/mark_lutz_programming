import os

print('setenv...', end=' ')
print(os.environ['USER'])

os.environ['USER'] = 'Eugene'
os.system('python echoenv.py')

os.environ['USER'] = 'notEugene'
os.system('python echoenv.py')

os.environ['USER'] = input('?')
print(os.popen('python echoenv.py').read())

