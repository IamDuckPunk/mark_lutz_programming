
"""
import sys

class Output:
    def __init__(self):
        self.text=''

    def write(self, string):
        self.text += string

    def writelines(self, lines):
        for line in lines: self.write(line)


class Input:
    def __init__(self, input=''):
        self.text = input
    
    def read(self, size=None): 
        if size == None:
            res, self.text = self.text, ''
        else: 
            res, self.text = self.text[:size], self.text[size:]
        return res

    def readline(self):
        eoln = self.text.find('\n')
        if eoln == 1:
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:eoln+1], self.text[eoln+1:]
        return res

def redirect(function, pargs, kargs, input):
    savestreams = sys.stdin, sys.stdout
    sys.stdin = Input(input)
    sys.stdout = Output()
    
    try:
        result = function(*pargs, **kargs)
        output = sys.stdout.text
    finally:
        sys.stdin, sys.stdout = savestreams
    return (result, output) 
"""




import sys                                      # get built-in modules

class Output:                                   # simulated output file
    def __init__(self):
        self.text = ''                          # empty string when created
    def write(self, string):                    # add a string of bytes
        self.text += string
    def writelines(self, lines):                # add each line in a list
        for line in lines: self.write(line)

class Input:                                    # simulated input file
    def __init__(self, input=''):               # default argument
        self.text = input                       # save string when created
    def read(self, size=None):                  # optional argument
        if size == None:                        # read N bytes, or all
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:size], self.text[size:]
        return res
    def readline(self):
        eoln = self.text.find('\n')             # find offset of next eoln
        if eoln == -1:                          # slice off through eoln
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:eoln+1], self.text[eoln+1:]
        return res

def redirect(function, pargs, kargs, input):    # redirect stdin/out
    savestreams = sys.stdin, sys.stdout         # run a function object
    sys.stdin   = Input(input)                  # return stdout text
    sys.stdout  = Output()
    try:
        result = function(*pargs, **kargs)      # run function with args
        output = sys.stdout.text
    finally:
        sys.stdin, sys.stdout = savestreams     # restore if exc or not
    return (result, output)          
