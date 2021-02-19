from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import random


class ActionSetSlot(Action):

    def name(self) -> Text:
        return "action_set_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        curr_intent = tracker.latest_message['intent'].get('name')
        pdf_slot = tracker.get_slot("Pdf")
        gif_slot = tracker.get_slot("Gif")
        if curr_intent == "user_insomnia":
            pdf_slot = "Insomnia_pdf_pending"
            gif_slot = "scared"
        elif curr_intent == "user_nightmares" or curr_intent == "ask_bot_scared":
            pdf_slot = "Insomnia 2"
            gif_slot = "scared"
        elif curr_intent == "user_tensed":
            if pdf_slot == "Insomnia_pdf_pending":
                pdf_slot = "Insomnia 1"
                gif_slot = "night"  # "@seizetheawkward mental health"
            else:
                pdf_list = ["anxiety1-1", "anxiety1-2", "anxiety1-3"]
                randnum = random.randint(0,len(pdf_list)-1)
                gif_slot = "@seizetheawkward mental health"
                pdf_slot = "Anxiety {}".format(pdf_list[randnum])
        elif curr_intent == "user_irregular_lifestyle":
            pdf_slot = "Insomnia 3"
            gif_slot = "night"  # "@seizetheawkward mental health"
        elif curr_intent == "user_unhappy" or curr_intent == "user_heartbroken":
            gif_slot = "cute cat"
            pdf_slot = "Heartbreak heartbreak"
        elif curr_intent == "user_vent":
            gif_slot = "@looneytunes fall"
            pdf_slot = "Heartbreak heartbreak"
        elif curr_intent == "user_no_talk":
            gif_slot = "@seizetheawkward mental health"
            pdf_slot = "Heartbreak heartbreak"

        return [SlotSet("Gif", value=gif_slot), SlotSet("Pdf", value=pdf_slot)]
