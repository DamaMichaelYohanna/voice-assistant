import speech_recognition as sr
import webbrowser
import pyttsx3 as pyt

engine = pyt.init()
def open_browser():
    print("am going to open the browser")

def main():
    engine.say("hello")
    while True:
        command = input("Enter your command")
        if command == "open browser":
            pass
        elif command == "play music":
            pass
        elif command == "search ofline":
            pass
        elif command == "search online":
            pass
        pass

def lunch_browser(url):
    url = ''
    webbrowser.open('google.com')
    
