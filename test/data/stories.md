## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
  

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - action_hello_world
  - utter_did_that_help
* deny
  - utter_sorry
  - utter_goodbye

## sad path 3
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - action_hello_world
  - utter_did_that_help
* affirm
  -utter_happy

## say goodbye
* goodbye
  - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* mood_unhappy{"Mood": "sad"}
    - slot{"Mood": "sad"}
    - utter_cheer_up
    - utter_did_that_help
* affirm
    - utter_happy
* goodbye
    - utter_goodbye


## initial_interaction
* bot_challenge
    - utter_iamabot
    - submit_name_form
    - form{"name":"submit_name_form"}
    - form{"name":null}  
 * thank
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* mood_unhappy{"Mood": "uneasy"}
    - slot{"Mood": "uneasy"}
    - utter_cheer_up
    - utter_did_that_help
* deny
    - action_hello_world
    - utter_did_that_help
* affirm
    - utter_happy
* goodbye
    - utter_goodbye

## out_of_domain
* out_of_domain
    - action_custom_fallback
    
    