import random
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from create_playlist import createplaylist


class ActionPlayMusic(Action):

    def name(self) -> Text:
        return "action_play_music"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Here's a playlist that I've prepared for you!")
        user_sentiment = tracker.slots["Sentiment"]
        # if str(user_sentiment[0]) == 'neg':
        #     mood = (1 - user_sentiment[1]) + 0.01
        # else:
        mood = float("{:.2f}".format(random.uniform(0.0, 1.0)))
        url = createplaylist(mood)
        dispatcher.utter_message(url)
        return []
