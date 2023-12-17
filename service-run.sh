#!/usr/bin/env bash
set -e
source "/home/max/locust/.venv/bin/activate"
cd /home/max/locust/
locust --host https://www.observeshop.com --users 40 --autostart
