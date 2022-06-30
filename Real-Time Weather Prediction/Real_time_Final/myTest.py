import json
import unittest
from Parser import Parser
import pandas as pd
from Prediction import Predict
from Summary import Summary

input = {"date_hour": "2015-12-31 00:00:00", "dewpti": "43.0", "dewptm": "6.1", "heatindexi": "0.0", "heatindexm": "0.0", "hum": "89.0", "precipi": "0.027", "precipm": "0.7", "pressurei": "30.057", "pressurem": "1017.667", "rain": "1", "tempi": "46.0", "tempm": "7.8", "visi": "3.833", "vism": "6.133", "wdird": "20.0", "wgusti": "0.0", "wgustm": "0.0", "windchilli": "44.2", "windchillm": "6.767", "wspdi": "4.233", "wspdm": "6.8"}

#input2 = {"pickup_datetime": "2015-12-31 14:51:00", "tempm": "8.9", "tempi": "48.0", "dewptm": "0.6", "dewpti": "33.1", "hum": "56.0", "wspdm": "", "wspdi": "", "wgustm": "", "wgusti": "", "wdird": "0", "wdire": "North", "vism": "16.1", "visi": "10.0", "pressurem": "1016.7", "pressurei": "30.03", "windchillm": "", "windchilli": "", "heatindexm": "", "heatindexi": "", "precipm": "", "precipi": "", "conds": "Overcast", "icon": "cloudy", "fog": "0", "rain": "0", "snow": "0", "hail": "0", "thunder": "0", "tornado": "0"}


inputS = json.dumps(input)
#input2 = json.dumps(input2)

p = Parser()
df = p.get_train(inputS)
pd.set_option('display.max_columns',40)
#print(df)

pr = Predict("RainYN", 1)
pr.add_data(df)
#pr.add_data(df)

#print(pr.data)

result = pr.predict()
#print(result)

s = Summary()
s.add(result)




#df = p.get_train(input2)
#pr.add_data(df)
#pr.add_data(df)
#pr.add_data(df)
#print(pr.data)

#print(df)
pr2 = Predict("precipm", 24)
#print(pr2.model)
for i in range(24):
    pr2.add_data(df)
result = pr2.predict()
s.add(result)
s.summarize()
#print(result)






#self.assertEqual(True, False)  # add assertion here

