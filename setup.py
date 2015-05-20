#!/usr/bin/env python

import os
import sys
from setuptools import setup

if "install" in sys.argv: # If we are running python setup.py install
    sys.stdout.write("""

We are installing IRIS. Please wait...    
            
""")

# Do all apt-get stuff here

# End apt-get stuff

readme = open('README.rst', 'r') # Put all README.rst into a variable for metadata
README_TEXT = readme.read()
readme.close()

setup( # Meta-data for setuptools
    name = "iris-core",
    version = "0.0.1",
    author = "Jonathan Wheeler",
    author_email = "jonathan.m.wheeler@gmail.com",
    description = ("Core software framework necessary to tranform an RPi into "
                                   "IRIS, an intelligent personal assistant."),
    license = "GNU General Public Lisence",
    keywords = "rpi iris intelligent personal assistant",
    url = "http://github.com/iris-online",
    packages = [], # empty for now, see https://docs.python.org/2/distutils/setupscript.html#
    long_description= README_TEXT,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
)
