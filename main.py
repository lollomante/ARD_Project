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

import pandas as pd

# Load the dataset
data = pd.read_csv('Dataset\\US_Accidents_Sampled.csv')

# Define the bins and labels
#bins = list(range(0, 11, 1))  # Bins: [0-10), [10-20), ..., [100-110)
#labels = [i for i in range(0, 10, 1)]  # Labels: 0, 10, 20, ..., 90

# Discretize the 'Visibility(mi)' column
#data['Visibility_Discretized'] = pd.cut(data['Visibility(mi)'], bins=bins, labels=labels, right=False)

# Optional: Convert labels to integer type for convenience
#data['Visibility_Discretized'] = data['Visibility_Discretized'].astype(float).fillna(100).astype(int)

# Display the first few rows to verify
#print(data[['Visibility(mi)', 'Visibility_Discretized']].head())
# Seleziona la colonna categoriale (sostituisci 'colonna_categoriale' con il nome effettivo della tua colonna)
condizioni_meteo = data['Weather_Condition']

# Utilizza il metodo value_counts() per ottenere il conteggio delle voci uniche
count = condizioni_meteo.value_counts()

# Stampa i risultati
print(count[count > 10])

