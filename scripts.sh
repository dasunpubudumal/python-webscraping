echo "===== Installing Relevant Dependencies for Python 3.6 ====="

pip3 --version

if [ &? -eq 0]; then echo OK
else sudo apt-get install pip3
fi


pip3 install beautifulsoup4 certifi
