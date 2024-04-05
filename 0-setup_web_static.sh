#!/usr/bin/env bash
# setting up a web server for deployment

sudo apt update
sudo apt install nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo bash -c 'echo "This is a test" > /data/web_static/releases/test/index.html'
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "s/root \/var\/www\/html;/root \/var\/www\/html;\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}\n/" /etc/nginx/sites-available/default
sudo service nginx restart
