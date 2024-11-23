import random

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("start-maximized")
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()


def test_single_select(driver):
    url = "https://www.qa-practice.com/elements/select/single_select"
    driver.get(url)

    language = driver.find_element(By.ID, "id_choose_language")
    select_lang = Select(language)
    random_lang_txt = random.choice(select_lang.options).text
    select_lang.select_by_visible_text(random_lang_txt)
    submit = driver.find_element(By.ID, "submit-id-submit")
    submit.click()
    return_text = driver.find_element(By.ID, "result-text")
    assert return_text.text == random_lang_txt
