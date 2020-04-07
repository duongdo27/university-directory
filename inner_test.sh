#!/bin/bash
export DIRECTORIES="directory"

yapf -i --recursive -e directory/migrations $DIRECTORIES && pylint $DIRECTORIES --ignore=migrations
