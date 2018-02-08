# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="fastly-cli",
    version="0.1.0",
    description="Universal command line interface for Fastly CDN",
    license="MIT",
    url="https://github.com/mertsaygi/fastly-cli",
    author="Mert Saygı",
    author_email="mertsaygi@gmail.com",
    packages=find_packages(),
    install_requires=[
        'Click',
        'requests',
        'fastly',
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    entry_points = {
        'console_scripts': [
            'fastly-cli = fastlycli.__main__:entry_point'
        ]
    }
)
