# Run this command in terminal  before executing this program
# rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
# and also run this in separate terminal
# rasa run actions

import requests

sender = "User"
bot_message = " "
while bot_message != "Bye!" and bot_message != "Goodbye!" and bot_message != "Arrivederci!" and bot_message != "G'day and bye!":
    message = input("You: ")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"sender": sender, "message": message})

    print("Bot says: ", end=' ')
    for i in r.json():
        if "text" in i:
            bot_message = i['text']
            print(f"{i['text']}")
        if "image" in i:
            bot_message = i['image']
            print(f"{i['image']}")
