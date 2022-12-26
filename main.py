import pandas as pd #for database read/write
from instagrapi import Client

import os
from dotenv import load_dotenv
load_dotenv() #take environment variables from .env

# importing shutil module
import shutil

#get the google sheet id
id = os.environ.get("ID")#google sheet ID
USERNAME = os.environ.get("USERNAME")
print(USERNAME)
PASS = os.environ.get("PASS")
 
def getConnections(username):
    print(username)

if __name__ == "__main__":
    if(os.path.exists("config")):
        shutil.rmtree("config") #delete the config folder; remedy for some errors
    
    print("INSTAGRAM PROFILE COLLECTOR")
    print("Type 'collect' to collect the IDs of people following the UCSC Instagram page")
    print("Type 'parse' to parse through the follower IDs")
    action = input("Select action: ")
    
    if(action == "collect"):

        cl = Client()
        cl.login(USERNAME, PASS)

        user_id = cl.user_id_from_username("ucsc")
        print(user_id)
        getConnections("ucsc")
    elif(action == "parse"):
        print("will parse")
    else:
        print("Invalid action. Exiting program")