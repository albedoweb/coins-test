# coins-test

## Overview

App provides simple RESTful API for payments. App created for demo purpose.

## Installation

* `virtualenv ./env/`
* `source ./venv/bin/activate`
* `pip install -r ./requirements/development.txt`
* `python coins/manage.py migrate`

## Tests and PEP8

From project root:

* `flake8 ./coins` to run PEP8 check
* `cd ./coins; python ./manage.py test` to run tests

## Documentation

API documentation can be found in `./docs/api.generated.html`.

To rebuild docs:

```
npm install -g aglio

aglio -i docs/src/index.apib -o docs/api.generated.html --theme-variables flatly --theme-full-width
```