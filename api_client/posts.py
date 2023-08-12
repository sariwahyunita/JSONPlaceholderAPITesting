from api_client.base import APIClient


class PostAPI(APIClient):
    def __init__(self):
        super().__init__()
        self.base_url = "https://jsonplaceholder.typicode.com/posts"

    def get_all(self):
        return self.get(self.base_url)

    def get_by_id(self, post_id):
        return self.get(f"{self.base_url}/{post_id}")

    def create_post(self, requestBody):
        return self.post(f"{self.base_url}", data=requestBody)

