# Chapter 4

Encrypt a file with Ansible Vault.
```
ansible-vault encrypt roles/db_server/vars/test_environment.yml
```
View and encrypted file with Ansible Vault.
```
ansible-vault view roles/db_server/vars/test_environment.yml
```
Run an Ansible Playbook with ansible vault password.
```
ansible-playbook -i hosts site.yml -e django_app_location=`pwd` -e env=test --ask-vault-pass
```
Use Ansible Vault to view an encrypted file, using a password file instead of asking for a password.
```
ansible-vault view roles/db_server/vars/test_environment.yml --vault-password-file password_file.txt
```
Use Ansible Vault to edit an encrypted file.
```
ansible-vault edit roles/db_server/vars/test_environment.yml --vault-password-file password_file.txt
```
Use Ansible Vault to change the password on an encrypted file.
```
ansible-vault rekey roles/db_server/vars/test_environment.yml --ask-vault-pass
```
Use Ansible Vault to decrypt an encrypted file.
```
ansible-vault decrypt roles/db_server/vars/test_environment.yml --ask-vault-pass
```
