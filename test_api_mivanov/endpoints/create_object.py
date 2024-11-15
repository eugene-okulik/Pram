import json.decoder

import allure
import requests

from endpoints.endpoint import Object


class CreateObject(Object):
    obj_id = None

    @allure.step("Создание нового объекта")
    def create_new_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.url_endpoint, json=payload, headers=headers)
        try:
            self.json = self.response.json()
            self.obj_id = self.json["id"]
        except json.decoder.JSONDecodeError:
            pass
        return self.response

