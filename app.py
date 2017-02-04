import SimpleHTTPServer
import SocketServer
import os

os.chdir(os.environ['OPENSHIFT_REPO_DIR'])

PORT = 8080

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()