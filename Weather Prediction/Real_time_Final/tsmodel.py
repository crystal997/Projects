##creates ts model that uses the past 24 hrs of precipm data to predict the next 24 hrs of precipm 
import pandas as pd
from pmdarima.arima import ARIMA

class TS_model():
    def __init__(self,initial_input_data):
        self.model_pre=None
        self.model_hum=None
        self.input=initial_input_data
    def load_data(self,verbose=False):
         """
         expects dataframe with index set as date-hour format
         and singular column of precipm data that has at least the past 24 hr
         doesn't return anything, just updates input data in self
         """
         ## will code in some exceptions to make sure data format is right later
         train= self.input[['precipm','hum']].last('24h')
         self.input = train
         if verbose:
            print ('successfully updated input')
    def fit(self,verbose=False):
        """
         no return, just updates self.model
         """
        # arima_model_precip = auto_arima(self.input[['precipm']],max_p=5,max_d=5,max_q=5,seasonal=True)
        # arima_model_hum = auto_arima(self.input[['hum']],max_p=5,max_d=5,max_q=5,seasonal=True)
        arima_model_precip = ARIMA(order=(4, 0, 0),seasonal_order=(0,0,0,0))
        arima_model_precip.fit(self.input[['precipm']])
        arima_model_hum= ARIMA(order=(4, 0, 0),seasonal_order=(0,0,0,0))
        arima_model_hum.fit(self.input[['hum']])
        self.model_pre = arima_model_precip
        self.model_hum = arima_model_hum
        if verbose:
            print ('model training complete')
            print (self.model_pre.summary())


    def predict(self, time_interval=1):
        """
        returns prediction of time_interval input, default 24 hrs
        """
        results_precip = self.model_pre.predict(n_periods = time_interval)
        results_rain = self.model_hum.predict(n_periods = time_interval)
        return (results_precip,results_rain)

