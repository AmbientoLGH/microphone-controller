import pyaudio
import configuration
import numpy as np

CHUNK = 2 ** 11
RATE = 44100


def handle_data(part):
    level = int(part / (20-configuration.microphoneSensitivity)) - configuration.noiseFilter
    if level < 6:
        level = 0
    if level > configuration.maxInput:
        level = configuration.maxInput
    return level


def start_recording(callback):
    print("Starting microphone listener")
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    stream.start_stream()

    print("Microphone listener started")

    while configuration.microphoneRunning:
        data = np.fromstring(stream.read(CHUNK, exception_on_overflow=False), dtype=np.int16)
        abs_data = np.abs(data)
        items = []
        for x in range(configuration.inputRange):
            items.append(handle_data(abs_data[x]))
        callback(int(np.average(items)))

    stream.stop_stream()
    stream.close()
    p.terminate()

    print("Microphone listener stopped")
