# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from database_connectivity import dataupdate, dataverify
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        mylink = "https://belarr.com/bakercat/"
        print("Mood", tracker.get_slot('Mood'))
        dispatcher.utter_template("utter_enchanced_cheer_up", tracker, link=mylink)
        # dispatcher.utter_message("utter_enchanced_cheer_up", tracker, link=mylink)

        # dispatcher.utter_message(text="Hello World!")

        return []


class ActionCustomFallback(Action):

    def name(self) -> Text:
        return "action_custom_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_template("utter_custom", tracker)
        # dispatcher.utter_message("utter_enchanced_cheer_up", tracker, link=mylink)

        return [UserUtteranceReverted()]


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
        # SlotSet("Person_Name":)
        rows= dataverify(str(tracker.get_slot("Person_Name")))
        if rows == 0:
            dataupdate(str(tracker.get_slot("Person_Name")))
            dispatcher.utter_message(template="utter_appreciate_name")
        else:
            dispatcher.utter_message("Hey! I know you, {}! Pardon my forgetfulness...".format(value))

        return {"Person_Name": value}
