import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
# noinspection PyBroadException


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
    except Exception:
        print('fuck')
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        talk('CURRENT TIME IS' + time)
    elif 'search' in command:
        person = command.replace('search', '')
        info = wikipedia.summary(person,2)
        talk(info)
    elif 'date' in command:
        talk('Sorry ,I dont go out with Engineers')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('cannot understand')


while True:
    run_alexa()