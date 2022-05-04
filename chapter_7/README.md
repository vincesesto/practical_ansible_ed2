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




