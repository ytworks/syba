#!/usr/bin/env python
from setuptools import setup

setup(name='syba',
      version='1.0.0',
      description='SYBA',
      url='https://github.com/lich-uct/syba',
      author='Milan Vorsilak',
      license='GPL-3.0',
      packages=['syba',],
      # package_data={'syba': ['resources/syba.csv.gz'],},
      zip_safe=False,
      include_package_data=True,
     )