from distutils.core import setup
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='interactive-broker-python-web-api',

    version='0.1.2',
    description='A python client library for the Interactive Broker Web API.',

    long_description=long_description,

    long_description_content_type="text/markdown",

    install_requires=[
        'certifi>=2019.11.28',
        'requests>=2.22.0',
        'urllib3>=1.25.3'
    ],

    packages=find_packages(include=['ibw']),

    python_requires='>3.7'
)

