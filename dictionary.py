import json
import difflib
from difflib import get_close_matches
#>SequenceMatcher(None, "rain", "rainn").ratio()
#to get ratio of how similar the words are
#get_close_matches


data = json.load(open("dictionary.json"))

def define(word):
    word = word.lower()
    if word in data:
        return data[word]
    
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean: %s instead? Enter Y if yes, or N if no: " % get_close_matches(word,data.keys())[0])
        if yn == "Y": 
            return data[get_close_matches(word, data.keys())[0]]
        elif yn =="N":
            return "The word doesn't exist. Please double check it."
        else:
            return "I'm not sure what you mean."

    else:
        print("This word doesn't exist.")

word = input("Enter the word that you want to search for: ")

output = (define(word))

if type(output) == list:
    for item in output:
     print(item)
else:
    print(output)
