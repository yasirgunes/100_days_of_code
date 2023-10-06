import requests


class Post:
    def __init__(self, post_id: int):
        posts = {}
        response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
        response.raise_for_status()
        data = response.json()
        for i in range(1, len(data) + 1):
            posts[i] = data[i - 1]
        self.post_id = post_id
        self.title = posts[post_id]["title"]
        self.subtitle = posts[post_id]["subtitle"]
        self.body = posts[post_id]["body"]
