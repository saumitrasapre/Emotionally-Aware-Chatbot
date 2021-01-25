from gtts import gTTS
from playsound import playsound

myText = "Hey! I'm your personal chat buddy!"

language = 'en'

# Pass the text and language to the engine
# Mark slow = False indicating that the converted audio must have a high speed

myObj = gTTS(text=myText, lang=language)

# Save the converted audio to an mp3 file

myObj.save("Hello.mp3")

# Play the converted file
playsound('Hello.mp3')
