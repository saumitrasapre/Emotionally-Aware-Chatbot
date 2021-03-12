from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet,FollowupAction
from madlibs import generate_text, generate_madlib

# Global Variables for Mad Libs
y = 0
count = 0
fieldss = []
replacementss = []
nums = 0
titles = ""
texts = ""
madlibs = ""
final_sentences = ""


class ActionPreMadLibs(Action):

    def name(self) -> Text:
        return "action_pre_madlibs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("I'll now ask you to give me some words, and you'll type them up!")
        dispatcher.utter_message("We'll fill in random blanks, and cook up a funny story!")
        dispatcher.utter_message("Let the fun begin!")
        global fieldss, nums, titles, texts, madlibs, replacementss, final_sentences, y, count
        y = 0
        count = 0
        fieldss, nums, titles, texts = generate_text()
        if nums == 1 or nums == 2:
            fieldss, madlibs = generate_madlib(texts)
            replacementss = []
            final_sentences = ""
            dispatcher.utter_message("Enter a {} ".format(fieldss[y]))
            y += 1
            return [FollowupAction('mad_lib_input'), SlotSet("MadLib", None)]
        elif nums == 3:
            dispatcher.utter_message("Enter a {} ".format(fieldss[y]))
            final_sentences += str(texts[count])
            count += 1
            y += 1
            return [SlotSet("MadLib", None)]


class MadLibInput(FormAction):

    def name(self) -> Text:
        return "mad_lib_input"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["MadLib"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "MadLib": [
                self.from_text(intent=None)
            ]
        }

    def validate_MadLib(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        global fieldss, nums, titles, texts, madlibs, replacementss, final_sentences, y, count
        print(y)
        if nums == 1 or nums == 2:
            if y != len(fieldss):
                replacementss.append(tracker.latest_message["text"])
                dispatcher.utter_message("Enter a {} ".format(fieldss[y]))
                y += 1
                return {"MadLib": None}
            else:
                return {"MadLib": tracker.latest_message["text"]}
        elif nums == 3:
            if y != len(fieldss):
                final_sentences += tracker.latest_message["text"]
                dispatcher.utter_message("Enter a {} ".format(fieldss[y]))
                y += 1
                final_sentences += str(texts[count])
                count += 1
                return {"MadLib": None}
            else:
                final_sentences += tracker.latest_message["text"]
                while count != len(texts) - 1:
                    final_sentences += str(texts[count])
                    count += 1
                return {"MadLib": tracker.latest_message["text"]}

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        global fieldss, nums, titles, texts, madlibs, replacementss, final_sentences, y, count
        dispatcher.utter_message("Okay! We're done!")
        if nums == 1 or nums == 2:
            replacementss.append(tracker.latest_message["text"])
            if y == len(fieldss):
                print(replacementss)
                i = 0
                for s in madlibs.split():
                    if s.find('<') != -1:
                        s = s.replace(s, replacementss[i])
                        i += 1
                    final_sentences += " {}".format(s)
                if titles != "Mad-Lib":
                    dispatcher.utter_message("This Mad Lib is an excerpt from the book {}".format(titles))
                else:
                    dispatcher.utter_message("Let's see what we have!")
                dispatcher.utter_message(final_sentences)
                y = 0
                count = 0
                fieldss = []
                replacementss = []
                nums = 0
                titles = ""
                texts = ""
                madlibs = ""
                final_sentences = ""
                return []
            else:
                return [SlotSet("MadLib", None)]
        if nums == 3:
            if y == len(fieldss):
                dispatcher.utter_message("This Mad Lib is titled: {}".format(titles))
                dispatcher.utter_message(final_sentences)
                y = 0
                count = 0
                fieldss = []
                replacementss = []
                nums = 0
                titles = ""
                texts = ""
                madlibs = ""
                final_sentences = ""
                return []
            else:
                return [SlotSet("MadLib", None)]
