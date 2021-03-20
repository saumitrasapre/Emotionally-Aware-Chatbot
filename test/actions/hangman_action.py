from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, FollowupAction
from misc_utils.hangman import get_word, display_hangman

# Global Variables for Hangman
word = ""
tries = 6
word_completion = "."
guessed = False
guessed_letters = []
guessed_words = []


class ActionPlayHangman(Action):

    def name(self) -> Text:
        return "action_play_Hangman"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global tries, word, word_completion, guessed, guessed_letters, guessed_words

        dispatcher.utter_message(text="Alright! Let's get started!")
        dispatcher.utter_message(text="You'll have 6 tries to guess this word")
        dispatcher.utter_message(display_hangman(tries))
        word = get_word()
        print(word)
        word_completion = "." * len(word)
        dispatcher.utter_message(text=word_completion)
        dispatcher.utter_message(text="❤" * tries)
        dispatcher.utter_message(text="Type in a letter or word")
        return [SlotSet("Hangman", None)]


class HangmanInput(FormAction):
    def name(self) -> Text:
        return "hangman_input"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["Hangman"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "Hangman": [
                self.from_text(intent=None)
            ]
        }

    @staticmethod
    def validate_Hangman(
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        global tries, word, word_completion, guessed, guessed_letters, guessed_words
        guess = str(tracker.latest_message.get('text')).upper()
        if not guessed and tries > 0:
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    dispatcher.utter_message(text="You already guessed the letter {}".format(guess))
                    dispatcher.utter_message(display_hangman(tries))
                    dispatcher.utter_message(text=word_completion)
                    dispatcher.utter_message(text="❤" * tries)
                    dispatcher.utter_message(text="Type in a letter or word")
                    return {"Hangman": None}
                elif guess not in word:
                    dispatcher.utter_message(text="{} is not in the word.".format(guess))
                    tries -= 1
                    guessed_letters.append(guess)
                    if tries <= 0:
                        dispatcher.utter_message(display_hangman(tries))
                        dispatcher.utter_message(text=word_completion)
                        return {"Hangman": "Lost"}
                    else:
                        dispatcher.utter_message(display_hangman(tries))
                        dispatcher.utter_message(text=word_completion)
                        dispatcher.utter_message(text="❤" * tries)
                        dispatcher.utter_message(text="Type in a letter or word")
                        return {"Hangman": None}
                else:
                    dispatcher.utter_message(text="Good job! {} is in the word!".format(guess))
                    guessed_letters.append(guess)
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "." not in word_completion:
                        guessed = True
                        return {"Hangman": word_completion}
                    else:
                        dispatcher.utter_message(display_hangman(tries))
                        dispatcher.utter_message(text=word_completion)
                        dispatcher.utter_message(text="❤" * tries)
                        dispatcher.utter_message(text="Type in a letter or word")
                        return {"Hangman": None}
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    dispatcher.utter_message(text="You already guessed the word {}".format(guess))
                    dispatcher.utter_message(display_hangman(tries))
                    dispatcher.utter_message(text=word_completion)
                    dispatcher.utter_message(text="❤" * tries)
                    dispatcher.utter_message(text="Type in a letter or word")
                    return {"Hangman": None}
                elif guess != word:
                    dispatcher.utter_message(text="{} is not the word.".format(guess))
                    tries -= 1
                    guessed_words.append(guess)
                    if tries <= 0:
                        dispatcher.utter_message(display_hangman(tries))
                        dispatcher.utter_message(text=word_completion)
                        return {"Hangman": "Lost"}
                    else:
                        dispatcher.utter_message(display_hangman(tries))
                        dispatcher.utter_message(text=word_completion)
                        dispatcher.utter_message(text="❤" * tries)
                        dispatcher.utter_message(text="Type in a letter or word")
                        return {"Hangman": None}
                else:
                    guessed = True
                    word_completion = word
                    return {"Hangman": word_completion}
        else:
            dispatcher.utter_message(text="Not a valid guess.")
            dispatcher.utter_message(display_hangman(tries))
            dispatcher.utter_message(text=word_completion)
            dispatcher.utter_message(text="❤" * tries)
            dispatcher.utter_message(text="Type in a letter or word")
            return {"Hangman": None}

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        global tries, word, word_completion, guessed, guessed_letters, guessed_words
        if guessed:
            dispatcher.utter_message(text="Congrats buddy, you guessed the word -- {}! You win! 😉".format(word.upper()))
        else:
            dispatcher.utter_message(text="Sorry, you ran out of tries. The word was {}. Better luck next time! 😅".format(word))
        word = ""
        tries = 6
        word_completion = "."
        guessed = False
        guessed_letters = []
        guessed_words = []
        return [SlotSet("Hangman", None)]
