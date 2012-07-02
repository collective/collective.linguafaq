# -*- coding: utf-8 -*-
"""
This module contains the tool of collective.linguafaq
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.5'

long_description = (
    read('README.txt')
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    read('collective', 'linguafaq', 'README.txt')
    + '\n' +
    read('CONTRIBUTORS.txt')
    )


setup(name='collective.linguafaq',
      version=version,
      description="A simple multilanguage faq",
      long_description=long_description,
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        'Framework :: Plone',
        # "Framework :: Plone :: 3.3",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone faq',
      author='Benoit Suttor - CIRB/CIBG',
      author_email='bsuttor@cirb.irisnet.be',
      url='http://www.cirb.irisnet.be',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        ],
      extras_require={
        'test': ['plone.app.testing'],
        },
      entry_points="""
      # -*- entry_points -*-
      [distutils.setup_keywords]
      paster_plugins = setuptools.dist:assert_string_list

      [egg_info.writers]
      paster_plugins.txt = setuptools.command.egg_info:write_arg

      [z3c.autoinclude.plugin]
      target = plone
      """,
      paster_plugins=["ZopeSkel"],
      )
