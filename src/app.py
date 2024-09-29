from http.server import BaseHTTPRequestHandler, HTTPServer


class Orders(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"[]")


if __name__ == "__main__":
    HTTPServer(("", 8080), Orders).serve_forever()
