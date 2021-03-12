import random
from typing import Any, Text, Dict, List
from datetime import date
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from chitchat import fetchfact, fetchjoke, fetchdatefact, fetchmusic, fetchgif


class ActionCureBoredom(Action):

    def name(self) -> Text:
        return "action_cure_boredom"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        num = random.randint(1, 5)
        if num == 1:
            dispatcher.utter_message("Did you know?")
            dispatcher.utter_message(fetchfact())
        elif num == 2:
            dispatcher.utter_message("Nothing like a joke to lighten the mood!")
            dispatcher.utter_message(fetchjoke())
        elif num == 3:
            today = date.strftime(date.today(), '%d %B')
            dispatcher.utter_message("Today is {} isn't it?".format(today))
            dispatcher.utter_message(fetchdatefact())
        elif num == 4:
            happy_list = ["cute cat", "kitten", "puppy", "cute racoon"]
            gif_num = random.randint(0, len(happy_list))
            gif = fetchgif(str(happy_list[gif_num]))
            dispatcher.utter_message(json_message={"animation": gif})
            dispatcher.utter_message("Ain't that cute? 🤗")
        elif num == 5:
            mydict = fetchmusic(2)
            album_name = mydict["album_name"]
            artist_name = mydict["artist_name"]
            track_name = mydict["track_name"]
            url = mydict["url"]
            genre = mydict["genre"]
            dispatcher.utter_message("I just found this awesome {} song called '{}' !".format(genre, track_name))
            if album_name == track_name:
                dispatcher.utter_message(
                    "It's from an album with the same name and is performed by {}".format(artist_name))
            else:
                dispatcher.utter_message(
                    "It's from an album called {}, performed by {}".format(album_name, artist_name))
            dispatcher.utter_message("Check it out here! {}".format(url))

        return []
