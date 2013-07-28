__doc__ = """
=====================
2to6 Introduction
=====================

:Author: Limodou <limodou@gmail.com>

.. contents:: 

About 2to6
----------------

This module is used to convert python 2.6+ source code to python 3.3+ source code, and 
it'll use six for supporing two versions of python.

License
------------

This module is the modified version of 2to3, so the license is based on 2to3.

"""

from setuptools import setup

setup(name='2to6',
    version='1.0',
    description="Convertation tools for python 2.6+ to python 3.3+",
    long_description=__doc__,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
    ],
    packages = ['lib2to6', 'lib2to6.fixes', 'lib2to6.pgen2'],
    platforms = 'any',
    keywords='2to3',
    author='limodou',
    author_email='limodou@gmail.com',
    url='https://github.com/limodou/2to6',
    include_package_data=True,
    zip_safe=False,
    entry_points = {
          'console_scripts': [
              '2to6 = lib2to6.main:main',
          ],
    },
)
