# accessCeramics
[![Build Status](https://travis-ci.org/accessCeramics/accessCeramics.svg?branch=master)](https://travis-ci.org/accessCeramics/accessCeramics)
[![Coverage Status](https://codecov.io/gh/accessCeramics/accessCeramics/branch/master/graph/badge.svg)](https://codecov.io/gh/accessCeramics/accessCeramics)
[![Requirements Status](https://requires.io/github/accessCeramics/accessCeramics/requirements.svg?branch=master)](https://requires.io/github/accessCeramics/accessCeramics/requirements/?branch=master)
[![Code Health](https://landscape.io/github/accessCeramics/accessCeramics/master/landscape.svg?style=flat)](https://landscape.io/github/accessCeramics/accessCeramics/master)

[accessCeramics](accessceramics.org) is a growing collection of contemporary ceramics images by recognized artists enhancing ceramics education worldwide.

The current version is built using [django](), with source code hosted on [GitHub](github.com/accessCeramics/accessCeramics). You can also view the [code documentation](accessceramics.github.io/accessceramics).

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
5. Run a development server:
```sh
(venv) $ python manage.py runserver
```
The project will be served at <http://localhost:8000/> by default.

### Testing

Unit tests are written with [pytest](http://doc.pytest.org/) but use
Django fixture loading and convenience testing methods when that makes
things easier. To run them:
1. Ensure development requirements are installed:
```sh
(venv) $ pip install -r dev-requirements.txt
```
2. Run tests using `pytest`:
```sh
(venv) $ pytest
```

### Documentation
Documentation is generated using [sphinx](http://www.sphinx-doc.org/).
To generate documentation:
1. Ensure development requirements are installed:
```sh
(venv) $ pip install -r dev-requirements.txt
```
2. Build documentation using the `Makefile`:
```sh
$ make docs
```
Documentation source files are in the `docs-src` folder. Built documentation
lives in the `docs` folder on master to be served via GitHub pages.

### License
This project is licensed under the [Apache 2.0 License](https://github.com/accessCeramics/accessCeramics/blob/master/LICENSE).