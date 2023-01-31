#!/usr/bin/python3

# Define constants
language = ("en") # first available is used - always include english at the end

# Asynchronously download json file from linku.la
from requests import get
import json
r = get("https://linku.la/jasima/data.json")
data = r.json()
json.dump(data, open("data.json", "w"))
print("Downloaded data.json.")
#data = json.load(open("data.json", "r"))

# Create a simplified dictionary
simplified = {}
counter = 0
for word in data["data"]:
	for lang in language:
		try:
			simplified[word] = data["data"][word]["def"][lang]
			break
		except KeyError:
			counter += 1
			continue
json.dump(simplified, open("simplified.json", "w"))
print("Created simplified json.")
#print("Number of times where definition in some language was unavailable:", counter)
