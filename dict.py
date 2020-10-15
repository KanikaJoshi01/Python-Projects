import json
#The data file is with extension .json
from difflib import get_close_matches
#it is a library having a function of getting closest matches according to your need
data = json.load(open("data.json"))
#loading the data.json file for data
press = "y"
while press == "y":

    def translate(word):
        word = word.lower()
        #converting the word in lower case
        if word in data:
        #checking the word in dictionary    
            return data[word]
        elif word.title() in data:
        #checking the word with title case in dictionary    
            return data[word.title()]
        elif word.upper() in data:
        #checking the word with upper case in Dictionary    
            return data[word.upper()]
        elif len(get_close_matches(word , data.keys()))	> 0:
        #If the length of the word is having close matches according to your need
            print("Did you mean %s instead "%get_close_matches(word , data.keys())[0])
            #string formatting
            #%s will be formatted with the word found using first closest match
            decide = input("Press y for Yes or n for No ")
            if decide == "y":
                return data[get_close_matches(word , data.keys())[0]]
                #printing the closest match
            elif decide == "n":
                print("The word you have entered does not exist in the dictionary!")
                #if it is not the word they mean
            else:
                print("Press either y or n")
                #when pressed wrong key instead of y or n
        else:
        #condition when the word is not present in the dictionary    
            print("The word you have entered does not exist in the dictionary!")
    word = input("Search ")
    #taking input word from the user
    output = translate(word)
    #Store the translation of word from dictionary
    if type(output) == list:
    #It will check if the output is having list
        for item in output:
            print(item)
            #it wil print the items in list in new line
    else:
        print(output)
        #printing the translation as it is
    press = input("Press y to search another word ")    