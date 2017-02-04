#!/usr/bin/python
import os
import SimpleHTTPServer
import SocketServer

STATIC_URL_PREFIX = '/static/'
STATIC_FILE_DIR = 'Pokhi/Pokhi/'
MIME_TABLE = {'.txt': 'text/plain',
              '.html': 'text/html',
              '.css': 'text/css',
              '.js': 'application/javascript',
             }    	



try:
    virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
    virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
    execfile(virtualenv, dict(__file__=virtualenv))
except Exception:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#



def content_type(path):
    """Return a guess at the mime type for this path
    based on the file extension"""
    
    name, ext = os.path.splitext(path)
    
    if ext in MIME_TABLE:
        return MIME_TABLE[ext]
    else:
        return "application/octet-stream"

def static_app(start_response , path):
    """Serve static files from the directory named
    in STATIC_FILES""" 
    
    h = open(path, 'rb')
    content = h.read()
    h.close()
    headers = [('content-type', content_type(path))]
    start_response('200 OK', headers)
    return [content]
 

def application(environ, start_response):

    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "Pokhi/Pokhi/Views/Index.html"
    abs_file_path = os.path.join(script_dir, rel_path)
    ctype = 'text/plain'

    path = os.path.normpath(environ['PATH_INFO'])
    # we want to remove '/static' from the start
    path = path.replace(STATIC_URL_PREFIX, '')

    abs_req = os.path.abspath(os.path.join(script_dir , STATIC_FILE_DIR , environ['PATH_INFO'].replace(STATIC_URL_PREFIX,'')))

    print(os.path.exists(abs_req))
    if environ['PATH_INFO'] == '/health':
        response_body = "1"
    elif environ['PATH_INFO'] == '/env':
        response_body = ['%s: %s' % (key, value)
                    for key, value in sorted(environ.items())]
        response_body = '\n'.join(response_body)
    elif environ['PATH_INFO'].startswith(STATIC_URL_PREFIX) and os.path.exists(abs_req):
        return static_app(start_response , abs_req)
    else:
        ctype = 'text/html'
        response_body = open(abs_file_path).read()

    status = '200 OK'
    response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]
    #
    start_response(status, response_headers)
    return [response_body]

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
