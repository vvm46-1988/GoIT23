import json
with open('storage.json', 'r') as file:
    store = json.load(file)
print(store)
print(store.get('tuple'))