from setuptools import setup

setup(
    name='kpn_senml',
    version='1.1.0',
    packages=['kpn_senml'],
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
    install_requires=[
          'cbor2==4.1.0',
    ]
)
