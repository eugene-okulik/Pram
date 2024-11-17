import random
from locust import task, HttpUser
from helpers import load_data


class ObjectUser(HttpUser):
    headers = {'Content-type': 'application/json'}
    objs_id = []

    @staticmethod
    def create_test_data():
        return load_data("create_object_positive_test_data.json")

    def on_start(self) -> None:
        for test_data in self.create_test_data():
            obj_id = self.create_object(test_data).json()["id"]
            self.objs_id.append(obj_id)

    def on_stop(self):
        for obj_id in self.objs_id:
            self.delete_object(obj_id)
        self.objs_id = []

    def get_all_object(self):
        return self.client.get("/object", headers=self.headers)

    def get_one_object(self, obj_id: int):
        return self.client.get(f"/object/{obj_id}", headers=self.headers)

    def create_object(self, payload: dict):
        return self.client.post("/object", json=payload, headers=self.headers)

    def put_update_object(self, obj_id: int, payload: dict):
        return self.client.put(f"/object/{obj_id}", json=payload, headers=self.headers)

    def patch_update_object(self, obj_id: int, payload: dict, update_payload: dict):
        return self.client.patch(f"/object/{obj_id}", json=payload, headers=self.headers)

    def delete_object(self, obj_id: int):
        return self.client.delete(f"/object/{obj_id}", headers=self.headers)

    @task(1)
    def test_get_all_object(self):
        return self.get_all_object()

    @task(5)
    def test_get_one_object(self):
        obj_id = random.choice(self.objs_id)
        return self.get_one_object(obj_id=obj_id)

    @task(3)
    def test_put_update_object(self):
        payload = random.choice(self.create_test_data())
        obj_id = random.choice(self.objs_id)
        self.put_update_object(obj_id=obj_id, payload=payload)
