import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("start-maximized")
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()


def test_input_text(driver):
    url = "https://www.qa-practice.com/elements/input/simple"
    text = "Example_text"
    driver.get(url)
    input_field = driver.find_element(By.ID, "id_text_string")
    input_field.send_keys(text)
    input_field.send_keys(Keys.RETURN)
    result_element = driver.find_element(By.ID, "result-text")
    assert text == result_element.text
