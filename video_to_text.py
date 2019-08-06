#importing required libraries
import subprocess
import os
import speech_recognition as sr

f=open("Text_Output.txt","w+"); #Create a text file.

cmdline = ['ffmpeg',        #Convert .mp4 file to .wav file
           '-i',            #using ffmpeg
           'Test.mp4',
           '-vn',
           '-f',
           'wav',
           'test.wav']
subprocess.call(cmdline)

r=sr.Recognizer()           #Create Speech_recognizer Object
Thh=sr.AudioFile('test.wav')
with Thh as source:
    r.adjust_for_ambient_noise(source)  #Noise adjustmest 
    audio=r.record(source)
r.recognize_google(audio)
f.write(r.recognize_google(audio))
print(r.recognize_google(audio))        #print the speech in text fomat
f.close()
