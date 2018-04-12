from senml_pack import SenmlPack
from senml_record import SenmlRecord

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
    print("with value: " + record.value)

pack = SenmlPack("device_name", generic_callback)
actuate_me = SenmlRecord("actuator", callback=do_actuate)

pack.append(actuate_me)
pack.from_json('[{"bn": "device_name", "n":"actuator", "v": 10 }]')
pack.from_json('[{"bn": "device_name", "n":"actuator", "v": 20 }, {"n": "another_actuator", "vs": "a value"}]')