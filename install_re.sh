#!/bin/bash

if [[ $EUID -ne 0 ]]; then
	echo "This script must be run as root (use sudo)" 1>&2
	exit 1
fi

#cp re_test /usr/bin/
cp leds /usr/bin
cp gpio /usr/bin
cp re.service /lib/systemd/system/
systemctl enable re.service
systemctl start re

exit 0

