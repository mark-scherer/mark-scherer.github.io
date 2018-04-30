#! python

"""
dummy.py
Proof-of-concept for web-based python scripts.
Causes simple redirection to results.html
"""

import cgi
cgitb.enable()

form = cgi.FieldStorage()
username = form.getlist("username")

print('Content-Type: text/html')
print()  # HTTP says you have to have a blank line between headers and content
print('<html>')
print('  <head>')
print('    <meta http-equiv="refresh" content="0; URL=\'TC1/src/site/results.html\' />')
print('    <title>You are going to be redirected</title>')
print('  </head>')
print('  <body>')
print('    Redirecting... <a href="TC1/src/site/results.html">Click here if you are not redirected</a>')
print('  </body>')
print('</html>')
