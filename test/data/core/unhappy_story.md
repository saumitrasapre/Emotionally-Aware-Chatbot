## unhappy path
* user_unhappy
    - utter_sorry
    - utter_unhappy_user_ask_talk  
    - action_set_slot
    - action_set_sentiment
> check_user_unhappy_interest_talk

## unhappy path deny talk
> check_user_unhappy_interest_talk
* deny OR user_no_talk
  - utter_unhappy_user_deny_talk_1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_unhappy_user_deny_talk_2
  - action_play_music
  - utter_goodbye


## unhappy path affirm talk
> check_user_unhappy_interest_talk
* affirm OR user_vent
  - utter_angry_pipeline_1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_unhappy_user_affirm_talk_1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_unhappy_user_affirm_talk_2
  - utter_unhappy_user_affirm_talk_3
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_unhappy_user_affirm_talk_4
> check_user_unhappy_keep_promise 

## unhappy path affirm talk affirm promise
> check_user_unhappy_keep_promise
* affirm
  - utter_anxiety_affirm_worried_affect_tool_3.2
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_unhappy_user_affirm_talk_5
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_unhappy_user_affirm_talk_6
  - action_play_music
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_session_conclusion
  - utter_pdf_msg

## unhappy path affirm talk deny promise
> check_user_unhappy_keep_promise
* deny
  - utter_probe
> check_user_unhappy_keep_promise  