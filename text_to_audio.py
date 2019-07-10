import pyttsx3
import win32com

eng = pyttsx3.init()
eng.setProperty('rate', 110)
listVoices = eng.getProperty('voices')
eng.setProperty('voice',listVoices[0].id)

def reproducir(texto):
    eng.say(texto)
    eng.runAndWait()

#reproducir('la ruta es la ruta 3')
#tts("la ruta 3a", "ES","audio2.wav")
#reproducir()


"""
from gtts import gTTS
#import pygame
#from pydub import AudioSegment
#from pydub.playback import play
#from playsound import playsound
#import winsound
#import pyglet

winsound.PlaySound("explosion", winsound.SND_FILENAME)

pygame.init()
audio = pygame.mixer.Sound("D:\Escritorio\Artificial intelligent\proyecto IA/audio2.wav")
audio.play()
#audio.stop()

def tts(texto, lang, name_file):
    file= gTTS(text=  texto, lang = lang)
    file.save(name_file)

def tts(text_file, lang, name_file):
    with open(text_file, "r") as file:
        text = file.read()
        file = gTTS(text = text, lang = lang)
        filename = name_file
        file.save(filename)

def reproducir():
    fname = "D:\Escritorio\Artificial intelligent\proyecto IA\audio2.wav"
    mysong = AudioSegment.from_wav(fname)
    play(mysong)

tts("prueba.txt", "ES", "audio.mp3")
"""
