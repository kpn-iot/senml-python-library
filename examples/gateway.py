# _  __  ____    _   _
# | |/ / |  _ \  | \ | |
# | ' /  | |_) | |  \| |
# | . \  |  __/  | |\  |
# |_|\_\ |_|     |_| \_|
#
# (c) 2018 KPN
# License: MIT license.
# Author: Jan Bogaerts
#
# gateway example

from kpn_senml import *
import time

gateway_pack = SenmlPack("gateway")

dev1_pack = SenmlPack("dev1")
dev2_pack = SenmlPack("dev2")

temp = SenmlRecord(SenmlNames.KPN_SENML_TEMPERATURE, unit=SenmlUnits.SENML_UNIT_DEGREES_CELSIUS, value=23.5)
door_pos = SenmlRecord("doorPos", update_time=20, value=True)
str_val = SenmlRecord("str val")

gateway_pack.add(temp)
gateway_pack.add(dev1_pack)
gateway_pack.add(dev2_pack)
dev1_pack.add(door_pos)
dev2_pack.add(str_val)

while True:
    temp.value = round(temp.value + 1.1, 2)         # use round() to get consistent rendering length for value, otherwise there are rounding errors.
    door_pos.value = not door_pos.value
    str_val.value = "test"
    print(gateway_pack.to_json())
    time.sleep(1)
