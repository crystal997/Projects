
run:

1. Server: python tcp_server.py -p 9999 -f working_data.csv -t 2
2. Client: python Client.py

* I set the time interval as 2 when I test it, but in real situation, weather data will not change so fast.
It should be half or one hour.

Parser.py: Data Cleaning
Prediction.py: Initialize the prediction with a specific model name, load model, select feature, and make the prediction
Summary.py: Summarize the predicted results from each model and format output as desired
tsmodel.py: Build the time series model

SnowYN.sav: Snow prediction model
RainYN.sav: Rain prediction model

working_data.csv: data input
