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
# actuator example

from kpn_senml import *
import binascii

def do_actuate(record):
    '''
    called when actuate_me receives a value.
    :return: None
    '''
    print(record.value)

def generic_callback(record, **kwargs):
    """
    a generic callback, attached to the device. Called when a record is found that has not yet been registered
    in the pack. When this callback is called, the record will already be added to the pack.
    :param record: the newly found record.
    :return: None
    """
    print("found record: " + record.name)
    print("with value: " + str(record.value))

pack = SenmlPack("device_name", generic_callback)
actuate_me = SenmlRecord("actuator", callback=do_actuate)

pack.add(actuate_me)

json_data = '[{"bn": "device_name", "n":"actuator", "v": 10 }]'
print(json_data)
pack.from_json(json_data)

json_data = '[{"bn": "device_name", "n":"actuator", "v": 20 }, {"n": "another_actuator", "vs": "a value"}]'
print(json_data)
pack.from_json(json_data)

print('[{"bn": "device_name", "n":"temp", "v": 20, "u": "Cel" }]')
# this represents the cbor json struct: [{-2: "device_name", 0: "temp", 1: "Cel", 2: 20}]
cbor_data =  binascii.unhexlify("81A4216B6465766963655F6E616D65006474656D70016343656C0214")
pack.from_cbor(cbor_data)