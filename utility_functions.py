
# filter dataset by year
def FilterByYear(df_filtred, year):
    if year != 'all':
        df_filtred = df_filtred[df_filtred['Start_Time'].dt.year == int(year)]
    return df_filtred

def GrouBySeverity(df, TimeInterval, Severity):
    if (TimeInterval == 'Yearly'):
        categories = df['Start_Time'].dt.year.value_counts().sort_index().index
        values1 = Severity[0]['Start_Time'].dt.year.value_counts().sort_index()
        values2 = Severity[1]['Start_Time'].dt.year.value_counts().sort_index()
        values3 = Severity[2]['Start_Time'].dt.year.value_counts().sort_index()
        values4 = Severity[3]['Start_Time'].dt.year.value_counts().sort_index()
        return [categories,values1,values2,values3,values4]
    
    if (TimeInterval == 'Monthly'):
        categories = df['Start_Time'].dt.month.value_counts().sort_index().index
        values1 = Severity[0]['Start_Time'].dt.month.value_counts().sort_index()
        values2 = Severity[1]['Start_Time'].dt.month.value_counts().sort_index()
        values3 = Severity[2]['Start_Time'].dt.month.value_counts().sort_index()
        values4 = Severity[3]['Start_Time'].dt.year.value_counts().sort_index()
        return [categories,values1,values2,values3,values4]
    
    if (TimeInterval == 'Daily'):
        categories = df['Start_Time'].dt.dayofweek.value_counts().sort_index().index
        values1 = Severity[0]['Start_Time'].dt.dayofweek.value_counts().sort_index()
        values2 = Severity[1]['Start_Time'].dt.dayofweek.value_counts().sort_index()
        values3 = Severity[2]['Start_Time'].dt.dayofweek.value_counts().sort_index()
        values4 = Severity[3]['Start_Time'].dt.year.value_counts().sort_index()
        return [categories,values1,values2,values3,values4]
    
    if (TimeInterval == 'Hourly'):
        categories = df['Start_Time'].dt.hour.value_counts().sort_index().index
        values1 = Severity[0]['Start_Time'].dt.hour.value_counts().sort_index()
        values2 = Severity[1]['Start_Time'].dt.hour.value_counts().sort_index()
        values3 = Severity[2]['Start_Time'].dt.hour.value_counts().sort_index()
        values4 = Severity[3]['Start_Time'].dt.year.value_counts().sort_index()
        return [categories,values1,values2,values3,values4]