import json

import allure
import requests

from endpoints.endpoint import Object


class PatchObject(Object):
    obj_id = None

    @allure.step("Изменение объекта методом PATCH")
    def patch_update_object(self, payload, obj_id: int, headers=None):
        self.obj_id = obj_id
        self.url_endpoint = f"{self.url_endpoint}/{self.obj_id}"
        headers = headers if headers else self.headers
        self.response = requests.patch(self.url_endpoint, json=payload, headers=headers)
        try:
            self.json = self.response.json()
        except json.decoder.JSONDecodeError:
            pass
        return self.response

    @allure.step("Проверка данных объекта")
    def check_output_data(self, payload, payload_patch):
        data = self.json.copy()
        del data["id"]
        payload_temp = dict(payload)
        payload_temp.update(payload_patch)
        assert data == payload_temp
