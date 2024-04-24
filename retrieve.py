import requests
import json

url = "https://jsonplaceholder.typicode.com/todos"

res = requests.get(url)

if res.status_code == 200:
    data = json.loads(res.text)

    with open("todo_data.json", "w") as file:
        json.dump(data, file, indent=4)
else:
    print("Error retrieving data")
