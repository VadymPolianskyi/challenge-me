import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name='challenge-me',
    version='1.0',
    packages=find_packages(),
    url='',
    license='',
    author='Vadym Polianskyi',
    author_email='vadym.polyanski@gmail.com',
    description='',
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    include_package_data=True
)
