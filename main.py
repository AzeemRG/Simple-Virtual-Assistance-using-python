import pyttsx3
import datetime
from datetime import date
import speech_recognition as sr
import wikipedia
import webbrowser
import pyjokes
import time
import pywhatkit
from ecapture import ecapture as ec
import PySimpleGUI as sg
import subprocess
import requests

sg.theme('DarkAmber')
layout = [[sg.Image(filename='wolfie.png', key='key1', size=(600, 600),background_color="black")], [sg.Text("Your very own virtual assistant!",font=("Helvetica", 15), background_color='black')], [sg.Button("Launch Edith!",font=("Helvetica", 10),size=(70, 3))], [sg.Output(size=(70, 10))]]
window = sg.Window("Edith", layout, margins=(650, 30), background_color="black")
while True:
    event, values = window.read()
    if event == "Launch Edith!":
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('rate', 145)
        engine.setProperty('volume', 0.7)
        engine.setProperty('voice', voices[0].id)


        def speak(text):
            engine.say(text)
            engine.runAndWait()


        def wish():
            hour = datetime.datetime.now().hour
            if 0 <= hour < 12:
                speak("Good Morning")
                print("Good Morning")
            elif 12 <= hour < 18:
                speak("Good Afternoon")
                print("Good Afternoon")
            else:
                speak("Good Evening")
                print("Good Evening")


        def tell_day():
            localtime = time.asctime(time.localtime(time.time()))
            day = localtime[0:3]
            if day == "Sun":
                speak("it's sunday")
                print("It's Sunday!")
            if day == "Mon":
                speak("it's monday")
                print("It's Monday")
            if day == "Tue":
                speak("it's tuesday")
                print("It's Tuesday")
            if day == "Wed":
                speak("it's wednesday")
                print("It's Wednesday")
            if day == "Thu":
                speak("it's thursday")
                print("It's Thursday")
            if day == "Fri":
                speak("it's friday")
                print("It's Friday!")
            if day == "Sat":
                speak("it's saturday")
                print("It's Saturday!")


        print("Hello Varun")
        speak("Hello Varun")
        wish()
        tell_day()


        def takeCommand():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)

                try:
                    statement = r.recognize_google(audio, language='en-in')
                    print(f"user said:{statement}\n")

                except Exception as e:
                    speak("Pardon me, say that again")
                    return "None"
                return statement


        if __name__ == '__main__':

            while True:
                speak("How may I help you?")
                statement = takeCommand().lower()

                if 0 == statement:
                    continue
                if "what is your name" in statement:
                    speak("My name is Edith, and I am your personal assistant")
                    print("My name is Edith")

                if "good bye" in statement or "ok bye" in statement or "stop" in statement or "bye" in statement:
                    speak('your personal assistant Edith is shutting down. Goodbye')
                    print('your personal assistant Edith is shutting down,Good bye')
                    break

                if 'wikipedia' in statement:
                    speak('Searching Wikipedia...')
                    statement = statement.replace("wikipedia", "")
                    results = wikipedia.summary(statement, sentences=3)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                elif 'search' in statement:
                    statement = statement.replace("search", "")
                    webbrowser.open_new_tab(statement)
                    time.sleep(5)
                elif 'open youtube' in statement:
                    webbrowser.open_new_tab("https://www.youtube.com")
                    speak("youtube is open now")
                    time.sleep(5)

                elif 'open google' in statement:
                    webbrowser.open_new_tab("https://www.google.com")
                    speak("Google chrome is open now")
                    time.sleep(5)

                elif 'open mail' in statement or 'mail' in statement:
                    webbrowser.open_new_tab("https://gmail.com")
                    speak("Gmail open now")
                    time.sleep(5)
                elif 'time' in statement:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"the time is {strTime}")
                elif 'date' in statement:
                    today = date.today()
                    print("Today's date:", today)
                    speak(f"Today's date is {today}")
                elif "who is the best" in statement:
                    speak("Varun is the best")
                    print("Varun is the best")
                elif 'news' in statement:
                    news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                    speak('Here are some headlines from the Times of India')
                    time.sleep(6)

                elif "what is my name" in statement or "my name" in statement:
                    speak("Your name is varun")
                    print("Varun")
                elif "camera" in statement or "take a photo" in statement:
                    ec.capture(0, False, "img.jpg")
                elif "play" in statement:
                    song = statement.replace("play", "")
                    speak("playing" + song)
                    pywhatkit.playonyt(song)

                elif "tell me a joke" in statement or "joke" in statement or "jokes" in statement:
                    print(pyjokes.get_joke())
                    speak(pyjokes.get_joke())
                elif 'open maps' in statement or 'maps' in statement or "map" in statement:
                    webbrowser.open_new_tab("https://www.google.com/maps")
                    speak("Google Maps is open now")
                    time.sleep(5)
                elif "weather" in statement or "what is it like outside" in statement:
                    api_key = "6e02eec9d5193ca5acc8fb39b2460a1f"
                    base_url = "https://api.openweathermap.org/data/2.5/weather?"
                    speak("In which city?")
                    city_name = takeCommand()
                    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                    response = requests.get(complete_url)
                    x = response.json()
                    if x["cod"] != "404":
                        y = x["main"]
                        current_temperature = y["temp"]
                        current_humidiy = y["humidity"]
                        z = x["weather"]
                        weather_description = z[0]["description"]
                        speak("In" + city_name + "Temperature in Kelvin is " +
                              str(current_temperature) +
                              "\n humidity in percentage is " +
                              str(current_humidiy))
                        print(" Temperature in kelvin unit = " +
                              str(current_temperature) +
                              "\n humidity (in percentage) = " +
                              str(current_humidiy) +
                              "\n description = " +
                              str(weather_description))
                elif "log off" in statement or "sign out" in statement or "shutdown" in statement:
                    speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                    subprocess.call(["shutdown", "/l"])



