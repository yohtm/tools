from webapp import webserver

if __name__ == '__main__':
    print "Running app"


    # To enable a simple server with websockets, use socketIO. There are changes to do here
    # and a few more in webserver.py. Also please install eventlet
    # Doc here: https://flask-socketio.readthedocs.io/en/latest/
    # webserver.socketio.run(webserver.app, host="0.0.0.0")

    # Comment this line for websocket, only the socketio.run is required.
    webserver.app.run(host="0.0.0.0")
