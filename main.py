# external dependencies
import pandas as pd
import os


# pandas
# import dataset
path_game_data_csv = 'Dataset\game_data_all.csv'
data = pd.read_csv(path_game_data_csv)

data.dropna()

data.head()

