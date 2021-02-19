## anxiety path
* user_tensed
    - utter_anxiety_pipeline
    - action_set_slot  
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
    - utter_anxiety_affirm_worried_affirm_affect_3 
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_anxiety_affirm_worried_affirm_affect_4
    - utter_anxiety_affirm_worried_affect_tool_1
> check_user_anxiety_tool_confused

## anxiety user affected by anxiety confused
> check_user_anxiety_tool_confused
* user_confused
  - utter_anxiety_affirm_worried_affect_tool_1.1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_anxiety_affirm_worried_affect_tool_2
* affirm
  - utter_anxiety_affirm_worried_affect_tool_2.1  
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}  
  - utter_anxiety_affirm_worried_affect_tool_3
* affirm
  - utter_anxiety_affirm_worried_affect_tool_3.1
> check_user_anxiety_promise

## anxiety user affected by anxiety not confused
> check_user_anxiety_tool_confused
* affirm
  - utter_anxiety_affirm_worried_affect_tool_2
* affirm
  - utter_anxiety_affirm_worried_affect_tool_2.1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}  
  - utter_anxiety_affirm_worried_affect_tool_3
* affirm
  - utter_anxiety_affirm_worried_affect_tool_3.1
> check_user_anxiety_promise

## anxiety user affected by anxiety affirm promise
> check_user_anxiety_promise
* affirm
  - utter_anxiety_affirm_worried_affect_tool_3.2
  - utter_session_conclusion
  - slot {"Pdf":"Anxiety anxiety1-1"}
  - utter_pdf_msg
  - action_get_pdf
  
## anxiety user deny path
> check_user_anxiety_promise
> check_user_anxiety_accept_or_deny_tools
* deny
  - utter_probe
> check_user_anxiety_promise
> check_user_anxiety_accept_or_deny_tools

## anxiety user deny idea path
> check_user_anxiety_hear_idea
* deny
  - utter_probe
> check_user_anxiety_hear_idea

## anxiety user not affected by anxiety
> check_user_anxiety_affect
* deny
  - utter_anxiety_affirm_worried_deny_affect_1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_anxiety_affirm_worried_deny_affect_2
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_anxiety_affirm_worried_deny_affect_3
> check_user_anxiety_accept_or_deny_tools  


## anxiety user not affected by anxiety show tools
> check_user_anxiety_accept_or_deny_tools
* affirm
  - utter_anxiety_affirm_worried_deny_affect_tool_1
* user_confused OR affirm
  - utter_anxiety_affirm_worried_deny_affect_tool_1.1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_anxiety_affirm_worried_deny_affect_tool_1.2
> check_user_anxiety_music_podcast_or_deny

## anxiety user not affected by anxiety choose music
> check_user_anxiety_music_podcast_or_deny
* user_request_music
  - action_play_music
  - utter_anxiety_affirm_worried_deny_affect_tool_2
> check_user_anxiety_continue_tools

## anxiety user not affected by anxiety choose podcast
> check_user_anxiety_music_podcast_or_deny
* user_request_story
  - action_get_stories
  - utter_anxiety_affirm_worried_deny_affect_tool_2
> check_user_anxiety_continue_tools

## anxiety user not affected by anxiety deny music or podcast
> check_user_anxiety_music_podcast_or_deny
* deny OR affirm
  - utter_anxiety_affirm_worried_deny_affect_tool_2
> check_user_anxiety_continue_tools

## anxiety user not affected by anxiety continue tools
> check_user_anxiety_continue_tools
* user_confused OR affirm
  - utter_heartbreak_vent_moderate_5
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_anxiety_affirm_worried_deny_affect_tool_3
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null} 
  - utter_session_conclusion
  - slot {"Pdf":"Anxiety anxiety1-1"}
  - utter_pdf_msg
  - action_get_pdf
  
## anxiety user not uneasy
> check_user_uneasy
* deny
  - utter_anxiety_affirm_worried_1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_anxiety_deny_worried_1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_anxiety_deny_worried_2
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_anxiety_deny_worried_3
> check_user_anxiety_hear_idea  

## anxiety user not uneasy hear idea
> check_user_anxiety_hear_idea
* affirm OR user_confused
  - utter_anxiety_deny_worried_4
  - utter_anxiety_deny_worried_5
> check_user_anxiety_hear_story 

## anxiety user not uneasy hear story
> check_user_anxiety_hear_story
* affirm OR user_confused
  - utter_anxiety_deny_worried_story_1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_anxiety_deny_worried_story_2
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_anxiety_deny_worried_story_3
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_anxiety_deny_worried_story_4 
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_anxiety_deny_worried_after_story_1
> check_user_anxiety_after_story 

## anxiety user not uneasy not hear story
> check_user_anxiety_hear_story
* deny
  - utter_anxiety_deny_worried_after_story_1
> check_user_anxiety_after_story

## anxiety user not uneasy after story
> check_user_anxiety_after_story
* affirm
  - utter_anxiety_deny_worried_after_story_2
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_anxiety_deny_worried_after_story_3
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_anxiety_deny_worried_after_story_4
* affirm OR user_confused
  - utter_insomnia_anxiety_tool_2.1
  - utter_session_conclusion
  - slot {"Pdf":"Anxiety anxiety1-1"}
  - utter_pdf_msg
  - action_get_pdf  


