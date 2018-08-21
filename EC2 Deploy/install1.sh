#!/bin/bash

chmod 777 ~/COMM002-Build/EC2\ Deploy/install2.sh
sudo apt-get -y update
sudo apt-get -y install python3-pip
sudo apt-get -y install nginx
sudo /etc/init.d/nginx start
sudo rm /etc/nginx/sites-enabled/default
sudo touch /etc/nginx/sites-available/flask-settings
sudo chmod 666 /etc/nginx/sites-available/flask-settings
sudo echo "server {
        location / {
                proxy_pass http://127.0.0.1:8000;
                proxy_set_header Host \$host;
                proxy_set_header X-Real-IP \$remote_addr;
       }
}
" > /etc/nginx/sites-available/flask-settings
sudo ln -s /etc/nginx/sites-available/flask-settings  /etc/nginx/sites-enabled/flask_settings
sudo /etc/init.d/nginx restart
sudo apt-get install -y python3-venv
cd COMM002-Build
python3 -m venv WISLEY_ENV