# Chapter 2

Running your playbook for the webserver from the test_playbooks directory.
```
ansible-playbook -i hosts webserver-playbook.yml
```

Running the previous playbook with the verbose option.
```
ansible-playbook -i hosts webserver-playbook.yml -v
```

Run the playbook for the database server.
```
ansible-playbook -i hosts dbserver-playbook.yml
```
