#!/bin/bash

# Install system dependencies
apt-get update
apt-get install -y python3.9 python3.9-dev python3-pip build-essential

# Install Python dependencies
pip3 install --upgrade pip
pip3 install -r requirements.txt

# Create symbolic link for Python
ln -sf /usr/bin/python3.9 /usr/bin/python 