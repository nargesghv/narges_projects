
from ast import Await
from http import client
import speech_recognition as sr
import pyttsx3
import pyaudio
import pywhatkit as kit
import datetime
import wikipedia
import python_weather
import asyncio


listener=sr.Recognizer()
engine=pyttsx3.init()
volume=engine.getProperty('volume')
print(volume)
engine.setProperty('volume',1.0)
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[1].id)


def engin_talk(text):
    engine.say(text)
    engine.runAndWait()

def user_commands():
    
    try:
        with sr.Microphone() as source:
            print("start speaking please!!")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace("alexa"," ")
                print(command)
                #print(type(command))
                return command
    except:
        return command
        
        pass

    

   

def run_alexa():
    command=user_commands()
    new_command=str(command)
    if 'play' in new_command:
        song=new_command.replace("play"," ")
        #print(new_command)
        engin_talk('playing'+ song)
        kit.playonyt(song)  
    elif 'time' in new_command:
        time=datetime.datetime.now().strftime('%I:%M:%P')
        engin_talk('the time is:' + time)
    elif 'who is' in new_command:
        name=new_command.replace('who is', '')
        info=wikipedia.summary(name)    
        print(info)
        engin_talk(info)
    
    else:
        engin_talk('I could not hear properly! ')
    

#run_alexa()


    
    


