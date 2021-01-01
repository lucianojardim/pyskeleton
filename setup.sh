#!/usr/bin/env bash

# Install virtual environment and run make

echo 'python3 -m venv .venv'
python3 -m venv .venv

echo 'source .venv/bin/activate'
source .venv/bin/activate

echo 'copy pip.conf to virtual environment'
cp -vf pip.conf .venv/pip.conf

echo 'make setup'
make setup
