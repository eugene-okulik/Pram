import pytest

from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.patch_object import PatchObject
from endpoints.put_object import PutObject


@pytest.fixture()
def create_object():
    obj = CreateObject()
    yield obj
    obj_for_delete = DeleteObject()
    if obj.obj_id:
        obj_for_delete.delete_object(obj_id=obj.obj_id)

@pytest.fixture()
def put_object():
    obj = PutObject()
    yield obj

@pytest.fixture()
def patch_object():
    obj = PatchObject()
    yield obj

@pytest.fixture()
def delete_object():
    obj = DeleteObject()
    yield obj