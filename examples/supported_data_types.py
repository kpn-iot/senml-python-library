from senml_pack import SenmlPack
from senml_record import SenmlRecord
import cbor2

pack = SenmlPack("device_name")

double_val = SenmlRecord("double", value=23.5)
int_val = SenmlRecord("int", value=23)
bool_val = SenmlRecord("bool", value=True)
str_val = SenmlRecord("str val", value="test")
bytes_val = SenmlRecord("bytes", value=bytearray.fromhex(u'00 1e 05 ff'))

#invalid value
try:
    invalid = SenmlRecord("invalid", value={'a': 1})
except Exception as error:
    print(error)


pack.append(double_val)
pack.append(int_val)
pack.append(bool_val)
pack.append(str_val)
pack.append(bytes_val)

print(pack.to_json())
cbor_val = pack.to_cbor()
print(cbor_val)
print(cbor2.loads(cbor_val))