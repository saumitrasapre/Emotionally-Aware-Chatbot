## angry path
* user_angry
    - utter_angry_pipeline_1
    - action_set_sentiment
    - action_set_slot  
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_angry_pipeline_2
* affirm
    - utter_angry_pipeline_3
> check_user_choice_anger_cause  

## angry path user shares cause 1
> check_user_choice_anger_cause
> check_user_anger_share_cause
* affirm OR user_confused
    - utter_heartbreak_vent_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_angry_user_share_cause
    - user_anger_intensity_input
    - form{"name":"user_anger_intensity_input"}  
    - form{"name":null}
    - slot{"Anger_Intensity":"1"}
    - utter_angry_user_level_1_start_1
> check_user_anger_if_shared_cause

## angry path user shares cause level 1 angry
> check_user_anger_if_shared_cause
* affirm OR user_confused
    - utter_angry_user_level_1_start_2
* affirm OR user_confused
    - utter_angry_user_level_1_example_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_angry_user_level_1_example_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_angry_user_level_1_example_3
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_1_example_4
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}  
    - utter_angry_user_level_1_example_5
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_1_continue_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - slot{"Anger_Intensity":"1"}
    - utter_angry_user_level_1_continue_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_1_continue_3
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_1_continue_4
    - utter_session_conclusion
    - utter_pdf_msg

## angry path user shares cause level 2 angry
> check_user_anger_if_shared_cause
* affirm OR user_confused
    - utter_angry_user_level_1_start_2
* affirm OR user_confused
    - utter_angry_user_level_1_example_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_angry_user_level_1_example_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_angry_user_level_1_example_3
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_1_example_4
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}  
    - utter_angry_user_level_1_example_5
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_1_continue_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - slot{"Anger_Intensity":"2"} 
    - utter_angry_user_level_1_continue_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_1_continue_3
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_1_continue_4
    - utter_session_conclusion
    - utter_pdf_msg


## angry path user shares cause level 3 angry
> check_user_anger_if_shared_cause
* affirm OR user_confused
    - utter_angry_user_level_1_start_2
* affirm OR user_confused
    - utter_angry_user_level_1_example_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_angry_user_level_1_example_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_angry_user_level_1_example_3
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_1_example_4
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}  
    - utter_angry_user_level_1_example_5
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_1_continue_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - slot{"Anger_Intensity":"3"}
    - utter_angry_user_level_3_cont_1  
* affirm
    - utter_angry_user_level_3_cont_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}     
    - utter_angry_user_level_3_cont_3
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_1_continue_3
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_1_continue_4
    - utter_session_conclusion
    - utter_pdf_msg
  
## angry deny path    
> check_user_anger_if_shared_cause
* deny
  - utter_probe
> check_user_anger_if_shared_cause

## angry path user shares cause 2
> check_user_choice_anger_cause
> check_user_anger_share_cause
* affirm OR user_confused
    - utter_heartbreak_vent_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_angry_user_share_cause
    - user_anger_intensity_input
    - form{"name":"user_anger_intensity_input"}  
    - form{"name":null}
    - slot{"Anger_Intensity":"2"}
    - utter_angry_user_level_2_begin_1
    - action_cure_boredom
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_no_share_2
    - utter_angry_user_level_2_begin_2
> check_user_anger_happy_place

## user knows happy place
> check_user_anger_happy_place
* affirm
  - utter_angry_user_level_2_begin_3
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_angry_user_level_2_begin_4
* affirm OR user_confused
  - utter_angry_user_level_1_start_1
> check_user_anger_if_shared_cause

## user doesnt know happy place
> check_user_anger_happy_place
* deny OR user_confused
  - utter_angry_user_level_2_happy_place_explain_1
* affirm OR user_confused
  - utter_angry_user_level_2_happy_place_explain_2
> check_user_anger_happy_place  

## angry path user shares cause 3
> check_user_choice_anger_cause
> check_user_anger_share_cause
* affirm OR user_confused
    - utter_heartbreak_vent_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_angry_user_share_cause
    - user_anger_intensity_input
    - form{"name":"user_anger_intensity_input"}  
    - form{"name":null}
    - slot{"Anger_Intensity":"3"}
    - utter_angry_user_level_3_initiate_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}     
    - utter_angry_user_level_3_initiate_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_2_begin_1
    - action_cure_boredom
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_no_share_2
    - utter_angry_user_level_2_begin_2
> check_user_anger_happy_place

## angry path user shares cause 4
> check_user_choice_anger_cause
> check_user_anger_share_cause
* affirm OR user_confused
    - utter_heartbreak_vent_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_angry_user_share_cause
    - user_anger_intensity_input
    - form{"name":"user_anger_intensity_input"}  
    - form{"name":null}
    - slot{"Anger_Intensity":"4"}
    - utter_angry_user_level_3_initiate_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}       
    - utter_angry_user_level_4_audio
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_4_beginning_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_4_beginning_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_3_cont_1  
* affirm
    - utter_angry_user_level_3_cont_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}     
    - utter_angry_user_level_4_cont_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_4_cont_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_1_continue_3
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_4_cont_3
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_session_conclusion
    - utter_pdf_msg

## angry path user shares cause 5
> check_user_choice_anger_cause
> check_user_anger_share_cause
* affirm OR user_confused
    - utter_heartbreak_vent_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_angry_user_share_cause
    - user_anger_intensity_input
    - form{"name":"user_anger_intensity_input"}  
    - form{"name":null}
    - slot{"Anger_Intensity":"5"}
    - utter_angry_user_level_3_initiate_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}       
    - utter_angry_user_level_4_audio
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}    
    - utter_angry_user_level_4_beginning_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_4_beginning_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}  
    - utter_angry_user_level_5_story_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_angry_user_level_5_story_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_angry_user_level_5_story_3
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_angry_user_level_5_story_4
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_3_cont_1
* affirm
    - utter_angry_user_level_3_cont_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_4_cont_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_5_story_5
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_angry_user_level_1_continue_3
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}       
    - utter_angry_user_level_1_continue_4
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_angry_user_level_5_ask
> check_user_angry_level_five_continue_advice  

## angry path user continues level 5 advice affirm
> check_user_angry_level_five_continue_advice
* affirm OR user_confused
  - utter_angry_user_level_2_happy_place_explain_1
* affirm OR user_confused
  - utter_angry_user_level_2_happy_place_explain_2
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}   
  - utter_angry_user_level_5_ask_continue
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_angry_user_level_4_cont_3
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_session_conclusion
  - utter_pdf_msg

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
> check_user_angry_level_five_continue_advice
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