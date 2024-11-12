from typing import Dict

import pytest

from data_test import headers, base_url, payload, payload_put, payload_patch, payload_create
from object_methods import create_object, get_one_object, put_object, patch_object, delete_object


@pytest.mark.parametrize("payload", payload_create)
def test_create_object(start_end_session, before_after_test, payload: Dict):
    new_obj_id, new_obj_status_code = create_object(base_url, headers, payload)
    get_new_obj, get_new_obj_status_code = get_one_object(base_url, headers, new_obj_id)
    del get_new_obj["id"]
    assert new_obj_status_code == 200
    assert get_new_obj == payload
    delete_object(base_url, headers, new_obj_id)
    return


@pytest.mark.medium
def test_put_object(before_after_test, new_object_id):
    put_obj, put_obj_status_code = put_object(base_url, headers=headers, obj_id=new_object_id, payload=payload_put)
    del put_obj["id"]
    assert put_obj_status_code == 200
    assert put_obj == payload_put


@pytest.mark.critical
def test_patch_object(before_after_test, new_object_id):
    patch_obj, patch_obj_status_code = patch_object(base_url, headers=headers, obj_id=new_object_id, payload=payload_patch)
    del patch_obj["id"]
    payload_temp = dict(payload)
    payload_temp.update(payload_patch)
    assert patch_obj_status_code == 200
    assert patch_obj == payload_temp
    delete_object(base_url, headers=headers, obj_id=new_object_id)


@pytest.mark.medium
def test_delete_object(before_after_test, new_object_id):
    deleted_obj = delete_object(base_url, headers=headers, obj_id=new_object_id)
    assert deleted_obj.status_code == 200
    assert deleted_obj.text == f"Object with id {new_object_id} successfully deleted"
