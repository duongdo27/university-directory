#!/bin/bash
python manage.py test directory

export DIRECTORIES="directory"

yapf -i --recursive -e directory/migrations $DIRECTORIES && pylint $DIRECTORIES --ignore=migrations
