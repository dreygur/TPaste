#!/usr/bin/env python

#############################################################################
#    TPaste.py - Python Pastebin App.
#    Copyright (C) 2017  ISTT_Cyborgs
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

#############################################################################


from setuptools import setup

long_desc = open('readme.rst').read()

setup(name='TPaste',
      version='1.0.0',
      py_modules=['pastebin'],
      author='Rakibul Yeasin Totul',
      author_email='rytotul@gmail.com',
      url='http://www.facebook.com/rytotul',
      license='GNU General Public License (GPL)',
      description='Python Pastebin interacted App based on Pastebin Module.',
      long_description=long_desc,
      platforms=['Windows', 'Unix', 'OS X'],
      download_url=" ",
      keywords=["pastebin", "paste", "xml", "pastebin API", "tpaste"],
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7, 3",
          "Development Status :: 1 - Beta",
          "Environment :: Other Environment",
          "Intended Audience :: Developers",
          "Intended Audience :: Education",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Topic :: Education",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      install_requires=['setuptools'],
      
      )
