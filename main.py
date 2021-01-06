import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
from plyer import * 
import psutil

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)




def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source, timeout=5.1)
            
            command = listener.recognize_google(voice)
            
            command = command.lower()
            if 'max' in command:
                command = command.replace('max', '')
                print(command)
    
    except :
        print('Check your your mic connection(or)Check your network')    
    return command


def run_max():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif "bye"  in command:
        talk("Thank u have a nice day")
        return quit()
        
    elif "open facebook"  in command:
        talk("Openning facebook in web browser") 
        webbrowser.open("https://www.facebook.com")                
    elif "battery status"  in command:
       battery = psutil.sensors_battery()
       plugged = battery.power_plugged
       percent = str(battery.percent)

       plugged = "U are Plugged In dont Worry" if plugged else "Not Plugged and to get best performance get plugged with power adapter"

       talk(percent+'% | '+plugged )
    else:
        talk('Please say the command again.')


while True:
    run_max()

