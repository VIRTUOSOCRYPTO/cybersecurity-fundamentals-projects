#!/bin/bash
sudo ufw enable
sudo ufw allow ssh
sudo chmod 700 /home/user/private
systemctl list-unit-files --type=service

