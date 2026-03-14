#!/data/data/com.termux/files/usr/bin/bash

pkg update -y
pkg upgrade -y

pkg install -y python git

pip install --upgrade pip
pip install -r requirements.txt

chmod +x start.sh
chmod +x update.sh

echo ""
echo "Setup complete."
echo "Run: bash start.sh"
