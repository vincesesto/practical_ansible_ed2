# Chapter 7

Use the setup Ansible module to get the facts of an EC2 instance running on AWS.
```
ansible all -i "ec2-user@<public_ip_address>," -m setup  --key-file "<your_key_file>"
```
Use the setup Ansible module with the filter option to extract specific details of an EC2 instance running on AWS.
```
ansible all -i "ec2-user@<public_ip_address>," -m setup  --key-file "<your_key_file>" -a "filter=ansible_processor_vcpus"
```
Use the ec2_facts Ansible module to specifically gather details for AWS EC2 instances.
```
ansible all -i "ec2-user@<public_ip_address>," -m ec2_facts  --key-file "<your_key_file>"
```

## Troubleshooting Ansible Playbooks
Using the --start-at-taks option to start at a ddifferent taks of your Ansible playbook.
```
ansible-playbook -i hosts cloudformation_deploy.yml  --start-at-task="<task_name>"
```
Using the --step option to step through your Ansible playbook.
```
ansible-playbook -i hosts cloudformation_deploy.yml --step
```
Using the --check option with Ansible.
```
ansible-playbook -i hosts server_deploy.yml --check  
```
Using the Ansible --syntax-check option on your playbook.
```
ansible-playbook -i hosts cloudformation_deploy.yml --syntax-check -v
```

## Ansible Lint
Check the version of Ansible Lint that is installed on your system.
```
ansible-lint --version
```
Run the Ansible Lint command over a speciic playbook.
```
ansible-lint server_deploy.yml -v
```
Using Ansible Lint with a specific rules directory, using the -r option.
```
ansible-lint server_deploy.yml -r <rules_directory>
```
Using Ansible Lint with a specific config file, using the -c option.
```
ansible-lint server_deploy.yml -c <config_file>
```
Using Ansible lint to display all the tasks going to be run by the playbook.
```
ansible-playbook -i hosts server_deploy.yml --list-tasks
```


Page 16 output
```
[701] Role info should contain platforms
roles/splunk_server/meta/main.yml:1
{'meta/main.yml': {'galaxy_info': {'author': 'your name', 'description': 'your role description', 'company': 'your company (optional)', 'license': 'license (GPL-2.0-or-later, MIT, etc)', 'min_ansible_version': 2.9, 'galaxy_tags': [], '__line__': 2, '__file__': '/home/vincesesto/practical_ansible_ed2/chapter_7/splunk_server/roles/splunk_server/meta/main.yml'}, 'dependencies': [], '__line__': 1, '__file__': '/home/vincesesto/practical_ansible_ed2/chapter_7/splunk_server/roles/splunk_server/meta/main.yml', 'skipped_rules': []}}

[703] Should change default metadata: author
roles/splunk_server/meta/main.yml:1
{'meta/main.yml': {'galaxy_info': {'author': 'your name', 'description': 'your role description', 'company': 'your company (optional)', 'license': 'license (GPL-2.0-or-later, MIT, etc)', 'min_ansible_version': 2.9, 'galaxy_tags': [], '__line__': 2, '__file__': '/home/vincesesto/practical_ansible_ed2/chapter_7/splunk_server/roles/splunk_server/meta/main.yml'}, 'dependencies': [], '__line__': 1, '__file__': '/home/vincesesto/practical_ansible_ed2/chapter_7/splunk_server/roles/splunk_server/meta/main.yml', 'skipped_rules': []}}

[201] Trailing whitespace
roles/splunk_server/tasks/main.yml:69
 

You can skip specific rules or tags by adding them to your configuration file:                                    

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ # .ansible-lint                                                                                                │
│ warn_list:  # or 'skip_list' to silence them completely                                                        │
│   - '201'  # Trailing whitespace                                                                               │
│   - '206'  # Variables should have spaces before and after: {{ var_name }}                                     │
│   - '701'  # meta/main.yml should contain relevant info                                                        │
│   - '703'  # meta/main.yml default values should be changed                                                    │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```

page 20 output
```
[ANSWERS01] Line too long (95 characters)
roles/splunk_server/tasks/main.yml:60
    url: "https://{{ ec2.instances[0].public_ip}}:8089/services/apps/local/ansible_answers_app"

[ANSWERS02] Playbook May Contain AWS Credentials
server_deploy.yml:9
    aws_secret_access_key: AGSJDFKSHDGD122343

You can skip specific rules or tags by adding them to your configuration file:                                    

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ # .ansible-lint                                                                                                │
│ warn_list:  # or 'skip_list' to silence them completely                                                        │
│   - 'ANSWERS01'  # Line too long (95 characters)                                                               │
│   - 'ANSWERS02'  # Playbook May Contain AWS Credentials                                                        │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```




'''


Page 18 output
```
[ANSWERS01] Line too long (95 characters)
roles/splunk_server/tasks/main.yml:60
    url: "https://{{ ec2.instances[0].public_ip}}:8089/services/apps/local/ansible_answers_app"

You can skip specific rules or tags by adding them to your configuration file:                                    

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ # .ansible-lint                                                                                                │
│ warn_list:  # or 'skip_list' to silence them completely                                                        │
│   - 'ANSWERS01'  # Line too long (95 characters)                                                               │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────
```
