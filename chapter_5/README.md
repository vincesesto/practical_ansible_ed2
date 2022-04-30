# Chapter 5

AWS Pricing and Rates: https://aws.amazon.com/pricing/services/

AWS Pricing Document: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/awsaccountbilling-aboutv2.pdf

IAM Services: https://console.aws.amazon.com/iam/home

Export your AWS credentials to use on your system.
```
export AWS_ACCESS_KEY_ID=<your_access_key>
export AWS_SECRET_ACCESS_KEY=<your_secret_key>
export AWS_DEFAULT_REGION=<your_region>
```  

Use awscli to test the current user that is accessing AWS.
```
aws sts get-cller-identity
```

Use SSH to connect to your running EC2 server.
```
ssh -i splunkserver.pem ec2-user@<public_ip_address>
```

Use Ansible to remove a running AWS EC2 instance.
```
ansible localhost -m ec2 -a "instance_ids=<your_instance_id> region=<your_aws_region> state=absent"
```
