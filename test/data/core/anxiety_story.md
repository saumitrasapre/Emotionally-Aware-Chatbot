## anxiety path
* user_tensed
    - utter_anxiety_pipeline
    - action_set_sentiment
> check_user_uneasy

## anxiety user uneasy
> check_user_uneasy
* affirm
    - utter_anxiety_affirm_worried_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_anxiety_affirm_worried_2
> check_user_anxiety_affect   
> check_user_anxiety_explanation    

## anxiety user explain
> check_user_anxiety_explanation
* user_confused
    - utter_anxiety_affirm_worried_explain
> check_user_anxiety_affect 

## anxiety user affected by anxiety
> check_user_anxiety_affect
* affirm
    - utter_anxiety_affirm_worried_affirm_affect_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_anxiety_affirm_worried_affirm_affect_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
     


## anxiety user not affected by anxiety
> check_user_anxiety_affect
* deny
    - utter_anxiety_affirm_worried_deny_affect

