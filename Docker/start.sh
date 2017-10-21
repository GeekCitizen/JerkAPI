#!/bin/bash

function start_JerkAPI {
  cd /opt/JerkAPI/app
  source JerkAPIenv/bin/activate
  uwsgi --ini JerkAPI.ini
}

function start_nginx {
  nginx -g "daemon off;"
}

start_JerkAPI &
start_nginx
