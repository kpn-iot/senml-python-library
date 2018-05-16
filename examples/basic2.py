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

pack = SenmlPack("device_name")
temp = SenmlRecord(SenmlNames.KPN_SENML_TEMPERATURE, unit=SenmlUnits.SENML_UNIT_DEGREES_CELSIUS, value=23.5)
door_pos = SenmlRecord("doorPos", update_time=20, value=True)
str_val = SenmlRecord("str val")

pack.add(temp)
pack.add(door_pos)
pack.add(str_val)

while True:
    temp.value = temp.value + 1.1
    door_pos.value = not door_pos.value
    str_val.value = "test"
    print(pack.to_json())
    time.sleep(1)
