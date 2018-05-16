# _  __  ____    _   _
# | |/ / |  _ \  | \ | |
# | ' /  | |_) | |  \| |
# | . \  |  __/  | |\  |
# |_|\_\ |_|     |_| \_|
#
# (c) 2018 KPN
# License: GNU General Public License v3.0.
# Author: Jan Bogaerts
#
# basic example

from kpn_senml import *
import time
import random

pack = SenmlPack("device_name")

while True:
    with SenmlRecord("test", value=random.randint(0,1000)) as rec:           # use a with statement to automatically remove the item from the list when it goes out of scope, generate a value for the record
        pack.add(rec)
        print(pack.to_json())
    time.sleep(1)
