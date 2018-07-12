#!/bin/bash

pip install -r requirements.txt
git clone https://github.com/jswhit/pyproj.git
cd pyproj
python setup.py build
python setup.py install
cd ..
pip install -e COMM002
export FLASK_APP=wisley
flask run
