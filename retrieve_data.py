import requests
import json
from transfrom_data import retrieve_title_for_user_1

url = "https://jsonplaceholder.typicode.com/todos"

res = requests.get(url)

if res.status_code == 200:
    data = json.loads(res.text)

    with open("todo_data.json", "w") as file:
        json.dump(data, file, indent=4)
    retrieve_title_for_user_1()
else:
    print("Error retrieving data")
