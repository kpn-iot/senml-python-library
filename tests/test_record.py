#!/usr/bin/env python
# -*- coding: utf-8 -*-


import kpn_senml
import random
import json


def test_basic():
    pack = kpn_senml.SenmlPack("foobar")
    with kpn_senml.SenmlRecord("qux", value=random.randint(1,1000)) as record:
        pack.add(record)
        json_data = json.loads(pack.to_json())

        assert json_data[0]["bn"] == "foobar"
        assert json_data[0]["n"] == "qux"
        assert 1000 > json_data[0]["v"] > 1
