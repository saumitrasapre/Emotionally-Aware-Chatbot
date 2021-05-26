## heartbreak path
* user_heartbroken
    - utter_heartbreak_pipeline_start
    - action_set_slot
    - action_set_sentiment
> check_heartbreak_branches

## user_okay
> check_heartbreak_branches
* affirm
    - utter_heartbreak_okay_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_heartbreak_okay_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_heartbreak_okay_3
    - action_play_music
    - utter_heartbreak_okay_4
    - utter_goodbye

## user_vent_1
> check_heartbreak_branches
> check_if_user_wants_to_talk
* user_vent
    - action_set_slot
    - slot{"Gif": "@looneytunes fall"}
    - utter_heartbreak_vent
    - user_heartbreak_intensity_input
    - form{"name":"user_heartbreak_intensity_input"}  
    - form{"name":null}
    - slot{"Heartbreak_Intensity":"1"}
    - utter_heartbreak_vent_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_heartbreak_vent_mild_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_heartbreak_vent_mild_2
* affirm
    - utter_heartbreak_vent_mild_3
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_heartbreak_vent_mild_4
> check_vent_1_user_feels_better

## user_vent_1_better
> check_vent_1_user_feels_better
* affirm
  - utter_heartbreak_vent_mild_better
  - action_cure_boredom
  - utter_session_conclusion
  - slot {"Pdf":"Heartbreak heartbreak"}
  - utter_pdf_msg
  - action_get_pdf

## user_vent_1_not_better
> check_vent_1_user_feels_better
* deny
  - utter_heartbreak_vent_mild_not_better
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_heartbreak_vent_mild_not_better_1
> check_vent_user_walk 

## user_vent_1_not_better
> check_vent_user_walk
* affirm
  - utter_heartbreak_vent_mild_not_better_2
  - action_play_music
  - utter_session_conclusion
  - slot{"Pdf":"Heartbreak heartbreak"}
  - utter_pdf_msg
  - action_get_pdf  

## user_vent_1_not_better
> check_vent_user_walk
* deny
  - utter_happy_pipeline_deny
  - utter_session_conclusion
  - slot{"Pdf":"Heartbreak heartbreak"}
  - utter_pdf_msg
  - action_get_pdf  
  
## user_vent_2
> check_heartbreak_branches
> check_if_user_wants_to_talk
* user_vent
    - action_set_slot
    - slot{"Gif": "@looneytunes fall"}
    - utter_heartbreak_vent
    - user_heartbreak_intensity_input
    - form{"name":"user_heartbreak_intensity_input"}  
    - form{"name":null}
    - slot{"Heartbreak_Intensity":"2"}
    - utter_heartbreak_vent_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_heartbreak_vent_moderate_1
* affirm
    - utter_heartbreak_vent_moderate_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_heartbreak_vent_mild_4
> check_vent_2_user_feels_better 

## user_vent_2_better
> check_vent_2_user_feels_better
* affirm
  - utter_heartbreak_vent_mild_better
  - action_cure_boredom
  - utter_heartbreak_vent_moderate_3
* provide_hobby OR affirm
  - utter_heartbreak_vent_moderate_4
  - utter_heartbreak_vent_moderate_5
  - utter_session_conclusion
  - slot{"Pdf":"Heartbreak heartbreak"}
  - utter_pdf_msg
  - action_get_pdf  

## user_vent_2_not_better
> check_vent_2_user_feels_better
* deny
  - utter_heartbreak_vent_mild_not_better
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_heartbreak_vent_moderate_not_better_1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_heartbreak_vent_moderate_not_better_2
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_heartbreak_vent_moderate_not_better_tool_1
* affirm
  - utter_heartbreak_vent_moderate_not_better_tool_1.1
* affirm
  - utter_heartbreak_vent_moderate_not_better_tool_2
* affirm
  - utter_heartbreak_vent_moderate_not_better_3
* affirm
  - utter_heartbreak_vent_moderate_not_better_tool_3 
> check_vent_user_walk   
  
## user_vent_3
> check_heartbreak_branches
> check_if_user_wants_to_talk
* user_vent
    - action_set_slot
    - slot{"Gif": "@looneytunes fall"} 
    - utter_heartbreak_vent
    - user_heartbreak_intensity_input
    - form{"name":"user_heartbreak_intensity_input"}  
    - form{"name":null}
    - slot{"Heartbreak_Intensity":"3"}
    - utter_heartbreak_vent_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_heartbreak_vent_moderate_1
* affirm
    - utter_heartbreak_vent_moderate_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_heartbreak_vent_extreme_1
* affirm
    - utter_heartbreak_vent_extreme_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_heartbreak_vent_extreme_3
    - utter_heartbreak_vent_extreme_4
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_heartbreak_vent_extreme_5
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_heartbreak_vent_extreme_6
    - utter_heartbreak_vent_extreme_7
    - action_get_gif  
    - utter_heartbreak_vent_extreme_8
    - utter_heartbreak_vent_extreme_tool_1
* affirm
    - utter_heartbreak_vent_extreme_tool_2
* affirm
    - utter_heartbreak_vent_mild_4
> check_vent_2_user_feels_better



## user_no_talk
> check_heartbreak_branches
* user_no_talk
  - action_set_slot
  - slot{"Gif": "@seizetheawkward mental health"}
  - utter_heartbreak_no_talk_1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_heartbreak_no_talk_2
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - action_get_gif  
  - utter_heartbreak_no_talk_3
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_heartbreak_no_talk_4
> check_if_user_wants_to_talk 

## user_no_talk_no_talk
> check_if_user_wants_to_talk
* affirm 
  - utter_heartbreak_vent_mild_not_better_2
  - action_play_music

## user_confused_heartbreak
> check_heartbreak_branches
* user_confused
  - utter_heartbreak_confused_1
  - utter_heartbreak_vent_1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null} 
  - utter_heartbreak_confused_2
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_heartbreak_refined
> check_heartbreak_branches  