# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType, FollowupAction
import ast
from database.mongo_database_connectivity import mongodataupdate, mongodataverify, mongohobbyupdate, mongohobbyretrieve


class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    @staticmethod
    def fetch_slots(dispatcher: CollectingDispatcher, tracker: Tracker) -> List[EventType]:
        """Collect slots that contain the user's name and hobbies."""

        slots = []

        for key in ("Person_First_Name", "Person_Last_Name", "Person_ID", "Hobby1", "Hobby2", "Hobby3"):
            value = tracker.get_slot(key)
            if value is not None:
                slots.append(SlotSet(key=key, value=value))
        if tracker.get_slot("Person_First_Name") is None or tracker.get_slot(
                "Person_Last_Name") is None or tracker.get_slot("Person_ID") is None:
            message_metadata = []
            events = tracker.current_state()['events']
            for e in events:
                if e['event'] == 'user' or e['event'] == 'session_started':
                    message_metadata.append(e)
            meta = message_metadata[-1]["metadata"]["metadata"]
            meta_dict = ast.literal_eval(meta)
            print(meta_dict)
            per_id = meta_dict["id"]
            fname = meta_dict["first_name"]
            lname = meta_dict["last_name"]
            slots.append(SlotSet(key="Person_ID", value=str(per_id)))
            slots.append(SlotSet(key="Person_First_Name", value=fname))
            slots.append(SlotSet(key="Person_Last_Name", value=lname))
            if mongodataverify(str(per_id)) == 0:
                mongodataupdate(str(per_id), str(fname), str(lname))
            elif mongodataverify(str(per_id)) == 1:
                hobby1, hobby2, hobby3 = mongohobbyretrieve(str(per_id))
                if hobby1 is not None and hobby2 is not None and hobby3 is not None:
                    slots.append(SlotSet(key="Hobby1", value=str(hobby1)))
                    slots.append(SlotSet(key="Hobby2", value=str(hobby2)))
                    slots.append(SlotSet(key="Hobby3", value=str(hobby3)))
        return slots

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[EventType]:
        # the session should begin with a `session_started` event
        message_metadata = []
        events = tracker.current_state()['events']
        for e in events:
            if e['event'] == 'user' or e['event'] == 'session_started':
                message_metadata.append(e)
        meta = message_metadata[-1]["metadata"]["metadata"]
        meta_dict = ast.literal_eval(meta)
        per_id = meta_dict["id"]
        fname = meta_dict["first_name"]
        lname = meta_dict["last_name"]
        events = [SessionStarted()]
        dispatcher.utter_message(template="utter_iamabot")
        dispatcher.utter_message("Pleased to meet you, {}!".format(fname))
        dispatcher.utter_message("How're you doing today?")
        # any slots that should be carried over should come after the
        # `session_started` event
        events.extend(self.fetch_slots(dispatcher, tracker))

        # an `action_listen` should be added at the end as a user message follows
        events.append(ActionExecuted("action_listen"))

        return events


class ActionCustomFallback(Action):

    def name(self) -> Text:
        return "action_custom_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_custom")

        return [UserUtteranceReverted()]
