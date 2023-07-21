
def rm_duplicate_nan(df):

    df = df[~df.duplicated(keep='first')] #remove the duplicates and keep the first rows


    #change the nan value

    change = {
        'marital': 'unknown',
        'education': 'unknown',
        'default': 'unknown',
        'balance': 0,
        'housing': 'unknown',
        'loan': 'unknown',
        'contact': 'unknown',
        'day': 0,
        'month': 0,
        'duration': 0,
        'campaign': 0,
        'pdays': -1,
        'previous': 0
    }

    df = df.fillna(value=change)  

    return df

