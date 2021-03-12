## sick path
* user_sick
    - utter_angry_pipeline_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - action_set_sentiment
    - action_set_slot
    - utter_sick_pipeline_start_1
    - utter_sick_pipeline_start_2
> check_sick_user_choice 

## sick path user talk
> check_sick_user_choice
* user_vent
  - utter_sick_pipeline_talk
> check_sick_user_talk_choice

## sick path user talk vent
> check_sick_user_talk_choice
* user_vent
  - utter_sick_pipeline_talk_vent_1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_sick_pipeline_talk_vent_2
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_sick_pipeline_talk_vent_3
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_sick_pipeline_conclude
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_heartbreak_vent_mild_not_better_2
  - action_play_music

## sick path user talk check in
> check_sick_user_talk_choice
* user_general_check_in
  - utter_sick_pipeline_conclude
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_heartbreak_vent_mild_not_better_2
  - action_play_music
  
## sick path user feel better
> check_sick_user_choice
* user_sick_feel_better_request
  - utter_sick_pipeline_feel_better_1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_sick_pipeline_feel_better_2
  - utter_sick_pipeline_feel_better_3
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null} 
  - utter_sick_pipeline_feel_better_4
> check_sick_user_promise 

## sick path user affirms promise
> check_sick_user_promise
* affirm OR user_confused
  - utter_anxiety_affirm_worried_affect_tool_3.2
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null} 
  - utter_sick_pipeline_feel_better_5
  - action_cure_boredom  
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_sick_pipeline_feel_better_6
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_sick_pipeline_feel_better_7
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}  
  - utter_sick_pipeline_feel_better_8
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_sick_pipeline_feel_better_9
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null} 
  - utter_sick_pipeline_feel_better_10
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_pdf_msg

## sick path user affirms promise
> check_sick_user_promise
* deny OR user_no_talk
  - utter_probe
> check_sick_user_promise  