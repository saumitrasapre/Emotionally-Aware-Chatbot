# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


import random
from typing import Any, Text, Dict, List, Union
from datetime import date
from rasa.core.events import Event
from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
from mongo_database_connectivity import mongodataupdate, mongodataverify, mongohobbyupdate, mongohobbyretrieve
from chitchat import fetchfact, fetchjoke, fetchgif, fetchdatefact, fetchmusic
from create_playlist import createplaylist


# from database_connectivity import dataupdate, dataverify, hobbyupdate, hobbyretrieve


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


class ActionPlayMusic(Action):

    def name(self) -> Text:
        return "action_play_music"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Here's a playlist that I've prepared for you!")
        url = createplaylist()
        dispatcher.utter_message(url)
        return []


class ActionCheckName(Action):

    def name(self) -> Text:
        return "action_check_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        rows = mongodataverify(str(tracker.latest_message['entities'][0]['value']))
        if rows == 0:
            mongodataupdate(str(tracker.latest_message['entities'][0]['value']))
            dispatcher.utter_message(
                "{}... That's a nice name!".format(str(tracker.latest_message['entities'][0]['value'])))
            return [SlotSet("Person_Name", value=str(tracker.latest_message['entities'][0]['value']))]
        else:
            hobby1, hobby2, hobby3 = mongohobbyretrieve(str(tracker.latest_message['entities'][0]['value']))
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


class ActionCureBoredom(Action):

    def name(self) -> Text:
        return "action_cure_boredom"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        num = random.randint(1, 4)
        if num == 1:
            dispatcher.utter_message("Did you know?")
            dispatcher.utter_message(fetchfact())
        elif num == 2:
            dispatcher.utter_message("Nothing like a joke to lighten the mood!")
            dispatcher.utter_message(fetchjoke())
        elif num == 3:
            today = date.strftime(date.today(), '%d %B')
            dispatcher.utter_message("Today is {} isn't it?".format(today))
            dispatcher.utter_message(fetchdatefact())
        elif num == 4:
            dispatcher.utter_message("In the mood for some songs?")
            mydict = fetchmusic(2)
            album_name = mydict["album_name"]
            artist_name = mydict["artist_name"]
            track_name = mydict["track_name"]
            url = mydict["url"]
            genre = mydict["genre"]
            dispatcher.utter_message("I just found this awesome {} song called '{}' !".format(genre, track_name))
            if album_name == track_name:
                dispatcher.utter_message(
                    "It's from an album with the same name and is performed by {}".format(artist_name))
            else:
                dispatcher.utter_message(
                    "It's from an album called {}, performed by {}".format(album_name, artist_name))
            dispatcher.utter_message("Check it out here! {}".format(url))

        return []
