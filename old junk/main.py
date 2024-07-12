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

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# input components:

# first graph options
input1 = dbc.Col(
    dbc.Row(
        [
        dbc.Col([
            html.P("Time Interval:"),
            dbc.Select(
                options=[
                        {"label":"Monthly", "value":"Monthly"}, 
                        {"label":"Yearly", "value":"Yearly"}, 
                        {"label":"Daily", "value":"Daily"},
                        {"label":"Hourly", "value":"Hourly"}  
                ],
                value='Monthly',
                id="Time-Interval-Select"
            )
        ], width = 6
        ),
        dbc.Col([
                html.P("View Mode:"),
                dbc.RadioItems(
                    options=[
                            {"label":"Grouped", "value":"Grouped"}, 
                            {"label":"Separated", "value":"Separated"}
                    ],
                    value='Grouped',
                    id='ViewMode-Select'
                )
            ], width = 6)
        ]
    )
)
# secong graph options
input2 = dbc.Col(
    [
        html.P("Period:"),
        dbc.Select(
            options=[
                    {"label":"All", "value":"all"}, 
                    {"label":"2017", "value":"2017"},
                    {"label":"2018", "value":"2018"},
                    {"label":"2019", "value":"2019"},
                    {"label":"2020", "value":"2020"},
                    {"label":"2021", "value":"2021"},
                    {"label":"2022", "value":"2022"}        
            ],
            value='all',
            id="Time-Interval-Select-pie"
        ),
        
    ]
)
# third graph options
input3 = dbc.Col(
    dbc.Row(
        [
        dbc.Col([
            html.P("Order:"),
            dbc.Select(
                options=[
                    {"label":"None", "value":"None"}, 
                    {"label":"Worst to best", "value":"WorstToBest"},
                    {"label":"Best to worst", "value":"BestToWorst"},      
                ],
                value='None',
                id="Accident_per_populetion_order_select"
            )
        ]),
        dbc.Col(
            [
            html.P("Show:"),
            dbc.RadioItems(
                options=[
                        {"label":"All", "value":"all"}, 
                        {"label":"Top 10", "value":"Top 10"}
                ],
                value='Top 10',
                id='Show-Select'
            )
            ]
        )
        ]
    )
)

# graphs:
FirstGraph = dbc.Col(
    [dcc.Graph(id='Temporal-Distribution-acc-graph')]
)

SecondGraph = dbc.Col(
    [dcc.Graph(id='Severity-distribution-pie')]
)

ThirdGraph = dbc.Col(
    [dcc.Graph(id='Accident_per_populetion_barchart')]
)

TemperatureGraph = dbc.Col(
    [dcc.Graph(id='Temperature_PIE')],
    width=6
)

LocationGraph = dbc.Col(
    [dcc.Graph(id='Location_Graph_Scatter')],
    width=6
)
# page components:

# title
title = dbc.Row(
    dbc.Col(html.H1("USA Accidents"), width="auto"),
    justify="center",
    className="mb-2",
)

FirstInputRow = dbc.Row(
    [input1, input2, input3]
)

FirstRow = dbc.Row(
    [FirstGraph, SecondGraph],
    className="mb-2",
)


SecondRow = dbc.Row(
    [
    TemperatureGraph, LocationGraph
    ]
)

lcol =  dbc.Col(
         [FirstRow, SecondRow],
         width=8
)

# right column
rcol = dbc.Col(
        [dbc.Row(ThirdGraph)],
         width=4
)

# app layout
app.layout=dbc.Container([
    dbc.Col([
        title,
        FirstInputRow,
        dbc.Row([lcol, rcol])
        ]
    )
],
style={'width' : '100%', 'backgroundColor' : BACKGROUND_COLOR},
fluid = True,
)

app.run(debug=True)

#Year,AL,AK,AZ,AR,CA,CO,CT,DE,FL,GA,HI,ID,IL,IN,IA,KS,KY,LA,ME,MD,MA,MI,MN,MS,MO,MT,NE,NV,NH,NJ,NM,NY,NC,ND,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VT,VA,WA,WV,WI,WY