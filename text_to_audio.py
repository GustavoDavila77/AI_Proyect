import pyttsx3 #instalar con pip3 install pyttsx3
import win32com

eng = pyttsx3.init()
eng.setProperty('rate', 110) #controla la velocidad del habla
listVoices = eng.getProperty('voices') #obtengo un objeto con info de la voz
eng.setProperty('voice',listVoices[0].id)  #puede cambiar a modo ingles con [1]

#reproduce un texto
def reproducir(texto):
    eng.say(texto)
    eng.runAndWait()

#reproducir('la ruta es la ruta 3')
#tts("la ruta 3a", "ES","audio2.wav")
#reproducir()

