# Island Adventure field guide

Open your assigned Showroom and select **VS Code**. The lab provides a terminal, three managed hosts and Ansible Automation Platform (AAP). Your AAP login is in Showroom module **2.1 Introduction to Ansible Automation Platform**. Use your game account to submit answers. Start with the four warm-ups on the **Challenges** page.

## Get the field kit

Run these commands in the VS Code terminal.

```bash
cd ~
git clone https://github.com/agilleyrh/ansible-island-adventure.git
cd ansible-island-adventure
ansible-navigator run fieldkit/playbooks/hello-world.yml -m stdout --ee false
```

The clone includes the playbooks, roles, training Vault keys, rulebooks and challenge data. Start each terminal challenge in `~/ansible-island-adventure`. For the two playbooks that connect to managed nodes, the challenge commands run Ansible from `~/lab_inventory`. Ansible loads the lab’s SSH settings there automatically.

To see which hosts belong to each inventory group, run `ansible-inventory -i ~/lab_inventory/hosts --graph`.

## Controller project

1. In **Automation Execution → Projects**, create a project named `Island Adventure` in the **Workshop** organization.
2. Choose source control type **Git**, enter `https://github.com/agilleyrh/ansible-island-adventure.git` as the URL and `main` as the branch. Leave **Source Control Credential** empty.
3. Save the project and wait for its sync to succeed. When you create job templates, select **Workshop Inventory**. For jobs that connect to a managed node, also select the existing **Workshop Credential**. The sealed-dispatch challenge explains how to create a Vault credential for encrypted training files.

## Coastal field station

Start the HTTP service when a challenge first mentions `COAST`. It listens on your seat’s loopback interface. Commands to start the station and its receiver are in the [field kit instructions](https://github.com/agilleyrh/ansible-island-adventure/blob/main/fieldkit/README.md#coastal-field-station).

## Event-Driven Ansible

1. In **Automation Decisions → Projects**, create a project named `Island Adventure EDA` in **Workshop**. Enter `https://github.com/agilleyrh/ansible-island-adventure.git` as the Git URL and `main` as the branch. Leave the source control credential empty and keep TLS verification enabled. Wait for the import to complete.
2. Under **Automation Decisions → Rulebook Activations**, create `Island Tides`. Select **Workshop**, your EDA project, `tide-watch.yml` and **Default Decision Environment**. Choose restart policy **Never**. The rulebook writes to Rule Audit, so leave the optional AAP credential empty.
3. Enter these **Variables** as YAML, save with the activation enabled and wait for it to finish. Open the activation’s instance output or filter **Rule Audit** by its name.

```yaml
lower_tide: 3
upper_tide: 6
```

## Send an authenticated storm report

1. In your VS Code terminal, generate a unique event token with `openssl rand -hex 24`. In **Automation Decisions → Infrastructure → Credentials**, create a **Token Event Stream** credential in **Workshop**. Enter the generated value as the token and set the HTTP header key to `X-Island-Token`. Name the credential `Island Storm Token`.
2. Open **Automation Decisions → Event Streams**, create a stream in **Workshop**, and name it `Island Storm Reports` and select your token credential. Leave test mode off so the stream delivers events. Copy the stream's generated URL. On this Showroom image the generated hostname is often `aap.example.org`. Replace that hostname with the hostname from your own **AAP** tab. Keep the full stream path, UUID and trailing slash, and use HTTPS.
3. Create an activation named `Island Storm Relay` using the same organization and EDA project. Select `storm-relay.yml`. In **Source mappings** (or **Event streams**), enable the mapping and select your stream for the named source `station_reports`. Use **Default Decision Environment**, restart policy **Never**, and leave the variables empty. Save, enable and wait for **Running**.
4. In the VS Code terminal, run the commands below from the repository root. Paste your own URL and token at the prompts. Each request should return a successful HTTP status. The stream should receive three events and the rule should fire once.

```bash
read -r -p 'Event stream URL: ' ISLAND_STREAM
read -rs -p 'Event token: ' ISLAND_TOKEN; echo
for report in quiet offshore alert; do
  curl --fail-with-body -sS -o /dev/null -w "$report %{http_code}\n" \
    -H "X-Island-Token: $ISLAND_TOKEN" -H 'Content-Type: application/json' \
    --data-binary "@fieldkit/data/storm-$report.json" "$ISLAND_STREAM"
done
unset ISLAND_TOKEN
```

5. Open the matching Rule Audit entry and its associated event. The JSON you sent appears under `payload`. Disable your storm activation when you finish.
