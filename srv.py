# Required for session token lifetime generation
import datetime

# Required to set up a simple HTTP server
from http.server import HTTPServer, BaseHTTPRequestHandler

# Required to check if HTTP-requested files exist
import os

# Required to create randomised session tokens
import random

# Required to print to standard error output
import sys

# Required to output detailed Python error messages
import traceback

# The server request handler.
from http.server import BaseHTTPRequestHandler, HTTPServer

import time

import mimetypes

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/web/index.html'
        try:
            split_path = os.path.splitext(self.path)
            request_extension = split_path[1]
            if request_extension != ".py":
                print(request_extension)
                if request_extension == ".html":
                    f = open((self.path[1:])).read()
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(bytes(f, 'utf-8'))
                elif request_extension == ".css":
                    self.httpsrv(self.path, "text/css")
                elif request_extension == ".png":
                    self.httpsrv(self.path, "image/png")
                elif request_extension == ".svg":
                    self.httpsrv(self.path, "image/svg+xml")
                elif request_extension == ".php":
                    self.httpsrv(self.path, "text/php")
                
                
            else:
                f = "File not found"
                self.send_error(404,f)
        except:
            f = "File not found"
            self.send_error(404,f)
    def httpsrv(self, srvfpath, mimetype, statcode=200):
        self.send_response(statcode)
        self.send_header("Content-type", mimetype)
        self.end_headers()
        print(f"/web{srvfpath}")
        with open(f"./web{srvfpath}", "rb") as f:
            self.wfile.write(f.read())
    def httperr(self, errno):
        str_errno = str(errno)
        self.httpsrv(f"/err/{str_errno}.html", "text/html", statcode=errno)
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")