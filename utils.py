import json


def get_posts_all():
    with open(f"/Users/anna/KURSOVAYA_2 2/data/data.json", "r") as file:
        return json.load(file)


def get_posts_by_user(user_name):
    with open(f"/Users/anna/KURSOVAYA_2 2/data/data.json", "r") as file:
        data = json.load(file)

    result = []
    for item in data:
        if item.get('poster_name') == user_name:
            result.append(item)

    if len(result) == 0:
        raise ValueError

    return result


def get_comments_by_post_id(post_id):
    with open("/Users/anna/KURSOVAYA_2 2/data/data.json", "r") as file:
        data = json.load(file)

    result = []
    for item in data:
        if str(item.get('post_id')) == str(post_id):
            result.append(item)

    if len(result) == 0:
        raise ValueError

    return result


def search_for_posts(query):
    with open("/Users/anna/KURSOVAYA_2 2/data/data.json", "r") as file:
        data = json.load(file)

    result = []
    for item in data:
        if str(query) in str(item.get('content')):
            result.append(item)

    return result


def get_post_by_pk(pk):
    with open("/Users/anna/KURSOVAYA_2 2/data/data.json", "r") as file:
        data = json.load(file)

    for item in data:
        if str(item.get('pk')) == str(pk):
            return item


if __name__ == '__main__':
    print(get_posts_by_user('leo'))
