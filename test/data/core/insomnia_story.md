## insomnia path
* user_insomnia
    - utter_insomnia_pipeline_start_1
    - action_set_sentiment
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
> insomnia_tension_user_affirm_or_confused

## tension_confused
> insomnia_tension_user_affirm_or_confused
* user_confused
  - utter_insomnia_anxiety_explanation
  - utter_insomnia_anxiety_explanation_example
  - utter_insomnia_after_anxiety_explanation
> insomnia_tension_user_accept_or_deny_bad_thoughts

## tension_affirm
> insomnia_tension_user_affirm_or_confused
* affirm
  - utter_insomnia_after_anxiety_explanation
> insomnia_tension_user_accept_or_deny_bad_thoughts 

## tension_affirm_bad_thoughts
> insomnia_tension_user_accept_or_deny_bad_thoughts
* affirm
  - utter_insomnia_ask_thoughts
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_after_listening_to_thoughts
>  insomnia_tension_user_reason_for_bad_thoughts 

## tension_deny_bad_thoughts
> insomnia_tension_user_accept_or_deny_bad_thoughts
* deny
  - utter_probe
  - utter_insomnia_ask_thoughts
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_after_listening_to_thoughts
>  insomnia_tension_user_reason_for_bad_thoughts 

## tension_reason_for_bad_thoughts_affirm
> insomnia_tension_user_reason_for_bad_thoughts
* affirm
  - utter_insomnia_ask_reason
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_introduce_tools

## tension_reason_for_bad_thoughts_deny
> insomnia_tension_user_reason_for_bad_thoughts
* deny
  - utter_probe
  - utter_insomnia_ask_reason
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_introduce_tools
> insomnia_tension_accept_or_deny_tools  
  
## tension_accept_or_deny tools
> insomnia_tension_accept_or_deny_tools
* affirm
  - utter_insomnia_anxiety_tool_1
* affirm
  - utter_insomnia_anxiety_tool_1.1
* affirm
  - utter_insomnia_anxiety_tool_1.2
* affirm
  - utter_insomnia_anxiety_tool_1.3
* affirm
  - utter_insomnia_anxiety_tool_2
* affirm
  - utter_insomnia_anxiety_tool_2.1
* affirm
  - utter_insomnia_anxiety_tool_3
* affirm
  - utter_insomnia_anxiety_tool_3.1
* affirm
  - utter_insomnia_anxiety_tool_3.2
  - utter_insomnia_anxiety_tool_3.3
  - utter_insomnia_anxiety_tool_3.3
  - utter_insomnia_anxiety_tool_3.3
  - utter_insomnia_anxiety_tool_3.4
* affirm   
  - utter_insomnia_anxiety_tool_recap
> insomnia_tension_tools_understood  
  
## Tension tools got it affirm
> insomnia_tension_tools_understood
* affirm
  - slot{"Pdf": "Insomnia 1"} 
  - utter_insomnia_tool_pdf_msg
  - action_get_pdf
  - action_get_gif  
  - utter_good_night

## Tension tools got it deny
> insomnia_tension_tools_understood
* deny
  - utter_probe
> insomnia_tension_tools_understood
  
  
## tension_accept_or_deny tools
> insomnia_tension_accept_or_deny_tools
* deny
  - utter_probe
> insomnia_tension_accept_or_deny_tools  

## nightmares
> check_user_insomnia_pipeline_options
* user_nightmares
  - action_set_sentiment
  - action_set_slot
  - utter_insomnia_nightmares
> check_joke_or_tools

## nightmares_joke
> check_joke_or_tools
* deny
  - utter_insomnia_nightmares_joke
  - action_get_gif  
  - utter_insomnia_nightmares_introduce_tools
> check_nightmare_accept_deny_bad_thoughts
  
## nightmares_tools
> check_joke_or_tools
* affirm
  - utter_insomnia_nightmares_introduce_tools
> check_nightmare_accept_deny_bad_thoughts

## nightmares_affirm_bad_thoughts
> check_nightmare_accept_deny_bad_thoughts
* affirm
  - utter_insomnia_ask_thoughts
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_insomnia_nightmares_after_thoughts
> check_nightmare_accept_deny_tools 

## nightmares_affirm_tools
> check_nightmare_accept_deny_tools
* affirm
  - utter_insomnia_nightmares_tool_1
* affirm
  - utter_insomnia_nightmares_tool_1.1
* affirm
  - utter_insomnia_nightmares_tool_1.2
* affirm
  - utter_insomnia_nightmares_tool_1.3
* affirm
  - utter_insomnia_nightmares_tool_2
* affirm
  - utter_insomnia_nightmares_tool_2.1
> nightmares_tools_play_music_or_deny

## nightmares_tools_play_music
> nightmares_tools_play_music_or_deny
* affirm
  - action_play_music
  - utter_insomnia_nightmares_tool_3
* affirm
  - utter_insomnia_nightmares_tool_3.1  
* affirm
  - utter_insomnia_nightmares_tool_3.2 
* affirm
  - utter_insomnia_nightmares_tool_3.3
* affirm
  - utter_insomnia_nightmares_tool_recap
> insomnia_nightmare_tools_understood  

## nightmares_tools_deny_music
> nightmares_tools_play_music_or_deny
* deny
  - utter_insomnia_nightmares_tool_3
* affirm
  - utter_insomnia_nightmares_tool_3.1  
* affirm
  - utter_insomnia_nightmares_tool_3.2 
* affirm
  - utter_insomnia_nightmares_tool_3.3
* affirm
  - utter_insomnia_nightmares_tool_recap
> insomnia_nightmare_tools_understood  
  
## Nightmare tools got it affirm
> insomnia_nightmare_tools_understood
* affirm
  - slot{"Pdf": "Insomnia 2"}
  - utter_insomnia_tool_pdf_msg
  - action_get_pdf
  - utter_good_night
  
## lifestyle
> check_user_insomnia_pipeline_options
* user_irregular_lifestyle
  - action_set_sentiment
  - action_set_slot
  - utter_insomnia_lifestyle
> insomnia_lifestyle_user_affirm_or_deny_test

## lifestyle_test_affirm
> insomnia_lifestyle_user_affirm_or_deny_test
* affirm
  - action_launch_lifestyle_form
  - lifestyle_input
  - form{"name":"lifestyle_input"}  
  - form{"name":null}
  - slot{"Lifestyle_Type":"Bad lifestyle"}
  - utter_insomnia_lifestyle_quote
  - utter_insomnia_lifestyle_bad  
  - utter_insomnia_lifestyle_introduce_tools
> insomnia_lifestyle_user_affirm_or_deny_tools

## lifestyle_test_affirm
> insomnia_lifestyle_user_affirm_or_deny_test
* affirm
  - action_launch_lifestyle_form
  - lifestyle_input
  - form {"name":"lifestyle_input"}  
  - form{"name":null}
  - slot{"Lifestyle_Type":"Average lifestyle"}
  - utter_insomnia_lifestyle_quote
  - utter_insomnia_lifestyle_average
  - utter_insomnia_lifestyle_tools_3.1
> insomnia_lifestyle_user_affirm_or_deny_stories

## lifestyle_test_affirm_bad_tools_show
> insomnia_lifestyle_user_affirm_or_deny_tools
* affirm
  - utter_insomnia_lifestyle_tools_1
* affirm
  - utter_insomnia_lifestyle_tools_2
  - utter_insomnia_lifestyle_tools_2.1
> insomnia_lifestyle_user_affirm_or_deny_sounds

## lifestyle_test_affirm_bad_tools_affirm_sounds
> insomnia_lifestyle_user_affirm_or_deny_sounds
* affirm
  - action_play_music
  - utter_insomnia_lifestyle_tools_3
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
  - utter_insomnia_lifestyle_tool_recap
  - slot{"Pdf": "Insomnia 3"}
  - utter_insomnia_tool_pdf_msg
  - action_get_pdf
  - action_get_gif  
  - utter_good_night

## lifestyle_test_affirm_bad_tools_deny_stories
> insomnia_lifestyle_user_affirm_or_deny_stories
* deny
  - utter_insomnia_lifestyle_tool_recap
  - slot{"Pdf": "Insomnia 3"}
  - utter_insomnia_tool_pdf_msg
  - action_get_pdf
  - action_get_gif  
  - utter_good_night  
  
## lifestyle_test_affirm
> insomnia_lifestyle_user_affirm_or_deny_test
* affirm
  - action_launch_lifestyle_form
  - lifestyle_input
  - form{"name":"lifestyle_input"}  
  - form{"name":null}
  - slot{"Lifestyle_Type":"Good lifestyle"}
  - utter_insomnia_lifestyle_good 
  - slot{"Pdf": "Insomnia 3"}
  - utter_insomnia_tool_pdf_msg
  - action_get_pdf
  - action_get_gif  
  - utter_good_night
  

## insomnia_deny_things
> check_nightmare_accept_deny_bad_thoughts
> check_nightmare_accept_deny_tools
> insomnia_nightmare_tools_understood
> insomnia_lifestyle_user_affirm_or_deny_test
> insomnia_lifestyle_user_affirm_or_deny_tools
* deny
  - utter_probe
> check_nightmare_accept_deny_bad_thoughts  
> check_nightmare_accept_deny_tools
> insomnia_nightmare_tools_understood
> insomnia_lifestyle_user_affirm_or_deny_test
> insomnia_lifestyle_user_affirm_or_deny_tools
