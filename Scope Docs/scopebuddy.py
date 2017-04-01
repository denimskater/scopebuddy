#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class


import speech_recognition as sr

#Scope Identification requires an execution of a VX11 command in this program
#FIX ME ADD VX11 COMMAND

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
    #r.adjust_for_ambient_noise(source) # listen for 1 second to calibrate the energy threshold for ambient noise levels
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

# send audio packet back to scope also using VX11 commands

audioPacket = r.recognize_sphinx(audio)
print(type(audioPacket))

#if 'scope' in audio:
#    if 'stop' in audio:
#        audioPacket = 'stop'
#    elif 'run' in audio:
#        audioPacket = 'run'
#    elif 'single' in audio:
#        audioPacket = 'single'
#    elif 'auto' in audio:
#        audioPacket = 'auto'
#print(audio)
print(audioPacket)
   




