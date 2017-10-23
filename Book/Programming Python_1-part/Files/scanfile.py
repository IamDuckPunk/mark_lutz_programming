"""
def scanner(name, function):
    file = open(name, 'r')
    while True:
        line = file.readline()
        if not line: break
        function(line)
    file.close()
"""


def scanner(name, function):
    for line in open(name, 'r'):
        function(line)

"""     
def scanner(name, function):
    list(map(function, open(name, 'r')))

def scanner(name, function):
    [function(line) for line in open(name, 'r')]


def scanner(name, function):
    list(function(line) for line in open(name, 'r'))
"""
