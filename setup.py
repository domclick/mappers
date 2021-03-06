import os
import itertools
from distutils.command.upload import upload as upload_orig

from setuptools import setup, find_packages

tests_requirements = [
    'pytest'
]

setup(
    name='mappers',
    version='1.0.0',
    description="""Abstracting complex multilevel dict data""",
    author='Vsevolod Glumov, Michael Vostrykh',
    author_email='seva17@gmail.com, MAVostrykh@domclick.ru',
    url='',
    packages=find_packages(exclude=('tests', )),
    dependency_links=[],
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Operating System :: MacOS',
      'Operating System :: POSIX :: Linux',
      'Topic :: System :: Software Distribution',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
    ],
    tests_require=tests_requirements
)
