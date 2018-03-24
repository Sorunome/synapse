#!/bin/bash
python2 setup.py build
python2 setup.py install --root "/" --optimize=1 --skip-build
