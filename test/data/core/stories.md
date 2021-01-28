## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - action_set_slot
  - action_set_sentiment
  - utter_cheer_up
  - action_get_gif
  - utter_did_that_help
* affirm
  - utter_happy
  

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - action_set_slot
  - action_set_sentiment
  - utter_cheer_up
  - action_get_gif
  - utter_did_that_help
* deny
  - action_play_music
  - utter_did_that_help
* deny
  - utter_sorry

## sad path 3
* greet
  - utter_greet
* mood_unhappy
  - action_set_slot
  - action_set_sentiment
  - utter_cheer_up
  - action_get_gif
  - utter_did_that_help
* deny
  - action_play_music
  - utter_did_that_help
* affirm
  -utter_happy

## say goodbye
* goodbye
  - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* mood_unhappy
    - action_set_slot
    - action_set_sentiment
    - utter_cheer_up
    - action_get_gif
    - utter_did_that_help
* affirm
    - utter_happy
* goodbye
    - utter_goodbye

    
## initial_challenge_interaction
* bot_challenge
    - utter_iamabot
    - submit_name_form
    - form{"name":"submit_name_form"}
    - form{"name":null} 
    - submit_hobby_form
    - form{"name":"submit_hobby_form"}
    - form{"name":null} 
 * thank
    - utter_smile

## interactive_story_2
* greet
    - utter_greet
* mood_unhappy{"Mood": "uneasy"}
    - action_set_slot
    - action_set_sentiment
    - slot{"Mood": "uneasy"}
    - utter_cheer_up
    - action_get_gif
    - utter_did_that_help
* deny
    - action_play_music
    - utter_did_that_help
* affirm
    - utter_happy
* goodbye
    - utter_goodbye

## out_of_domain
* out_of_domain
    - action_custom_fallback
  

## name_response
* provide_name
    - action_check_name
    - submit_hobby_form
    - form{"name":"submit_hobby_form"}
    - form{"name":null}
    - utter_greet
* mood_great
    - action_set_sentiment
    - utter_happy_pipeline_start
> check_user_choice_happy

## thanks_response
* thank
    - utter_smile
