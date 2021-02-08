from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
from database.mongo_database_connectivity import mongodataupdate, mongodataverify, mongohobbyupdate, mongohobbyretrieve
import ast


## Called when user inputs name in his own volition
## If name exists, retrieves and sets hobbies, else inserts name into db
class ActionCheckName(Action):

    def name(self) -> Text:
        return "action_check_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message_metadata = []
        events = tracker.current_state()['events']
        for e in events:
            if e['event'] == 'user':
                message_metadata.append(e)
        meta = message_metadata[-1]["metadata"]["metadata"]
        meta_dict = ast.literal_eval(meta)
        per_id = meta_dict["id"]
        fname = meta_dict["first_name"]
        lname = meta_dict["last_name"]
        rows = mongodataverify(str(per_id))
        print(rows)
        if rows == 0:
            mongodataupdate(str(per_id), str(fname), str(lname))
            dispatcher.utter_message("{}... That's a nice name!".format(str(fname)))
            return [SlotSet("Person_ID", value=str(per_id)),
                    SlotSet("Person_First_Name", value=str(fname)),
                    SlotSet("Person_Last_Name", value=str(lname))]
        else:
            hobby1, hobby2, hobby3 = mongohobbyretrieve(str(per_id))
            dispatcher.utter_message("Pleased to meet you, {}!".format(str(fname)))
            if hobby1 is None or hobby2 is None or hobby3 is None:
                return [SlotSet("Person_ID", value=str(per_id)),
                        SlotSet("Person_First_Name", value=str(fname)),
                        SlotSet("Person_Last_Name", value=str(lname))]
            else:
                return [SlotSet("Person_ID", value=str(per_id)),
                        SlotSet("Person_First_Name", value=str(fname)),
                        SlotSet("Person_Last_Name", value=str(lname)),
                        SlotSet("Hobby1", value=str(hobby1)),
                        SlotSet("Hobby2", value=str(hobby2)),
                        SlotSet("Hobby3", value=str(hobby3)),
                        ]
