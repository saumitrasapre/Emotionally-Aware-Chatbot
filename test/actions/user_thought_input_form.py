from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet


class UserThoughtInput(FormAction):
    def name(self) -> Text:
        return "user_thought_input"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["Thought"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "Thought": [
                self.from_text(intent=None)
            ]
        }

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        return [SlotSet("Thought", None)]
