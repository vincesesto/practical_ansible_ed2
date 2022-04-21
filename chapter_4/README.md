# Chapter 4

Encrypt a file with Ansible Vault.
```
ansible-vault encrypt roles/db_server/vars/test_environment.yml
```
View and encrypted file with Ansible Vault.
```
ansible-vault view roles/db_server/vars/test_environment.yml
```
Run an Ansible Playbook with ansible vault passwod
```
ansible-playbook -i hosts site.yml -e django_app_location=`pwd` -e env=test --ask-vault-pass
```



