from senml_pack import SenmlPack
from senml_record import SenmlRecord
from senml_unit import SenmlUnits
import time

pack = SenmlPack("device_name")
temp = SenmlRecord("temp", unit=SenmlUnits.SENML_UNIT_DEGREES_CELSIUS, value=23.5)
door_pos = SenmlRecord("doorPos", update_time=20, value=True)
str_val = SenmlRecord("str val")

pack.append(temp)
pack.append(door_pos)
pack.append(str_val)

while True:
    temp.value = temp.value + 1.1
    door_pos.value = not door_pos.value
    str_val.value = "test"
    print(pack.to_json())
    time.sleep(1)
