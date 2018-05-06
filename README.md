# Introduction

The KPN SenML library helps you create [senml documents](https://tools.ietf.org/html/draft-ietf-core-senml-13) so you
can transport and/or receive data in a uniform way to and from devices using a communication protocol of your choice.

# key features

- Object oriented design.
- built in support for [senml's unit registry](https://tools.ietf.org/html/draft-ietf-core-senml-12#section-12.1)
- extensible for new data types
- makes use of (but doesn't restrict to) KPN's predefined list of record names.
- direct support to read/write in json and cbor format.
- automatically adjusts record data with respect to base time, base value & base sum.

