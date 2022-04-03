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
ansible mylaptop -i hosts -m ping
```

Using the Ansible Setup module.
```
ansible mylaptop -i hosts -m setup
```

Using the Ansible Git module.
```
ansible mylaptop -i hosts -m git -a "repo='https://github.com/vincesesto/markdown-cheatsheet.git' -dest=/tmp/markdown-­cheatsheet/"
```

Using the Ansible Shell module.
```
ansible mylaptop -i hosts -m shell -a "ls -l /tmp/"
```

Using the Ansible Apt module.
```
ansible mylaptop -i hosts -m apt -a "name=apache2 state=present"
```

Using the Ansible Package module.
```
ansible mylaptop -i hosts -m package -a "name=apache2 state=present"
```

Using the Ansible Service module.
```
ansible mylaptop -i hosts -m service -a "name=apache2 state=started"
```

Using the Ansible Get_url module.
```
ansible mylaptop -i hosts -m get_url -a "url=http://localhost dest=/tmp/"
```

Using the Ansible File module.
```
ansible mylaptop -i hosts -m file -a "path=/tmp/another_test owner=root group=root state=directory"
```







