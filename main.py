import pyttsx3
import speech_recognition as sr
import pywhatkit as wt
import datetime
import wikipedia
import pyjokes
import json
from urllib.request import urlopen
import time
import webbrowser
import numpy as np
import random

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer()

name = ""

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning !")

    elif hour >= 12 and hour < 18:
        talk("Good Afternoon !")

    else:
        talk("Good Evening !")

    talk("I am Alexa your Virtual Voice Assistant! ")
    talk("What do you want me to do?")


def take():
    try:
        with sr.Microphone() as source:
            talk("Listening")
            audio = r.listen(source)
            query = r.recognize_google(audio, language='en-in')

            query = query.lower()

            if 'alexa' in query:
                query = query.replace("alexa", '')
                print("Recognizing...")
                print(f'User said: {query}\n')

            else:
                text = "call my name first"
                print(text)
                talk(text)
                query=""
    except:
        time.sleep(10)
        return "None"
    return query


def run_alexa():

    command = take()
    command = command.replace("alexa", '')
    # print(command)

    if 'tell me about yourself' in command or 'introduce yourself' in command:
        talk('I am Alexa your virtual voice assistant.I do what you tell me to do. I do several things like I can play songs and videos on youtube, I can tell you some jokes to make you laugh, I can keep you motivated with my quotes, I can write a note and show you the note, I can tell you the top news, I can tell you the time, I can tae your Quiz, I can answer your questions, I can search on web and open different browsers and can do many more things. Now tell me what you want me to do? ')
    elif 'hi' in command or 'hello' in command:
        talk('hello my friend')
    elif 'how are you' in command:
        talk('I am fine. Hope you are fine too')
    elif 'play' in command or 'song' in command:
        song = command.replace('play', '')
        print('playing')
        wt.playonyt(song)
        text = "it will take 2 min"
        talk(text)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)

    elif 'tell me about' in command or 'tell me something about' in command:
        info_for = command.replace("tell me about", "")
        info = wikipedia.summary(info_for, 2)
        print(info)
        talk(info)
    elif 'joke' in command or 'laugh' in command:
        jk = pyjokes.get_joke()
        print(jk)
        talk(jk)

    elif 'motivate' in command or 'motivational' in command or 'quote'in command:
        n = int(random.random()*10)
        arr=['All our dreams can come true, if we have the courage to pursue them.',
             'The secret of getting ahead is getting started.',
             'It’s hard to beat a person who never gives up.',
             'Everything you can imagine is real.',
             'Do one thing every day that scares you.',
             'It’s no use going back to yesterday, because I was a different person then.',
             'Happiness is not something ready made. It comes from your own actions.',
             'Whatever you are, be a good one',
             'Your passion is waiting for your courage to catch up.',
             'Magic is believing in yourself. If you can make that happen, you can make anything happen.']
        print(arr[n])
        talk(arr[n])

    elif 'quiz' in command or 'questions' in command:

        def quizplay(o1,o2,o3,o4):
            print(opt1)
            talk(opt1)
            print(opt2)
            talk(opt2)
            print(opt3)
            talk(opt3)
            print(opt4)
            talk(opt4)

        q1="question 1: Which weighs more: A ton of bricks or a ton of feathers?"
        print(q1)
        talk(q1)
        opt1='option1: A ton of bricks'
        opt2='option2: A ton of feathers'
        opt3='option3: they weigh the same'
        opt4='option4: Not enough information to know'
        quizplay(opt1,opt2,opt3,opt4)
        ans=take()
        if 'they weigh same' in ans or 'same' in ans or 'option 3' in ans:
            print('hurray!! your answer is correct. They weight the same! A ton weighs a ton, no matter which objects you are weighing.')
            talk('hurray!! your answer is correct. They weight the same! A ton weighs a ton, no matter which objects you are weighing.')
        else:
            print('oops: your answer is wrong. They weight the same! A ton weighs a ton, no matter which objects you are weighing.')
            talk('oops: your answer is wrong. They weight the same! A ton weighs a ton, no matter which objects you are weighing.')

        q2='question2: Book is to reading, as spoon is to...'
        print(q2)
        talk(q2)
        opt1='option1:writing'
        opt2='option2:painting'
        opt3='option3:baking'
        opt4='option4:eating'
        quizplay(opt1,opt2,opt3,opt4)
        ans=take()
        if 'eating' in ans or 'option 4' in ans:
            print('hurray!! your answer is correct. It is eating! You read with a book, and you eat with a spoon. ')
            talk('hurray!! your answer is correct. It is eating! You read with a book, and you eat with a spoon.  ')
        else:
            print('oops: your answer is wrong. It is eating! You read with a book, and you eat with a spoon. ')
            talk('oops: your answer is wrong. It is eating! You read with a book, and you eat with a spoon. ')

        q3='question3: How many edges does a cube have?'
        print(q3)
        talk(q3)
        opt1 = 'option1: 6'
        opt2 = 'option2: 8'
        opt3 = 'option3: 10'
        opt4 = 'option4: 12'
        quizplay(opt1,opt2,opt3,opt4)
        ans=take()
        if '12' in ans or 'twelve' in ans or 'option 4' in ans:
            print('hurray!! your answer is correct.A cube has 12 edges!Cubes also have six faces and eight vertices (corners). ')
            talk('hurray!! your answer is correct. A cube has 12 edges!Cubes also have six faces and eight vertices (corners).  ')
        else:
            print('oops: your answer is wrong. A cube has 12 edges!Cubes also have six faces and eight vertices (corners).')
            talk('oops: your answer is wrong. A cube has 12 edges!Cubes also have six faces and eight vertices (corners).')

        q4='question4: If you’re in a race and pass the person in second place, which place are you in?'
        print(q4)
        talk(q4)
        opt1='option1: First place'
        opt2='option2: Second place'
        opt3='option3: Third place'
        opt4='option4: Not enough information to know'
        quizplay(opt1,opt2,opt3,opt4)
        ans=take()
        if 'second place' in ans or 'option 2' in ans:
            print('hurray!! your answer is correct. Second place! You will go from third place to second.')
            talk(
                'hurray!! your answer is correct.Second place! You will go from third place to second.')
        else:
            print('oops: your answer is wrong. Second place! You will go from third place to second.')
            talk('oops: your answer is wrong. Second place! You will go from third place to second.')

        q5 = 'question5: Which one of these is least like the others?'
        print(q5)
        talk(q5)
        opt1 = 'option1: Antelope'
        opt2 = 'option2: Snake'
        opt3 = 'option3: Dog'
        opt4 = 'option4: Camel'
        quizplay(opt1, opt2, opt3, opt4)
        ans = take()
        if 'snake' in ans or 'option 2' in ans:
            print('hurray!! your answer is correct. It is a snake! All of the other animals have four legs.')
            talk('hurray!! your answer is correct. It is a snake! All of the other animals have four legs.')
        else:
            print('oops: your answer is wrong')
            talk('oops: your answer is wrong')

        talk('hope you like the quiz. what would you like me to do?')


    elif "write a note" in command:
        talk("What should i write")
        note = take()
        file = open('jarvis.txt', 'w')
        talk("Should i include date and time")
        snfm = take()
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now().strftime('%I:%M %p')
            file.write(strTime)
            file.write(" :- ")
            file.write(note)
        else:
            file.write(note)

    elif "show note" in command:
        talk("Showing Notes")
        file = open("jarvis.txt", "r")
        txt=file.read()
        print(txt)
        talk(txt)

    elif "do you love me" in command:
        talk("Yes I Love you so much")

    elif "who is the most beautiful person" in command:
        talk("You are the most beautiful person in the world. And Your heart is most beautiful heart")

    elif "let us go out" in command:
        talk("Sorry. I have some urgent work today. ")

    elif 'open google' in command:
        talk("Here you go to Google\n")
        webbrowser.open("google.com")


    elif 'open stackoverflow' in command:
        talk("Here you go to Stack Over flow.Happy coding")
        webbrowser.open("stackoverflow.com")

    elif 'search' in command:

        command = command.replace("search", "")
        webbrowser.open(command)

    elif 'news' in command:

        try:
            jsonObj = urlopen(
                '''https://newsapi.org/v2/top-headlines?country=in&apiKey=65ec20d28c21432e8ba016e81c931e23''')
            data = json.load(jsonObj)
            i = 1

            talk('here are some top news ')
            print('''=============== NEWS FOR TODAY ============''' + '\n')

            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                #print(item['description'] + '\n')
                talk(str(i) + '. ' + item['title'] + '\n')
                i += 1
        except Exception as e:

            print(str(e))



    elif 'stop' in command:
        talk("Thank you for spending your precious time with me")
        exit()
    else:
        talk("cant understand")

wishMe()
while True:
    run_alexa()
