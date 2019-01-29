import configuration
import microphone
import ambiento_socket
from _thread import start_new_thread

print("Starting Ambiento-Python-Module v%s" % configuration.version)


def microphone_callback(value):
    if configuration.current_socket is not None:
        configuration.current_socket.emit(configuration.socketCommunicationChannel, {"value": value})
        if configuration.debugMicrophoneValue:
            print("Microphone value: %d" % value)


def socket_callback(message, data):
    if message == "connected":
        print("Socket connection established")
        configuration.microphoneRunning = True
        configuration.current_socket = data
        start_new_thread(microphone.start_recording, (microphone_callback,))
    if message == "disconnected" or message == "error":
        print("Socket connection disconnected or error (%s)" % data)
        configuration.microphoneRunning = False


ambiento_socket.start_socket(socket_callback)
