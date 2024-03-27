#Json Manipulation
import json

json_data = '{"name": "Brian", "age": 30, "city": "New York"}'
data = json.loads(json_data) #converts the JSON string into a Python dictionary

updated_json_data = json.dumps(data, indent=4, sort_keys=True) #converts the data into a JSON string and pretty prints it
#print(updated_json_data) #prints the updated JSON data


# write the data to a json  Name of the file is 08_json_data.json

with open('08_json_data.json', 'w') as file:
    json.dump(data, file, indent=2) #writes the data to the json file

# read the data from the json file

with open('08_json_data.json', 'r') as file:
    data = json.load(file)
    print(data) #prints the data from the JSON file
    





