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

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
