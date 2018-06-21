import json
import string
from difflib import get_close_matches

data = json.load(open("data.json"))

def getmeaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        if len(get_close_matches(word,data.keys()))==0:
            return "The word doesn't exist. Please double check it."
        else:
            print ("do you mean",get_close_matches(word,data.keys())[0],"instead ?")
            YN = input("Enter Y if yes , or N if no : ")
            if YN == "y" or YN == "Y":
                return data[get_close_matches(word,data.keys())[0]]
            elif YN == "n" or YN == "N":
                return "The word doesn't exist. Please double check it."
            else:
                return "We didn't understand your entry."

word = input("Enter Word : ")

output = getmeaning(word)

if type(output) == list:
    for item in output:
        print("->",item)
else:
    print(output)
