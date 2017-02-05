#!/usr/bin/python
import os
import SimpleHTTPServer
import SocketServer

from flaskapp import app as application

virtenv = os.environ['APPDIR'] + '/venv/'
os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python2.7/site-packages')
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
#
# Below for testing only
#
if __name__ == '__main__':
    #PORT = 8025
    #Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    #httpd = SocketServer.TCPServer(("", PORT), Handler)
    #print("serving at port", PORT)

    #httpd.serve_forever()
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    httpd.serve_forever()
