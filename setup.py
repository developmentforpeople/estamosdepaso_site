# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in estamosdepaso_site/__init__.py
from estamosdepaso_site import __version__ as version

setup(
	name='estamosdepaso_site',
	version=version,
	description='EstamosDePaso Site',
	author='DFP',
	author_email='developmentforpeople@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
