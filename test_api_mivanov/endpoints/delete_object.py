import allure
import requests

from endpoints.endpoint import Object


class DeleteObject(Object):
    obj_id = None
    text = None
    @allure.step("Удаление объекта по id")
    def delete_object(self, obj_id ,headers=None):
        self.obj_id = obj_id
        self.url_endpoint = f"{self.url_endpoint}/{self.obj_id}"
        headers = headers if headers else self.headers
        self.response = requests.delete(self.url_endpoint, headers=headers)
        self.text = self.response.text
        return self.response

    @allure.step("Проверка что объект удален")
    def check_deleted_object(self):
        assert self.text == f"Object with id {self.obj_id} successfully deleted"
