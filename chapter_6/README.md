# Chapter 6

AWS Billing console: https://console.aws.amazon.com/billing/home.


New Variables file for the splunk server
```
ansible-vault encrypt roles/splunk_server/vars/main.yml
```
Page 7, run the following
```
ansible-playbook -i hosts server_deploy.yml --ask-vault-pass
```



