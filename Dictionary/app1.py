import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    '''
    Enter a word to see the meaning
    '''
    word = word.lower()

    if word in data:
        return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input(
            f"Did you mean {get_close_matches(word, data.keys())[0]} instead? Enter Y for yes and N for no: ")

        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]

        elif yn == "N":
            return "Your word doesn't exist in the dictionary, please double check it"

        else:
            return "Sorry! we didn't understand your entry"

    else:
        return "The word doesn't exist in the dictionary! Please double check it"


word = input("Enter a word: ")

output = translate(word)

if type(output) == list:

    for items in output:
        print(items)

else:
    print(output)
