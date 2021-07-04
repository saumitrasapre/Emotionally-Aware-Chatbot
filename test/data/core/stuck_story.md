## stuck path
* user_stuck
    - utter_stuck_pipeline_begin_1
    - action_set_slot      
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_stuck_pipeline_begin_2
* affirm OR user_confused
    - utter_stuck_pipeline_begin_3
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_stuck_pipeline_begin_4
> check_stuck_user_choice

## stuck path user affirms idea
> check_stuck_user_choice
* affirm OR user_confused
    - utter_stuck_affirm_idea_1
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}
    - utter_stuck_affirm_idea_2
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null}     
    - utter_stuck_affirm_idea_3
* affirm OR user_confused
    - utter_stuck_affirm_idea_4
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_stuck_affirm_idea_5
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_stuck_affirm_idea_6
    - user_thought_input
    - form{"name":"user_thought_input"}
    - form{"name":null} 
    - utter_stuck_affirm_idea_7  
> check_stuck_user_choice_lighten

## stuck path user affirms lighten
> check_stuck_user_choice_lighten
* affirm OR user_confused
    - utter_happy_pipeline_games_ask_games
> check_user_begin_games    

## stuck path user game madlibs
> check_user_begin_games  
* play_mad_libs
  - action_pre_madlibs
  - mad_lib_input 
  - form{"name":"mad_lib_input"}  
  - form{"name":null}
  - utter_stuck_return_from_games_1
> check_user_return_from_games

## stuck path user game tictactoe
> check_user_begin_games  
* play_tic_tac_toe
  - action_play_tictactoe
  - form{"name":null}
  - utter_stuck_return_from_games_1
> check_user_return_from_games

## stuck path user game hangman
> check_user_begin_games  
* play_hangman
  - action_play_Hangman
  - hangman_input
  - form{"name":"hangman_input"}  
  - form{"name":null}
  - utter_stuck_return_from_games_1
> check_user_return_from_games

## stuck path user returns from games affirm
> check_user_return_from_games  
* deny OR user_confused
  - utter_stuck_return_from_games_2
> check_user_stuck_procon_list  

## stuck path user doesnt know procon
> check_user_stuck_procon_list  
* deny OR user_confused
  - utter_stuck_return_from_games_example_1 
  - utter_stuck_return_from_games_example_2
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}    
  - utter_stuck_return_from_games_example_3
> check_user_stuck_procon_list  

## stuck path user knows procon
> check_user_stuck_procon_list  
* affirm
  - utter_stuck_return_from_games_3
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null} 
  - utter_stuck_return_from_games_4
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_stuck_return_from_games_5
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}  
  - utter_stuck_return_from_games_6
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_stuck_return_from_games_7
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_stuck_return_from_games_8
> check_user_stuck_promise

## stuck path user affirms promise
> check_user_stuck_promise  
* affirm OR user_confused
  - utter_anxiety_affirm_worried_affect_tool_3.2
  - utter_stuck_extra_points_1
> check_user_extra_points

## stuck path user affirms extra points
> check_user_extra_points  
* affirm OR user_confused
  - utter_stuck_extra_points_2
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_stuck_extra_points_3
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}
  - utter_stuck_extra_points_4
  - user_thought_input
  - form{"name":"user_thought_input"}
  - form{"name":null}  
  - utter_session_conclusion
  - utter_pdf_msg
  

## stuck path user denies lighten
> check_stuck_user_choice_lighten  
* deny OR user_no_talk
  - utter_stuck_continue_without_games
> check_user_return_from_games

## stuck path user returns from games doesnt continue
> check_user_return_from_games 
> check_user_extra_points
* deny OR user_no_talk
  - utter_angry_user_no_share_affirm_idea_no_calm_1
  - utter_goodbye


## stuck path user affirms idea
> check_stuck_user_choice
> check_user_stuck_promise
* deny OR user_no_talk
    - utter_probe
> check_stuck_user_choice
> check_user_stuck_promise

 