## say goodbye
* goodbye
  - utter_goodbye
 
## ask_bot_scared_story
* ask_bot_scared
  - action_set_slot
  - utter_insomnia_nightmares_joke
  - action_get_gif
    
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
  
## goodnight_response
* goodnight
    - utter_good_night

