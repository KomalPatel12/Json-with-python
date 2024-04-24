import json


def retrieve_title_for_user_1():
    file = open("todo_data.json", "r")
    data = json.loads(file.read())
    title_list = []
    for item in data:
        if item["userId"] == 1:
            title_list.append(item["title"])
    final_titles = transform_title(title_list)
    with open("titles.json", "w") as file:
        json.dump(final_titles, file, indent=4)


def transform_title(title_list):
    final_titles = []
    final_titles = reversed(sorted(title_list))
    return final_titles
