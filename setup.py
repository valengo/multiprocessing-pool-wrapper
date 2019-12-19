# always prefer setuptools over distutils
from setuptools import setup, find_packages
# to use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
name = 'mppwrapper'

long_description = "A simple wrapper for Python's multiprocessing module. Currently, it works by employing the Pool " \
                   "object. "

setup(
    name=name,

    # versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.0b1',

    description='A Python3.x package to facilitate the usage of the multiprocessing module',
    long_description=long_description,

    # the project's main homepage.
    url='https://github.com/valengo/multiprocessing-pool-wrapper',

    # author details
    author='IP4 Team',
    author_email='ip4.developers@gmail.com',

    # is this ok?
    license='MIT',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    # What does your project relate to?
    keywords='multiprocessing',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['venv']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    # py_modules=["bedhandler"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['pytest'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    # extras_require={
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    # },

    python_requires='>=3'
)