import json

with open("MOCK_DATA.json") as json_file:
    json_data = json.load(json_file)
    #print(json_data)
    
    for k in reversed(sorted(json_data)):	
	print k["first_name"]
