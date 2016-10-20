'''
Created on 1-Apr-2015

@author: Asawari.Vaidya
'''


from http.server import HTTPServer, CGIHTTPRequestHandler


HOST = '127.0.0.1'
port = 3000

httpd = HTTPServer((HOST, port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))

CGIHTTPRequestHandler.cgi_directories = ['/']

httpd.serve_forever()	
