#!/usr/bin/env python
#
# Setup prog for bigpandamon-htcondor
#
#
from htcondor import __version__

import os
import re
import sys
from distutils.core import setup

setup(
    name = 'bigpandamon-htcondor',
    version = __version__,
    description = 'BigPanDA Monitoring Package - HTCondorjob',
    long_description = '''This package contains BigPanDA Monitoring Components - HTCondorjob''',
    license = 'GPL',
    author = 'Panda Team',
    author_email = 'hn-atlas-panda-pathena@cern.ch',
    url = 'https://twiki.cern.ch/twiki/bin/view/PanDA/BigPanDAmonitoring',
    packages = [ 
        'htcondor',
        'htcondor.api',
    ],
    py_modules = ['manage'],
    data_files = [
        ('etc/', ['requirements.txt',
            ]
    ),
        ('doc/', ['README.md',
            ]
    ),
    ],
)
