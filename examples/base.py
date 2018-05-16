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
# base value example

from kpn_senml import *
import time
import datetime

pack = SenmlPack("device_name")
temp = SenmlRecord(SenmlNames.KPN_SENML_TEMPERATURE, unit=SenmlUnits.SENML_UNIT_DEGREES_CELSIUS, value=23.5)
door_pos = SenmlRecord("doorPos", update_time=20, value=True)
int_val = SenmlRecord("int_val", sum=100)

pack.add(temp)
pack.add(door_pos)
pack.add(int_val)

random_time = datetime.datetime.strptime('Jan 1 2018  1:33PM', '%b %d %Y %I:%M%p')
pack.base_time = time.mktime(random_time.timetuple())                       # set a base time
pack.base_value = 5
pack.base_sum = 50
temp.time = time.mktime(datetime.datetime.now().timetuple())                             # all child objects will receive the time value



print(pack.to_json())
