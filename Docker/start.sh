#!/bin/bash

function start_JerkAPI {
  cd /opt/JerkAPI/Backend
  python Main.py
}

function start_JerkAPI_listener {
  cd /opt/JerkAPI/app
  source JerkAPIenv/bin/activate
  uwsgi --ini JerkAPI.ini
}

function start_nginx {
  nginx -g "daemon off;"
}

# Test env variable
# Env: LOGLEVEL

start_JerkAPI &
start_JerkAPI_listener &
start_nginx
