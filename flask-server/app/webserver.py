#!/usr/bin/env python
# -*- coding: utf-8 -*-

# all the imports
from flask import Flask

import os, sys
import socket
import logging
from logging.handlers import RotatingFileHandler

from flask import redirect, url_for, render_template

app = Flask(__name__)

#if local
if socket.gethostname() == "":
    app.debug = True
else:
    app.debug = False

app.config["PROPAGATE_EXCEPTIONS"] = False

reload(sys)
sys.setdefaultencoding("utf-8")

# configuration
app.logger.setLevel(logging.INFO)

def setup_logging():
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    file_handler = RotatingFileHandler("flas-app.log", maxBytes=10*1024*1024, backupCount=10)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    root_logger.addHandler(console_handler)

def log(data):
    logging.info(data)

@app.before_request
def before_request():
    pass

@app.teardown_request
def teardown_request(exception):
    pass

@app.route('/')
def home():
    log("home")
    return render_template('home.html')
