import allure
import requests

from test_api_mivanov.endpoints.endpoint import Object


class Get_one_object(Object):
    obj_id = None
    @allure.step("Получение одного объекта")
    def get_one_object(self, obj_id, headers=None):
        self.obj_id = obj_id
        self.url_endpoint = f"{self.url_endpoint}/{self.obj_id}"
        headers = headers if headers else self.headers
        self.response = requests.get(self.url_endpoint, headers=headers)
        self.json = self.response.json()
        self.obj_id = self.json["id"]
