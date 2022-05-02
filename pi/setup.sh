
sudo apt-get update
sudo apt-get upgrade -y

sudo apt-get install -y build-essential apt-utils git matchbox-keyboard tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev ipip wiringpi

wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
sudo tar zxf Python-3.7.0.tgz
cd Python-3.7.0 || exit
./configure
sudo make -j 4
sudo make altinstall
cd /usr/local/bin/ || exit
sudo ln -s python3.7 python
