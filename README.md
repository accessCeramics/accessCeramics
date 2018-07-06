# accessCeramics
[![Build Status](https://travis-ci.org/accessCeramics/accessCeramics.svg?branch=master)](https://travis-ci.org/accessCeramics/accessCeramics)
[![Coverage Status](https://codecov.io/gh/accessCeramics/accessCeramics/branch/master/graph/badge.svg)](https://codecov.io/gh/accessCeramics/accessCeramics)
[![Requirements Status](https://requires.io/github/accessCeramics/accessCeramics/requirements.svg?branch=master)](https://requires.io/github/accessCeramics/accessCeramics/requirements/?branch=master)
[![Code Health](https://landscape.io/github/accessCeramics/accessCeramics/master/landscape.svg?style=flat)](https://landscape.io/github/accessCeramics/accessCeramics/master)
[![Documentation Status](https://readthedocs.org/projects/accessceramics/badge/?version=latest)](https://accessceramics.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

[accessCeramics](http://accessceramics.org) is a growing collection of contemporary ceramics images by recognized artists enhancing ceramics education worldwide.

The current version is built using [django](), with source code hosted on [GitHub](https://github.com/accessCeramics/accessCeramics). You can also view the [code documentation](http://accessceramics.readthedocs.io/).

## Developing

This repo uses [git-flow](https://github.com/nvie/gitflow) conventions; **master**
contains the most recent release, and work in progress will be on the **develop** branch. Pull requests should be made against **develop**.

### Setup

1. Clone the repository:
```sh
$ git clone https://github.com/accessCeramics/accessCeramics.git
$ cd accessCeramics
```
2. Create and activate a python 3 virtual environment:
```sh
$ python3 -m venv venv
$ source venv/bin/activate
```
3. Install dependencies with `pip`:
```sh
(venv) $ pip install -r requirements.txt
```
4. Run migrations to prepare the database:
```sh
(venv) $ python manage.py migrate
```
5. Create a superuser account for testing:
```sh
(venv) $ python manage.py createsuperuser
```
6. Run a development server:
```sh
(venv) $ python manage.py runserver
```
The project will be served at <http://localhost:8000/> by default. You can view
the admin backend at <http://localhost:8000/admin>.

### Testing

Unit tests are written with [pytest](http://doc.pytest.org/). To run them:
1. Ensure development requirements are installed:
```sh
(venv) $ pip install -r dev-requirements.txt
```
2. Run tests using `pytest`:
```sh
(venv) $ python -m pytest
```

### Documentation
Docs are hosted by [Read the Docs](https://readthedocs.org/) and automatically 
rebuilt on a push to master.

Docs are generated using [sphinx](http://www.sphinx-doc.org/).

To build a copy of the docs locally:
1. Ensure development requirements are installed:
```sh
(venv) $ pip install -r dev-requirements.txt
```
2. Build docs using the `Makefile`:
```sh
$ cd docs
$ make html
```

### License
This project is licensed under the [Apache 2.0 License](https://github.com/accessCeramics/accessCeramics/blob/master/LICENSE).