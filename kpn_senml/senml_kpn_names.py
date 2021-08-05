# _  __  ____    _   _
# | |/ / |  _ \  | \ | |
# | ' /  | |_) | |  \| |
# | . \  |  __/  | |\  |
# |_|\_\ |_|     |_| \_|
#
# (c) 2018 KPN
# License: MIT license.
# Author: Jan Bogaerts
#
# sensor names

from kpn_senml.senml_unit import enum


SenmlNames = enum(KPN_SENML_PRESSURE="pressure",
                KPN_SENML_ANGLE="angle",
                KPN_SENML_LENGHT="length",
                KPN_SENML_LENGTH="length",
                KPN_SENML_BREADTH="breadth",
                KPN_SENML_HEIGHT="height",
                KPN_SENML_WEIGHT="weight",
                KPN_SENML_THICKNESS="thickness",
                KPN_SENML_DISTANCE="distance",
                KPN_SENML_AREA="area",
                KPN_SENML_VOLUME="volume",
                KPN_SENML_VELOCITY="velocity",
                KPN_SENML_ELECTRICCURRENT="electricCurrent",
                KPN_SENML_ELECTRIC_CURRENT="electricCurrent",
                KPN_SENML_ELECTRICPOTENTIAL="electricPotential",
                KPN_SENML_ELECTRIC_POTENTIAL="electricPotential",
                KPN_SENML_ELECTRICRESISTANCE="electricResistance",
                KPN_SENML_ELECTRIC_RESISTANCE="electricResistance",
                KPN_SENML_TEMPERATURE="temperature",
                KPN_SENML_ILLUMINANCE="illuminance",
                KPN_SENML_ALTITUDE="altitude",
                KPN_SENML_ACCELERATIONX="accelerationX",
                KPN_SENML_ACCELERATION_X="accelerationX",
                KPN_SENML_ACCELERATIONY="accelerationY",
                KPN_SENML_ACCELERATION_Y="accelerationY",
                KPN_SENML_ACCELERATIONZ="accelerationZ",
                KPN_SENML_ACCELERATION_Z="accelerationZ",
                KPN_SENML_HEADING="heading",
                KPN_SENML_LONGITUDE="longitude",
                KPN_SENML_LATTITUDE="latitude",
                KPN_SENML_LATITUDE="latitude",
                KPN_SENML_CARBONMONOXIDE="carbonMonoxide",
                KPN_SENML_CARBONDIOXIDE="carbonDioxide",
                KPN_SENML_SOUND="sound",
                KPN_SENML_FREQUENCY="frequency",
                KPN_SENML_BATTERYLEVEL="batteryLevel",
                KPN_SENML_BATTERY_LEVEL="batteryLevel",
                KPN_SENML_BATTERY_VOLTAGE="batteryVoltage",
                KPN_SENML_BATTERY_LEVEL_LOW="batteryLevelLow",
                KPN_SENML_HUMIDITY="humidity",
                KPN_SENML_POWER="power",
                KPN_SENML_CO_CONCENTRATION="COConcentration",
                KPN_SENML_CO2_CONCENTRATION="CO2Concentration",
                KPN_SENML_RADIUS="radius",
                KPN_SENML_COMPASS_X="compassX",
                KPN_SENML_COMPASS_Y="compassY",
                KPN_SENML_COMPASS_Z="compassZ",
                KPN_SENML_READ_SWITCH="readSwitch",
                KPN_SENML_PRESENCE="presence",
                KPN_SENML_COUNTER="counter",
                KPN_SENML_URL="url",
                KPN_SENML_TOKEN="token",
                KPN_SENML_FIRMWARE="firmware"
)