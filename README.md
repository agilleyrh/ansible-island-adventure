# Ansible Island Adventure

Use Ansible to recover a sealed dispatch, bring a shore beacon online and respond to a storm alert. The 40 challenges use the VS Code terminal, three RHEL hosts, automation controller and Event-Driven Ansible in your assigned Showroom lab. Submit answers on the game site your facilitator shares with you.

## Start in VS Code

```bash
cd ~
git clone https://github.com/agilleyrh/ansible-island-adventure.git
cd ansible-island-adventure
ansible-navigator run fieldkit/playbooks/hello-world.yml -m stdout --ee false
```

Open the [field guide](workshop/field-guide.md) for inventory, controller project and EDA setup. Start the four warm-ups on the game’s Challenges page. You can also read the [challenge instructions](workshop/challenges.md) in your clone.

The [field kit](fieldkit/) contains the playbooks, roles, training Vault keys, data and local services. The [rulebooks](rulebooks/) are ready to import into your seat’s EDA project.

Adapted from the AnsibleCTF Island Adventure created by Joon Paik and Red Hat contributors.
