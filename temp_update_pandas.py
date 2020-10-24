import os
import time
import pandas as pd

while True:
    if os.path.exists("./test.txt"):
        data= pd.read_csv("test.txt")
        print(data.mean())
    else:
        print("File not found")
    time.sleep(10)