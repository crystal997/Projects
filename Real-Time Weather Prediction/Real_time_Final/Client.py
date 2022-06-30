import socket
import sys
import json
from Parser import Parser
import pandas as pd
from Prediction import Predict
from Summary import Summary
import warnings
warnings.filterwarnings('ignore')


HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    # sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    i = 0
    pr2 = Predict("precipm", 24)
    p = Parser()
    pr = Predict("RainYN", 1)
    pr3 = Predict("SnowYN", 1)

    while True:
        received = str(sock.recv(1024), "utf-8")
        # print("Sent:     {}".format(data))

        #print(f"Received: {i}")
        df = p.get_train(received)
        pr.add_data(df)
        result = pr.predict()
        pr2.add_data(df)
        result2 = pr2.predict()
        pr3.add_data(df)
        result3 = pr3.predict()
        s = Summary()
        i += 1
        #print(result)
        #print(result2)
        if result is not None and result2 is not None:
            print("##################################################")
            print("Received: {}".format(received))
            #print(result2)
            s.add(result)
            s.add(result2)
            s.add(result3)
            s.summarize()



# print("Sent:     {}".format(data))
# print("Received: {}".format(received))


# handle_data_from_server

# handle_data_from_strategy

# send_data