# Island Adventure challenge catalog

Each heading gives the challenge ID, points, category, prerequisite IDs and title. Start each terminal exercise in `~/ansible-island-adventure`. The [field guide](field-guide.md) covers the initial setup.

## 1 | 10 | Warm-up | - | Write your name in the sand

The rescue crew needs to recognize you on the scoreboard. Open **Settings** from the game menu. Choose a display name or nickname, save it and confirm that it appears in your profile. You may keep your assigned workshop email. Submit `done`.

## 17 | 10 | Warm-up | - | Unlock the island

Your facilitator has the expedition word. Enter it to open the beach. See **Field guide** in the game menu for the seat setup and repository instructions.

## 23 | 10 | Warm-up | - | Ansible documentation

Find the Ansible community documentation home page in your browser. Submit its hostname, without a protocol or path.

## 24 | 10 | Warm-up | - | Ansible collections

Find Ansible Galaxy, the community catalog where you can discover collections by namespace. Submit its hostname, without a protocol or path.

## 3 | 10 | At the beach | 17 | Read the beach sign

Open your assigned Showroom seat, select **VS Code** and open a terminal. Run `ansible-navigator --version`. Submit the numeric version, including both dots.

## 4 | 10 | At the beach | 17 | Find the controller version

In Showroom, open **AAP** and sign in with the seat credentials in module 2.1. In the same browser, open `/api/controller/v2/ping/` on the AAP hostname. Read the top-level `version` field. Submit the numeric automation controller version.

## 25 | 10 | At the beach | 3 | Hello, world!

Use the clone you created in **Field guide → Get the field kit**. You can return to it with `cd ~/ansible-island-adventure`. From the repository root, run `ansible-navigator run fieldkit/playbooks/hello-world.yml -m stdout --ee false`. Submit the single word at the end of the greeting.

## 26 | 20 | At the beach | 25 | Message in a bottle

You found a sealed bottle. Use `ansible-vault view` to read `fieldkit/data/message-in-a-bottle.txt` with the training password in `fieldkit/training/bottle-key.txt`. Keep the original file encrypted. Submit the sentence inside.

## 31 | 10 | At the beach | 25 | Find the lint violation

Use the seat's installed linter. Run `ansible-lint --offline fieldkit/playbooks/test-lint.yml`. Look for the rule concerning a fully qualified collection name. Submit the recommended module name in the `ansible.builtin` namespace.

## 32 | 30 | At the beach | 31 | Clean the ship's log

In VS Code, repair the module name in your own copy of `fieldkit/playbooks/test-lint.yml`. Run the same lint command again and confirm that it exits successfully. Run the corrected playbook with Navigator in stdout mode and with `--ee false`. Submit the sentence printed by the corrected task.

## 33 | 20 | At the beach | 25 | Filter the water

Run `fieldkit/playbooks/filter-water.yml` with Navigator in stdout mode and with `--ee false`. In the debug task, apply Ansible's Base64 decoding filter to the sample, then run the playbook again. Submit the decoded message, including its punctuation.

## 34 | 30 | At the beach | 26 | Open the shore chest

Read the treasure role in `fieldkit/roles/treasure/tasks/main.yml`. Run the playbook from the lab inventory directory so Navigator picks up the seat’s SSH settings. The parentheses return you to your clone when the command finishes.

```bash
(
  cd ~/lab_inventory && ansible-navigator run ~/ansible-island-adventure/fieldkit/treasure-site.yml -m stdout --ee false \
    -i hosts --vault-password-file ~/ansible-island-adventure/fieldkit/training/treasure-key.txt
)
curl -fsS http://node01/island-workshop.txt
```

Submit the text served by the page. The final playbook task also prints it.

## 35 | 10 | At the beach | 3 | Read the mark on the ball

In the VS Code terminal, list local execution images with `podman images --format '{{.Repository}}:{{.Tag}}'`. Find the image that includes `ee-supported`. Submit the final repository component, without the registry path or tag.

## 36 | 10 | At the beach | 3 | Find the oasis

Use `ansible-inventory -i "$HOME/lab_inventory/hosts" --graph` in VS Code. Identify the host in the `db` group. Submit its inventory name, including any leading zero in the number.

## 37 | 20 | At the beach | 25 | Sort the fruit

Open `fieldkit/playbooks/check-diff.yml`. Change the debug expression to show labels present in exactly one of the two baskets. Sort the result numerically and run the playbook. Submit the numbers in ascending order, separated by commas.

## 28 | 20 | Controller treasure hunt | 4,25 | Light the controller beacon

Use **Field guide → Controller project** to create and sync your seat's Git project. Under **Automation Execution → Templates**, create a job template in the **Workshop** organization. Use your project, **Workshop Inventory** and `fieldkit/playbooks/treasure.yml`. The playbook runs on the controller execution environment's localhost. Launch it and submit the initials printed by the beacon.

## 29 | 20 | Controller treasure hunt | 28 | Read the sealed dispatch

Under **Automation Execution → Infrastructure → Credentials**, create a **Vault** credential in **Workshop** named `Island Vault`. Its training Vault password is `AAP`. Create another job template with your project, **Workshop Inventory**, `fieldkit/playbooks/secret.yml` and the new Vault credential. Launch the template and submit the sentence from the debug task.

## 30 | 30 | Controller treasure hunt | 29 | Raise the treasure chest

Create a job template for `fieldkit/treasure-site.yml`. Select **Workshop Inventory**, **Workshop Credential** (Machine) and your Vault credential. Enable **Privilege Escalation**. Leave **Variables** empty and launch the job. From VS Code, run `curl -fsS http://node01/island-workshop.txt`. Submit the page text printed by the HTTP check or by curl.

## 101 | 10 | Coastal field station | 25 | Start the hello service

Follow **Coastal field station** in `fieldkit/README.md` to start a personal HTTP service and set `COAST` in the current terminal. Request `curl -fsS "$COAST/"`. Submit the greeting, including the underscores.

## 5 | 15 | Coastal field station | 101 | The French connection

Open `fieldkit/data/station.json`. Decode `encoded_french` from Base64 and place the decoded text in the `french` field. Request `"$COAST/bonjour"` with curl and submit the response. The service reloads the file on each request.

## 6 | 30 | Coastal field station | 101 | Morse coding

At dusk, the lighthouse transmits a string of dots and dashes. Fetch `"$COAST/morse"` and inspect the letter-to-code dictionary in `fieldkit/data/morse.json`. Follow **Receive a signal** in `fieldkit/README.md` to start your personal receiving API.

Implement `decode_morse(message, alphabet)` in `fieldkit/decoders.py`. Spaces separate letters. Replay the transmission with `python3 fieldkit/replay.py morse`. It sends a JSON message to your `POST /decode-morse` endpoint. Submit the word your receiver returns.

## 7 | 30 | Coastal field station | 101 | Bottles on the grid

Request `"$COAST/bottles"`. Each record contains a character and integer coordinates. Start your receiving API as described under **Receive a signal** in `fieldkit/README.md`.

Implement `collect_bottles(bottles)` in `fieldkit/decoders.py`. Read rows in ascending `y` order and columns in ascending `x` order. Run `python3 fieldkit/replay.py bottles`. It posts the recorded list to `/collect-bottles`. Submit the island name returned by your service.

## 8 | 10 | Coastal field station | 25 | Native Java

The shore crew saved a small catalog in `fieldkit/data/shore.json`. Find the object whose kind is `Template` and whose name is `native-java`. Submit the Java runtime in its `annotations.runtime` field.

## 10 | 20 | Coastal field station | 25,35 | Monkey business

A chaos monkey has taken a beacon offline. Find the desired replica count for the `beacon` Deployment in `fieldkit/data/shore.json`. Use the supported execution image already on your seat. Start three HTTP replicas, then take the third one offline.

```bash
EE=$(podman images --format '{{.Repository}}:{{.Tag}}' | awk '/\/ee-supported/ {print; exit}')
for n in 1 2 3; do
  podman run -d --label island.beacon=workshop --name "island-beacon-$n" --entrypoint python3 "$EE" -m http.server 8080
done
podman stop island-beacon-3
podman ps --filter label=island.beacon=workshop --format '{{.Names}}'
podman exec island-beacon-1 python3 -c "from urllib.request import urlopen; print(urlopen('http://127.0.0.1:8080').status)"
```

Use the number of running containers and the manifest's desired count to calculate how many replacements are needed. Submit an integer. When finished, remove only these three exercise replicas with `podman rm -f island-beacon-1 island-beacon-2 island-beacon-3`.

## 11 | 20 | Coastal field station | 101 | Aloha!

Add an entry to the `aliases` object in `fieldkit/data/station.json`. Use `/aloha` as the path and copy the value of `island_greeting` into it. Request `"$COAST/aloha"` and submit the response.

## 12 | 15 | Coastal field station | 25 | Treasure map

Find the `treasure-map` ConfigMap in `fieldkit/data/shore.json`. Decode the value of `data.map` from Base64. Submit the resulting phrase, keeping the hyphens.

## 15 | 30 | Explorer records | 25 | Top explorer

The survivors recorded their skills in `fieldkit/data/explorers.sql`. Run a SQL query with `python3 fieldkit/explorer.py "SELECT ..."`. Join the explorer and assessment tables, sum each person's scores and find the highest total. Submit that explorer's name.

## 16 | 20 | Explorer records | 15 | Read the final journal entry

Use the same query runner and the `journal` table. Find the most skilled explorer's most recent entry by timestamp. Submit the entire entry, including punctuation.

## 18 | 25 | Coastal field station | 35 | Persistence pays off

From the repository root, use the local supported execution image to create a named Podman volume. The first disposable container writes the key. A second container reads it after the first exits.

```bash
EE=$(podman images --format '{{.Repository}}:{{.Tag}}' | awk '/\/ee-supported/ {print; exit}')
podman volume create island-locker
podman run --rm -i --user 0 -v island-locker:/locker:Z --entrypoint sh "$EE" \
  -c 'cat > /locker/mykey.txt' < fieldkit/data/locker.txt
podman run --rm --user 0 -v island-locker:/locker:Z --entrypoint cat "$EE" /locker/mykey.txt
```

Submit the text exactly as stored. After submitting, you can remove your own volume with `podman volume rm island-locker`.

## 19 | 20 | Navigator's charts | 101 | Mapster peers

The field station replays a recorded Mapster survey so each seat receives the same chart. Request `"$COAST/peers"`. Count only entries whose state is `connected`. Submit an integer.

## 20 | 15 | Navigator's charts | 19 | Scrambled islands

Fetch `/island/1`, `/island/2`, `/island/3` and `/island/4` from your field station. Each tile contains a letter. Rearrange all four letters to name a vessel. Submit the word.

## 21 | 20 | Navigator's charts | 19 | Island hopping

Request `"$COAST/maps"`. Each entry is an ordered pair of Cartesian coordinates in kilometers. Find the straight-line distance between the first two entries. Round once to the nearest kilometer and submit the integer.

## 22 | 40 | Navigator's charts | 21 | The traveling sailor

Use the same coordinates. Find the shortest open trip that visits every island exactly once. You may start and finish anywhere. Sum unrounded straight-line leg lengths, then round the shortest total to the nearest kilometer. Submit that integer.

## 100 | 10 | Coastal field station | 25 | Kubernetes version

The facilitator saved the game cluster's Kubernetes API version in `fieldkit/data/platform.json`. Read its `gitVersion` field. Submit it exactly, including the leading `v`.

## 38 | 35 | Rescue operations | 37 | Reconcile the relief manifest

The quartermaster needs a backorder list. Read the orders and delivery records in `fieldkit/data/relief.yml`. A delivery counts only after inspection releases it. Several shipments can contain the same cargo.

Edit `fieldkit/playbooks/relief.yml`. For each order, total the released crates of that cargo, subtract them from the order and suppress fully filled orders. Keep the remaining cargo names in alphabetical order. Run your playbook in the VS Code terminal. Submit the resulting `cargo=count` pairs, separated by commas. A pair looks like `lamps=2`.

## 39 | 40 | Rescue operations | 34 | Repair the beacon without drift

The radio accepts each channel once, in ascending numeric order. Edit `fieldkit/templates/beacon.conf.j2` so that the rendered `channels=` line meets that requirement. Preserve the station line and the final newline.

Preview the change on **node02**, apply it, then apply it again to check idempotence.

```bash
(
  cd ~/lab_inventory || exit
  playbook=~/ansible-island-adventure/fieldkit/playbooks/beacon-config.yml
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

## 43 | 50 | Event-Driven Ansible | 42 | Relay the storm warning

Follow **Field guide → Send an authenticated storm report** to create an event-stream credential and event stream for your seat. Create an activation for `storm-relay.yml`. Connect its `station_reports` source to your stream. Enable it and wait for **Running**.

From VS Code, send the quiet, offshore and alert JSON files once each, in that order. Inspect your stream's received-event count and the **Dispatch the harbor launch** entry in **Rule Audit**. Identify the station and sequence from the event that triggered dispatch. Submit the dispatch identifier as `station-sequence`. Disable this activation after you collect the evidence.
