from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, FollowupAction
from misc_utils.tictactoe import *

# Global Variables for TicTacToe
boards = [' ' for x in range(10)]


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
