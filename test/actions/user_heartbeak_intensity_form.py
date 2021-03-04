from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet


class UserHBIntensityInput(FormAction):
    def name(self) -> Text:
        return "user_heartbreak_intensity_input"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["Heartbreak_Intensity"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "Heartbreak_Intensity": [
                self.from_text(intent=None)
            ]
        }

    def validate_Heartbreak_Intensity(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        slot_value = str(tracker.get_slot("Heartbreak_Intensity"))
        if '1' <= slot_value <= '5':
            return {"Heartbreak_Intensity": None}
        user_input = tracker.latest_message.get('text')
        print(user_input)
        if '1' <= user_input <= '3':
            return {"Heartbreak_Intensity": user_input}
        else:
            dispatcher.utter_message("Help me help you, buddy! Enter a number between 1 and 3...")
            return {"Heartbreak_Intensity": None}

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        user_input = tracker.latest_message.get('text')
        return [SlotSet("Heartbreak_Intensity", value=user_input)]
