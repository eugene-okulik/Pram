from typing import Dict

import requests


def get_all_objects(base_url: str, headers: Dict):
    endpoint_url = "object"
    all_objects = requests.get(f"{base_url}/{endpoint_url}", headers=headers)
    return all_objects.json()["data"]


def get_one_object(base_url: str, headers: Dict, obj_id: int):
    endpoint_url = "object"
    object = requests.get(f"{base_url}/{endpoint_url}/{obj_id}", headers=headers)
    return object.json()


def create_object(base_url: str, headers: Dict, payload: Dict):
    endpoint_url = "object"
    object = requests.post(f"{base_url}/{endpoint_url}", json=payload, headers=headers)
    return object.json()["id"]


def put_object(base_url: str, headers: Dict, obj_id: int, payload: Dict):
    endpoint_url = "object"
    object = requests.put(f"{base_url}/{endpoint_url}/{obj_id}", json=payload, headers=headers)
    return object.json()


def patch_object(base_url: str, headers: Dict, obj_id: int, payload: Dict):
    endpoint_url = "object"
    object = requests.patch(f"{base_url}/{endpoint_url}/{obj_id}", json=payload, headers=headers)
    return object.json()


def delete_object(base_url: str, headers: Dict, obj_id: int):
    endpoint_url = "object"
    request = requests.delete(f"{base_url}/{endpoint_url}/{obj_id}", headers=headers)
    return request
