import os
from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except:
    long_description = ''

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: Apache Software License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 3.7',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(
    name         = 'MPU9250',
    version      = '1.0.0',
    author       = 'Masoud',
    author_email = '',
    description  = 'Python3 driver for mpu9250 sensor',
    long_description=long_description,
    url          = 'https://github.com/masoudhassani/mpu9250_driver',
    license      = 'Apache License 2.0',
    classifiers  = classifiers,
    packages     = find_packages()
)