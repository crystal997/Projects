#take in realtime information, predict based on different models and return the prediction

from collections import deque
import pickle
import sklearn
import pandas as pd
from datetime import datetime
from tsmodel import TS_model


class Predict:

    def __init__(self, model, size):
        self.model = model
        self.data = pd.DataFrame()
        self.size = size
        self.date = None

    #save data for models
    def add_data(self, new_data):
        #print(new_data)
        self.set_date(new_data)
        toAdd = self.feature_selection(new_data)
        self.data = self.data.append(toAdd)
        #print(self.size)
        #print(self.data)
        #print(len(self.data))
        if len(self.data) > self.size:
            self.data = self.data.iloc[1:]


    def feature_selection(self, raw_data):
        if self.model == "RainYN" or self.model == "SnowYN":
            result = raw_data.drop(columns=["date_hour", "precipm"])
        if self.model == "precipm":
            result = raw_data.set_index("date_hour")
            result.index = pd.to_datetime(result.index)
        return result


    #load the model, make prediction and return it
    def predict(self):
        if len(self.data) < self.size:
            return None
        #print(self.data)
        if self.model == "RainYN":
            theModel = self.load_model()
            y = theModel.predict(self.data)
            prob = theModel.predict_proba(self.data)[0][1]
            return (self.model, self.date, int(y), prob, self.data[-1:])
        if self.model == "SnowYN":
            theModel = self.load_model()
            y = theModel.predict(self.data)
            prob = theModel.predict_proba(self.data)[0][1]
            return (self.model, self.date, int(y), prob, self.data[-1:])
        if self.model == "precipm":
            ts = TS_model(self.data)
            ts.load_data()
            ts.fit()
            result = ts.predict(24)
            pre = result[0][0]
            hum = result[1][0]
            if pre < 0:
                pre = 0
            if hum < 0:
                hum = 0
            return (self.model, self.date, pre, hum, self.data[-1:])

        #print(self.date)


    def load_model(self):
        loaded_model = None
        if self.model == "RainYN":
            filename = "RainYN.sav"
            loaded_model = pickle.load(open(filename, 'rb'))
        if self.model == "SnowYN":
            filename = "SnowYN.sav"
            loaded_model = pickle.load(open(filename, 'rb'))
        return loaded_model

    #update the date for each prediction result
    def set_date(self, df):
        self.date = df["date_hour"][0]




