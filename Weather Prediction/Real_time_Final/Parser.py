
#pass in a dictionary/json information, transform to the desire format, and pickout the desired data
#return a dataframe

import pandas as pd
import json
from pandas import json_normalize

class Parser():

    def load_data(self, data):
        # Use json_normalize() to convert JSON to DataFrame
        dict_data = json.loads(data)
        df = json_normalize(dict_data)
        return df

    def feature_select(self, df):
        # drop columns with same information
        cleaned_df = df.drop(columns=['tempm', 'dewptm', 'wspdm', 'wgustm',
                                      'vism', 'pressurem', 'windchillm', 'heatindexm'])

        # extract the time
        time = pd.DataFrame()
        time['year'] = pd.DatetimeIndex(cleaned_df['date_hour']).year
        time['month'] = pd.DatetimeIndex(cleaned_df['date_hour']).month
        time['day'] = pd.DatetimeIndex(cleaned_df['date_hour']).day
        time['hour'] = pd.DatetimeIndex(cleaned_df['date_hour']).hour
        # time['minute'] = pd.DatetimeIndex(cleaned_df['date_hour']).minute
        cleaned_df = time.join(cleaned_df)

        # drop unrelated info
        col_drop = ['heatindexi', 'windchilli']
        cleaned_df = cleaned_df.drop(columns=col_drop)

        missing_cols = ['wgusti', 'precipi']  # can fill na
        #print(cleaned_df[missing_cols].isempty.sum())
        cleaned_df = cleaned_df.replace('', 0)
        #print(cleaned_df['wgusti'])
        #cleaned_df = cleaned_df.dropna()

        return cleaned_df

    def get_train(self, data):
        df = self.load_data(data)
        df = self.feature_select(df)
        # pred_cols = ['conds', 'icon', 'fog', 'rain', 'snow', 'hail', 'thunder', 'tornado']
        pred_cols = ['rain']
        trainData = df.drop(columns=pred_cols)
        # y = df[['rain']]

        return trainData
