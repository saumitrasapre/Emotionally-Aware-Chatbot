## say goodbye
* goodbye
  - utter_goodbye

## greet
* greet
  - utter_greet
 
## ask_bot_scared_story
* ask_bot_scared
  - action_set_slot
  - utter_insomnia_nightmares_joke
  - action_get_gif
    
## challenge_interaction
* bot_challenge
    - utter_iamabot
    - action_check_name
    - submit_hobby_form
    - form{"name":"submit_hobby_form"}
    - form{"name":null} 
* thank
    - utter_smile
  
## out_of_domain
* out_of_domain
    - action_custom_fallback
  
## freestyle_mode_story
* freestyle_mode
  - action_freestyle_mode
  - freestyle_input
  - form{"name":"freestyle_input"}  
  - form{"name":null}


## name_response
* provide_name
    - action_check_name
    - submit_hobby_form
    - form{"name":"submit_hobby_form"}
    - form{"name":null}
    - utter_greet
* user_happy
    - utter_happy_pipeline_start_1
    - action_set_sentiment  
    - submit_hobby_form
    - form{"name":"submit_hobby_form"}
    - form{"name":null}  
    - utter_happy_pipeline_start_2
> check_user_choice_happy

## thanks_response
* thank
    - utter_smile
  
## goodnight_response
* goodnight
    - utter_good_night

