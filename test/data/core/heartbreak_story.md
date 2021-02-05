## heartbreak/sad path
* user_heartbroken OR user_unhappy
    - utter_heartbreak_pipeline_start
    - action_set_slot
    - action_set_sentiment
> check_heartbreak_branches

# user_okay
> check_heartbreak_branches
* affirm
    - utter_happy_pipeline_deny

# user_vent_1
> check_heartbreak_branches
* user_vent
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

# user_vent_1_better
> check_vent_1_user_feels_better
* affirm
  - utter_heartbreak_vent_mild_better
  - action_cure_boredom
  - utter_heartbreak_conclusion
  - slot {"Pdf":"Heartbreak heartbreak"}
  - utter_pdf_msg
  - action_get_pdf

# user_vent_1_not_better
> check_vent_1_user_feels_better
* deny
  - utter_heartbreak_vent_mild_not_better
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_heartbreak_vent_mild_not_better_1
> check_vent_user_walk 

# user_vent_1_not_better
> check_vent_user_walk
* affirm
  - utter_heartbreak_vent_mild_not_better_2
  - action_play_music
  - utter_heartbreak_conclusion
  - slot{"Pdf":"Heartbreak heartbreak"}
  - utter_pdf_msg
  - action_get_pdf  

# user_vent_1_not_better
> check_vent_user_walk
* deny
  - utter_happy_pipeline_deny
  - utter_heartbreak_conclusion
  - slot{"Pdf":"Heartbreak heartbreak"}
  - utter_pdf_msg
  - action_get_pdf  
  
# user_vent_2
> check_heartbreak_branches
* user_vent
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

# user_vent_2_better
> check_vent_2_user_feels_better
* affirm
  - utter_heartbreak_vent_mild_better
  - action_cure_boredom
  - utter_heartbreak_vent_moderate_3
* provide_hobby
  - utter_heartbreak_vent_moderate_4
  - utter_heartbreak_vent_moderate_5
  - utter_heartbreak_conclusion
  - slot{"Pdf":"Heartbreak heartbreak"}
  - utter_pdf_msg
  - action_get_pdf  

# user_vent_2_not_better
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
  
# user_vent_3
> check_heartbreak_branches
* user_vent 
    - utter_heartbreak_vent
    - user_heartbreak_intensity_input
    - form{"name":"user_heartbreak_intensity_input"}  
    - form{"name":null}
    - slot{"Heartbreak_Intensity":"3"}
    - utter_heartbreak_vent_extreme
    