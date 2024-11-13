from typing import Dict

import pytest
import allure

from data_test import headers, base_url, payload, payload_put, payload_patch, payload_create
from object_methods import create_object, get_one_object, put_object, patch_object, delete_object


@allure.feature("API объекта")
@allure.story("Создание объекта")
@allure.title("Тест на создание объекта")
@allure.link("http://167.172.172.115:52353/", "API")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("payload", payload_create)
def test_create_object(start_end_session, before_after_test, payload: Dict):
    with allure.step(f"Создание объекта с данными {payload}"):
        new_obj_id, new_obj_status_code = create_object(base_url, headers, payload)
    with allure.step(f"Получение объекта с id={new_obj_id}"):
        get_new_obj, get_new_obj_status_code = get_one_object(base_url, headers, new_obj_id)
    del get_new_obj["id"]
    with allure.step("Проверка что статус ответа 200"):
        assert new_obj_status_code == 200
    with allure.step(f"Проверка что получен объект с данными {payload}"):
        assert get_new_obj == payload
    delete_object(base_url, headers, new_obj_id)
    return


@allure.feature("API объекта")
@allure.story("Изменение объекта")
@allure.title("Тест на изменение объекта методом PUT")
@allure.link("http://167.172.172.115:52353/", "link", "API")
@pytest.mark.medium
def test_put_object(before_after_test, new_object_id):
    with allure.step(f"Отправка PUT запроса с данными {payload}"):
        put_obj, put_obj_status_code = put_object(base_url, headers=headers, obj_id=new_object_id, payload=payload_put)
    del put_obj["id"]
    with allure.step("Проверка что статус ответа 200"):
        assert put_obj_status_code == 200
    with allure.step(f"Проверка что получен объект с данными {payload}"):
        assert put_obj == payload_put


@allure.feature("API объекта")
@allure.story("Изменение объекта")
@allure.title("Тест на изменение объекта методом PATCH")
@allure.link("http://167.172.172.115:52353/", "link", "API")
@pytest.mark.critical
def test_patch_object(before_after_test, new_object_id):
    with allure.step(f"Отправка PUT запроса с данными {payload}"):
        patch_obj, patch_obj_status_code = patch_object(base_url, headers=headers, obj_id=new_object_id,
                                                        payload=payload_patch)
    del patch_obj["id"]
    payload_temp = dict(payload)
    payload_temp.update(payload_patch)
    with allure.step("Проверка что статус ответа 200"):
        assert patch_obj_status_code == 200
    with allure.step(f"Проверка что получен объект с данными {payload}"):
        assert patch_obj == payload_temp


@allure.feature("API объекта")
@allure.story("Удаление объекта")
@allure.title("Тест на удаление объекта")
@allure.link("http://167.172.172.115:52353/", "link", "API")
@pytest.mark.medium
def test_delete_object(before_after_test, new_object_id):
    with allure.step("Отправка DELETE запроса"):
        deleted_obj = delete_object(base_url, headers=headers, obj_id=new_object_id)
    with allure.step("Проверка что статус ответа 200"):
        assert deleted_obj.status_code == 200
    with allure.step("проверка ответа после удаления"):
        assert deleted_obj.text == f"Object with id {new_object_id} successfully deleted"
