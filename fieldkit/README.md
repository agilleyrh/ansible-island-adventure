# Island Adventure field kit

Run commands from the root of your workshop clone. The [field guide](../workshop/field-guide.md) covers setup, controller and EDA. The [challenge cards](../workshop/challenges.md) give each objective and the command to test it.

## Managed nodes

`fieldkit/run-managed` runs the named playbook from `~/lab_inventory` with the seat’s inventory and SSH settings. For example, `fieldkit/run-managed station.yml --limit node01` publishes the field station. Local container exercises use rootless Podman on the VS Code host.

## Radio receiver

For Morse and bottle reports, open a second terminal and leave this command running while you work.

```bash
cd ~/ansible-island-adventure
python3 fieldkit/receiver.py
```

The receiver prints its loopback address. The signal playbook reads that address from the clone. A correct POST returns the acknowledged message. HTTP 422 means the translation or coordinate order needs another look. Stop the receiver with Ctrl+C when both cards are complete.

## Offline collection

The kit includes the unmodified Galaxy release of `containers.podman` 1.16.3, licensed under GPL-3.0-or-later. Its COPYING file and source are inside the archive. SHA-256 is `2f48a06782619fa7eb9b76b2bfadd90fca7bad254dc2ee7ccf3ac8e870ae29d7`. [Upstream release](https://galaxy.ansible.com/ui/repo/published/containers/podman/)
