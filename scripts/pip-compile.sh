#!/bin/bash

# A script for runing pip-compile for prod, test and dev requirements

pip-compile requirements/production.in
pip-compile requirements/testing.in
pip-compile requirements/development.in