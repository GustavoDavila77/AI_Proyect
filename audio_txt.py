import speech_recognition as sr

r = sr.Recognizer()

def Listening():
    with sr.Microphone() as source:
        print('has la pregunta')
        audio = r.listen(source,phrase_time_limit=4)
        print('El tiempo se acabo')
    try:
        text = r.recognize_google(audio, language='es-CO')
        print('TEXT' + text)
    except:
        text = 'error con la lib'
        print(text)
    
    return text 

print(Listening())