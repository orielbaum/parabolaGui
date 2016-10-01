#!/usr/bin/python
from setuptools import setup

setup(
	name = "ParabolaGui",
	description = "A gui interfase for drawing parabolas",
	packages=['ParabolaGui'],
	install_requires = [
		'matplotlib',
		'wxPython'
		]
	)
