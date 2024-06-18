

def ASingleBarChart(df, TimeInterval):

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