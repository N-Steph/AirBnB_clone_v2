#!/usr/bin/env bash
# setting up a web server for deployment

sudo apt-get -qq update
sudo apt-get -qq install nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo bash -c 'echo "This is a test" > /data/web_static/releases/test/index.html'
sudo chown -R ubuntu:ubuntu /data/
RESULT=$(grep -E "hbnb_static" /etc/nginx/sites-available/default)
if [ ${#RESULT} -eq 0 ]
then
    sudo sed -i "s/root \/var\/www\/html;/root \/var\/www\/html;\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}\n/" /etc/nginx/sites-available/default
fi
sudo service nginx restart
