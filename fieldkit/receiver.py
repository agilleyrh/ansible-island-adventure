"""Receive local POST requests and load the participant's decoder on each request."""

import importlib
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

import decoders


class Receiver(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path not in ("/decode-morse", "/collect-bottles"):
            self.send_error(404)
            return
        size = self.headers.get("Content-Length", "")
        if not size.isdecimal() or not 0 < int(size) <= 65536:
            self.send_error(400, "Expected a small JSON report")
            return
        try:
            item = json.loads(self.rfile.read(int(size)))
            decoder = importlib.reload(decoders)
            if self.path == "/decode-morse":
                table = Path(__file__).parent / "data/morse.json"
                result = decoder.decode_morse(
                    item["message"], json.loads(table.read_text())
                )
            else:
                result = decoder.collect_bottles(item)
            body = (result + "\n").encode()
        except (ValueError, TypeError, KeyError, AttributeError, SyntaxError) as error:
            self.send_error(400, type(error).__name__)
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 0), Receiver)
    url = f"http://127.0.0.1:{server.server_port}"
    Path(".receiver-url").write_text(url + "\n")
    print(url, flush=True)
    server.serve_forever()
