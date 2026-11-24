"""Serve a personal copy of the island's recorded signals on loopback."""

import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

DATA = Path(__file__).parent / "data"


class Coast(BaseHTTPRequestHandler):
    def do_GET(self):
        station = json.loads((DATA / "station.json").read_text())
        chart = json.loads((DATA / "chart.json").read_text())
        routes = {
            "/": station["greeting"],
            "/bonjour": station["french"],
            "/morse": chart["morse"],
            "/bottles": chart["bottles"],
            "/peers": chart["peers"],
            "/maps": chart["islands"],
        }
        for index, letter in enumerate(chart["tiles"], start=1):
            routes[f"/island/{index}"] = letter
        for alias, greeting in station["aliases"].items():
            routes[alias] = greeting
        if self.path not in routes:
            self.send_error(404)
            return
        item = routes[self.path]
        is_text = isinstance(item, str)
        body = ((item if is_text else json.dumps(item)) + "\n").encode()
        self.send_response(200)
        self.send_header(
            "Content-Type",
            "text/plain; charset=utf-8" if is_text else "application/json",
        )
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=0)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Coast)
    url = f"http://127.0.0.1:{server.server_port}"
    Path(".coast-url").write_text(url + "\n")
    print(url, flush=True)
    server.serve_forever()
