from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from staticpdfs.pdfcreator import get_pdf


class ActionGetPDF(Action):

    def name(self) -> Text:
        return "action_get_pdf"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pdf_slot = tracker.get_slot("Pdf")
        slot_list = pdf_slot.split(" ")
        url = get_pdf(slot_list[0], slot_list[1])
        dispatcher.utter_message(json_message={"document": url})
        return [SlotSet("Pdf", value=None)]
