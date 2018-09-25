#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


def get_requires(filename):
    requirements = []
    with open(filename) as req_file:
        for line in req_file.read().splitlines():
            if not line.strip().startswith("#"):
                requirements.append(line)
    return requirements


setup(
    name='kpn_senml',
    version='1.1.0',
    packages=find_packages(exclude=['tests']),
    url='https://kpn-iot.github.io/senml-python-library/',
    license='MIT',
    author='Jan Bogaerts',
    author_email='jb@elastetic.com',
    description='generate and parse senml json and cbor data',
    long_description='With this library you can generate senml packs containing sensor data in both json and cbor format.  It can also parse senml data in both json and cbor format in order to support actuators.',
    classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Embedded Systems',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Operating System :: OS Independent',
    ],
    keywords='senml kpn cbor json',
    install_requires=get_requires('requirements.txt'),
    extras_require={'test': get_requires('requirements_test.txt')},
)
