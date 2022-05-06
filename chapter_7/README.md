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

## Troubleshooting Asible Playbooks
Using the --start-at-taks option to start at a ddifferent taks of your Ansible playbook.
```
ansible-playbook -i hosts cloudformation_deploy.yml  --start-at-task="<task_name>"
```
Using the --step option to step through your Ansible playbook.
```
ansible-playbook -i hosts cloudformation_deploy.yml --step
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
