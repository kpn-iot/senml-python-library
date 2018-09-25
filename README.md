# KPN SenML

#### Introduction

The KPN SenML library helps you create and parse [senml documents](https://tools.ietf.org/html/draft-ietf-core-senml-13)
in both json and cbor format.

#### Key Features

- Object oriented design.
- built in support for [senml's unit registry](https://tools.ietf.org/html/draft-ietf-core-senml-12#section-12.1)
- extensible for new data types
- makes use of (but doesn't restrict to) KPN's predefined list of record names.
- direct support to read/write in json and cbor format.
- automatically adjusts record data with respect to base time, base value & base sum.
- for python 2.7 and 3.5 (geared towards embedded systems)

#### Testing

To execute all unit tests:

    $ pip install -r requirements_test.txt
    $ cd tests
    $ pytest . -v --cov=kpn_senml --cov-report=html

Please visit our [docs site](https://kpn-iot.github.io/senml-python-library) for more info.

#### LICENSE
[MIT](LICENSE)

