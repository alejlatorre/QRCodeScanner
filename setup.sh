#1 /bin/bash
#
# /HEADER/
# Providing all the tools for reproducing code
# Author: Alejandro Latorre
#
#-------------------------------------------------------------------------------
# OS check so it only runs on GNU/Linux
#-------------------------------------------------------------------------------
OS_CHECK=$(uname -o)
if [ "${OS_CHECK}" != "GNU/Linux" ]; then
    echo "This script was made for the GNU/Linux system and you are using: ${OS_CHECK}"
    exit 1
else
    echo "You are using: ${OS_CHECK}"
fi
#-------------------------------------------------------------------------------
# Check if QRCodeScanner has already been installed
#-------------------------------------------------------------------------------
echo '##########################################################'
echo 'Have you already configured QRCodeScanner repository? (y or n)'
echo '##########################################################'
read answer
if [[ $answer =~ ^[Yy]$ ]]; then
    echo "Upgrading dependencies will be skipped..."
    echo "Installation of asdf and python will be skipped..."
else
    echo 'Upgrading dependencies...'
    sudo apt update
    sudo apt upgrade -y
    sudo apt autoremove -y
    sudo apt autoclean

    sudo apt install curl wget openssh-server openssh-client git tar silversearcher-ag unzip -y
    sudo apt-get update
    sudo apt-get install --no-install-recommends -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
    sudo apt-get install -y gcc make zlib1g-dev libreadline-dev libreadline8 sqlite3 libsqlite3-dev libbz2-dev python-tk python3-tk tk-dev

    echo 'Installing asdf...'
    git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.10.2
    echo '. $HOME/.asdf/asdf.sh' >>~/.bashrc
    echo '. $HOME/.asdf/completions/asdf.bash' >>~/.bashrc
    source ~/.bashrc
    sleep 5
    source ~/.bashrc

    echo 'Installing Python...'
    asdf plugin-add python
    asdf install python 3.9.9
    asdf global python 3.9.9

    echo 'Installing Poetry...'
    asdf plugin-add poetry https://github.com/asdf-community/asdf-poetry.git
    asdf install poetry 1.2.1
    echo 'export PATH="$HOME/.poetry/bin:$PATH"' >>~/.bashrc

    echo 'Cloning the project QRCodeScanner...'
    cd ~/
    mkdir truora
    cd truora
    git clone git@github.com:alejlatorre/QRCodeScanner.git
    cd QRCodeScanner/
fi

echo 'Installing dependencies...'
cd ~/truora/QRCodeScanner
poetry install
poetry run pre-commit install

echo 'Setting VcXsrv to show images in WSL...'
echo '##########################################################'
echo 'Have you already installed VcXsrv? (y or n)'
echo '##########################################################'
read answer
if [[ $answer =~ ^[Yy]$ ]]; then
    echo 'Please install VcXsrv with the following instructions: PATH TO README.md'
else
    echo 'Dynamically exporting the DISPLAY enviroment variable in WSL2...'
    echo "export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0" >>~/.bashrc
    echo 'export QT_DEBUG_PLUGINS=1' >>~/.bashrc
    echo 'echo $DISPLAY'
fi
