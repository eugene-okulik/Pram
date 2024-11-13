import allure
import pytest

from data_test import headers, payload, base_url
from object_methods import create_object, delete_object


@pytest.fixture(scope="session", autouse=True)
def start_end_session():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture()
def before_after_test():
    print("\nBefore testing")
    yield
    print("\nAfter testing")


@pytest.fixture
def new_object_id():
    with allure.step("Создание объекта"):
        obj_id, obj_status_code = create_object(base_url, headers, payload)
    yield obj_id
    with allure.step("Удаление объекта"):
        delete_object(base_url, headers, obj_id)
