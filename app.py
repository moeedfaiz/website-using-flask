import json


with open('config.json', 'r') as file:
    data = json.load(file)

# Access the "params" key in the loaded JSON data
params = data.get("params", {})

# Now you can use the "params" dictionary as needed

