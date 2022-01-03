import numpy as np
import pandas as pd





def store_preprocess(storefile):
    # reading store_id file
    store = pd.read_csv(storefile)
    # Creating columns of competition and Promo2history with total period in months, and weeks
    store['CompetitionPeriod'] = (12-store.CompetitionOpenSinceMonth) + ((2015-store.CompetitionOpenSinceYear)*12)
    store['Promo2history'] = (52-store.Promo2SinceWeek) + ((2015-store.Promo2SinceYear)*52)
    # Dropping unnecessary columns
    store.drop(columns=['CompetitionOpenSinceMonth','CompetitionOpenSinceYear','Promo2SinceWeek', 'Promo2SinceYear'], inplace=True)
    return store

def data_preprocess(df, trainpath, store):
    # reading trainpath file
    dataframe = pd.read_csv(df)
    dataframe.replace({"StateHoliday": {0:'0'}}, inplace=True)
    # Exctraction of month and year columns in the dataframe
    dataframe['Date'] = pd.to_datetime(dataframe['Date'])
    dataframe['year'] = pd.DatetimeIndex(dataframe['Date']).year
    dataframe['month'] = pd.DatetimeIndex(dataframe['Date']).month
    dataframe['Day'] = dataframe.Date.dt.day
    dataframe['DayOfWeek'] = dataframe.Date.dt.dayofweek
    dataframe['WeekOfYear'] = dataframe.Date.dt.weekofyear
    # reading trainpath file
    train = pd.read_csv(trainpath)
    train.replace({"StateHoliday": {0:'0'}}, inplace=True)
    # Exctraction of month and year columns in trainpath file
    train['Date'] = pd.to_datetime(train['Date'])
    train['year'] = pd.DatetimeIndex(train['Date']).year
    train['month'] = pd.DatetimeIndex(train['Date']).month
    train['Day'] = train.Date.dt.day
    train['DayOfWeek'] = train.Date.dt.dayofweek
    train['WeekOfYear'] = train.Date.dt.weekofyear
    # Feature extraction of average customers per store, and average sales per store.
    groupy = train.groupby(['Store','month'])['Customers','Sales'].mean().rename(columns={'Customers':'CustomersAvg', 'Sales':'SalesAvg'}).reset_index()    
    # Adding feature extraction to our dataframe
    dataframe = pd.merge(dataframe, groupy,  how='inner', on=['Store','month'])
    dataframe = pd.merge(dataframe, store,  how='inner', on=['Store'])
    # Dropping unnecessary columns
    if 'Customers' in dataframe.columns:
        dataframe.drop(columns= 'Customers', inplace=True)
    dataframe.loc[:,['Promo2history']]= dataframe.loc[:,['Promo2history']].fillna(0)
    dataframe.loc[:,['CompetitionPeriod']]= dataframe.loc[:,['CompetitionPeriod']].fillna(1400)
    dataframe.loc[:,'PromoInterval']= dataframe.loc[:,'PromoInterval'].fillna('na')
    dataframe.loc[:,'CompetitionDistance']= dataframe.loc[:,'CompetitionDistance'].fillna(dataframe.CompetitionDistance.max())
    if 'Sales' in dataframe.columns:
        dataframe=dataframe.loc[dataframe['Sales']!=0]
    return dataframe



