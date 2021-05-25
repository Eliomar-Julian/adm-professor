#!/usr/bin/env bash

export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_DEBUG=true

flask run --host=localhost