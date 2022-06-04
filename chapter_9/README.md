# Chapter 9



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






