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
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## ask for time zone long
* greet
  - utter_greet
* find_time_zone
  - utter_ask_location
* city_info
  - utter_finding-time_zone
  - action_show_time_zone
* thanks
  - utter_you_are_welcome
  - utter_goodbye  


## ask for time zone short
* greet
  - utter_greet
* find_time_zone_for_location
  - utter_finding-time_zone
  - action_show_time_zone
* thanks
  - utter_you_are_welcome
  - utter_goodbye 
## interactive_story_1
* greet
    - utter_greet
* find_time_zone
    - utter_ask_location
* city_info{"city": "Austin"}
    - slot{"city": "Austin"}
    - utter_finding-time_zone
    - action_show_time_zone
* thanks
    - utter_you_are_welcome
    - utter_goodbye
* goodbye
    - utter_goodbye
