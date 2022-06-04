# Chapter 9


```
wget https://github.com/ansible/awx/archive/17.1.0.zip




    1  sudo yum update
    2  sudo yum install docker
    3  sudo usermod -a -G docker ec2-user
    4  sudo pip3 install docker-compose
    5  sudo systemctl enable docker.service
    6  sudo systemctl start docker.service
    7  ansible --version
    8  sudo yum install ansible
    9  sudo pip3 install ansible==2.10
   10  git
   11  sudo yuminstall git pwgen
   12  sudo yum install git pwgen
   13  wget https://github.com/ansible/awx/archive/17.1.0.zip
   14  ls
   15  unzip 17.1.0.zip 
   16  cd awx-17.1.0/installer/
   17  ls
   18  vi inventory 








107 admin_user=admin
108 admin_password=password
109 
110 # Whether or not to create preload data for demonstration purposes
111 create_preload_data=True
112 
113 # AWX Secret key
114 # It's *very* important that this stay the same between upgrades or you will lose the ability to decrypt
115 # your credentials
116 secret_key=awxsecret


ansible-playbook -i inventory install.yml


[root@ip-172-31-10-109 installer]# docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED          STATUS          PORTS                                   NAMES
97bdf8fd626d   ansible/awx:17.1.0   "/usr/bin/tini -- /u…"   51 seconds ago   Up 47 seconds   8052/tcp                                awx_task
79d10cf03f46   ansible/awx:17.1.0   "/usr/bin/tini -- /b…"   4 minutes ago    Up 45 seconds   0.0.0.0:80->8052/tcp, :::80->8052/tcp   awx_web
314c7667d776   redis                "docker-entrypoint.s…"   4 minutes ago    Up 45 seconds   6379/tcp                                awx_redis
9e9291c7751a   postgres:12          "docker-entrypoint.s…"   4 minutes ago    Up 45 seconds   5432/tcp                                awx_postgres
[root@ip-172-31-10-109 installer]# docker images
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
postgres      12        bc02a3fd9d66   6 days ago      373MB
redis         latest    53aa81e8adfa   6 days ago      117MB
centos        8         5d0da3dc9764   8 months ago    231MB
ansible/awx   17.1.0    599918776cf2   15 months ago   1.41GB



```



