accessCeramics
==============

django web application for `accessCeramics <http://accessceramics.org/>`_.

Code and architecture documentation for the current release available
at `<https://accessCeramics.github.io/accessCeramics/>`_.

.. image:: https://travis-ci.org/accessCeramics/accessCeramics.svg?branch=master
   :target: https://travis-ci.org/accessCeramics/accessCeramics
   :alt: Build status

.. image:: https://landscape.io/github/accessCeramics/accessCeramics/master/landscape.svg?style=flat
   :target: https://landscape.io/github/accessCeramics/accessCeramics/master
   :alt: Code Health

.. image:: https://codecov.io/gh/accessCeramics/accessCeramics/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/accessCeramics/accessCeramics
   :alt: Code coverage

.. image:: https://requires.io/github/accessCeramics/accessCeramics/requirements.svg?branch=master
   :target: https://requires.io/github/accessCeramics/accessCeramics/requirements/?branch=master
   :alt: Requirements Status

This repo uses `git-flow <https://github.com/nvie/gitflow>`_ conventions; **master**
contains the most recent release, and work in progress will be on the **develop** branch.
Pull requests should be made against **develop**.


Development instructions
------------------------

Initial setup and installation:

- **recommended:** create and activate a python 3 virtualenv::

     python3 -m venv venv
     source venv/bin/activate

- Use pip to install required python dependencies::

    pip install -r requirements.txt

- Create a database, configure in settings, and run migrations::

    python manage.py migrate


Unit Tests
~~~~~~~~~~

Unit tests are written with `pytest <http://doc.pytest.org/>`_ but use
Django fixture loading and convenience testing methods when that makes
things easier. To run them, first install development requirements::

    pip install -r dev-requirements.txt

Run tests using py.test::

    pytest


Documentation
-------------

Documentation is generated using `sphinx <http://www.sphinx-doc.org/>`__
To generate documentation, first install development requirements::

    pip install -r dev-requirements.txt

Then build documentation using the Makefile::

    make html

Documentation source files are in the `docs-src` folder. Built documentation
lives in the `docs` folder on master to be served via GitHub pages.

License
-------
This project is licensed under the `Apache 2.0 License <https://github.com/accessCeramics/accessCeramics/blob/master/LICENSE>`_.
