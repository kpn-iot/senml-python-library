from senml_pack import SenmlPack
from senml_record import SenmlRecord
from senml_unit import SenmlUnits
from senml_kpn_names import SenmlNames
import time

gateway_pack = SenmlPack("gateway")

dev1_pack = SenmlPack("dev1")
dev2_pack = SenmlPack("dev2")

temp = SenmlRecord(SenmlNames.KPN_SENML_TEMPERATURE, unit=SenmlUnits.SENML_UNIT_DEGREES_CELSIUS, value=23.5)
door_pos = SenmlRecord("doorPos", update_time=20, value=True)
str_val = SenmlRecord("str val")

gateway_pack.append(temp)
gateway_pack.append(dev1_pack)
gateway_pack.append(dev2_pack)
dev1_pack.append(door_pos)
dev2_pack.append(str_val)

while True:
    temp.value = temp.value + 1.1
    door_pos.value = not door_pos.value
    str_val.value = "test"
    print(gateway_pack.to_json())
    time.sleep(1)
