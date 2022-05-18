# Chapter 8

Use pip3 to install Molecule and supporting applications.
```
pip3 install molecule docker-py testinfra
```
Check the Molecule version you are running on your system.
```
molecule --version
```
Create a new Ansible role using the Molecule init command.
```
molecule init role test_role
```
If your role already exists, create Molecule a scenario.
```
molecule init scenario 
```

Set up a provisioner for Molecule.
molecule create 


Prepare a Docker inatance ready for testing
molecule create

Check instances are available and ready
molecule list


Run tests over a provisioned image
molecule converge


Login directly to an image that has been provisioned
molecule login



molecule test
 
