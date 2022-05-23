# Chapter 8

Use pip3 to install Molecule and supporting applications.
```
sudo pip3 install molecule[lint,docker]
```
Check the Molecule version you are running on your system.
```
molecule --version
```
Create a new Ansible role using the Molecule init command.
```
molecule init role vincesesto.test_role --driver-name docker
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


Test File
```
import os
import testinfra.utils.ansible_runner
import urllib2

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('splunk_server')

def test_splunk_service_is_running(host):
    splunk_service = host.service('splunk')
    assert splunk_service.is_running

def test_splunk_is_accessible_on_port_8000(host):
    host_ip = host.interface("eth0").addresses[0]
    response = urllib2.urlopen(ip+':8000')
    assert len(response.read()) > 0
    
def test_splunk_apps_are_installed(host):
    app_dir = host.file('/opt/splunk/etc/apps/ansible_test_app')
    assert app_dir.exists
    assert app_dir.contains('Test App Installed')
```
