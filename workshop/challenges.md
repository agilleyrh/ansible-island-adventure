# Island Adventure review challenges

Run commands from `~/island-review`. Submit each answer on the review board.

## 1 | 10 | Warm-up | - | Write your name in the sand

The rescue crew needs to recognize you on the scoreboard. Open **Settings** from the game menu. Choose a display name or nickname, save it and confirm that it appears in your profile. You may keep your assigned workshop email. Submit `done`.

## 17 | 10 | Warm-up | - | Unlock the island

Your facilitator has the expedition word. Enter it to open the beach. See **Field guide** in the game menu for the seat setup and repository instructions.

## 23 | 10 | Warm-up | - | Read the module manual

Open the installed module help with `ansible-doc ansible.builtin.uri`. Find the Boolean option that makes the HTTP response body available to later tasks even for a successful request. Submit the option name.

## 24 | 10 | Warm-up | - | Equip the container crew

From `~/island-review`, install the bundled collection alongside the playbooks. Run `ansible-galaxy collection install --offline -p fieldkit/playbooks/collections fieldkit/vendor/containers-podman-1.16.3.tar.gz`, then `ansible-galaxy collection list -p fieldkit/playbooks/collections containers.podman`. Submit the installed version number. The warning about the default search path is expected because these playbooks use their adjacent `collections` directory.

## 3 | 10 | At the beach | 17 | Check in from the beach

Run `ansible-navigator --version`. Then run `(cd ~/lab_inventory && ansible all -i hosts -m ansible.builtin.ping -o)`. Confirm all three hosts returned the same ping value. Submit that value, a slash and the numeric Navigator version.

## 4 | 10 | At the beach | 17 | Query the controller from a playbook

Run `ansible-playbook fieldkit/playbooks/controller-version.yml` from VS Code. At the prompt paste the HTTPS base URL from your assigned AAP tab. Inspect the `uri` task and the field selected from its registered JSON. Submit the controller version it returns.

## 25 | 10 | At the beach | 3 | Hello, world!

Run `ansible-navigator run fieldkit/playbooks/hello-world.yml -m stdout --ee false` from your review clone. Submit the single word at the end of the greeting.

## 26 | 20 | At the beach | 25 | Message in a bottle

You found a sealed bottle. Use `ansible-vault view` to read `fieldkit/data/message-in-a-bottle.txt` with the training password in `fieldkit/training/bottle-key.txt`. Keep the original file encrypted. Submit the sentence inside.

## 31 | 10 | At the beach | 25 | Find the lint violation

Use the seat's installed linter. Run `ansible-lint --offline fieldkit/playbooks/test-lint.yml`. Look for the rule concerning a fully qualified collection name. Submit the recommended module name in the `ansible.builtin` namespace.

## 32 | 30 | At the beach | 31 | Clean the ship's log

In VS Code, repair the module name in your own copy of `fieldkit/playbooks/test-lint.yml`. Run the same lint command again and confirm that it exits successfully. Run the corrected playbook with Navigator in stdout mode and with `--ee false`. Submit the sentence printed by the corrected task.

## 33 | 20 | At the beach | 25 | Filter the water

Run `fieldkit/playbooks/filter-water.yml` with Navigator in stdout mode and with `--ee false`. In the debug task, apply Ansible's Base64 decoding filter to the sample, then run the playbook again. Submit the decoded message, including its punctuation.

## 34 | 30 | At the beach | 26 | Open the shore chest

Read the treasure role and deploy its encrypted page to node01. From your clone run `fieldkit/run-managed treasure-site.yml --vault-password-file ~/island-review/fieldkit/training/treasure-key.txt`. The role reads the installed page over HTTP. Submit its text.

## 35 | 10 | At the beach | 3,24 | Inspect the execution image

Run `ansible-playbook fieldkit/playbooks/image.yml` in the VS Code terminal. Inspect `fieldkit/playbooks/tasks/supported-image.yml` to see how `podman_image_info` selects the supported execution environment. Submit the last component of the image repository, omitting its tag.

## 36 | 10 | At the beach | 3 | Find the oasis

Use `ansible-inventory -i "$HOME/lab_inventory/hosts" --graph` in VS Code. Identify the host in the `db` group. Submit its inventory name, including any leading zero in the number.

## 37 | 20 | At the beach | 25 | Sort the fruit

Open `fieldkit/playbooks/check-diff.yml`. Change the debug expression to show labels present in exactly one of the two baskets. Sort the result numerically and run the playbook. Submit the numbers in ascending order, separated by commas.

## 28 | 20 | Controller treasure hunt | 4,25 | Light the controller beacon

Use **Field guide → Controller project** to create and sync your seat's Git project. Under **Automation Execution → Templates**, create a job template in the **Workshop** organization. Use your project, **Workshop Inventory** and `fieldkit/playbooks/treasure.yml`. The playbook runs on the controller execution environment's localhost. Launch it and submit the initials printed by the beacon.

## 29 | 20 | Controller treasure hunt | 28 | Read the sealed dispatch

Under **Automation Execution → Infrastructure → Credentials**, create a **Vault** credential in **Workshop** named `Island Vault`. Its training Vault password is `AAP`. Create another job template with your project, **Workshop Inventory**, `fieldkit/playbooks/secret.yml` and the new Vault credential. Launch the template and submit the sentence from the debug task.

## 30 | 30 | Controller treasure hunt | 29 | Raise the treasure chest

Create a controller job template for `fieldkit/treasure-site.yml` with **Workshop Inventory**, **Workshop Credential** and your training Vault credential. Enable **Privilege Escalation**, leave **Variables** empty and launch it. Inspect the task that reads the deployed page from node01 over HTTP. Submit the page text.

## 101 | 10 | Coastal field station | 25 | Open the coastal station

Run `fieldkit/run-managed station.yml --limit node01`. Follow the role from package installation to the final HTTP read-back. Confirm the URL on node01 is serving the new station and submit its greeting.

## 5 | 15 | Coastal field station | 101 | The French connection

Inspect `fieldkit/data/station.json`. Edit the station role’s `templates/bonjour.txt.j2` to decode the supplied French greeting with a Jinja filter. Deploy again with `fieldkit/run-managed station.yml --limit node01`. Run `fieldkit/run-managed playbooks/greetings.yml --limit node01 -e message_name=bonjour` and submit the text from the live page.

## 6 | 30 | Coastal field station | 101 | Morse coding

Start the supplied radio receiver in a second terminal with `cd ~/island-review && python3 fieldkit/receiver.py`. Leave it running for both signal exercises. In `fieldkit/playbooks/signals.yml`, edit **Assemble the Morse message**. Split the recorded signal into codes, look up each code in the supplied `letters` dictionary, and join the results. Run `ansible-playbook fieldkit/playbooks/signals.yml --tags morse -e signal=morse`. The play fetches the live station report and POSTs your translation. Submit the acknowledged word. Hint: Ansible’s `extract` filter can look up a list of keys.

## 7 | 30 | Coastal field station | 101 | Bottles on the grid

In `fieldkit/playbooks/signals.yml`, edit **Read the bottles in chart order**. Sort rows by increasing `coordinates.y` and columns by increasing `coordinates.x`, then join their characters. With your radio receiver running, execute `ansible-playbook fieldkit/playbooks/signals.yml --tags bottles -e signal=bottles`. Submit the island name acknowledged by the receiver. Hint: Jinja sorts are stable, so sort the secondary key first. Stop the receiver when both signals are acknowledged.

## 8 | 10 | Coastal field station | 101 | Publish the runtime label

In `fieldkit/playbooks/shore-assets.yml`, adjust the runtime expression to select the `native-java` Template and read `annotations.runtime`. Deploy with `fieldkit/run-managed playbooks/shore-assets.yml --tags runtime`. Submit the value retrieved from the published HTTP label.

## 10 | 20 | Coastal field station | 35 | Monkey business

Three rootless HTTP beacons should be running in VS Code. Run `ansible-playbook fieldkit/playbooks/replicas.yml --tags drill` once to create the rehearsal fault. In the same playbook, set `beacon_state` to the state that starts a stopped container. Run `ansible-playbook fieldkit/playbooks/replicas.yml --tags repair`. Identify the down replica from the inspection **before** repair. Check all three HTTP probes and repeat the repair to confirm `changed=0`. Submit the name of the replica you recovered.

## 11 | 20 | Coastal field station | 5 | Aloha!

Personalize the station role’s `templates/aloha.txt.j2` so the page contains `inventory_hostname`, an equals sign and the supplied `island_greeting`. Run `fieldkit/run-managed station.yml` on both web hosts, then `fieldkit/run-managed playbooks/greetings.yml -e message_name=aloha`. Submit both HTTP responses in inventory-name order, separated by a comma.

## 12 | 15 | Coastal field station | 101 | Treasure map

The map in the archived ConfigMap is encoded. Edit **Extract the treasure map** in `fieldkit/playbooks/shore-assets.yml` to decode its data using Ansible. Run `fieldkit/run-managed playbooks/shore-assets.yml --tags map`. Submit the text retrieved from the deployed map.

## 15 | 30 | Crew muster | 36 | Muster the crew

Read `fieldkit/playbooks/muster.yml` and its template `fieldkit/templates/muster.txt.j2`. The starter template only visits the web group. Change the loop to visit both `web` and `db`, take unique names and sort them. Run `fieldkit/run-managed playbooks/muster.yml`. The play gathers live OS facts and renders the manifest on node03. Inspect it with `(cd ~/lab_inventory && ansible db -i hosts -m ansible.builtin.command -a 'cat /var/tmp/island-review/muster.txt')`. Submit the hostnames in file order, comma-separated.

## 16 | 20 | Crew muster | 15 | Verify the ship's manifest

Edit **Decode the report** in `fieldkit/playbooks/verify-muster.yml` to decode the remote file returned by `slurp`. Run `fieldkit/run-managed playbooks/verify-muster.yml`. The assertion checks the complete inventory order before printing a fingerprint. Submit the 12-character SHA-256 prefix after the slash. Preserve the template’s final newline.

## 18 | 25 | Coastal field station | 35 | Persistence pays off

Edit `reader_mount` in `fieldkit/playbooks/locker.yml`. Mount the same named volume used by the writer at the reader’s `/locker` path and keep its SELinux `:Z` suffix. Run `ansible-playbook fieldkit/playbooks/locker.yml`. The writer is removed before the reader starts. Submit the key the reader recovers. The play cleans up the volume and both containers.

## 19 | 20 | Navigation and rollout | 101 | Mapster peers

Edit the debug expression in `fieldkit/playbooks/peers.yml`. Filter the registered survey records to peers whose `state` is `connected`, turn the result into a list and count it. Run `ansible-playbook fieldkit/playbooks/peers.yml`. Submit the integer.

## 20 | 15 | Navigation and rollout | 19 | Scrambled islands

Take a puzzle break. Open `fieldkit/data/chart.json`, find the four single-letter `tiles`, and rearrange them to name a vessel. Submit the word.

## 21 | 20 | Navigation and rollout | 11 | Roll out the green beacon

The launch crew needs one healthy web host during each update. In `fieldkit/playbooks/rollout.yml`, set the batch size so only one host changes at a time. Run `fieldkit/run-managed playbooks/rollout.yml`. Check that the first HTTP health check finishes before the second host updates. Repeat and confirm no changes. Submit both live release markers in inventory-name order, comma-separated.

## 22 | 40 | Navigation and rollout | 21 | Recover the rejected release

Open `fieldkit/playbooks/recover.yml`. A deliberately bad candidate is written to a dedicated practice page on node02. In the `rescue` block, restore the decoded bytes read from the known-good release. Run `fieldkit/run-managed playbooks/recover.yml`. Expect one rescued failure and a successful final health check. Submit the complete `restored/…` result.

## 100 | 10 | Crew muster | 36 | Check the RHEL fleet

Run `fieldkit/run-managed playbooks/muster.yml --tags facts`. Check that the distribution assertion passes on all three nodes. Submit the common `distribution/major-version` signature printed by the play.

## 38 | 35 | Rescue operations | 37 | Reconcile the relief manifest

The quartermaster needs a backorder list. Read the orders and delivery records in `fieldkit/data/relief.yml`. A delivery counts only after inspection releases it. Several shipments can contain the same cargo.

Edit `fieldkit/playbooks/relief.yml`. For each order, total the released crates of that cargo, subtract them from the order and suppress fully filled orders. Keep the remaining cargo names in alphabetical order. Run your playbook in the VS Code terminal. Submit the resulting `cargo=count` pairs, separated by commas. A pair looks like `lamps=2`.

## 39 | 40 | Rescue operations | 34 | Repair the beacon without drift

The radio accepts each channel once, in ascending numeric order. Edit `fieldkit/templates/beacon.conf.j2` so that the rendered `channels=` line meets that requirement. Preserve the station line and the final newline.

Preview the change on **node02**, apply it, then apply it again to check idempotence.

```bash
(
  cd ~/lab_inventory || exit
  playbook=~/island-review/fieldkit/playbooks/beacon-config.yml
  ansible-playbook -i hosts "$playbook" --check --diff &&
    ansible-playbook -i hosts "$playbook" &&
    ansible-playbook -i hosts "$playbook"
)
```

Confirm that the final play recap shows `changed=0` for node02. Submit the 12-character SHA-256 prefix printed by the task that reads the installed file.

## 40 | 30 | Rescue operations | 36 | Tune the lookout radios

Three radios inherit channel settings from different inventory levels. Inspect `fieldkit/radio/group_vars` and `fieldkit/radio/host_vars`. Predict the settings on **east**, **launch** and **west**.

Run `ansible-playbook -i fieldkit/radio/hosts.yml fieldkit/playbooks/radio.yml`. Run it again with `-e channel=9` and confirm the effect of an extra variable. Submit the original three channel numbers in the host order above, followed by a slash and the common override. Use the form `1,2,3/9`.

## 41 | 45 | Rescue operations | 28 | Pass the sailing orders

In your controller project, create two job templates that use **Workshop Inventory**. Use `fieldkit/playbooks/dispatch-plan.yml` for the planner and set the template variable `party_size: 5`. Use `fieldkit/playbooks/dispatch-sail.yml` for the launch. The planner publishes its selection with `set_stats`.

Create a **Workflow Job Template** in **Workshop**. In its visualizer, add the planner as the first node. Add the launch template as its successor with **On Success**. Save and run the workflow. Open the second job's output and submit its sailing ticket.

## 42 | 40 | Event-Driven Ansible | 25 | Catch the crossing window

Create the EDA project and tide activation using **Field guide → Event-Driven Ansible**. Choose `tide-watch.yml`, use the default decision environment and set the restart policy to **Never**. In the activation's variables, set the numeric lower bound to **3** and the numeric upper bound to **6** using the variable names in the rulebook.

Start the activation. The source sends nine samples and then finishes. In **Rule Audit**, open your activation's **Record a navigable tide** entries. Inspect the matching event's `i` field or the activation output. Which sample numbers passed the condition? Submit them in ascending order, separated by commas. A completed finite activation is the expected outcome.

## 43 | 50 | Event-Driven Ansible | 42,28 | Dispatch the harbor launch

Follow **Field guide → Send an authenticated storm report** to create your dispatch job, EDA launch credential, token-protected event stream and mapped activation. Send the three recorded reports with the supplied Ansible playbook. In Rule Audit, find the one matching event. Check the controller job’s event variables and successful output. From VS Code, read the independent receipt with `(cd ~/lab_inventory && ansible node03 -i hosts -m ansible.builtin.command -a 'cat /var/tmp/island-review/dispatch.txt')`. Submit the receipt and disable your activation.
