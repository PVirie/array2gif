#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


long_description = open('README.rst').read()
packages = ['array2gif']


setup(
    name="array2gif",
    version="1.0",
    description='Write a (list of) NumPy array(s) to an (animated) GIF.',
    long_description=long_description,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering :: Visualization'
    ),
    keywords='array2gif animated gif encoder numpy rgb',
    author="Tanya Schlusser",
    maintainer='Tanya Schlusser',
    url='https://github.com/PVirie/array2gif',
    license='BSD',
    packages=packages,
    install_requires=[
        'numpy'
    ]
)
