# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='lwp_mgmt',
    version=version,
    description='this app is to calculate lwp from attendance',
    author='New Indictrans Technologies pvt ltd.',
    author_email='support@indictranstech.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
