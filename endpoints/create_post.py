import requests
import allure
from endpoints.endpoint import Endpoint


class CreatePost(Endpoint):

    def __init__(self):
        self.post_id = None
        self.headers = None

    @allure.step('Создание объекта')
    def create_new_meme(self, body, token_post):
        self.response = requests.post(
            url=f'{self.url}/meme',
            json=body,
            headers={'Authorization': token_post}
        )

        try:
            self.json = self.response.json()
            return self.response
        except requests.exceptions.JSONDecodeError:
            return None
