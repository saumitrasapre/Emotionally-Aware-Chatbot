## heartbreak/sad path
* user_heartbroken OR user_unhappy
    - utter_heartbreak_pipeline_start
> check heartbreak branches

# user_okay
> check heartbreak branches
* affirm
    - utter_happy_pipeline_deny

# user_vent_1
> check heartbreak branches
* user_vent
    - utter_heartbreak_vent
    - user_heartbreak_intensity_input
    - form{"name":"user_heartbreak_intensity_input"}  
    - form{"name":null}
    - slot{"Heartbreak_Intensity":"1"}
    - utter_heartbreak_vent_mild

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
    