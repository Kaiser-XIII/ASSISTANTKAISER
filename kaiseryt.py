import pywhatkit
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.say('Hello. I am Kaiser. Your personal assistant.')
engine.say('What can i do for you today. Sir?')
engine.runAndWait()


def take_command():

    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    
    return command



def run_kaiser():
    command = take_command()
    print(command)
    if 'play' in command:
        song= command.replace('play', '')
        talk=('playing ' + song)
        pywhatkit.playonyt(song)

run_kaiser()