import json

import allure
import requests

from endpoints.endpoint import Object


class PutObject(Object):
    obj_id = None
    @allure.step("Изменение объекта методом PUT")
    def put_update_object(self, payload, obj_id: int, headers=None):
        self.obj_id = obj_id
        self.url_endpoint = f"{self.url_endpoint}/{self.obj_id}"
        headers = headers if headers else self.headers
        self.response = requests.put(self.url_endpoint, json=payload, headers=headers)
        try:
            self.json = self.response.json()
        except json.decoder.JSONDecodeError:
            pass
        return self.response
