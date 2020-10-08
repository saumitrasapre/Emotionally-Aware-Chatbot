# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import random
from typing import Any, Text, Dict, List, Union
from datetime import date
from rasa.core.events import Event
from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
from database_connectivity import dataupdate, dataverify, hobbyupdate, hobbyretrieve
from chitchat import fetchfact, fetchjoke, fetchgif, fetchdatefact


class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    @staticmethod
    def fetch_slots(dispatcher: CollectingDispatcher, tracker: Tracker) -> List[EventType]:
        """Collect slots that contain the user's name and hobbies."""

        slots = []

        for key in ("Person_Name", "Hobby1", "Hobby2", "Hobby3"):
            value = tracker.get_slot(key)
            if value is not None:
                slots.append(SlotSet(key=key, value=value))

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


class ActionCheerUpGif(Action):

    def name(self) -> Text:
        return "action_cheer_up_gif"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        meow = fetchgif("cute cat")
        dispatcher.utter_message(json_message={"animation": meow})

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
            return [SlotSet("Person_Name", value=str(tracker.latest_message['entities'][0]['value']))]
        else:
            hobby1, hobby2, hobby3 = hobbyretrieve(str(tracker.latest_message['entities'][0]['value']))
            dispatcher.utter_message(
                "Pleased to meet you, {}!".format(str(tracker.latest_message['entities'][0]['value'])))
            if hobby1 == "None" or hobby2 == "None" or hobby3 == "None":
                return [SlotSet("Person_Name", value=str(tracker.latest_message['entities'][0]['value']))]
            else:
                return [SlotSet("Person_Name", value=str(tracker.latest_message['entities'][0]['value'])),
                        SlotSet("Hobby1", value=str(hobby1)),
                        SlotSet("Hobby2", value=str(hobby2)),
                        SlotSet("Hobby3", value=str(hobby3)),
                        ]


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
            return {"Person_Name": value}
        else:
            hobby1, hobby2, hobby3 = hobbyretrieve(value)
            dispatcher.utter_message("Pleased to meet you, {}!".format(value))
            if hobby1 == "None" or hobby2 == "None" or hobby3 == "None":
                return {"Person_Name": value}
            else:
                return {"Person_Name": value, "Hobby1": hobby1, "Hobby2": hobby2, "Hobby3": hobby3}


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
                    entity="Hobby", intent=["provide_hobby"]
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
            ],

        }

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        hobbyupdate(str(tracker.get_slot("Hobby1")), 1, str(tracker.get_slot("Person_Name")))
        hobbyupdate(str(tracker.get_slot("Hobby2")), 2, str(tracker.get_slot("Person_Name")))
        hobbyupdate(str(tracker.get_slot("Hobby3")), 3, str(tracker.get_slot("Person_Name")))
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


class ActionCureBoredom(Action):

    def name(self) -> Text:
        return "action_cure_boredom"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # dispatcher.utter_message(json_message={"animation":"https://media3.giphy.com/media/H4DjXQXamtTiIuCcRU/giphy-downsized.gif?cid=ac92730c368j5vpcpw66knr02x3eizba55ht8u69mgu75hdf&rid=giphy-downsized.gif"})
        num = random.randint(1, 3)
        if num == 1:
            dispatcher.utter_message("Did you know that?")
            dispatcher.utter_message(fetchfact())
        elif num == 2:
            dispatcher.utter_message("Nothing like a joke to lighten the mood!")
            dispatcher.utter_message(fetchjoke())
        elif num == 3:
            today = date.strftime(date.today(), '%d %B')
            dispatcher.utter_message("Today is {} isn't it?".format(today))
            dispatcher.utter_message(fetchdatefact())

        return []
