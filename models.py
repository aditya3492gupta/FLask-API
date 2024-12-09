# accessing the json data saved
import json

with open("data/books.json", "r") as f:
    books = json.load(f)

with open("data/members.json", "r") as f:
    members = json.load(f)
