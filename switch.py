import pyttsx3
import speech_recognition as sr
import os
from bs4 import BeautifulSoup
import requests
from time import ctime

from random import randint
engine=pyttsx3.init()
engine.setProperty('rate',180)
voices=engine.getProperty("voices")


def speak(text):
    engine.say(text)
    engine.runAndWait()
print("Switch ON")
speak("Switch ON")
speak("hey there this is switch.")

def listen():
    r=sr.Recognizer()
    with sr.Microphone()as source:
        audio=r.listen(source)

        try:
                word=r.recognize_google(audio)
        except:
                print("----------plz-retry----------")
                speak("please retry")
                switch()
    return word.casefold()

def change_voice():
    print ("Here is an example of my other voice")
    engine.setProperty('voice',voices[1].id)
    speak("Here is an example of my other voice")
    print ("Do you prefer this voice?")
    speak("Do you prefer this voice?")
    ans=input()
    if ("yes" in ans or "y" in ans):
        print("OK.")
        speak("OK.")
    else:
        print("Changing back to old voice")
        engine.setProperty('voice',voices[0].id)
        speak("Changing back to old voice")
    speak("What can I do for you now?")
def music():
    os.chdir("D:\\")
    print ("what do you want to listen")
    speak("what do you want to listen")
    #ans=listen()
    ans=input()
    ans=ans.casefold()
    lst=os.listdir()

    if ("what" and "can you play" in ans):
        print("Here is the list of playable songs in your directory->")
        speak("Here is the list of playable songs in your directory.")
        print("-----------------------------------------------------------------------------------------------------")
        for i in lst:
            if ".mp3" in i or ".flac" in i:
                print(i)
        print("-----------------------------------------------------------------------------------------------------")
        speak("What do you want to listen")
        ans=input()
        
    print("User: ",ans)
    print("Switch: Playing "+ans)
    speak("Playing "+ans)
    
    
    i=0
    while(i<len(lst)):
        if ans in lst[i].casefold():
            ans=lst[i]
            print (ans)
            break
        i=i+1
    try:
        os.startfile("D:\\"+ans)
    except:
        speak("Sorry, No such song found")
        speak("Please retry")
        music()
def what(w):
    
    source=requests.get("https://www.google.co.in/search?q="+w).text
    soup=BeautifulSoup(source,"lxml")
    st=soup.find('span',class_='st').text
    spans=soup.findAll('span',class_='st')
    for i in spans:
        if (not len(i.text) < 6):
            lst=i.text.split(".")
            break   
    for i in lst:
        if (not len(i) < 18):
            print(i+".")
            speak(i+".")
            break
    
def switch():
        word=listen()
        #word=input()
        word=word.casefold()
        while word==(None):
            print("type your command instead")
            speak ("type your command instead")
            word=input("Type here -")
            if word =="no" or word=="No" or word=="NO":
                print(" ok then speak again now")
                speak ("ok then speak now")
                break
        
            
        print("User:",word)
        print("Switch: ", end=' ')
        
        if "how are you" in word:
            print("I'm fine")
            speak("I'm fine")
        if "open" in word:    
            if "chrome" in word:
                os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
            if "codeblocks" in word:
                os.startfile("C:\Program Files (x86)\CodeBlocks\codeblocks.exe")
        if "music" in word:            
            music()
        if "change" and "voice" in word:
            change_voice()
        if "what time is it" in word:
            print("its "+ctime())
            speak("its"+ctime())
        if "what is" in word or "search" in word or "who is" in word:
            '''speak("Let me google it")
            os.startfile("https://www.google.co.in/search?q="+word[7:])'''
            what(word)
        elif "hi" in word or "hello" in word or "hey" in word:
            reply=["hey there master!","Hello","Hey there!","hello what can i do for you"]
            k=randint(0,3)
            print(reply[k])
            speak(reply[k])
        if "where is" in word:
            speak("Here is its location on maps")
            os.startfile("https://www.google.co.in/maps/search/"+word[8:])         
        if word=="exit" or word=="switch off" :
            speak("switch")
            engine.setProperty('rate',80)
            speak("off")
        if word!="exit" and word!="switch off":
            switch()
switch()

