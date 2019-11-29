#!/bin/bash

echo 'staring project'
cd /use/src/yuetu-api
pip install -r requirements.txt -i https://mirros.aliyun.com/pypi/simple
gunicorn -w 1 -b 0.0.0.0:5000 manage:application