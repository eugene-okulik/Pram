import pytest

from load_test_data import (test_data_create, test_data_create_negative, test_data_one_object, test_data_put,
                            test_data_patch)


@pytest.mark.parametrize("test_data_create", test_data_create)
def test_create_object(create_object, test_data_create):
    create_object.create_new_object(payload=test_data_create)
    create_object.check_that_status_is_200()
    create_object.check_output_data(payload=test_data_create)


@pytest.mark.parametrize("test_data_create_negative", test_data_create_negative)
def test_create_object_with_negative_data(create_object, test_data_create_negative):
    create_object.create_new_object(payload=test_data_create_negative)
    create_object.check_that_status_is_400()


@pytest.mark.parametrize("test_data_one_object", test_data_one_object)
@pytest.mark.parametrize("test_data_put", test_data_put)
def test_put_object(create_object, put_object, test_data_one_object, test_data_put):
    create_object.create_new_object(payload=test_data_one_object)
    put_object.put_update_object(payload=test_data_put, obj_id=create_object.obj_id)
    put_object.check_that_status_is_200()
    put_object.check_output_data(payload=test_data_put)


@pytest.mark.parametrize("test_data_one_object", test_data_one_object)
@pytest.mark.parametrize("test_data_patch", test_data_patch)
def test_patch_object(create_object, patch_object, test_data_one_object, test_data_patch):
    create_object.create_new_object(payload=test_data_one_object)
    patch_object.patch_update_object(payload=test_data_patch, obj_id=create_object.obj_id)
    patch_object.check_that_status_is_200()
    patch_object.check_output_data(payload=test_data_one_object, payload_patch=test_data_patch)


@pytest.mark.parametrize("test_data_create", test_data_create)
def test_delete_patch(create_object, delete_object, test_data_create):
    create_object.create_new_object(payload=test_data_create)
    delete_object.delete_object(obj_id=create_object.obj_id)
    delete_object.check_that_status_is_200()
    delete_object.check_deleted_object()
