from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from chitchat import fetchgif


class ActionGetGif(Action):

    def name(self) -> Text:
        return "action_get_gif"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        gif_text = tracker.get_slot("Gif")
        gif = fetchgif(str(gif_text))
        dispatcher.utter_message(json_message={"animation": gif})
        return [SlotSet("Gif", value=None)]