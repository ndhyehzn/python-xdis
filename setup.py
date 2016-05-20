#!/usr/bin/env python

"""Setup script for the 'pyxdis' distribution."""

from __pkginfo__ import \
    author,           author_email,       \
    license,          long_description,   classifiers,               \
    entry_points,     modname,            py_modules,                \
    short_desc,       VERSION,            web,                       \
    zip_safe

from setuptools import setup, find_packages
setup(
       author             = author,
       author_email       = author_email,
       classifiers        = classifiers,
       description        = short_desc,
       entry_points       = entry_points,
       license            = license,
       long_description   = long_description,
       name               = modname,
       packages           = find_packages(),
       py_modules         = py_modules,
       test_suite         = 'nose.collector',
       url                = web,
       setup_requires     = ['nose>=1.0'],
       version            = VERSION,
       zip_safe           = zip_safe)
