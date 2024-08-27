import webbrowser
import os
import speech_recognition as sr
import win32com.client
import pygame


def say(t):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(t)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said : {query}")
            return query
        except Exception as e:
            return "Some error occured! Sorry "


if __name__ == "__main__":

    pygame.mixer.init()
    start = 1
    while start > 0:
        print("Listening.....")
        text = takeCommand()
        if f"Bye".lower() in text.lower():
            print("byee, have a nice day.....")
            start = 0
        sites = [['youtube', 'https://www.youtube.com/'], ['google', 'https://www.google.com/']]
        songs = [['Aapka kya hoga janabe ',
                  "C:/Users/yashk/Music/_Aapka Kya Hoga Janabe Ali_ (Dhanno) Housefull Full Song _ Akshay Kumar _ Mika Singh.mp3"],
                 ['Angreji beat','C:/Users/yashk/PycharmProjects/JarvisAI2/music/Angreji Beat.mp3']]
        for site in sites:
            if f"open {site[0]}".lower() in text.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])

        for song in songs:
            if f"play {song[0]}".lower() in text.lower():
                say(f"playing music")
                pygame.mixer.music.load(song[1])
                pygame.mixer.music.play()
        if "Stop music".lower() in text.lower():
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        if "Pause music".lower() in text.lower():
            pygame.mixer.music.pause()
        if "Resume music".lower() in text.lower():
            pygame.mixer.music.unpause()


