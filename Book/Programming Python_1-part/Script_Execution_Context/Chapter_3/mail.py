#!/usr/bin/python

import os, glob

for pyfile in glob.glob('*.py'):
    print(pyfile)
    os.system('mail evgeniy.belyaev.96@mail.ru -s %s < %s' % (pyfile, pyfile))

