import allure

from settings import BASE_URL


class Object:
    url = BASE_URL
    endpoint = "object"
    url_endpoint = f"{url}/{endpoint}"
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    def check_that_status_is_value(self, value):
        assert self.response.status_code == value

    @allure.step('Проверка что код ответа 200')
    def check_that_status_is_200(self):
        print()
        self.check_that_status_is_value(200)

    @allure.step('Проверка что код ответа 400')
    def check_that_status_is_400(self):
        self.check_that_status_is_value(400)

    @allure.step("Проверка данных объекта")
    def check_output_data(self, payload):
        data = self.json.copy()
        del data["id"]
        assert data == payload
