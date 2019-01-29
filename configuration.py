version = 1.0
socketHost = "http://localhost:3000"  # Host of socket io NodeJS server
microphoneSensitivity = 0  # Sensitivity between 0 and 20
noiseFilter = 6  # Noise filter to reduce sough
maxInput = 1000  # Maximum input for audio
inputRange = 1500  # Range of analyzing input data
socketCommunicationChannel = "ambiento"  # Input channel for socket message flow
socketReconnectionDelay = 1  # Reconnection delay on disconnection or error in seconds
debugMicrophoneValue = True  # Print microphone value while socket is connected

# Instance values
microphoneRunning = True
current_socket = None
