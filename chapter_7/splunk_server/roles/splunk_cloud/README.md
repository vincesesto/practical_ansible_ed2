Role Name
=========

This role deploys your Splunk Server AMI onto a CloudFormation Stack into the Amazon Cloud.

Requirements
------------

You need to have a valid AWS account an have your AWS Access and Security keys availble on your system.
You also need to install boto to allow the modules specific for AWS to be run by Ansible.

Role Variables
--------------

The variables specific for this role are in the vars/main.yml file and are explained below:
* aws_region: The AWS region you want to install your Splunk server into.
* aws_instance_type: The AWS EC2 instance size.
* aws_image: The AMI identitification number of the Splunk server to be used.
* aws_keypair: Use a valid key pair to be able to SSH to the server.
* aws_ssh_location: The IP range the server will be able to be SSH'd to.

Dependencies
------------

The Splunk Server role should be run as this will create the Splunk AMI used by the Splunk Cloud role. This role can be found at the folloing location: https://github.com/vincesesto/practical_ansible_ed2/tree/main/chapter_6/splunk_server/roles/splunk_server

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: localhost
      connection: local
      gather_facts: false
      user: root
      roles:
      - splunk_cloud
      tasks:
      - debug:
        msg: "Production Server Public IP Address {{  splunk_public_ip }}"      

License
-------

BSD

Author Information
------------------

More details about the author can be found at the following link: https://www.amazon.com/Vincent-Sesto/e/B073R3VW2G
