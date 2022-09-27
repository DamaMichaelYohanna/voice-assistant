import speech_recognition as sr
import webbrowser
import pyttsx3 as pyt

engine = pyt.init()

def main():
    engine.say("hello")

def lunch_browser(url):
    url = ''
    webbrowser.open('google.com')
    
