#!/usr/bin/python3

"""task_03_http_server:
Create a simple http server using python
"""
import http.server
import json


class SimpleServer(http.server.BaseHTTPRequestHandler):
    """Simple server, inherits from BaseHTTPRequestHandler
    Implements a simple http server that responds to GET requests

    Covers the "/", "/data" and "/info" entry points,
    every other path will return a 404 response
    """

    data = {"name": "John", "age": 30, "city": "New York"}
    desc = {"version": "1.0", "description": "A simple API using http.server"}

    def do_GET(self):
        path = self.path

        if path == "/":
            self.send_response(200, "Hello")
            self.end_headers()
            self.wfile.write(bytes("Hello, this is a simple API!\n", "utf-8"))
        elif path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(self.data).encode("utf-8") + b"\n")
        elif path == "/status":
            self.send_response(200)
            self.end_headers()
        else:
            self.send_response(404, "Endpoint not found")
            self.end_headers()


def run(PORT=8000):
    server_address = ("", PORT)
    httpd = http.server.HTTPServer(server_address, SimpleServer)
    print(f"serving at port: {PORT}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
