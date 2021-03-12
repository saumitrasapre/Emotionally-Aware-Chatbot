## happy path
* user_happy
  - utter_happy_pipeline_start_1
  - action_set_sentiment  
  - submit_hobby_form
  - form{"name":"submit_hobby_form"}
  - form{"name":null}
  - utter_happy_pipeline_start_2
> check_user_choice_happy

## user chooses games
> check_user_choice_happy
* user_request_games
  - utter_happy_pipeline_games
> check_user_games_choice

## user accepts games
> check_user_games_choice
* affirm
  - utter_happy_pipeline_games_1
* affirm
  - utter_happy_pipeline_games_2
> confirm_user_ready_for_game

## user goes ahead with games
> confirm_user_ready_for_game
* affirm
  - utter_happy_pipeline_games_ask_games
  
## mad_libs
* play_mad_libs
  - utter_happy
  - action_pre_madlibs  
  - mad_lib_input 
  - form{"name":"mad_lib_input"}  
  - form{"name":null}
  
## hangman
* play_hangman
  - utter_happy
  - action_play_Hangman
  - hangman_input
  - form{"name":"hangman_input"}  
  - form{"name":null}

## tic_tac_toe
* play_tic_tac_toe
  - action_play_tictactoe
  - form{"name":null}

## bedtime_story
* user_request_story
  - action_get_stories
 
## user chooses music free will
* user_request_music
  - action_play_music

## user chooses music
> check_user_choice_happy
* user_request_music
  - utter_happy_pipeline_music
> check_user_music_choice

## user accepts music
> check_user_music_choice
* affirm
  - utter_happy_pipeline_music_affirm
  - action_play_music
  
## user denies overall pipeline
> check_user_choice_happy
> check_user_music_choice
> check_user_games_choice
> confirm_user_ready_for_game
* deny
  - utter_happy_pipeline_deny
  