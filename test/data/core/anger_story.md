## angry path
* user_angry
    - utter_angry_pipeline_1
    - action_set_sentiment  
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_angry_pipeline_2
* affirm
    - utter_angry_pipeline_3
> check_user_choice_anger_cause  

## angry path user shares cause
> check_user_choice_anger_cause 
* affirm OR user_confused
    - utter_heartbreak_vent_1
  
## angry path user doesn't share cause
> check_user_choice_anger_cause 
* deny 
  - utter_angry_user_no_share_1
  - action_cure_boredom
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null} 
  - utter_angry_user_no_share_2
  - utter_angry_user_no_share_3
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_angry_user_no_share_4
> check_user_choice_idea_anger

## angry path user doesn't share cause affirms idea
> check_user_choice_idea_anger 
* affirm OR user_confused 
  - utter_angry_user_no_share_affirm_idea_1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_angry_user_no_share_affirm_idea_2
* affirm
  - utter_angry_user_no_share_affirm_idea_3
  
## angry path user doesn't share cause denies idea
> check_user_choice_idea_anger 
* deny
  - utter_angry_user_no_share_deny_idea_1
