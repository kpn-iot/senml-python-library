from senml_pack import SenmlPack
from senml_record import SenmlRecord
from senml_unit import SenmlUnits

import datetime
import time


class Coordinates(SenmlRecord):

    def __init__(self, name, **kwargs):
        '''overriding the init function so we can initiate the 3 senml records that will represent lat,lon, alt'''
        self._lat = SenmlRecord("lat", unit=SenmlUnits.SENML_UNIT_DEGREES_LATITUDE)     # create these befor calling base constructor so that all can be init correctly from constructor
        self._lon = SenmlRecord("lon", unit=SenmlUnits.SENML_UNIT_DEGREES_LONGITUDE)
        self._alt = SenmlRecord("alt", unit=SenmlUnits.SENML_UNIT_METER)
        super(Coordinates, self).__init__(name, **kwargs)                                 # need to call base init, to make certain all is ok.


    def _check_value_type(self, value):
        '''overriding the check on value type to make certain that only an array with 3 values is assigned: lat,lon/alt'''
        if (not value == None):
            if not isinstance(value, list):
                raise Exception("invalid data type: array with 3 elements expected lat, lon, alt")

    def _build_rec_dict(self, naming_map, appendTo):
        '''
        override the rendering of the senml data objects. These will be converted to json or cbor
        :param naming_map: {dictionary} a map that determines the field names, these are different for json vs cbor
        :param appendTo: {list} the result list
        :return: None
        '''
        self._lat._build_rec_dict(naming_map, appendTo)
        self._lon._build_rec_dict(naming_map, appendTo)
        self._alt._build_rec_dict(naming_map, appendTo)

    @SenmlRecord.value.setter
    def value(self, value):
        '''set the current value.
        this is overridden so we can pass on the values to the internal objects. It's also stored in the parent
        so that a 'get-value' still returns the array.
        '''
        SenmlRecord.value.fset(self, value)                     # do this first, it will check the data type
        if value:
            self._lat.value = value[0]
            self._lon.value = value[1]
            self._alt.value = value[2]
        else:
            self._lat.value = None
            self._lon.value = None
            self._alt.value = None

    @SenmlRecord.time.setter
    def time(self, value):
        '''set the time stamp.
        this is overridden so we can pass on the values to the internal objects.
        '''
        SenmlRecord.time.fset(self, value)  # do this first, it will check the data type
        self._lat.time = value
        self._lon.time = value
        self._alt.time = value

    @SenmlRecord.update_time.setter
    def update_time(self, value):
        '''set the time stamp.
        this is overridden so we can pass on the values to the internal objects.
        '''
        SenmlRecord.update_time.fset(self, value)  # do this first, it will check the data type
        self._lat.update_time = value
        self._lon.update_time = value
        self._alt.update_time = value

    @SenmlRecord._parent.setter
    def _parent(self, value):
        '''set the time stamp.
        this is overridden so we can pass on the values to the internal objects.
        This is needed so that the child objects can correctly take base time (optionally also base-sum, base-value) into account
        '''
        SenmlRecord._parent.fset(self, value)  # do this first, it will check the data type
        self._lat._parent = value
        self._lon._parent = value
        self._alt._parent = value



pack = SenmlPack("device_name")
loc = Coordinates("location")
loc2 = Coordinates("location", value=[52.0259, 5.4775, 230])
pack.append(loc)
pack.append(loc2)

loc.value = [51.0259, 4.4775, 10]
print(pack.to_json())

random_time = datetime.datetime.strptime('Jan 1 2018  1:33PM', '%b %d %Y %I:%M%p')
pack.base_time = time.mktime(random_time.timetuple())                       # set a base time
loc.time = time.mktime(datetime.datetime.now().timetuple())                             # all child objects will receive the time value
print(pack.to_json())

