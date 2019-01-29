import socketio
import configuration
import time


def start_socket(callback, reconnect=True):
    socket = socketio.Client()

    def reconnect_socket():
        if reconnect:
            print("Socket connection error: Reconnecting in %d seconds" % configuration.socketReconnectionDelay)
            time.sleep(configuration.socketReconnectionDelay)
            start_socket(callback, reconnect)

    try:
        @socket.on("connect")
        def on_connect():
            callback("connected", socket)

        @socket.on(configuration.socketCommunicationChannel)
        def on_communicate(data):
            callback("message", data)

        @socket.on("disconnect")
        def on_disconnect():
            callback("disconnected", socket)
            reconnect_socket()

        socket.connect(configuration.socketHost)
        socket.wait()

        reconnect_socket()
    except Exception as exception:
        callback("error", exception)
        reconnect_socket()
