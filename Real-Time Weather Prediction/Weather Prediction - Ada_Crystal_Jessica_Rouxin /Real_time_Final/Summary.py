# summarize the prediction result of different models and format output
from datetime import datetime

class Summary:
    def __init__(self):
        self.result = {}
        self.time = None

    def add(self, result):
        type = result[0]
        time = result[1]
        self.result[type] = result
        self.time = time

    def summarize(self):
        day, time = self.time.split(" ")
        temp = self.result["RainYN"]
        data = temp[4]
        tempe= data["tempi"][0]
        wind = data["wspdi"][0]
        ts = self.result["precipm"]
        snow = self.result["SnowYN"][3]
        #print(data)
        print(f"Today: {day}")
        print(f"Time: {time}")
        print(f"Current temperature is {tempe} Fahrenheit, Wind speed is {wind} mph.")
        print("Next Hour:")
        print(f"The probability of raining is {round(temp[3]*100,2)}%.")
        print(f"The probability of Snowing is {round(snow * 100, 2)}%.")
        print(f"The predicted precipitation is {round(ts[2],4)} mm. ")
        print(f"The predicted humidity is {round(ts[3], 2)}%. ")

