#!/bin/bash

set -e

cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

VENV=".venv"
REQUIREMENTS="requirements.txt"

if [ ! -d ${VENV} ]; then
    virtualenv ${VENV}
fi

source ${VENV}/bin/activate
pip install -r $REQUIREMENTS
py.test
