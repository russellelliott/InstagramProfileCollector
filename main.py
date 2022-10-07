import pandas as pd #for database read/write
from instabot import Bot #for isntagram profile collection

import os
from dotenv import load_dotenv
load_dotenv() #take environment variables from .env

# importing shutil module
import shutil

#get the google sheet id
id = os.environ.get("ID")#google sheet ID
USERNAME = os.environ.get("USERNAME")
print(USERNAME)
#USERNAME = "russell_2001"
PASS = os.environ.get("PASS")

def getConnections(username):
    #get follower/following ids
    followers = bot.get_user_followers(username)
    print(followers)
    following = bot.get_user_following(username)
    print(following)
    #join together
    connectionID = followers.append(following)
    connections = [bot.get_username_from_user_id(i) for i in connectionID]
    print(connections)
    

if __name__ == "__main__":
    shutil.rmtree("config") #delete the config folder; remedy for some errors
    bot = Bot()
    bot.login(username=USERNAME, password=PASS) #need to login
    #initialize the dataframe
    #df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{id}/export?format=csv")

    #print(df) #print the dataframe
    #getConnections("ucsc")
    user_id = bot.get_user_id_from_username("ucsc")
    user_info = bot.get_user_info(user_id)
    print(user_info['biography'])
    getConnections("ucsc")