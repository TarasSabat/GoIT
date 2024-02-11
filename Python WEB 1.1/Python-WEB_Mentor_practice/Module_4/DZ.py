import http
import json
import mimetypes
import urllib
from datetime import datetime
import pathlib
import socket
from email import mime
from http.server import BaseHTTPRequestHandler, HTTPServer

BASE_DIR = pathlib.Path()
CODE_REDIR: int = 302
C0DE_OK: int = 200
CODE_ERR: int = 404
SERVER_P0RT_1 = 3000
SERVER_IP = "127.0.0.1"
SERVER_HOST = "0.0.0.0"
SERVER_P0RT_2 = 5000
BUFFER_SIZE = 1024


def send_data_to_socket(body):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK.DGRAM)
    client_socket.sendto(body, (SERVER_IP, SERVER_P0RT_2))
    client_socket.close()


class HTTPHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        body = self.rfile.read(int(self.headers["Content-Length"]))
        send_data_to_socket(body)
        self.send_response(CODE_REDIR)
        self.send_header("Location", "/message")
        self.end_headers()

    def do_GET(self):
        route = urllib.parse.urlparse(self.path)
        match route.path:
            case "/":
                self.send_html("Index. html")
            case "/message":
                self.send_html("message.html")
            case _:
                file = BASE_DIR / route.path[1:]
                if file.exists():
                    self.send.stotic(file)
                else:
                    self.send_html("error.html", CODE_ERR)

    def send_html(self, filename, status_code=CODE_OK):
        self.send_response(status_code)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open(filename, "rb") as f:
            self.wfile.write(f.read())

    def send_static(self, filename):
        self.send_response(CODE_OK)
        mime_type, *rest = mimetypes.guess_type(filename)
        if mime_type:
            self.send_header("Content-type", mime_type)
        else:
            self.send_header("Content-type", "text/plain")
        self.end_headers()
        with open(filename, "rb") as f:
            self.wfile.write(f.read())


def run(server=HTTPServer, handler=HTTPHandler):
    address = (SERVER_HOST, SERVER_P0RT_1)
    http.server = server(address, handler)
    try:
        http.server.serve_forever()
    except KeyboardInterrupt:
        http.server.server_close()

def save_data(data):
    body = urllib.parse.unquote_plus(data.decode())
    try:
        payload = {key: value for key, value in [el.split('=') for el in body.split('&')]}
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        json_record = {
            current_time: {
                "usernaroe": payload.get('username', ''),
                "message": payload.get('message', ' ')
            }
        }

        file_path = BASE_DIR.joinpath('storage/data.json')
        if file_path.exists():
            with open(file_path,   'r+', encoding='utf-8')  as  source_file:
                source_data = json.load(source_file)
            else:
                source_data  =  {}