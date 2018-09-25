#!/usr/bin/env python
# -*- coding: utf-8 -*-


import kpn_senml
import random
import json
import cbor2


def test_basic():
    pack = kpn_senml.SenmlPack("foobar")
    with kpn_senml.SenmlRecord("qux", value=random.randint(1,1000)) as record:
        pack.add(record)
        json_data = json.loads(pack.to_json())

        assert json_data[0]["bn"] == "foobar"
        assert json_data[0]["n"] == "qux"
        assert 1000 > json_data[0]["v"] > 1


def test_cbor():
    pack = kpn_senml.SenmlPack("device_name")
    with kpn_senml.SenmlRecord("test", value=random.randint(0, 1000)) as record:
            pack.add(record)
            cbor_data = cbor2.loads(pack.to_cbor())

            assert 'device_name' in cbor_data[0].values()
            assert 'test' in cbor_data[0].values()


def test_gateway():
    gateway_pack = kpn_senml.SenmlPack("gateway")
    dev1_pack = kpn_senml.SenmlPack("dev1")
    dev2_pack = kpn_senml.SenmlPack("dev2")

    temp = kpn_senml.SenmlRecord(kpn_senml.SenmlNames.KPN_SENML_TEMPERATURE, unit=kpn_senml.SenmlUnits.SENML_UNIT_DEGREES_CELSIUS, value=23.5)
    door_pos = kpn_senml.SenmlRecord("doorPos", update_time=20, value=True)
    str_val = kpn_senml.SenmlRecord("str val")
    str_val.value = "test"

    gateway_pack.add(temp)
    gateway_pack.add(dev1_pack)
    gateway_pack.add(dev2_pack)
    dev1_pack.add(door_pos)
    dev2_pack.add(str_val)

    json_data = json.loads(gateway_pack.to_json())
    assert json_data[0]["bn"] == "gateway"
