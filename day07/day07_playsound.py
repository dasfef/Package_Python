'''
날짜: 2023.07.28
작성자: 최연웅
목표: 웹캠의 마이크를 활용해 녹음 후 재생
'''
import pyaudio
import wave
from playsound import playsound
import keyboard

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = r"output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("음성녹음을 시작합니다.")

frames = []

while True:
    
    data=stream.read(CHUNK)
    frames.append(data)
    print('0', end="")
    if keyboard.is_pressed(" "):
        print("BREAK")
        break

print("음성녹음을 완료하였습니다.")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print("녹음된 파일을 재생합니다.")
playsound(WAVE_OUTPUT_FILENAME)