# external dependencies
import pandas as pd
import os

# dataset structure
# ----------------------------------------------------------------------------------------------------------
# ind                   -> progressive index of the game
# game                  -> name of the game
# link                  -> link to the steam page in the form of https://store.steampowered.com/*****
# release               -> release date (YYYY-MM-DD)
# peak_players          -> Maximum number of player at the same time
# positive_reviews      -> Number of positive reviews
# negative_reviews      -> Number of negative reviews
# total_reviews         -> Number of reviews (positive or negative)
# rating                -> percentace of positive reviews
# primary_genre         -> main genere of the game (mapped to number between 1 - 25)
# store_genres          -> list of all genres (mapped to number between 1 - 25)
# publisher             -> publisher of the game
# developer             -> developer of the game
# detected_technologies -> suppoeted tecnologies
# store_asset_mod_time  -> ?
# review_percentage     -> percentace of positive reviews
# players_right_now     -> number of player at dataset creation time
# 24_hour_peak          -> maximum number of players in 24h
# all_time_peak         -> maximum number of players
# all_time_peak_date    -> date of the all time peak
#-------------------------------------------------------------------------------------------------------------

# pandas
# import dataset
path_game_data_csv = 'US_Accidents.csv'
data = pd.read_csv(path_game_data_csv)

print(data.info())

