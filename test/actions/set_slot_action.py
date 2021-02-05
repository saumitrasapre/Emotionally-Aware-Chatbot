from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionSetSlot(Action):

    def name(self) -> Text:
        return "action_set_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        curr_intent = tracker.latest_message['intent'].get('name')
        pdf_slot = None
        gif_slot = None
        if curr_intent == "user_nightmares" or curr_intent == "ask_bot_scared":
            pdf_slot = "Insomnia 2"
            gif_slot = "scared"
        elif curr_intent == "user_tensed":
            pdf_slot = "Insomnia 1"
            gif_slot = "night"  # "@seizetheawkward mental health"
        elif curr_intent == "user_irregular_lifestyle":
            pdf_slot = "Insomnia 3"
            gif_slot = "night"  # "@seizetheawkward mental health"
        elif curr_intent == "user_unhappy" or curr_intent == "user_heartbroken":
            gif_slot = "cute cat"
            pdf_slot = "Heartbreak heartbreak"

        return [SlotSet("Gif", value=gif_slot), SlotSet("Pdf", value=pdf_slot)]
