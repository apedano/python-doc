import json

with open("weather_data.json", "r") as json_file:
     weather_data = json.load(json_file)
     print(weather_data) #this is a dict with all loaded data

     print(weather_data['city'])
     print(weather_data['current']['temperature'])
     print(weather_data['forecast'][0]['high']) #nested object property
     print(weather_data['forecast'][1]['high'])

import json

import json

#this is a Python dictionary, not a Json string
data_dictionary = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "coding", "gaming"]
}

# Indent the JSON output with 2 spaces
json_string = json.dumps(data_dictionary, indent=2)
#print JSON string
print(json_string)

#Write a dictionary as JSON indented content
with open('output_data.json', 'w') as f:
    json.dump(data_dictionary, f, indent=4)



