
# external dependencies
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, html, dcc
import plotly.express as px


def SingleBarChart(df, TimeInterval):

    if (TimeInterval == 'Yearly'):
        yearly_counts = df['Start_Time'].dt.year.value_counts().sort_index()
        fig = px.bar(
            x = yearly_counts.index, 
            y = yearly_counts.values,          
            labels = {'x': 'Year', 'y': 'Number of Accidents'},
            title = 'Number of Accidents per Year'
        )
        return fig
    
    if (TimeInterval == 'Monthly'):
        monthly_counts = df['Start_Time'].dt.month.value_counts().sort_index()
        fig = px.bar(
            x = monthly_counts.index, 
            y = monthly_counts.values,          
            labels = {'x': 'Month', 'y': 'Number of Accidents'},
            title = 'Number of Accidents per Month'
        )
        return fig
   
    if (TimeInterval == 'Daily'):
        daily_counts = df['Start_Time'].dt.dayofweek.value_counts().sort_index()
        day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        fig = px.bar(
            x = [day_names[day] for day in daily_counts.index], 
            y = daily_counts.values,          
            labels = {'x': 'Day of the Week', 'y': 'Number of Accidents'},
            title = 'Number of Accidents per Day'
        )
        return fig
    
    if (TimeInterval == 'Hourly'):
        hourly_counts = df['Start_Time'].dt.hour.value_counts().sort_index()
        fig = px.bar(
            x = hourly_counts.index, 
            y = hourly_counts.values,          
            labels = {'x': 'Hour', 'y': 'Number of Accidents'},
            title = 'Number of Accidents per Hour'
        )
        return fig

def MultiBarChart(df, TimeInterval):
    #devide dataset on severity of the accident
    Severity1 = df[df.Severity == 1]
    Severity2 = df[df.Severity == 2]
    Severity3 = df[df.Severity == 3]
    Severity4 = df[df.Severity == 4]
    
    if (TimeInterval == 'Yearly'):
        categories = df['Start_Time'].dt.year.value_counts().sort_index().index

        values1 = Severity1['Start_Time'].dt.year.value_counts().sort_index()
        values2 = Severity2['Start_Time'].dt.year.value_counts().sort_index()
        values3 = Severity3['Start_Time'].dt.year.value_counts().sort_index()
        values4 = Severity4['Start_Time'].dt.year.value_counts().sort_index()


        trace1 = go.Bar(
            x=categories,
            y=values1.values,
            name='Series 1'
        )
        trace2 = go.Bar(
            x=categories,
            y=values2.values,
            name='Series 2'
        )
        trace3 = go.Bar(
            x=categories,
            y=values3.values,
            name='Series 3'
        )
        trace4 = go.Bar(
            x=categories,
            y=values4.values,
            name='Series 4'
        )

        # Create the figure
        fig = go.Figure(data=[trace1, trace2, trace3, trace4])

        # Update layout for better visualization
        fig.update_layout(
            title='Multiple Bar Chart',
            #xaxis=dict(title='Categories'),
            #yaxis=dict(title='Values'),
            barmode='group',  # This will group the bars side by side
            bargap=0.15,      # Gap between bars of adjacent location coordinates
            bargroupgap=0.1   # Gap between bars of the same location coordinate
        )

        return fig
    
    if (TimeInterval == 'Monthly'):
        categories = df['Start_Time'].dt.month.value_counts().sort_index().index

        values1 = Severity1['Start_Time'].dt.month.value_counts().sort_index()
        values2 = Severity2['Start_Time'].dt.month.value_counts().sort_index()
        values3 = Severity3['Start_Time'].dt.month.value_counts().sort_index()
        values4 = Severity4['Start_Time'].dt.year.value_counts().sort_index()

        trace1 = go.Bar(
            x=categories,
            y=values1.values,
            name='Series 1',
            
        )
        trace2 = go.Bar(
            x=categories,
            y=values2.values,
            name='Series 2',
            
        )
        trace3 = go.Bar(
            x=categories,
            y=values3.values,
            name='Series 3',
            
        )
        trace4 = go.Bar(
            x=categories,
            y=values4.values,
            name='Series 4',
            
        )

        # Create the figure
        fig = go.Figure(data=[trace1, trace2, trace3, trace4])
        # Update layout for better visualization
        fig.update_layout(
            title='Multiple Bar Chart',
            #xaxis=dict(title='Categories'),
            #yaxis=dict(title='Values'),
            barmode='group',  # This will group the bars side by side
            bargap=0.15,      # Gap between bars of adjacent location coordinates
            bargroupgap=0.1   # Gap between bars of the same location coordinate
        )

        return fig
    
    if (TimeInterval == 'Daily'):
        categories = df['Start_Time'].dt.dayofweek.value_counts().sort_index().index

        values1 = Severity1['Start_Time'].dt.dayofweek.value_counts().sort_index()
        values2 = Severity2['Start_Time'].dt.dayofweek.value_counts().sort_index()
        values3 = Severity3['Start_Time'].dt.dayofweek.value_counts().sort_index()
        values4 = Severity4['Start_Time'].dt.year.value_counts().sort_index()

        trace1 = go.Bar(
            x=categories,
            y=values1.values,
            name='Series 1'
        )
        trace2 = go.Bar(
            x=categories,
            y=values2.values,
            name='Series 2'
        )
        trace3 = go.Bar(
            x=categories,
            y=values3.values,
            name='Series 3'
        )

        trace4 = go.Bar(
            x=categories,
            y=values4.values,
            name='Series 4'
        )

        # Create the figure
        fig = go.Figure(data=[trace1, trace2, trace3, trace4])
        # Update layout for better visualization
        fig.update_layout(
            title='Multiple Bar Chart',
            #xaxis=dict(title='Categories'),
            #yaxis=dict(title='Values'),
            barmode='group',  # This will group the bars side by side
            bargap=0.15,      # Gap between bars of adjacent location coordinates
            bargroupgap=0.1   # Gap between bars of the same location coordinate
        )

        return fig
    
    if (TimeInterval == 'Hourly'):
        categories = df['Start_Time'].dt.hour.value_counts().sort_index().index

        values1 = Severity1['Start_Time'].dt.hour.value_counts().sort_index()
        values2 = Severity2['Start_Time'].dt.hour.value_counts().sort_index()
        values3 = Severity3['Start_Time'].dt.hour.value_counts().sort_index()
        values4 = Severity4['Start_Time'].dt.year.value_counts().sort_index()

        trace1 = go.Bar(
            x=categories,
            y=values1.values,
            name='Series 1'
        )
        trace2 = go.Bar(
            x=categories,
            y=values2.values,
            name='Series 2'
        )
        trace3 = go.Bar(
            x=categories,
            y=values3.values,
            name='Series 3'
        )
        trace4 = go.Bar(
            x=categories,
            y=values4.values,
            name='Series 4'
        )

        # Create the figure
        fig = go.Figure(data=[trace1, trace2, trace3, trace4])
        # Update layout for better visualization
        fig.update_layout(
            title='Multiple Bar Chart',
            #xaxis=dict(title='Categories'),
            #yaxis=dict(title='Values'),
            barmode='group',  # This will group the bars side by side
            bargap=0.15,      # Gap between bars of adjacent location coordinates
            bargroupgap=0.1   # Gap between bars of the same location coordinate
        )

        return fig
    

    #pie chart for distribution of severity of the accident

def PieChart(df_acc, time_interval):

    
    if(time_interval != 'all'):

        #bad solution:
        if(time_interval=='2016'):
            df_acc = df_acc[(df_acc['Start_Time'].dt.year == 2016)]
        elif(time_interval=='2017'):
            df_acc = df_acc[(df_acc['Start_Time'].dt.year == 2017)]
        elif(time_interval=='2018'):
            df_acc = df_acc[(df_acc['Start_Time'].dt.year == 2018)]
        elif(time_interval=='2019'):
            df_acc = df_acc[(df_acc['Start_Time'].dt.year == 2019)]
        elif(time_interval=='2020'):
            df_acc = df_acc[(df_acc['Start_Time'].dt.year == 2020)]
        elif(time_interval=='2021'):
            df_acc = df_acc[(df_acc['Start_Time'].dt.year == 2021)]
        elif(time_interval=='2022'):
            df_acc = df_acc[(df_acc['Start_Time'].dt.year == 2022)]   
        #time_interval = 2016
        #df_acc = df_acc[(df_acc['Start_Time'].dt.year == time_interval)]
    # Calculate the distribution of 'severity'
    severity_counts = df_acc['Severity'].value_counts().sort_index()

    # Create a pie chart
    fig = px.pie(values=severity_counts, names=severity_counts.index, title="Distribution of Severity")

    return fig

# number of accidents per 100,000 abitants
def BestWorstAcc(df_acc, df_pop, time_interval, orderby, SampleRescalingFactor):
    
    # Group accident data by state and year
    accidents_grouped = df_acc.groupby(['State', 'Year']).size().reset_index(name='Accident_Count')

    # Reshape population data from wide to long format
    population_long = pd.melt(df_pop, id_vars=['Year'], var_name='State', value_name='Population')

    # Merge population data with accidents data
    merged_data = pd.merge(accidents_grouped, population_long, how='inner', on=['State', 'Year'])

    # Calculate accident rate per 100,000 population
    merged_data['Accident_Rate_per_100k'] = (merged_data['Accident_Count'] / merged_data['Population']) * 100000 * SampleRescalingFactor

    # Select data for a specific year
    data_specific_year = merged_data[merged_data['Year'] == int(time_interval)]

    if(orderby=='WorstToBest'):
        # Sort the data by Accident_Rate_per_100k in descending order
        data_specific_year = data_specific_year.sort_values(by='Accident_Rate_per_100k', ascending=False)
    if(orderby=='BestToWorst'):
        data_specific_year = data_specific_year.sort_values(by='Accident_Rate_per_100k', ascending=True)
    
    # Create the bar chart using Plotly
    fig = px.bar(
        data_specific_year,
        x='State',
        y='Accident_Rate_per_100k',
        title=f'Accidents per 100,000 Residents by State in {time_interval}',
        labels={'Accident_Rate_per_100k': 'Accidents per 100,000 Residents'},
        text='Accident_Rate_per_100k'
    )
    return fig


