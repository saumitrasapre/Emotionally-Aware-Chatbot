from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
from database.mongo_database_connectivity import mongodataupdate, mongodataverify, mongohobbyupdate, mongohobbyretrieve


## Called when user inputs name in his own volition
## If name exists, retrieves and sets hobbies, else inserts name into db
class ActionCheckName(Action):

    def name(self) -> Text:
        return "action_check_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        rows = mongodataverify(str(tracker.latest_message['entities'][1]['value']))
        if rows == 0:
            mongodataupdate(str(tracker.latest_message['entities'][1]['value']))
            dispatcher.utter_message(
                "{}... That's a nice name!".format(str(tracker.latest_message['entities'][1]['value'])))
            return [SlotSet("Person_Name", value=str(tracker.latest_message['entities'][1]['value']))]
        else:
            hobby1, hobby2, hobby3 = mongohobbyretrieve(str(tracker.latest_message['entities'][1]['value']))
            dispatcher.utter_message(
                "Pleased to meet you, {}!".format(str(tracker.latest_message['entities'][1]['value'])))
            if hobby1 == "None" or hobby2 == "None" or hobby3 == "None":
                return [SlotSet("Person_Name", value=str(tracker.latest_message['entities'][1]['value']))]
            else:
                return [SlotSet("Person_Name", value=str(tracker.latest_message['entities'][1]['value'])),
                        SlotSet("Hobby1", value=str(hobby1)),
                        SlotSet("Hobby2", value=str(hobby2)),
                        SlotSet("Hobby3", value=str(hobby3)),
                        ]

## Called after bot asks user his/her name
## If name exists, retrieves and sets hobbies, else inserts name into db
class SubmitNameForm(FormAction):

    def name(self) -> Text:
        return "submit_name_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["Person_Name"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "Person_Name": [
                self.from_entity(
                    entity="Name", intent=["provide_name"]
                ),
            ]
        }

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:

        return []

    def validate_Person_Name(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        rows = mongodataverify(value)
        print(value)
        print(rows)
        if rows == 0:
            mongodataupdate(value)
            print(tracker.get_slot("Person_Name"))
            dispatcher.utter_message("{}... That's a nice name!".format(value))
            return {"Person_Name": value}
        else:
            hobby1, hobby2, hobby3 = mongohobbyretrieve(value)
            dispatcher.utter_message("Pleased to meet you, {}!".format(value))
            if hobby1 == "None" or hobby2 == "None" or hobby3 == "None":
                return {"Person_Name": value}
            else:
                return {"Person_Name": value, "Hobby1": hobby1, "Hobby2": hobby2, "Hobby3": hobby3}

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
        mongohobbyupdate(str(tracker.get_slot("Hobby1")), str(tracker.get_slot("Hobby2")),
                         str(tracker.get_slot("Hobby3")), str(tracker.get_slot("Person_Name")))
        dispatcher.utter_message(template="utter_smile")
        return []

    def validate_Hobby1(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        print(value)
        if value == "None":
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
        else:
            print("validate_Hobby2")
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
        else:
            print("validate_Hobby3")
            return {"Hobby1": tracker.get_slot("Hobby1"), "Hobby2": tracker.get_slot("Hobby2"), "Hobby3": value}

