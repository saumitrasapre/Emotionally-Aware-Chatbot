## insomnia path
* user_insomnia
    - utter_insomnia_pipeline_start
> check_user_choice_insomnia

## quick solution
> check_user_choice_insomnia
* deny
  - utter_insomnia_pipeline_quick_solution
> user_choice_music_insomnia  

## sleep tools
> check_user_choice_insomnia
* affirm
  - utter_insomnia_pipeline_options
> check_user_insomnia_pipeline_options

## tension
> check_user_insomnia_pipeline_options
* user_tensed
  - utter_insomnia_anxiety
> insomnia_tension_user_affirm_or_confused

## tension_confused
> insomnia_tension_user_affirm_or_confused
* confused
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
  - utter_insomnia_anxiety_tool_pdf_msg
  - action_get_pdf
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

