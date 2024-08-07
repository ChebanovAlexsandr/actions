import requests
import allure
from endpoints.endpoint import Endpoint


class UpdatePost(Endpoint):
    @allure.step("Обновление объекта")
    def put_update_meme(self, mem_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            url=f'{self.url}/meme/{mem_id}',
            json=body,
            headers=headers
        )
        try:
            self.json = self.response.json()
            self.meme_id = self.json['id']
            return self.response
        except requests.exceptions.JSONDecodeError:
            return None
