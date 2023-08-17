import webbrowser
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import os
import wolframalpha
import wikipedia

# creating take_commands() function which
# can take some audio, Recognize and return
# if there are not any errors
def take_commands():
    # initializing speech_recognition
    r = sr.Recognizer()
    # opening physical microphone of computer
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 0.6
        # storing audio/sound to audio variable
        audio = r.listen(source)
        try:
            print("Recognizing")
            # Recognizing audio using google api
            Query = r.recognize_google(audio)
            print("The query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Pardon me! please say that again Sir!")
            Speak("Pardon me! please say that again Sir!")
            
            # returning none if there are errors
            return "None"
        return Query
    
# creating Speak() function to giving Speaking power to our voice assistant 
def Speak(audio):
    # initializing pyttsx3 module
    engine = pyttsx3.init()
    # anything we pass inside engine.say(), will be spoken by our voice assistant
    engine.say(audio)
    engine.runAndWait()

print("Loading your AI personal assistant John")
Speak("Loading your AI personal assistant John")

def wishMe():
    hour=datetime.now().hour
    if hour>=0 and hour<12:
        Speak("Hello, Good Morning Sir!")
        print("Hello, Good Morning Sir!")
    elif hour>=12 and hour<16:
        Speak("Hello, Good Afternoon Sir!")
        print("Hello, Good Afternoon Sir!")
    else:
        Speak("Hello, Good Evening Sir!")
        print("Hello, Good Evening Sir!")
wishMe()

# Driver Code
if __name__ == '__main__':
    # using while loop to communicate infinitely
    while True:
        Speak("Tell me, how can I help you Sir?")
        command = take_commands()
        if "shutdown the computer" in command or "goodbye" in command or "ok bye" in command:
            Speak("Do you really want to shut down your computer. sir?")
            while True:
                command=take_commands()
                if "no" in command:
                    Speak("Thank you sir! I will not shutdown the computer")
                if "yes" in command:
                    #shutting down
                     Speak("Ok sir, Shutting down your computer in 5 seconds")
                     os.system("shutdown /s /t 05")
                break
        if "hi John" in command:
            Speak("Hello Sir!  How may I assist you ?")
        if "John" in command:
            Speak("John, Your Personal Assistant is in your service, Sir")
        if "how are you" in command:
            Speak("I am good Sir. and I hope you and your beloved ones are safe and healthy.")
        if "exit" in command: 
            Speak("Sure sir! as your wish, Have a nice day. Bye")
            break
        if "Wikipedia" in command:
            Speak("Searching Wikipedia ...")
            command = command.replace("wikipedia", 'take_commands()')
            results = wikipedia.summary(command, sentences=2)
            Speak("According to wikipedia")
            Speak(results)
            webbrowser.open(results)
        if "who are you" in command:
            Speak("I am John, a voice assistant created by Dheeraj Kumar")
        if "open Facebook" in command:
            Speak("Opening Facebook Sir!")
            webbrowser.open("https://www.facebook.com/")
        if "open Twitter" in command:
            Speak("Opening Twitter Sir!")
            webbrowser.open("https://twitter.com/home")
        if "open Instagram" in command:
            Speak("Opening Instagram Sir!")
            webbrowser.open("https://www.instagram.com/")
        if "what is my name" in command:
            Speak("Your name is Dheeraj Kumar")
        if "do you like my name" in command:
            Speak("Your name is unique, just like you")
        if "thank you" in command:
            Speak("You're most welcome Sir!")
        if "good morning" in command:
            Speak("Good Morning Sir! Have a Nice Day!")
        if "good afternoon" in command:
            Speak("Good Afternoon Sir!")
        if "good evening" in command:
            Speak("Good Evening Sir!")
        if "good night" in command:
            Speak("Good Night Sir! Take care")
        if "I love you" in command:
            Speak("Awwww! Thank you Sir! I love you too")
        if "you are awesome" in command:
            Speak("That's so funny. I was just thinking the same thing about you Sir!")
        if "I like talking with you" in command:
            Speak("I like our conversations, too! We are like peanut butter and jelly!")
        if "when is my birthday" in command:
            Speak("The 8th of September 2002")
        if "how do you know about my birthday" in command:
            Speak("I know everything about you Sir!")
        if "open Google" in command:
            Speak("Opening Google Sir!")
            webbrowser.open("https://www.google.co.in/")
        if "open Gmail" in command:
            Speak("Opening Gmail Sir!")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        if "open YouTube" in command:
            Speak("Opening Youtube Sir!")
            webbrowser.open("https://www.youtube.com/")
        if 'play music' in command:
            Speak("Playing Music Sir!")
            webbrowser.open("https://www.jiosaavn.com/song/kesariya-from-brahmastra/NQotZhVbc0A")
        if 'news' in command:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            Speak('Here are some headlines from the Times of India, Happy reading')
        if 'time' in command:
            strTime=datetime.now().strftime("%H:%M:%S")
            Speak(f"the time is {strTime}")
            print(strTime)
        if 'feeling bore' in command:
            Speak("Oh sorry Sir! You can't get bored with me. I know you like watching Rohit Sharma. So, I suggest you  some of his videos")
            webbrowser.open("https://www.youtube.com/shorts/ehbTi1r3-Ug")
        if 'can you show me your face' in command:
            Speak("Sorry Sir! I am a bit camera shy. I would like to keep our friendship all about my searching skills")
        if 'restaurants near me' in command:
            Speak("Here are the listing restaurants near you")
            webbrowser.open("https://www.bing.com/search?q=restaurants+near+me&FORM=GEOTRI&isRef=1&showTw=1&isAutoP=1")
        if "what is love" in command:
            Speak("Love is a 7th sense that destroy all other senses")
        if 'open local disk c' in command:
            Speak("opening local disk C")
            webbrowser.open("C://")
        if 'open local disk d' in command:
            Speak("opening local disk D")
            webbrowser.open("D://")
        if 'open local disk e' in command:
            Speak("opening local disk E")
            webbrowser.open("E://")


             
