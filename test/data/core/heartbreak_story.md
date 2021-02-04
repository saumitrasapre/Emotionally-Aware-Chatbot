## heartbreak/sad path
* user_heartbroken OR user_unhappy
    - utter_heartbreak_pipeline_start
> check heartbreak branches

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
    - utter_heartbreak_vent_mild
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



# user_vent_1_not_better
> check_vent_1_user_feels_better
* deny
  - utter_heartbreak_vent_mild_not_better
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_heartbreak_vent_mild_not_better_1
> check_vent_1_user_walk 

# user_vent_1_not_better
> check_vent_1_user_walk
* affirm
  - utter_heartbreak_vent_mild_not_better_2
  - action_play_music

# user_vent_1_not_better
> check_vent_1_user_walk
* deny
  - utter_happy_pipeline_deny


# user_vent_2
> check heartbreak branches
* user_vent
    - utter_heartbreak_vent
    - user_heartbreak_intensity_input
    - form{"name":"user_heartbreak_intensity_input"}  
    - form{"name":null}
    - slot{"Heartbreak_Intensity":"2"}
    - utter_heartbreak_vent_moderate
    
    
# user_vent_3
> check heartbreak branches
* user_vent
    - utter_heartbreak_vent
    - user_heartbreak_intensity_input
    - form{"name":"user_heartbreak_intensity_input"}  
    - form{"name":null}
    - slot{"Heartbreak_Intensity":"3"}
    - utter_heartbreak_vent_extreme
    