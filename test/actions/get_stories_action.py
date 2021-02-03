import random
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from spotify_utils.podcasts import get_podcasts


class ActionGetStories(Action):

    def name(self) -> Text:
        return "action_get_stories"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        search_list = ['sleep stories', 'bedtime stories']
        name, publisher, description, podcast_url = get_podcasts(search_list)
        dispatcher.utter_message("Here's some stories to choose from!")
        # dispatcher.utter_message("They're from a podcast called {} by {}".format(name, publisher))
        dispatcher.utter_message(podcast_url)
        return []
