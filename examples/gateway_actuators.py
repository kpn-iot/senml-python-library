from senml_pack import SenmlPack
from senml_record import SenmlRecord

def do_actuate(record):
    '''
    called when actuate_me receives a value.
    :return: None
    '''
    print("for known device: ")
    print(record.value)

def device_callback(record, **kwargs):
    """
    a generic callback, attached to the device. Called when a record is found that has not yet been registered
    in the pack. When this callback is called, the record will already be added to the pack.
    :param kwargs: optional extra parameters
    :param record: the newly found record.
    :return: None
    """
    print("found record: " + record.name)
    print("with value: " + record.value)


def gateway_callback(record, **kwargs):
    """
    a generic callback, attached to the device. Called when a record is found that has not yet been registered
    in the pack. When this callback is called, the record will already be added to the pack.
    :param record: the newly found record.
    :param kwargs: optional extra parameters (device can be found here)
    :return: None
    """
    if 'device' in kwargs and kwargs['device'] != None:
        print("for device: " + kwargs['device'].name)
    else:
        print("for gateway: ")
    print("found record: " + record.name)
    print("with value: " + str(record.value))




gateway = SenmlPack("gateway_name", gateway_callback)
device = SenmlPack("device_name", device_callback)
actuate_me = SenmlRecord("actuator", callback=do_actuate)

gateway.append(device)
device.append(actuate_me)
gateway.from_json('[{"bn": "gateway_name", "n":"temp", "v": 22},{"n": "gateway_actuator", "vb": true}, {"bn": "device_name", "n":"actuator", "v": 20 }, {"n": "another_actuator", "vs": "a value"}, {"bn": "device_2", "n":"temp", "v": 20 }, {"n": "actuator2", "vs": "value2"}]')