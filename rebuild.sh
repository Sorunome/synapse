#!/bin/bash
pypy setup.py build
pypy setup.py install --root "/" --optimize=1 --skip-build
