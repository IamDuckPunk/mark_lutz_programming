#!/usr/bin/python3

import cgi, cgitb
#cgitb.enable()

form = cgi.FieldStorage()
print('Content-type: text/html\n')
print('<title> Reply page</title>')
if not 'user' in form:
    print('<h1> what are you?<h1>')
else:
    print('<h1> Hello <i> %s</i>!</h1>' % cgi.escape(form['user'].value))
