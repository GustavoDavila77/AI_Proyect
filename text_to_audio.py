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

