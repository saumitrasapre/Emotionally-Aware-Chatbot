# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa.core.events import Event
from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from database_connectivity import dataupdate, dataverify
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType


class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    @staticmethod
    def fetch_slots(dispatcher: CollectingDispatcher, tracker: Tracker) -> List[EventType]:
        """Collect slots that contain the user's name and phone number."""

        slots = []
        value = tracker.get_slot("Person_Name")
        if value is not None:
            slots.append(SlotSet(key="Person_Name", value=value))
        return slots

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[EventType]:
        # the session should begin with a `session_started` event
        if str(tracker.get_slot("Person_Name")) == "None":
            dispatcher.utter_message(template="utter_iamabot")
            dispatcher.utter_message(template="utter_ask_Person_Name")
        else:
            dispatcher.utter_message("Pleased to meet you, {}!".format(str(tracker.get_slot("Person_Name"))))
            dispatcher.utter_message("How're you doing today?")
        events = [SessionStarted()]

        # any slots that should be carried over should come after the
        # `session_started` event
        events.extend(self.fetch_slots(dispatcher, tracker))

        # an `action_listen` should be added at the end as a user message follows
        events.append(ActionExecuted("action_listen"))

        return events


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


class ActionCheckName(Action):

    def name(self) -> Text:
        return "action_check_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        rows = dataverify(str(tracker.latest_message['entities'][0]['value']))
        if rows == 0:
            dataupdate(str(tracker.latest_message['entities'][0]['value']))
            dispatcher.utter_message(
                "{}... That's a nice name!".format(str(tracker.latest_message['entities'][0]['value'])))
        else:
            dispatcher.utter_message(
                "Pleased to meet you, {}!".format(str(tracker.latest_message['entities'][0]['value'])))

        return [SlotSet("Person_Name", value=str(tracker.latest_message['entities'][0]['value']))]


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
        rows = dataverify(value)
        print(value)
        print(rows)
        if rows == 0:
            dataupdate(value)
            print(tracker.get_slot("Person_Name"))
            # SlotSet("Person_Name", value=tracker.get_slot("Person_Name"))
            dispatcher.utter_message("{}... That's a nice name!".format(value))
        else:
            dispatcher.utter_message("Pleased to meet you, {}!".format(value))

        return {"Person_Name": value}
