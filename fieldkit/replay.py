"""Replay one recorded transmission into the participant's receiving API."""

import argparse
import json
from pathlib import Path
from urllib.request import Request, urlopen

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("signal", choices=["morse", "bottles"])
args = p.parse_args()
station = Path(".coast-url").read_text().strip()
receiver = Path(".receiver-url").read_text().strip()
with urlopen(f"{station}/{args.signal}", timeout=5) as response:
    if args.signal == "morse":
        payload = {"message": response.read().decode().strip()}
        path = "decode-morse"
    else:
        payload = json.load(response)
        path = "collect-bottles"
request = Request(
    f"{receiver}/{path}",
    data=json.dumps(payload).encode(),
    headers={"Content-Type": "application/json"},
)
with urlopen(request, timeout=5) as response:
    print(response.read().decode().strip())
