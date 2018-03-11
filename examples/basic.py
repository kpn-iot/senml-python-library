from senml_pack import SenmlPack
from senml_record import SenmlRecord
import time
import random

pack = SenmlPack("device_name")

while True:
    with SenmlRecord("test", value=random.randint(0,1000)) as rec:           # use a with statement to automatically remove the item from the list when it goes out of scope, generate a value for the record
        pack.append(rec)
        print(pack.to_json())
    time.sleep(1)
