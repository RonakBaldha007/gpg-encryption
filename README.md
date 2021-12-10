# Python gnupg (GPG) example

python-gnupg is a Python package for encrypting and decrypting strings or files using GNU Privacy Guard (GnuPG or GPG). GPG is an open source alternative to Pretty Good Privacy (PGP). A popular use of GPG and PGP is encrypting email.

## Install

$ sudo apt-get install gnupg <br />
$ sudo adduser testgpguser <br />
$ sudo su testgpguser <br />
$ cd <br />
$ virtualenv --no-site-packages venv <br />
$ source venv/bin/activate <br />
$ pip install python-gnupg <br />

## Generate a key

This creates a GPG key. This also creates the gpghome directory if it does not exist. You may need to supply random hardware activity during the key generation. To generate random numbers, you can also install the rng-tools package.

$ sudo apt-get install rng-tools 
