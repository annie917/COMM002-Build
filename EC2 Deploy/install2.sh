#!/bin/bash

pip install --upgrade pip
pip install flask gunicorn
pip install wheel
cd COMM002-Build
pip install -r requirements.txt
pip install pyproj
pip install -e COMM002
