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
> check_user_anger_share_cause
* affirm OR user_confused
    - utter_heartbreak_vent_1
  
## angry path user doesn't share cause
> check_user_choice_anger_cause 
* deny OR user_no_talk
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
> check_user_calm_anger  

## angry path user doesn't share cause affirms idea user calm
> check_user_calm_anger 
* affirm OR user_confused 
  - utter_angry_user_no_share_affirm_idea_calm
> check_user_anger_share_cause


## angry path user doesn't share cause affirms idea user calm and doesnt share cause
> check_user_anger_share_cause 
> check_user_calm_anger
> check_user_choice_anger_walk
* deny OR user_no_talk
  - utter_angry_user_no_share_affirm_idea_no_calm_1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_angry_user_no_share_affirm_idea_no_calm_2
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_angry_user_no_share_affirm_idea_no_calm_3
  - utter_pdf_msg

  
## angry path user doesn't share cause denies idea
> check_user_choice_idea_anger 
* deny OR user_no_talk
  - utter_angry_user_no_share_deny_idea_1
> check_user_choice_anger_walk

## angry path user doesn't share cause denies idea goes for walk
> check_user_choice_anger_walk 
* affirm OR user_confused 
  - utter_angry_user_no_share_deny_idea_2
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_heartbreak_vent_mild_not_better_2
  - action_play_music
  - utter_angry_user_no_share_affirm_idea_3
> check_user_calm_anger  