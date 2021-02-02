from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet


# Global Variables for Lifestyle form
qtn_count = 0
lifestyle_score = 0
qtns = []

class ActionLaunchLifestyleForm(Action):

    def name(self) -> Text:
        return "action_launch_lifestyle_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global qtn_count, qtns
        dispatcher.utter_message(text="Okay, so I'm going to ask you a series of simple YES / NO questions")
        dispatcher.utter_message(text="Be sure to answer them truthfully! 😇")
        with open("lifestyle_qtns.txt") as file:
            qtns = [line.rstrip('\n') for line in file]
        print(qtns)
        dispatcher.utter_message(text=qtns[qtn_count])
        return [SlotSet("Lifestyle", None)]


class LifestyleInput(FormAction):
    def name(self) -> Text:
        return "lifestyle_input"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["Lifestyle"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "Lifestyle": [self.from_text(intent=None)]
        }

    # "Lifestyle": [self.from_intent(intent='affirm', value="True"),
    #               self.from_intent(intent='deny', value="False")],
    def validate_Lifestyle(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        global qtns, qtn_count, lifestyle_score
        print(value)
        print(qtn_count)
        print(tracker.latest_message['intent'].get('name'))
        text_intent = tracker.latest_message['intent'].get('name')
        if text_intent == "affirm" or text_intent == "deny":
            if qtn_count != len(qtns) - 1:
                if text_intent == "affirm":
                    lifestyle_score += 1
                qtn_count += 1
                dispatcher.utter_message(text=qtns[qtn_count])
                return {"Lifestyle": None}
            elif qtn_count >= len(qtns) - 1:
                if text_intent == "affirm":
                    lifestyle_score += 1
                return {"Lifestyle": text_intent}
        else:
            dispatcher.utter_message(text=qtns[qtn_count])
            return {"Lifestyle": None}

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        global qtns, qtn_count, lifestyle_score
        qtns = []
        qtn_count = 0

        if lifestyle_score < 2:
            print("Bad Lifestyle")
            lifestyle_score = 0
            return [SlotSet("Lifestyle_Type", value="Bad lifestyle")]
        elif 2 <= lifestyle_score < 4:
            print("Average lifestyle")
            lifestyle_score = 0
            return [SlotSet("Lifestyle_Type", value="Average lifestyle")]
        elif lifestyle_score >= 4:
            print("Good lifestyle")
            lifestyle_score = 0
            return [SlotSet("Lifestyle_Type", value="Good lifestyle")]
