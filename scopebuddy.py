#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class


import speech_recognition as sr

#Scope Identification
scopeIdRead = 'Tektronix'
scopeMfg = ''
if 'LeCroy' in scopeIdRead:
    scopeMfg = 'LeCroy'
elif 'Tektronix' in scopeIdRead:
    scopeMfg = 'Tektronix'

print(scopeMfg)

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone(device_index = 2, sample_rate=48000, chunk_size = 512) as source:
    print("Say something!")
    audio = r.listen(source)

print('Heard ya!')

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

