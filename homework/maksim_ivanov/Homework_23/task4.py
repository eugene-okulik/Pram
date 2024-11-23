import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("start-maximized")
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()


def test_single_select(driver):
    url = "https://the-internet.herokuapp.com/dynamic_loading/2"
    driver.get(url)
    start = driver.find_element(By.TAG_NAME, "button")
    start.click()
    wait = WebDriverWait(driver, 10)
    locator = (By.ID, "finish")
    wait.until(EC.visibility_of_element_located(locator))
    hello_world = driver.find_element(*locator)
    assert hello_world.text == "Hello World!"
