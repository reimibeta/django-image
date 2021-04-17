#!/usr/bin/env python


import os

# allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

import setuptools

setuptools.setup(
    name='image_utils',
    version='1.0.2',
    packages=setuptools.find_packages()
)
