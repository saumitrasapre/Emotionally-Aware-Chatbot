from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
from database.mongo_database_connectivity import mongodataupdate, mongodataverify, mongohobbyupdate, mongohobbyretrieve
import ast


## Called after knowing the name of the user
## If name already exists, retrieves and sets hobbies
## Else asks hobbies one by one

class SubmitHobbyForm(FormAction):

    def name(self) -> Text:
        return "submit_hobby_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["Hobby1", "Hobby2", "Hobby3"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "Hobby1": [
                self.from_entity(
                    entity="Hobby", intent="provide_hobby"
                ),
            ],
            "Hobby2": [
                self.from_entity(
                    entity="Hobby", intent=["provide_hobby"]
                ),
            ],
            "Hobby3": [
                self.from_entity(
                    entity="Hobby", intent=["provide_hobby"]
                ),
            ]

        }

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        mongohobbyupdate(str(tracker.get_slot("Person_ID")), str(tracker.get_slot("Hobby1")),
                         str(tracker.get_slot("Hobby2")),
                         str(tracker.get_slot("Hobby3")))
        dispatcher.utter_message(template="utter_smile")
        return []

    def validate_Hobby1(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if value is None:
            return {"Hobby1": None, "Hobby2": None, "Hobby3": None}
        elif tracker.get_slot("Hobby1") == "fun things":
            return {"Hobby1": None, "Hobby2": None, "Hobby3": None}
        else:
            return {"Hobby1": value, "Hobby2": None, "Hobby3": None}

    def validate_Hobby2(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if value == tracker.get_slot("Hobby1") or value == tracker.get_slot("Hobby3"):
            return {"Hobby2": None}
        elif tracker.get_slot("Hobby2") == "fun things":
            return {"Hobby1": tracker.get_slot("Hobby1"), "Hobby2": None, "Hobby3": None}
        else:
            return {"Hobby1": tracker.get_slot("Hobby1"), "Hobby2": value, "Hobby3": None}

    def validate_Hobby3(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if value == tracker.get_slot("Hobby1") or value == tracker.get_slot("Hobby2"):
            return {"Hobby3": None}
        elif tracker.get_slot("Hobby3") == "fun things":
            return {"Hobby1": tracker.get_slot("Hobby1"), "Hobby2": tracker.get_slot("Hobby2"), "Hobby3": None}
        else:
            return {"Hobby1": tracker.get_slot("Hobby1"), "Hobby2": tracker.get_slot("Hobby2"), "Hobby3": value}
