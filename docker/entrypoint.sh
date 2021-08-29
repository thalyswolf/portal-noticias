#!/bin/bash
cd /home/news \
&& export PYTHONDONTWRITEBYTECODE=1 \
&& uvicorn src.main:app --host=0.0.0.0 --port=80 --reload