#!/bin/bash

readonly ROOT_DIR=$(dirname $(readlink -f $0))
readonly DIR=venv1

mkdir $DIR

python3 -m venv $DIR/issmoexproxy

source $DIR/issmoexproxy/bin/activate

pip3 install -r requirements.txt

export PYTHONPATH=$ROOT_DIR
echo Start proxy
python3 issmoexproxy/proxy.py
