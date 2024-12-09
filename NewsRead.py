import requests
import json
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('vaice',voices[0].id)
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def latestnews():
    apidict = {"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=6b4fd48d253e4c508132595b0435423f",
               "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=6b4fd48d253e4c508132595b0435423f",
               "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=6b4fd48d253e4c508132595b0435423f",
                "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=6b4fd48d253e4c508132595b0435423f",
                "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=6b4fd48d253e4c508132595b0435423f",
                "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=6b4fd48d253e4c508132595b0435423f"
                }
    content = None
    url = None
    speak("Which field news do you want,[business],[entertainment],[health],[science],[sports],[technology]")
    field = input("Type field news that you want: ")
    for key,value in apidict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break

        else:
             url = True

    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break

    speak("thats all")


