import json 
import pyttsx3 as ps
from difflib import get_close_matches

#loading json data into jsondata variable
jsondata = json.load(open("data.json"))
#this function deals user input and find out best match for their query
def recommender(searchString):
    searchString = searchString.lower()
    if searchString in jsondata:
        return jsondata[searchString]
    elif searchString.title() in jsondata:
        return jsondata[searchString.title()]
    elif searchString.upper() in jsondata: 
        return jsondata[searchString.upper()]
    elif len(get_close_matches(searchString,jsondata.keys()))>0:
        ps.speak("Are you trying to find %s ?\n If yes type Y else N :" %get_close_matches(searchString,jsondata.keys())[0])
        ot1= input("Are you trying to find %s ?\n If yes type Y else N :" %get_close_matches(searchString,jsondata.keys())[0])
        if ot1=="Y":
            return jsondata[get_close_matches(searchString,jsondata.keys())[0]]
        elif ot1=="N":
            return "Search String doesn't exist. Please try with proper search"
        else:
            return "Sorry We didn't understand what are you trying to find!"      
    else:
        return "Search String doesn't exist. Please try with proper search"
    
#using python speach lib for interactiveness
ps.speak(" Hello Thanks for using our search Engine What do you want me to find for you?")
searchString =input("What do you want me to find for you?")
ps.speak("You are searching for %s" % searchString)
finOut = recommender(searchString)
# processing list output to meaningful string
if type(finOut)==list:
    for out1 in finOut:
        print(out1)
        ps.speak(out1)
else:
    print(finOut)
    ps.speak(finOut)




    