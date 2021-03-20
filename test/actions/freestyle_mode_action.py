from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, FollowupAction
from misc_utils.nmt_post import get_nmt_response


class ActionFreestyleMode(Action):

    def name(self) -> Text:
        return "action_freestyle_mode"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Running in freestyle mode...")
        dispatcher.utter_message(text="Ask me something... My responses are not gonna be coherent tho... Type "
                                      "`Cancel` to quit")
        return [SlotSet("Freestyle", value=None)]


class FreestyleInput(FormAction):
    def name(self) -> Text:
        return "freestyle_input"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["Freestyle"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "Freestyle": [self.from_text(intent=None)]
        }

    def validate_Freestyle(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        slot_value = str(tracker.get_slot("Freestyle"))
        user_input = tracker.latest_message.get('text')
        if str(user_input).lower() == 'cancel':
            return {"Freestyle": user_input}
        else:
            reply = get_nmt_response(user_input)
            dispatcher.utter_message(text=reply)
            return {"Freestyle": None}

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        user_input = tracker.latest_message.get('text')
        dispatcher.utter_message(text="Returning to normal mode...")
        return [SlotSet("Freestyle", value=user_input)]
