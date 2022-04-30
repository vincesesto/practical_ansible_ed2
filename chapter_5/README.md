# Chapter 5


AWS Pricing and Rates
https://aws.amazon.com/pricing/services/.

AWS Pricing Document
https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/awsaccountbilling-aboutv2.pdf


IAM Services
https://console.aws.amazon.com/iam/home



  952  export AWS_ACCESS_KEY_ID=<your_access_key>
  953  export AWS_SECRET_ACCESS_KEY=<your_secret_key>
  954  export AWS_DEFAULT_REGION=<your_region>
  
  
  955  aws sts get-cller-identity





Use SSH to connect to your running EC2 server.
```
ssh -i splunkserver.pem ec2-user@<public_ip_address>
```
