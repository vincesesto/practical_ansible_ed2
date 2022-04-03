# Chapter 1
A copy of all the Ansible commands performed in this chapter are listed below in this README file.

```
ansible –-version
```

Our very first Ansible command.
```
ansible all -i "localhost," -m shell -a 'echo Ansible is fun'
```

Running our first Ansible command over multiple hosts.
```
ansible all -i "localhost, 127.0.0.1" -m shell -a 'echo Ansible is fun'
```

Running our first Ansible Playbook.
```
ansible-playbook test.yml -i “localhost,”
```

Running our basic Ansible command but using a hosts inventory file.
```
ansible all -i hosts -m shell -a 'echo Ansible is fun'
```

Using the Ansible Ping module.
```
ansible -i hosts mylaptop -m ping
```

Using the Ansible Setup module
```
ansible mylaptop -i hosts -m setup
```




