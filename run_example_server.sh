#!/bin/bash
. devenv/bin/activate
examples_path="$(pwd)/examples"
export PYTHONPATH=$examples_path
export DJANGO_SETTINGS_MODULE=examples.settings
django-admin migrate
django-admin runserver "$@"
