# Chapter 3

Run the new Ansible Playbook set up as a role.
```
ansible-playbook -i hosts site.yml
```

Run the Ansible Playbook that also uses the Django Playbook.
```
ansible-playbook -i hosts site.yml --extra-vars django_app_location=`pwd`
```

Run the development webserver for Django to test.
```
python3 web_app/manage.py runserver 0.0.0.0:8000
```

List all of the tags in a playbook.
```
ansible-playbook -i hosts site.yml -e django_app_location=`pwd` --list-tags
```

Run you playbook using a specific tag.
```
ansible-playbook -i hosts site.yml -e django_app_location=`pwd` --tags deploy_database_only
```
