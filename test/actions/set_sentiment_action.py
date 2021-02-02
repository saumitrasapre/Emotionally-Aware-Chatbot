from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionSetSentiment(Action):

    def name(self) -> Text:
        return "action_set_sentiment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pos = 0
        neg = 0
        neu = 0
        totposscore = 0
        totnegscore = 0
        totneuscore = 0
        finalscore = 0
        model_dict = tracker.latest_message['entities'][0]['value']
        for item in model_dict.items():
            if item[1]["Emotion"] == "Positive" or item[1]["Emotion"] == "Happy" or item[1]["Emotion"] == "Surprise":
                pos += 1
                totposscore += item[1]["Score"]
            elif item[1]["Emotion"] == "Negative" or item[1]["Emotion"] == "Angry" or item[1]["Emotion"] == "Sad" or \
                    item[1]["Emotion"] == "Fear":
                neg += 1
                totnegscore += abs(item[1]["Score"])
            elif item[1]["Emotion"] == 'Neutral':
                neu += 1
                totneuscore = abs(item[1]["Score"])
        # print("Pos: {}, Neg: {}, Neu: {}, PosScore: {}, NegScore: {}".format(pos, neg, neu, totposscore, totnegscore))
        # print(model_dict["Text2emotion"]["Emotion"])
        if pos >= 2:
            finalscore = totposscore / pos
        elif neg >= 2:
            finalscore = totnegscore / neg
        elif neu >= 2:
            finalscore = totneuscore / neu
        else:
            finalscore = model_dict["Text2emotion"]["Score"]

        return [SlotSet("Sentiment", value=[model_dict["Text2emotion"]["Emotion"], finalscore])]