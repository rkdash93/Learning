import json
import nltk

with open('intents.json') as file:
    data = json.load(file)

for intent in data['intents']:
    for pattern in intent['patterns']:
        print(pattern)    

