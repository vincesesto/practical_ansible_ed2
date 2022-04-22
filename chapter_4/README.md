# Chapter 4

## Ansible Vault Commands

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

## Ansible Galaxy Commands
Perform a search on Ansible Galaxy from the command line.
```
ansible-galaxy search django
```
Narrow your search using the --author option to look for a specific author.
```
ansible-galaxy search django --author ScorpionResponse
```
Perform a search from the command line, for only roles created by a specific author.
```
ansible-galaxy search --author ScorpionResponse
```
To get more infomormation on the specific galaxy role you want to use on your system.
```
ansible-galaxy info ScorpionResponse.django
```
To see if you currently have any Ansible Galaxy roles on your system using the list option.
```
ansible-galaxy list
```
This is the url for the Ansible Galaxy login page.
```
https://galaxy.ansible.com/login
```




ansible-galaxy login




ansible-galaxy install SimpliField.users --roles-path roles/










