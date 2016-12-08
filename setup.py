# -*- coding: utf-8 -*-

#!/usr/bin/env python


from distutils.core import setup

import montefevents

NAME = 'montefevents'
VERSION = montefevents.__version__
AUTHOR = "Jean-Michel Begon"
AUTHOR_EMAIL = "jm.begon@gmail.com"
URL = 'https://github.com/jm-begon/montef-events'
DESCRIPTION = "Toolkit to provide automatic (email) notification of the Montefiore unit's seminars"
with open('README.md') as f:
    LONG_DESCRIPTION = f.read()
CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Education',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Utilities',
]

if __name__ == '__main__':
    from clustertools.config import dump_config
    dump_config()
    setup(name=NAME,
          version=VERSION,
          author=AUTHOR,
          author_email=AUTHOR_EMAIL,
          url=URL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license='BSD3',
          classifiers=CLASSIFIERS,
          platforms='any',
          install_requires=["bs4"],
          packages=['montefevents', 'montefevents.test'],
          scripts=['bin/montefevents'])
