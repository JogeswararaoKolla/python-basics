import requests
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()
print(data['number'])
print(data['people'])
for person in data['people']:  # person is dictonarie from list
    print(person['name'])
