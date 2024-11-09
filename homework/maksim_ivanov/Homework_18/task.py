from typing import Dict

import requests

from homework.maksim_ivanov.Homework_18.decorators import log_function_name

BASE_URL = "http://167.172.172.115:52353"
headers = {'Content-Type': 'application/json'}
payload = {
    "name": "1",
    "data": {
        'color': 'red',
        'size': 'Biggest',
        'form': 'circle'
    }
}

payload_put = {
    "name": "aA",
    "data": {
        'color': 'blue',
    }
}

payload_patch = {
    "data": {
        'color': 'blue',
    }
}

def get_all_post(base_url: str, headers: Dict):
    endpoint_url = "object"
    all_objects = requests.get(f"{base_url}/{endpoint_url}", headers=headers)
    return all_objects.json()["data"]


def create_post(base_url: str, headers: Dict, payload: Dict):
    endpoint_url = "object"
    post = requests.post(f"{base_url}/{endpoint_url}", json=payload, headers=headers)
    return post.json()["id"]


def delete_post(base_url: str, post_id: int, headers: Dict):
    endpoint_url = "object"
    request = requests.delete(f"{base_url}/{endpoint_url}/{post_id}", headers=headers)
    return request.status_code


@log_function_name
def test_create_post(base_url: str, headers: Dict, payload: Dict):
    point = "object"
    post = requests.post(f"{base_url}/{point}", json=payload, headers=headers)
    post_id = post.json()["id"]
    post_data = post.json()
    del post_data["id"]
    assert post_data == payload
    delete_post(base_url, post_id, headers=headers)
    return


@log_function_name
def test_put_post(base_url: str, headers: Dict, payload_create: Dict, payload_put: Dict):
    post_id = create_post(base_url, headers=headers, payload=payload_create)
    endpoint_url = "object"
    post = requests.put(f"{base_url}/{endpoint_url}/{post_id}", json=payload_put, headers=headers)
    post_id = post.json()["id"]
    post_data = post.json()
    del post_data["id"]
    assert post_data == payload_put
    delete_post(base_url, post_id, headers=headers)


@log_function_name
def test_patch_post(base_url: str, headers: Dict, payload_create: Dict, payload_patch: Dict):
    post_id = create_post(base_url, headers=headers, payload=payload_create)
    endpoint_url = "object"
    post = requests.patch(f"{base_url}/{endpoint_url}/{post_id}", json=payload_patch, headers=headers)
    post_id = post.json()["id"]
    post_data = post.json()
    del post_data["id"]
    payload.update(payload_patch)
    assert post_data == payload
    delete_post(base_url, post_id, headers=headers)


@log_function_name
def test_delete_post(base_url: str, headers: Dict, payload: Dict):
    post_id = create_post(base_url, headers=headers, payload=payload)
    endpoint_url = "object"
    post = requests.delete(f"{base_url}/{endpoint_url}/{post_id}", headers=headers)
    assert post.text == f"Object with id {post_id} successfully deleted"


test_create_post(BASE_URL, headers=headers, payload=payload)
test_delete_post(BASE_URL, headers=headers, payload=payload)
test_put_post(BASE_URL, headers=headers, payload_create=payload, payload_put=payload_put)
test_patch_post(BASE_URL, headers=headers, payload_create=payload, payload_patch=payload_patch)
