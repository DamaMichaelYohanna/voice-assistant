import speech_recognition as sr
import webbrowser
import pyttsx3 as pyt

engine = pyt.init()

def open_browser():
    print("am going to open the browser")
    webbrowser.open("google.com")

def play_music():
    print("am going to play music")
    

def search_ofline():
    pass
    

def search_online():
    pass
    
def main():
    engine.say("hello")
    while True:
        command = input("Enter your command")
        if command == "open browser":
            open_browser()
        elif command == "play music":
            play_music()
        elif command == "search ofline":
            search_ofline()
        elif command == "search online":
            search_online()


