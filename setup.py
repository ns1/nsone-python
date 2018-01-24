from setuptools import setup, find_packages

from codecs import open
from os import path

cwd = path.abspath(path.dirname(__file__))

with open(path.join(cwd, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nsone',
    version='0.9.100',
    description='Legacy Python SDK for the NS1 DNS platform',
    long_description=long_description,
    license='MIT',
    install_requires=['ns1-python'],

    author='NS1 Developers',
    author_email='devteam@ns1.com',
    url='https://github.com/ns1/nsone-python',

    packages=find_packages(exclude=['tests']),
    test_suite='tests',
)
