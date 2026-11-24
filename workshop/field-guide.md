# Ansible Island Adventure review field guide

Register on the **review board** using its registration code and choose your own password. Start with the warm-ups. Use the **VS Code** and **AAP** tabs in your assigned Showroom. Module 2.1 supplies your seat’s AAP login.

## Clone the review branch

```bash
cd ~
git clone --branch codex/ansible-first-review --single-branch https://github.com/agilleyrh/ansible-island-adventure.git island-review
cd island-review
```

Start each card at `~/island-review`. Your local edits apply to CLI exercises. The supplied `fieldkit/run-managed` helper changes into `~/lab_inventory` and runs Ansible with the seat’s inventory and SSH settings. Local playbooks run directly in VS Code. In the **Equip the container crew** warm-up, install the included Podman collection once. Use one Showroom seat per participant or working pair.

## Controller project

1. Under **Automation Execution → Projects**, create **Island Review** in **Workshop**. Choose **Git**, URL `https://github.com/agilleyrh/ansible-island-adventure.git`, branch `codex/ansible-first-review`. Leave **Source Control Credential** empty. Save and wait for a successful sync.
2. Create the job templates each card names. Select **Workshop Inventory**. Jobs that connect to managed nodes also use the existing **Workshop Credential** (Machine). Add the training Vault credential where the card calls for it.

## Event-Driven Ansible

1. In **Automation Decisions → Projects**, create **Island Review EDA** in **Workshop**. Use the same public Git URL and review branch as the controller project, leave the Git credential empty and keep TLS verification enabled. Wait for a successful import.
2. Under **Automation Decisions → Rulebook Activations**, create **Island Review Tides** with your EDA project, `tide-watch.yml`, **Workshop**, **Default Decision Environment** and restart policy **Never**. Leave the optional AAP credential empty for the tide exercise. Set the following **Variables**. Save with the activation enabled, then inspect the instance output or Rule Audit after it completes.

```yaml
lower_tide: 3
upper_tide: 6
```

## Send an authenticated storm report

1. In **Automation Execution → Templates**, create a job template named exactly **Island Review Dispatch** using **Island Review**, **Workshop Inventory**, **Workshop Credential** and `fieldkit/playbooks/storm-dispatch.yml`. Enable **Prompt on launch** for **Variables** so the matching event reaches the job. Enable **Privilege Escalation**. Save it.
2. In **Automation Decisions → Infrastructure → Credentials**, create a **Red Hat Ansible Automation Platform** credential in **Workshop**. Name it **Island Review Launch**. For **Host**, use the HTTPS address from your AAP tab followed by `/api/controller`. Enter your Showroom AAP username and password and enable TLS verification. This credential allows the activation to launch the template in your seat.
3. In VS Code, generate a token with `openssl rand -hex 24`. In EDA Credentials, create **Island Review Token** of type **Token Event Stream** in **Workshop**. Set **HTTP header key** to `X-Island-Token` and enter the generated token. Save it.
4. Under **Automation Decisions → Event Streams**, create **Island Review Reports** with your token credential. Leave test mode off. Copy the generated URL. If its hostname is `aap.example.org`, replace only that hostname with the public hostname from your AAP tab. Retain the full path and trailing slash.
5. Create **Island Review Storm** with your EDA project, `storm-relay.yml`, **Workshop**, **Default Decision Environment**, restart **Never**, and the **Island Review Launch** AAP credential. Map the named source `station_reports` to **Island Review Reports**. In **Variables**, set `dispatch_template: Island Review Dispatch`. Save, enable and wait for **Running**.
6. At the root of your clone run `ansible-playbook fieldkit/playbooks/send-reports.yml`. Paste the corrected stream URL and your token when prompted. This sends the quiet, offshore and harbor reports once each. Open **Rule Audit** and **Automation Execution → Jobs**. Inspect the matching event and the linked dispatch job. Read the receipt on node03 as directed on the card. Disable the storm activation when you finish.

The [optional bonus puzzles](https://github.com/agilleyrh/ansible-island-adventure/blob/codex/ansible-first-review/workshop/bonuses.md) are available throughout the expedition.
