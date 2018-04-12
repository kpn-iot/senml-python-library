from senml_pack import SenmlPack
from senml_record import SenmlRecord
from senml_unit import SenmlUnits
from senml_kpn_names import SenmlNames
import time
import datetime

pack = SenmlPack("device_name")
temp = SenmlRecord(SenmlNames.KPN_SENML_TEMPERATURE, unit=SenmlUnits.SENML_UNIT_DEGREES_CELSIUS, value=23.5)
door_pos = SenmlRecord("doorPos", update_time=20, value=True)
int_val = SenmlRecord("int_val", value=10, sum=100)

pack.append(temp)
pack.append(door_pos)
pack.append(int_val)

random_time = datetime.datetime.strptime('Jan 1 2018  1:33PM', '%b %d %Y %I:%M%p')
pack.base_time = time.mktime(random_time.timetuple())                       # set a base time
pack.base_value = 5
pack.base_sum = 50
temp.time = time.mktime(datetime.datetime.now().timetuple())                             # all child objects will receive the time value



print(pack.to_json())
