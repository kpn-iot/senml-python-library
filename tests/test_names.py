#!/usr/bin/env python
# -*- coding: utf-8 -*-


import kpn_senml


def test_enums():
    assert kpn_senml.SenmlNames.KPN_SENML_PRESSURE == "pressure"
    assert kpn_senml.SenmlNames.KPN_SENML_ANGLE == "angle"
    assert kpn_senml.SenmlNames.KPN_SENML_LENGHT == "lenght"
    assert kpn_senml.SenmlNames.KPN_SENML_BREADTH == "breadth"
    assert kpn_senml.SenmlNames.KPN_SENML_HEIGHT == "height"
    assert kpn_senml.SenmlNames.KPN_SENML_WEIGHT == "weight"
    assert kpn_senml.SenmlNames.KPN_SENML_THICKNESS == "thickness"
    assert kpn_senml.SenmlNames.KPN_SENML_DISTANCE == "distance"
    assert kpn_senml.SenmlNames.KPN_SENML_AREA == "area"
    assert kpn_senml.SenmlNames.KPN_SENML_VOLUME == "volume"
    assert kpn_senml.SenmlNames.KPN_SENML_VELOCITY == "velocity"
    assert kpn_senml.SenmlNames.KPN_SENML_ELECTRICCURRENT == "electricCurrent"
    assert kpn_senml.SenmlNames.KPN_SENML_ELECTRICPOTENTIAL == "electricPotential"
    assert kpn_senml.SenmlNames.KPN_SENML_ELECTRICRESISTANCE == "electricResistance"
    assert kpn_senml.SenmlNames.KPN_SENML_TEMPERATURE == "temperature"
    assert kpn_senml.SenmlNames.KPN_SENML_ILLUMINANCE == "illuminance"
    assert kpn_senml.SenmlNames.KPN_SENML_ALTITUDE == "altitude"
    assert kpn_senml.SenmlNames.KPN_SENML_ACCELERATIONX == "accelerationX"
    assert kpn_senml.SenmlNames.KPN_SENML_ACCELERATIONY == "accelerationY"
    assert kpn_senml.SenmlNames.KPN_SENML_ACCELERATIONZ == "accelerationZ"
    assert kpn_senml.SenmlNames.KPN_SENML_HEADING == "heading"
    assert kpn_senml.SenmlNames.KPN_SENML_LONGITUDE == "longitude"
    assert kpn_senml.SenmlNames.KPN_SENML_LATTITUDE == "lattitude"
    assert kpn_senml.SenmlNames.KPN_SENML_CARBONMONOXIDE == "carbonMonoxide"
    assert kpn_senml.SenmlNames.KPN_SENML_CARBONDIOXIDE == "carbonDioxide"
    assert kpn_senml.SenmlNames.KPN_SENML_SOUND == "sound"
    assert kpn_senml.SenmlNames.KPN_SENML_FREQUENCY == "frequency"
    assert kpn_senml.SenmlNames.KPN_SENML_BATTERYLEVEL == "batteryLevel"
    assert kpn_senml.SenmlNames.KPN_SENML_HUMIDITY == "humidity"
