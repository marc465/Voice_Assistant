import os, re, webbrowser, sys, requests, pyttsx3


engine = pyttsx3.init()
engine.setProperty('rate', 180)


def speaker(text):
    engine.say(text)
    engine.runAndWait()


def weather():
    response = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D1%97%D0%B2')
    ans = re.search(r'(?<=<div class="description"> <!--noindex--> )[^A-za-z]+(?= <!--\/noindex--> <\/div>)', response.text).group(0)
    speaker(ans)


def start_internet():
    webbrowser.open('https://www.google.com/')


def start_film():
    webbrowser.open('https://rezka.ag/films/best/')


def fun():
    webbrowser.open('https://www.youtube.com/watch?v=6i1LrJhJNlQ&ab_channel=MarioandCompany')


def bot_shutdown():
    sys.exit()


def pc_shutdown():
    os.system('shudown /s')


def passive():
    pass
