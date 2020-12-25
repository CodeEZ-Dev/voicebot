import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listner=sr.Recognizer()
engine= pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(talk):
    engine.say(talk)
   # engine.say('How can i help you?')
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listner.listen(source)
            command=listner.recognize_google(voice)
            command = command.lower()
            if 'ok google' in command:
                command = command.replace('ok google',' ')
                pywhatkit.playonyt(command)
    except:
        pass
    return command

def run_google():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing '+ song)
        print(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk("Current time is " +time)
        print(time)

    elif 'who is the' in command:
        person = command.replace('who is the','')
        info=wikipedia.summary(person,2)
        talk(info)
        print(info)
    elif 'dating ' in command:
        talk('Sorr, I am busy this week!')
    elif 'i love you' in command:
        talk('Thank you, we will meet soon')
    elif 'are you married' in command:
        talk('Yes, i married with google')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'bye' in command:
        talk('See you soon')
    else:
        talk('Something went wrong')
   

while True:
    run_google()