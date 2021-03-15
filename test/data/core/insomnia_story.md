## insomnia path
* user_insomnia
    - utter_insomnia_pipeline_start_part_1
    - action_set_sentiment
    - action_set_slot
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_insomnia_pipeline_start_part_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_insomnia_pipeline_start_part_3
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}      
    - utter_insomnia_pipeline_start_2
> check_user_choice_insomnia

## quick solution
> check_user_choice_insomnia
* deny
  - utter_insomnia_pipeline_quick_solution

## sleep tools
> check_user_choice_insomnia
* affirm
  - utter_insomnia_pipeline_options
> check_user_insomnia_pipeline_options

## tension
> check_user_insomnia_pipeline_options
* user_tensed
  - action_set_sentiment
  - action_set_slot
  - utter_insomnia_anxiety
> insomnia_tension_user_check_anxiety

## tension_no_idea_anxiety
> insomnia_tension_user_check_anxiety
* deny OR user_confused
  - utter_insomnia_anxiety_explanation
  - utter_insomnia_anxiety_explanation_example
  - utter_stuck_return_from_games_example_3
> insomnia_tension_user_check_anxiety

## tension_affirm_anxiety
> insomnia_tension_user_check_anxiety
* affirm
  - utter_insomnia_after_anxiety_explanation
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_ask_thoughts
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_after_listening_to_thoughts
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_ask_reason
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_introduce_tools
> insomnia_tension_accept_or_deny_tools 

## tension_deny tools
> insomnia_tension_accept_or_deny_tools
* deny OR user_no_talk
  - utter_angry_user_no_share_affirm_idea_no_calm_1
  - utter_good_night
  
## tension_accept_tools
> insomnia_tension_accept_or_deny_tools
* affirm OR user_confused
  - utter_insomnia_anxiety_tool_1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_anxiety_tool_1.2
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_anxiety_tool_1.3
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_anxiety_tool_2
> insomnia_check_user_knows_to_do_list

## insomnia_check_to_do_list_deny
> insomnia_check_user_knows_to_do_list
* deny OR user_confused
  - utter_insomnia_anxiety_tool_2.1
  - utter_stuck_return_from_games_example_3
> insomnia_check_user_knows_to_do_list

## insomnia_check_to_do_list_affirm
> insomnia_check_user_knows_to_do_list
* affirm
  - utter_insomnia_anxiety_tool_2.2
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}  
  - utter_insomnia_anxiety_tool_3
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_anxiety_tool_3.1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_anxiety_tool_3.2
  - utter_insomnia_anxiety_tool_3.3
  - utter_insomnia_anxiety_tool_3.3
  - utter_insomnia_anxiety_tool_3.3
  - utter_insomnia_anxiety_tool_3.4
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}  
  - utter_insomnia_anxiety_tool_recap
> insomnia_tension_tools_understood  

## insomnia_tension_deny_understood
> insomnia_tension_tools_understood 
* deny
  - utter_probe
> insomnia_tension_tools_understood   

## Tension tools got it affirm
> insomnia_tension_tools_understood
* affirm
  - slot{"Pdf": "Insomnia 1"} 
  - utter_pdf_msg
  - action_get_pdf
  - action_get_gif  
  - utter_good_night
  
## Nightmares
> check_user_insomnia_pipeline_options
* user_nightmares
  - action_set_sentiment
  - action_set_slot
  - utter_insomnia_nightmares
> check_joke_or_tools

## Nightmares_joke
> check_joke_or_tools
* ask_bot_scared
  - utter_insomnia_nightmares_joke
  - action_get_gif  
  - utter_insomnia_nightmares_introduce_tools
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_ask_thoughts
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_nightmares_after_thoughts
> check_nightmare_accept_deny_tools 
  
## Nightmares_tools
> check_joke_or_tools
* affirm
  - utter_insomnia_nightmares_introduce_tools
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_ask_thoughts
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_nightmares_after_thoughts
> check_nightmare_accept_deny_tools 

## Nightmares_deny_tools
> check_nightmare_accept_deny_tools
* deny OR user_no_talk
  - utter_angry_user_no_share_affirm_idea_no_calm_1
  - utter_good_night


## Nightmares_affirm_tools
> check_nightmare_accept_deny_tools
* affirm OR user_confused
  - utter_insomnia_anxiety_tool_1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_anxiety_tool_1.2
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_anxiety_tool_1.3
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_nightmares_tool_2
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_nightmares_tool_2.1
> nightmares_tools_play_music_or_deny

## nightmares_tools_play_music
> nightmares_tools_play_music_or_deny
* affirm
  - action_play_music
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_nightmares_tool_3
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_nightmares_tool_3.1  
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_nightmares_tool_3.2 
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_nightmares_tool_recap
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}    
  - slot{"Pdf": "Insomnia 2"}
  - utter_pdf_msg
  - action_get_pdf
  - utter_good_night

## nightmares_tools_deny_music
> nightmares_tools_play_music_or_deny
* deny
  - utter_insomnia_nightmares_tool_3
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_nightmares_tool_3.1  
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_nightmares_tool_3.2 
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_nightmares_tool_recap
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}    
  - slot{"Pdf": "Insomnia 2"}
  - utter_pdf_msg
  - action_get_pdf
  - utter_good_night
  
## Lifestyle
> check_user_insomnia_pipeline_options
* user_irregular_lifestyle
  - action_set_sentiment
  - action_set_slot
  - utter_insomnia_lifestyle
> insomnia_lifestyle_user_affirm_or_deny_test

## Lifestyle_test_deny
> insomnia_lifestyle_user_affirm_or_deny_test
* deny OR user_no_talk
  - utter_angry_user_no_share_affirm_idea_no_calm_1
  - utter_good_night

## lifestyle_test_affirm_1
> insomnia_lifestyle_user_affirm_or_deny_test
* affirm
  - action_launch_lifestyle_form
  - lifestyle_input
  - form{"name":"lifestyle_input"}  
  - form{"name":null}
  - slot{"Lifestyle_Type":"Bad lifestyle"}
  - utter_insomnia_lifestyle_quote
  - utter_insomnia_lifestyle_bad
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}     
  - utter_insomnia_lifestyle_introduce_tools
> insomnia_lifestyle_user_affirm_or_deny_tools

## lifestyle_test_affirm_2
> insomnia_lifestyle_user_affirm_or_deny_test
* affirm
  - action_launch_lifestyle_form
  - lifestyle_input
  - form {"name":"lifestyle_input"}  
  - form{"name":null}
  - slot{"Lifestyle_Type":"Average lifestyle"}
  - utter_insomnia_lifestyle_quote
  - utter_insomnia_lifestyle_average
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}     
  - utter_insomnia_lifestyle_tools_3.1
> insomnia_lifestyle_user_affirm_or_deny_stories

## lifestyle_test_affirm_bad_tools_show
> insomnia_lifestyle_user_affirm_or_deny_tools
* affirm
  - utter_insomnia_lifestyle_tools_1
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}  
  - utter_insomnia_lifestyle_tools_2
> insomnia_lifestyle_user_affirm_or_deny_sounds

## lifestyle_test_affirm_bad_tools_affirm_sounds
> insomnia_lifestyle_user_affirm_or_deny_sounds
* affirm
  - action_play_music
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}      
  - utter_insomnia_lifestyle_tools_3
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}      
  - utter_insomnia_lifestyle_tools_3.1
> insomnia_lifestyle_user_affirm_or_deny_stories 

## lifestyle_test_affirm_bad_tools_deny_sounds
> insomnia_lifestyle_user_affirm_or_deny_sounds
* deny
  - utter_insomnia_lifestyle_tools_3
  - utter_insomnia_lifestyle_tools_3.1 
> insomnia_lifestyle_user_affirm_or_deny_stories 

## lifestyle_test_affirm_bad_tools_affirm_stories
> insomnia_lifestyle_user_affirm_or_deny_stories
* affirm
  - action_get_stories
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}      
  - utter_insomnia_lifestyle_tool_recap
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}      
  - slot{"Pdf": "Insomnia 3"}
  - utter_pdf_msg
  - action_get_pdf
  - action_get_gif  
  - utter_good_night

## lifestyle_test_affirm_bad_tools_deny_stories
> insomnia_lifestyle_user_affirm_or_deny_stories
* deny
  - utter_insomnia_lifestyle_tool_recap
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}      
  - slot{"Pdf": "Insomnia 3"}
  - utter_pdf_msg
  - action_get_pdf
  - action_get_gif  
  - utter_good_night  
  
## lifestyle_test_affirm_3
> insomnia_lifestyle_user_affirm_or_deny_test
* affirm
  - action_launch_lifestyle_form
  - lifestyle_input
  - form{"name":"lifestyle_input"}  
  - form{"name":null}
  - slot{"Lifestyle_Type":"Good lifestyle"}
  - utter_insomnia_lifestyle_good
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}      
  - slot{"Pdf": "Insomnia 3"}
  - utter_pdf_msg
  - action_get_pdf
  - action_get_gif  
  - utter_good_night
  
## insomnia_deny_things
> insomnia_lifestyle_user_affirm_or_deny_tools
* deny
  - utter_probe
> insomnia_lifestyle_user_affirm_or_deny_tools
