from setuptools import setup

setup(
    name='kpn_senml',
    version='1.0',
    packages=['kpn_senml'],
    url='',
    license='MIT',
    author='Jan Bogaerts',
    author_email='jb@elastetic.com',
    description='generate and parse senml json and cbor data',
    install_requires=[
          'cbor2',
    ]
)
