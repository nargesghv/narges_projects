
from ast import Await
from fnmatch import translate
from http import client
import speech_recognition as sr
import pyttsx3
import pyaudio
import pywhatkit as kit
import datetime
import wikipedia
import python_weather
import asyncio
import googletrans
import time

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
            engin_talk('My name is Alexa, What can I do for you')
            engin_talk("start speaking please!!")
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
def gettingorder():
    

        with sr.Microphone() as source:
            engin_talk('I am ready to send a message, Can I have your Number? ')
            print("Can I have your number!!")
            voice=listener.listen(source)
            number=listener.recognize_google(voice)
            print('your number is :{}'.format(number))
        return number
def tarans():
    engin_talk('please slowly say the text that you want to be translate')
    engin_talk("you can taype if works for you!!")
    with sr.Microphone() as source:
        if source!=0:
            voice=listener.listen(source)
            t_text=listener.recognize_google(voice)
            t_text=t_text.lower()
            print(t_text)
        else:
            t_text=input(str("please ensert your text as a string: "))
            print('I got the text message!')

        return t_text

tarans()
#generator,yeild,__next__,threat
    
def gettingmsg():
    try:
        with sr.Microphone() as source:
            engin_talk('May I have your message? ')
            voice=listener.listen(source)
            msg=listener.recognize_google(voice)
            
            print('your message is :{}'.format(msg))
        return msg
    except :
        print("error")
    

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
    elif 'message' in new_command:
        number=gettingorder()
        message=gettingmsg()
        try:
            kit.sendwhatmsg('+1'+'number',message='message',time_hour=13,time_min=15,wait_time=10)
            engin_talk("Message is sent")
        except:
            print("Error in sending message")
    elif 'translate' in new_command:
        engin_talk('please say the text that you want to taranslate')

        
    
    else:
        engin_talk('I could not hear properly! ')
    

#run_alexa()
#gettingorder()
#gettingmsg()


    
    


