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
    #print(username)
    
    #get list of followers and following
    followers = cl.user_followers(username)
    print(followers)
    following = cl.user_following(username)
    print(following)
    
    #write all the ids to a text file for future use
    #join together
    connectList = followers + following
    
    #make a csv file; add the username and their id. that way, getting either is easy when filtering data
    fileName = username + "-user-data" + ".csv" #ex: ucsc-user-data.csv
    
    header = ['name', 'id']
    
    #csv stuff
    import csv
    
    with open(fileName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        
        for id in connectList:
            #get the username from the id
            name = cl.username_from_user_id(id)
            data = [name, id]
            # write the data
            writer.writerow(data)

    # close the file
    f.close()
    

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