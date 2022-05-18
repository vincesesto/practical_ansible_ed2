# Chapter 8

Use pip3 to install Molecule and supporting applications.
```
pip3 install molecule docker-py testinfra
```
Check the Molecule version you are running on your system.
```
molecule --version

molecule 3.6.1 using python 3.9 
    ansible:2.10.8
    delegated:3.6.1 from molecule

```
Create a new Ansible role using the Molecule init command.
```
molecule init role test_role

molecule init role vincesesto.test_role
INFO     Initializing new role test_role...
No config file found; using defaults
- Role test_role was created successfully
[WARNING]: No inventory was parsed, only implicit localhost is available
localhost | CHANGED => {"backup": "","changed": true,"msg": "line added"}
INFO     Initialized role in /home/vincesesto/practical_ansible_ed2/chapter_8/splunk_server/roles/test_role successfully.


tree test_role/
test_role/
├── defaults
│   └── main.yml
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── molecule
│   └── default
│       ├── converge.yml
│       ├── create.yml
│       ├── destroy.yml
│       ├── INSTALL.rst
│       ├── molecule.yml
│       └── verify.yml
├── README.md
├── tasks
│   └── main.yml
├── tests
│   ├── inventory
│   └── test.yml
└── vars
    └── main.yml

8 directories, 14 files


cat test_role/molecule/default/molecule.yml 
---
dependency:
  name: galaxy
driver:
  name: delegated
platforms:
  - name: instance
provisioner:
  name: ansible
verifier:
  name: ansible



molecule create
INFO     default scenario test matrix: dependency, create, prepare
INFO     Performing prerun...
INFO     Set ANSIBLE_LIBRARY=/home/vincesesto/.cache/ansible-compat/88d782/modules:/home/vincesesto/.ansible/plugins/modules:/usr/share/ansible/plugins/modules
INFO     Set ANSIBLE_COLLECTIONS_PATH=/home/vincesesto/.cache/ansible-compat/88d782/collections:/home/vincesesto/.ansible/collections:/usr/share/ansible/collections
INFO     Set ANSIBLE_ROLES_PATH=/home/vincesesto/.cache/ansible-compat/88d782/roles:/home/vincesesto/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles
INFO     Using /home/vincesesto/.ansible/roles/vincesesto.test_role symlink to current repository in order to enable Ansible to find the role using its expected full name.
INFO     Running default > dependency
WARNING  Skipping, missing the requirements file.
WARNING  Skipping, missing the requirements file.
INFO     Running default > create

PLAY [Create] ******************************************************************

TASK [Populate instance config dict] *******************************************
skipping: [localhost]

TASK [Convert instance config dict to a list] **********************************
skipping: [localhost]

TASK [Dump instance config] ****************************************************
skipping: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=0    changed=0    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0

INFO     Running default > prepare
WARNING  Skipping, prepare playbook not configured.



```
If your role already exists, create Molecule a scenario.
```
molecule init scenario 
```
Set up a provisioner for Molecule.
```
molecule create 
```
Prepare a Docker inatance ready for testing.
```
molecule create
```
Check instances are available and ready.
```
molecule list


molecule list
INFO     Running default > list
                ╷             ╷                  ╷               ╷         ╷            
  Instance Name │ Driver Name │ Provisioner Name │ Scenario Name │ Created │ Converged  
╶───────────────┼─────────────┼──────────────────┼───────────────┼─────────┼───────────╴
  test_role     │ delegated   │ ansible          │ default       │ true    │ false      




```
Run tests over a provisioned image.
```
molecule converge
```
Login directly to an image that has been provisioned.
```
molecule login
```
Run all the Molecule testing from start to finish.
```
molecule test
```
