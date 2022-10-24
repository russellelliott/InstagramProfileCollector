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

#use instabot to get the user ids of the people following the account and the people the account follows
#this takes several minutes to do. to remedy this, all the ids are saved to a txt file.
def getConnections(username):
    #get follower/following ids
    followers = bot.get_user_followers(username)
    print(followers)
    following = bot.get_user_following(username)
    print(following)
    
    #write all the ids to a text file for future use
    #join together
    connectionID = followers + following
    fileName = username + "-user-ids" + ".txt" #ex: ucsc-user-ids.txt
    with open(fileName, "w") as f:
        for i in connectionID:
            f.write(i + "\n") #to write line, manually need to add newline character
            #username = bot.get_username_from_user_id(i) #get the username
            
        
        
    #connections = [bot.get_username_from_user_id(i) for i in connectionID]
    #print(connections)
    

if __name__ == "__main__":
    if(os.path.exists("config")):
        shutil.rmtree("config") #delete the config folder; remedy for some errors
    
    print("INSTAGRAM PROFILE COLLECTOR")
    print("Type 'collect' to collect the IDs of people following the UCSC Instagram page")
    print("Type 'parse' to parse through the follower IDs")
    action = input("Select action: ")
    
    if(action == "collect"):
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
    elif(action == "parse"):
        print("will parse")
    else:
        print("Invalid action. Exiting program")