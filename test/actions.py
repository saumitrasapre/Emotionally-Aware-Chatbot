# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
import random
from typing import Any, Text, Dict, List, Union
from datetime import date
from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType, FollowupAction
from database.mongo_database_connectivity import mongodataupdate, mongodataverify, mongohobbyupdate, mongohobbyretrieve
from chitchat import fetchfact, fetchjoke, fetchgif, fetchdatefact, fetchmusic
from spotify_utils.create_playlist import createplaylist
from madlibs import generate_text, generate_madlib
from misc_utils.tictactoe import *
from staticpdfs.pdfcreator import get_pdf

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

# Global Variables for TicTacToe
boards = [' ' for x in range(10)]

# Global Variables for Lifestyle form
qtn_count = 0
lifestyle_score = 0
qtns = []


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


class ActionSetSlot(Action):

    def name(self) -> Text:
        return "action_set_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        curr_intent = tracker.latest_message['intent'].get('name')
        pdf_slot = None
        gif_slot = None
        if curr_intent == "user_nightmares" or curr_intent == "ask_bot_scared":
            pdf_slot = "Insomnia 2"
            gif_slot = "nightmares"
        elif curr_intent == "user_tensed":
            pdf_slot = "Insomnia 1"
            gif_slot = "@seizetheawkward mental health"
        elif curr_intent == "user_irregular_lifestyle":
            pdf_slot = "Insomnia 3"
            gif_slot = "@seizetheawkward mental health"
        elif curr_intent == "mood_unhappy":
            gif_slot = "cute cat"
            pdf_slot = None

        return [SlotSet("Gif", value=gif_slot), SlotSet("Pdf", value=pdf_slot)]


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
            return [FollowupAction('mad_lib_input'), SlotSet("MadLib", None)]


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
                # output = generate_audio(final_sentences)
                # if output != "Error":
                #     dispatcher.utter_message("Let's listen to it... Shall we?")
                #     dispatcher.utter_message(json_message={"audio": output})
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
                # output = generate_audio(str(final_sentences))
                # if output != "Error":
                #     dispatcher.utter_message("Let's listen to it... Shall we?")
                #     dispatcher.utter_message(json_message={"audio": output})
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


class ActionPlayTictactoe(Action):

    def name(self) -> Text:
        return "action_play_tictactoe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global boards

        dispatcher.utter_message(text="Alright! Let's get our game faces on!")
        dispatcher.utter_message(text="Here's our board...")
        dispatcher.utter_message(printBoard(boards))
        dispatcher.utter_message(text="You'll have to fill in the board positions with numbers...")
        dispatcher.utter_message(text="Type in a number between 1-9 for the appropriate position")
        return [FollowupAction('tictactoe_input'), SlotSet("TicTacToe", None)]


class TicTacToeInput(FormAction):
    def name(self) -> Text:
        return "tictactoe_input"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["TicTacToe"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "TicTacToe": [
                self.from_text(intent=None)
            ]
        }

    def validate_TicTacToe(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        global boards
        if not isBoardFull(boards):
            if not isWinner(boards, 'O'):
                num = tracker.latest_message.get('text')
                boards, move = playerMove(boards, str(num))
                dispatcher.utter_message(str(move))
                strs = printBoard(boards)
                dispatcher.utter_message(strs)
                if move != 'Oops...This space is already occupied! Try again':
                    if not isBoardFull(boards):
                        if not isWinner(boards, 'X'):
                            boards, num = compMove(boards)
                            boards = insertLetter(boards, 'O', num)
                            dispatcher.utter_message(
                                'I placed an \'O\' at position number {}... Your turn! :'.format(str(num)))
                            dispatcher.utter_message(printBoard(boards))
                            return {"TicTacToe": None}
                        else:
                            dispatcher.utter_message('You won! Good Job!')
                            return {"TicTacToe": tracker.latest_message.get('text')}
                    else:
                        dispatcher.utter_message("Awww dang! It's a tie!")
                        return {"TicTacToe": tracker.latest_message.get('text')}
            else:
                dispatcher.utter_message('Sorry! I won ! Better luck next time, buddy')
                return {"TicTacToe": tracker.latest_message.get('text')}
        else:
            dispatcher.utter_message("Awww dang! It's a tie!")
            return {"TicTacToe": tracker.latest_message.get('text')}

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        global boards
        boards = [' ' for x in range(10)]
        return [SlotSet("TicTacToe", None)]


class ActionPlayMusic(Action):

    def name(self) -> Text:
        return "action_play_music"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Here's a playlist that I've prepared for you!")
        user_sentiment = tracker.slots["Sentiment"]
        if str(user_sentiment[0]) == 'neg':
            mood = (1 - user_sentiment[1]) + 0.01
        else:
            mood = float("{:.2f}".format(random.uniform(0.0, 1.0)))
        url = createplaylist(mood)
        dispatcher.utter_message(url)
        return []


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


class UserThoughtInput(FormAction):
    def name(self) -> Text:
        return "user_thought_input"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["Thought"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "Thought": [
                self.from_text(intent=None)
            ]
        }

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        return [SlotSet("Thought", None)]


class ActionGetPDF(Action):

    def name(self) -> Text:
        return "action_get_pdf"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pdf_slot = tracker.get_slot("Pdf")
        slot_list = pdf_slot.split(" ")
        url = get_pdf(slot_list[0], slot_list[1])
        dispatcher.utter_message(json_message={"document": url})
        return [SlotSet("Pdf", value=None)]


class ActionGetGif(Action):

    def name(self) -> Text:
        return "action_get_gif"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        gif_text = tracker.get_slot("Gif")
        if gif_text == 'nightmares':
            gif_text = "scared"
        gif = fetchgif(str(gif_text))
        dispatcher.utter_message(json_message={"animation": gif})
        return [SlotSet("Gif", value=None)]


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
        return [FollowupAction('lifestyle_input'), SlotSet("Lifestyle", None)]


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
            if qtn_count != len(qtns)-1:
                if text_intent == "affirm":
                    lifestyle_score += 1
                qtn_count += 1
                dispatcher.utter_message(text=qtns[qtn_count])
                return {"Lifestyle": None}
            elif qtn_count >= len(qtns)-1:
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
            return [SlotSet("Lifestyle_Type", value=False)]
        elif 2 <= lifestyle_score < 4:
            print("Average lifestyle")
            lifestyle_score = 0
            return [ SlotSet("Lifestyle_Type", value=True)]
        elif lifestyle_score >= 4:
            print("Good lifestyle")
            lifestyle_score = 0
            return [ SlotSet("Lifestyle_Type", value=True)]
