import json
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler


html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>Hello world</h1>
</body>
</html>
"""


class OurHttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        file = "index.html"
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        with open(file, "rb") as f:
            self.wfile.write(f.read())

    def do_POST(self):
        data = self.wfile.read(int(self.headers['Content-Length']))
        parsed = urllib.parse.unquote(data.decode('utf-8'))
        for elem in parsed.split('/n'):
            print(elem)

        # with open('data.json', 'w', encoding='utf-8') as f:
        #     json.dump(data, f, ensure_ascii=False)
        self.send_response(201)
        # self.send_header('Location', '/contact.html')
        self.end_headers()


def run(server_class=HTTPServer, our_handler=OurHttpHandler):
    server_address = ("", 8000)
    http = server_class(server_address, our_handler)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == "__main__":
    run(server_class=HTTPServer)
