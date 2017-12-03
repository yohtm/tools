#!/usr/bin/env python
# -*- coding: utf-8 -*-

# all the imports
import os, sys
import socket
import logging as log
import json
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask import redirect, url_for, render_template

app = Flask(__name__)

# Uncomment for websockets
# from flask_socketio import SocketIO
# from flask_socketio import send, emit
# from flask_socketio import SocketIO

# socketio = SocketIO(app)
#######

#if local
if socket.gethostname() == "":
    app.debug = True
else:
    app.debug = True

app.config["PROPAGATE_EXCEPTIONS"] = False

reload(sys)
sys.setdefaultencoding("utf-8")

# configuration
app.logger.setLevel(log.INFO)

class LoggerWriter:
    def __init__(self, level):
        self.level = level

    def write(self, message):
        if message != '\n':
            self.level(message)

    def flush(self):
        pass

def setup_logging(filename):
    formatter = log.Formatter('%(asctime)s %(levelname)s: %(message)s')
    root_logger = log.getLogger()
    root_logger.setLevel(log.INFO)

    file_handler = RotatingFileHandler(filename, maxBytes=5 * 1024 * 1024, backupCount=2)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(log.INFO)
    root_logger.addHandler(file_handler)

    console_handler = log.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(log.INFO)
    root_logger.addHandler(console_handler)

    #log.getLogger("requests").setLevel(log.WARNING)

    sys.stdout = LoggerWriter(root_logger.info)
    #sys.stderr = LoggerWriter(root_logger.error)

setup_logging("webserver.log")

@app.before_request
def before_request():
    pass

@app.teardown_request
def teardown_request(exception):
    pass

@app.route("/")
def home():
    log.info("home")
    return render_template('home.html')

@app.route("/socket_test")
def socket_test():
    log.info("socket_test")
    return render_template('socket_test.html')

# Uncomment for websocket
# @socketio.on('msg_in')
# def handle_message(data_dict):
#     log.info('received message: {}'.format(data_dict["data"]))
#     socketio.emit("msg_out", "Hello ")
#     socketio.sleep(2)
#     socketio.emit("msg_out", "world!")
#     socketio.sleep(2)
