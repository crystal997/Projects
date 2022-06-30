import pandas as pd
#read data
df=pd.read_csv('working_data.csv',index_col = 'date_hour')
# convert the 'Date' column to datetime format
df.index= pd.to_datetime(df.index)
train = df[['precipm','hum']].first('24h')

from tsmodel import TS_model
ts=TS_model(train)
ts.load_data()
ts.fit()
results = ts.predict()
print (results)