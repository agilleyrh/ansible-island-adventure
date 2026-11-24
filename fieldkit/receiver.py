"""Acknowledge a correctly assembled station report on the seat's loopback address."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

data = Path(__file__).resolve().parent / "data"
chart = json.loads((data / "chart.json").read_text())
alphabet = json.loads((data / "morse.json").read_text())
letters = {code: letter for letter, code in alphabet.items()}
bottles = sorted(chart["bottles"], key=lambda b: (b["coordinates"]["y"], b["coordinates"]["x"]))
signals = {
    "/ack/morse": "".join(letters[code] for code in chart["morse"].split()),
    "/ack/bottles": "".join(bottle["character"] for bottle in bottles),
}


class Receiver(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path not in signals:
            self.send_error(404)
            return
        size = self.headers.get("Content-Length", "")
        if not size.isdecimal() or not 0 < int(size) <= 4096:
            self.send_error(400, "Send a small JSON message")
            return
        try:
            payload = json.loads(self.rfile.read(int(size)))
        except (UnicodeError, ValueError):
            self.send_error(400, "Invalid JSON")
            return
        if not isinstance(payload, dict) or payload.get("message") != signals[self.path]:
            self.send_error(422, "Check the translation or coordinate order")
            return
        body = json.dumps({"received": payload["message"]}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    with HTTPServer(("127.0.0.1", 0), Receiver) as server:
        url_file = Path(__file__).resolve().parents[1] / ".receiver-url"
        url = f"http://127.0.0.1:{server.server_port}"
        url_file.write_text(url + "\n")
        print(url, flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            if url_file.exists() and url_file.read_text().strip() == url:
                url_file.unlink()
