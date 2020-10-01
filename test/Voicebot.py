import speech_recognition as sr
import requests
from gtts import gTTS
from playsound import playsound
import os

bot_message = ""
message = ""
language = 'en'

r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})
print("Bot: ", end=' ')

for i in r.json():
    if "text" in i:
        bot_message = i['text']
        print(f"{i['text']}")
        myObj = gTTS(text=bot_message, lang=language)
        myObj.save("Hello.mp3")

        # Playing the converted file
        playsound('Hello.mp3')
        os.remove('Hello.mp3')
    if "image" in i:
        # bot_message = i['image']
        print(f"{i['image']}")



while bot_message != "Bye!" and bot_message != "Goodbye!" and bot_message != "Arrivederci!" and bot_message != "G'day and bye!":

    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)  # listen to the source
        try:
            message = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
            print("You: {}".format(message))

        except:
            print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly

    if len(message) == 0:
        continue
    print("Sending message now...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

    print("Bot: ", end=' ')

    for i in r.json():
        if "text" in i:
            bot_message = i['text']
            print(f"{i['text']}")
            myObj = gTTS(text=bot_message, lang=language)
            myObj.save("Hello.mp3")

            # Playing the converted file
            playsound('Hello.mp3')
            os.remove('Hello.mp3')
        if "image" in i:
            # bot_message = i['image']
            print(f"{i['image']}")


