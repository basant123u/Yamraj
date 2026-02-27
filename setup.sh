#!/data/data/com.termux/files/usr/bin/bash

pkg update -y
pkg upgrade -y

pkg install -y python git chromium chromedriver

python -m pip install --upgrade pip==24.0 setuptools==69.1.1 wheel==0.42.0

pip install -r requirements.txt