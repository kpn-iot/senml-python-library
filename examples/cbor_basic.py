from kpn_senml import *
import time
import random
import cbor2

pack = SenmlPack("device_name")

while True:
    with SenmlRecord("test", value=random.randint(0,1000)) as rec:           # use a with statement to automatically remove the item from the list when it goes out of scope, generate a value for the record
        pack.add(rec)
        cbor_val = pack.to_cbor()
        print(cbor_val)
        print(cbor2.loads(cbor_val))                                          # convert to string again so we can print it.
    time.sleep(1)
