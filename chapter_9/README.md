# Chapter 9


Download AWX To your environment using wget.
```
wget https://github.com/ansible/awx/archive/17.1.0.zip
```
Unzip your file
```
unzip 17.1.0.zip
```
Move into the installation directoruy:
```
cd awx-17.1.0/installer/
```
Make sure you have a admin password and secret set
```
vi inventory 
```
Run the ansible playbook in the directory
```
ansible-playbook -i inventory install.yml
```

```
images
<ansible playbook output on tower >
<insert creating Job run>
<insert creating template>
<insert creating hosts>

```



