# this is our voice app
import speech_recognition as sr
import webbrowser as web
import pyttsx3 as pyt
import webbrowser
import getpass

print("welcoe tp mu rool")
print("speak you password")
r=sr.Recognizer()
pyt.speak("hi bhola")


passw=getpass.getpass("enterpass")
if passw =="pass":
    print("welcome to our home",end="")
    pyt.speak("hi bhola bhai what can i do for you")


    with sr.Microphone() as source:
        print("start saying..")
        audio=r.listen(source)
        print("okk thanks its compleate")
    change_api=r.recognize_google(audio)
    print("1)you can open site \n 2) you can play games \n 3) you can make image search  ")
    if (("please" in change_api)or("open" in change_api) and ("site" in change_api)or ("mysite" in change_api)):
        # print()
        # pyt.speak("welcome to fashion arth")
        web.open("https://fashionarth.com/")
    elif (("please" in change_api)or("open" in change_api) and ("game" in change_api)or ("" in change_api)):
        pass