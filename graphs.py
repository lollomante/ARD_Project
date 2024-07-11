# external dependencies
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, html, dcc
import plotly.express as px

from constants import *
from utility_functions import *



def SingleBarChart(df_singlebar, TimeInterval, Sampling_Factor, year):

    # Filter by year
    df_singlebar = FilterByYear(df_singlebar, year)
    
    # Define time intervals mapping dictionary
    interval_mapping = {
        'Yearly': {
            'resample': df_singlebar['Start_Time'].dt.year,
            'xlabel': 'Year',
            'xlabels': ['2017', '2018', '2019', '2020','2021', '2022']
        },
        'Monthly': {
            'resample': df_singlebar['Start_Time'].dt.month,
            'xlabel': 'Month',
            'xlabels': ['Genuary', 'February', 'March', 'April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        },
        'Daily': {
            'resample': df_singlebar['Start_Time'].dt.dayofweek,
            'xlabel': 'Day of the Week',
            'xlabels': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        },
        'Hourly': {
            'resample': df_singlebar['Start_Time'].dt.hour,
            'xlabel': 'Hour',
            #'xlabels': ['00:00', '01:00', '02:00', '03:00','04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00',
            #            '11:00', '12:00', '01:00 PM', '02:00 PM', '03:00 PM','04:00 PM', '05:00 PM', '06:00 PM', '07:00 PM', 
            #            '08:00 PM', '09:00 PM', '10:00 PM','11:00 PM', 
            #x            ]

        }
    }
    
    # Validate TimeInterval
    if TimeInterval not in interval_mapping:
        raise ValueError("TimeInterval must be one of 'Yearly', 'Monthly', 'Daily', or 'Hourly'")
    
    # Get resampling details
    interval_details = interval_mapping[TimeInterval]
    
    # Calculate counts and apply Sampling_Factor
    counts = (interval_details['resample'].value_counts().sort_index()) * Sampling_Factor
    
    # Define x labels
    x_labels = interval_details.get('xlabels', counts.index)
    
    # Create bar chart
    fig = px.bar(
        x = x_labels, 
        y = counts.values,          
        labels = {'x': interval_details['xlabel'], 'y': 'Number of Accidents'},
        title = TITLE_TEMPORAL_DIST_BARCHART[TimeInterval],
        height = TOP_ROW_HEIGHT
    )
    
    return fig

def MultiBarChart(df_multibar, TimeInterval, Sampling_Factor, year):

    df_multibar=FilterByYear(df_multibar,year)

    #devide dataset on severity of the accident
    Severity = [df_multibar[df_multibar.Severity == '1'], 
                df_multibar[df_multibar.Severity == '2'], 
                df_multibar[df_multibar.Severity == '3'], 
                df_multibar[df_multibar.Severity == '4']
            ]
    [categories,values1,values2,values3,values4] = GrouBySeverity(df_multibar, TimeInterval, Severity)
        
    # create single bars
    trace1 = go.Bar(
        x=categories,
        y=values1.values * Sampling_Factor,
        name='Very Light',
        marker=dict(color = GRADE1COLOR),
        textposition='auto'
    )
    trace2 = go.Bar(
        x=categories,
        y=values2.values * Sampling_Factor,
        name='Light',
        marker=dict(color = GRADE2COLOR),
        textposition='auto'
    )
    trace3 = go.Bar(
        x=categories,
        y=values3.values * Sampling_Factor,
        name='Medium',
        marker=dict(color = GRADE3COLOR),
        textposition='auto'
    )
    trace4 = go.Bar(
        x=categories,
        y=values4.values * Sampling_Factor,
        name='High',
        marker=dict(color = GRADE4COLOR),
        textposition='auto'
    )

    # Create the figure
    fig = go.Figure(data=[trace1, trace2, trace3, trace4])

    # Update layout for better visualization
    fig.update_layout(
        title=TITLE_TEMPORAL_DIST_BARCHART[TimeInterval],
        xaxis=dict(title='Categories'),
        yaxis=dict(title='Values'),
        barmode='group',  
        bargap=0.15,      
        bargroupgap=0.1,  
        height=TOP_ROW_HEIGHT
    )

     # Update the layout for the legend
    fig.update_layout(legend_title_text='Effect on traffic')

    return fig
       
def PieChart(df_pie, time_interval):
    # Filter the DataFrame based on the provided time interval
    if time_interval != 'all':
        df_pie = df_pie[df_pie['Start_Time'].dt.year == int(time_interval)]

    # Calculate the distribution of 'Severity'
    severity_counts = df_pie['Severity'].value_counts().sort_index()

    # Define the severity names corresponding to severity counts index
    severity_names = ['Very Light', 'Light', 'Medium', 'High']

    # Create a mapping from severity index to names
    severity_index_to_name = {i: name for i, name in zip(severity_counts.index, severity_names)}

    # Map the severity index to names
    severity_counts.index = severity_counts.index.map(severity_index_to_name)

    # Create a pie chart
    fig = px.pie(values=severity_counts, 
                 names=severity_counts.index,
                 title=TITLE_SEVERITY_DIST_PIECHART,
                 color=severity_counts.index,  # Specify the column for the colors
                 color_discrete_map={
                     'Very Light': GRADE1COLOR,
                     'Light': GRADE2COLOR,
                     'Medium': GRADE3COLOR,
                     'High': GRADE4COLOR
                    },
                height=TOP_ROW_HEIGHT
                )

    # Update the layout for the legend
    fig.update_layout(legend_title_text='Effect on traffic')

    return fig

def BestWorstAcc(df_BW_acc, df_BW_pop, time_interval, orderby, show_all, SampleRescalingFactor):
    
    # Group accident data by state and year
    accidents_grouped = df_BW_acc.groupby(['State', 'Year']).size().reset_index(name='Accident_Count')

    # Reshape population data from wide to long format
    population_long = pd.melt(df_BW_pop, id_vars=['Year'], var_name='State', value_name='Population')

    # Merge population data with accidents data
    merged_data = pd.merge(accidents_grouped, population_long, how='inner', on=['State', 'Year'])

    # Calculate accident rate per 100,000 population
    merged_data['Accident_Rate_per_100k'] = (merged_data['Accident_Count'] / merged_data['Population']) * 100000 * SampleRescalingFactor

    if time_interval == 'all':
        # Calculate the average accident rate per 100,000 population across all years
        data = merged_data.groupby('State').agg({'Accident_Rate_per_100k': 'mean'}).reset_index()
        title = 'Average Accidents per 100,000 Residents by State'
    else:
        # Select data for a specific year
        data = merged_data[merged_data['Year'] == int(time_interval)]
        title = f'Accidents per 100,000 Residents by State in {time_interval}'

    if orderby == 'WorstToBest':
        # Sort the data by Accident_Rate_per_100k in descending order
        data = data.sort_values(by='Accident_Rate_per_100k', ascending=True)
    elif orderby == 'BestToWorst':
        data = data.sort_values(by='Accident_Rate_per_100k', ascending=False)
    
    if(not(show_all)):
        data = data.tail(10)

    # Create the bar chart using Plotly

    # Map the full state names to the DataFrame
    data['State'] = data['State'].map(CODE_TO_NAME)

    fig = px.bar(
        data,
        y='State',
        x='Accident_Rate_per_100k',
        title=title,
        labels={'Accident_Rate_per_100k': 'Accidents per 100,000 Residents'},
        height=BESTWORST_HEIGHT
    )
    return fig


def TemperaturePIE(df_temp, year):

    df_temp=FilterByYear(df_temp, year)

    # Create temperature bins
    T_max = df_temp['Temperature(C)'].max()*2
    T_min = df_temp['Temperature(C)'].min()*2

    bins = [min(T_min,-40), -30, -10,  10, 25, 40, min(T_max,50)]
    labels = ['Extremely Cold', 'Very Cold', 'Cold', 'Average', 'Hot', 'Very Hot']
    # Assign temperature ranges to each row
    df_temp['Temperature_Category'] = pd.cut(df_temp['Temperature(C)'], bins=bins, labels=labels, include_lowest=True)

    # create labels using all unique values in the column named "population"
    labels = df_temp['Temperature_Category'].unique()# group by count of the "population" column.
    values = df_temp['Temperature_Category'].value_counts()


    # create piechart
    fig = go.Figure(
        data = [
            go.Pie(
                values=values,
                labels=labels,
                pull=[0, 0.002, 0.005, 0.07, 0.08, 0.09],
            )
        ],
        layout=go.Layout(
            height = BOTTOM_ROW_HEIGHT,
            #margin=dict(t=0, b=0, l=0, r=0), 
            title=TITLE_TEMPERATURE_PIECHART,
        )
    )
    return fig

def LocationScatterPlot(df_loc, year, ViewMode):

    # filter by year
    df_loc = FilterByYear(df_loc, year)

    if (ViewMode):
        color_discrete_map ={
            '1' : GRADE1COLOR,
            '2' : GRADE2COLOR,
            '3' : GRADE3COLOR,
            '4' : GRADE4COLOR
        }

        fig = px.scatter(
            df_loc, 
            y= 'Start_Lat', 
            x= 'Start_Lng', 
            height=BOTTOM_ROW_HEIGHT,
            color = 'Severity',
            color_discrete_map=color_discrete_map
        )
        return fig

    fig = px.scatter(
        df_loc, 
        y= 'Start_Lat', 
        x= 'Start_Lng', 
        height=BOTTOM_ROW_HEIGHT,
        title=TITLE_ACCIDENT_LOC_SCATTER,
    )

    return fig