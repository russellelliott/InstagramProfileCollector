
import pandas as pd

import os
from dotenv import load_dotenv
load_dotenv() #take environment variables from .env

#get the google sheet id
id = os.environ.get("ID")#google sheet ID

def getFollowers(username):
    pass

if __name__ == "__main__":
   #initialize the dataframe
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{id}/export?format=csv")

    print(df) #print the dataframe