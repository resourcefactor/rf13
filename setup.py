# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in rf13/__init__.py
from rf13 import __version__ as version

setup(
	name='rf13',
	version=version,
	description='Redesign Login Page',
	author='RF',
	author_email='sales@resourcefactors.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
