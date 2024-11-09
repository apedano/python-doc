# 07B-JSON and YAML

The json module is needed to read json files.

## Load JSON content from a text file
The loaded data is a **dictionary**

```python
with open("weather_data.json", "r") as json_file:
weather_data = json.load(json_file)
print(weather_data) #this is a dict with all loaded data

print(weather_data['city']) #New York
print(weather_data['current']['temperature']) #68
print(weather_data['forecast'][0]['high']) #nested object property - 72
print(weather_data['forecast'][1]['high']) #68
```

## Print a dictionary as JSON string

```python
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

#Writes a dictionary as JSON indented content
with open('data.json', 'w') as f:
    json.dump(data_dictionary, f, indent=4)
```









