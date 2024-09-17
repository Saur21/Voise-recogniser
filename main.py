import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
recognizer = sr.Recognizer()
ttsx =  pyttsx3.init()
newsApi = "378ed05e67ad4603b1d1b966b3160614"

def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()
    
def processCommand(c):
    if"open google" in c.lower():
        webbrowser.open("https://google.com")
    
    elif"open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    
    elif"open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    
    elif"open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link =musiclibrary.music [song]
        webbrowser.open(link)
        
    elif "news" in c.lower(): 
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=378ed05e67ad4603b1d1b966b3160614")
        if r.status_code == 200:
            # Parse the JSON response
            news_data = r.json()

            # Get the articles from the response
            articles = news_data.get("articles", [])

            # Display the headlines
            print("Top Headlines:")
            for  article in (articles):
                speak(article['title'])
        
        
if __name__ == "__main__":
    speak("Intialising jarvis...")
    while True:
    # Listen word to wake the jarvis
        r=sr.Recognizer()
    
    
    
        print("Recongising...")
        try:
            with sr.Microphone() as source:
                print("Listiing..")
                audio = r.listen(source , timeout = 2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Ya")
                # listen for command
                with sr.Microphone() as source:
                    print("Jarvis Activating")
                    audio = r.listen(source )
                    command = r.recognize_google(audio)
                    
                    
                    processCommand(command)
                    
                    
        except Exception as e:
            print("Error;{0}".format(e))