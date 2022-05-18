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
