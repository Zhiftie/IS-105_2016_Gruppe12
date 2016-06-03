# -*- coding: utf-8 -*-
import pyttsx

engine = pyttsx.init()
engine.setProperty('rate', 90)
voices = engine.getProperty('voices')
welcomeOpt = ["hi", "hello","greetings"]
howOpt = ["good", "great", "fine", "okay"]
howOpt2 = ["bad", "terrible", "dreadfull", "not good"]

def greet():
    engine.say("hi")
    engine.runAndWait()
    chatInput = raw_input("Enter your message: ")
    chatInput = chatInput.lower() #Setter strengen fra brukeren til kun små boksotaver
    if any(chatInput in s for s in welcomeOpt): #Sjekker om bruker input er en lovlig kommando iht. welcomeOpt[]
        hay()
    else:
        engine.say("Inproper response, prepare to be exterminated")
        engine.runAndWait()
        
def hay():
    engine.say("How are you?")
    engine.runAndWait()
    chatInput = raw_input("Enter your message: ")
    chatInput = chatInput.lower()
    
    if any(chatInput in s for s in howOpt):
        engine.say("Oh, thats nice!")
        engine.runAndWait()
        yourDay()
    elif any(chatInput in s for s in howOpt2):
        engine.say("Awwh, thats too bad")
        engine.runAndWait()
    else:
        engine.say("Unable to process, initiating selfdestruct! in t minus 5, 4, 3, 2, 1")
        engine.runAndWait()
def yourDay():
    engine.say("How was your day?")
    chatInput = raw_input("Enter your message: ")
    chatInput = chatInput.lower()
    
greet()
engine.runAndWait()