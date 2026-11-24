# Island field kit

Open your Showroom VS Code terminal and follow the [field guide](../workshop/field-guide.md#get-the-field-kit) to clone the repository. Run the commands below from `~/ansible-island-adventure`.

## Coastal field station

Start the station in a dedicated terminal. It prints its loopback URL when it is ready and reads your edited station data on each request.

```bash
cd ~/ansible-island-adventure
python3 fieldkit/coast.py
```

Leave that terminal running. In your working terminal, read the assigned address from the clone and request the greeting.

```bash
cd ~/ansible-island-adventure
COAST=$(cat .coast-url)
curl -fsS "$COAST/"
```

Use `$COAST` in that terminal for later chart requests. Stop the station with **Ctrl+C** in its own terminal when you finish.

### Receive a signal

The Morse and bottle challenges also use a receiver. Start it in another terminal and wait for it to print its loopback URL.

```bash
cd ~/ansible-island-adventure
python3 fieldkit/receiver.py
```

In your working terminal, implement the function named in the challenge in `fieldkit/decoders.py`. The receiver reloads it on each request. Run `python3 fieldkit/replay.py morse` or `python3 fieldkit/replay.py bottles` to send a recorded transmission. Stop the receiver with **Ctrl+C** in its own terminal when you finish.
