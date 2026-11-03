#!/bin/bash
cd ~/Documents/flaskTest
source .venv/bin/activate
python3 app.py &
sleep 1
xdg-open http://127.0.0.1:5000 && \
wait
