
from urllib import request
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyautogui
import ctypes
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
  
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=49dc7d36f9d447098f58ca7cfd457b04'
    main_page = request.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's{day[1]} news is: {head[i]}")        

def wishMe():
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12:
        speak('Good Morning!')

    elif hour>=12 and hour<18:
        speak('Good Afternoon!')

    else:
        speak('Good Evening')

    speak('i am nava how may i help you sir')
def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        
        audio = r.listen(source)
    
    try:
        print('recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}\n')

    except Exception as e:
        print(e)

        print('say that again')
        return 0
    return query    
wishMe()
while True:
    qurey = takecommand().lower()

    if 'wikipedia' in qurey:
        speak('searching wikipedia...')
        qurey = qurey.replace('wikipedia','')
        results = wikipedia.summary(qurey, sentences=2)
        speak('according to wikipedia')
        print(results)
        speak(results)

    elif 'open youtube' in qurey:
        webbrowser.open('youtube.com')

    elif 'open google' in qurey:
        webbrowser.open('google.com')  

    elif 'open stackoverflow' in qurey:
        webbrowser.open('stackoverflow.com')

    elif 'the time' in qurey:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        speak('current time is' + time)

    elif 'screenshot' in qurey:
        image = pyautogui.screenshot()
        image.save('screenshot.png')
        speak('screenshot taken.') 

    elif 'lock window' in qurey or 'lock the window' in qurey:
        speak("locking the device")
        ctypes.windll.user32.LockWorkStation()

    elif 'play' in qurey:
       song = qurey.replace('play', '')
       speak('playing ' + song) 
       pywhatkit.playonyt(song)

    elif 'open vlc' in qurey:
        codePath = "C:\\Users\\Public\\Desktop\\VLC media player.lnk" 
        os.startfile(codePath)

    elif 'how are you ' in qurey:
        speak("I am fine, Thank you")
        speak("How are you, Sir")
 
    elif 'fine' in qurey or "good" in qurey:
        speak("It's good to know that your fine")

    elif "what's your name" in qurey or "What is your name" in qurey:
        speak("My friends call me nava")
    
        print('My friends call me nava')
    elif 'hai' in qurey or 'hii' in qurey or 'hey' in qurey or 'hi' in qurey:
        speak('hello sir')
    

    elif 'exit' in qurey:
            speak("Thanks for giving me your time")
            exit()
    
    elif 'shutdown the system' in qurey:
        os.system("shutdown /s /t 5")
        speak('thanks you sir, your system will be shutdown')

    elif 'tell me news' in qurey:
       speak("please wait sir ,fetching the letest news")
       news()    

    else:
        qurey('please say again.')

