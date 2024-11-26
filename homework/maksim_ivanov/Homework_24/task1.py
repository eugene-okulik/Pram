import random

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("start-maximized")
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()


def test_add_product_to_cart(driver):
    url = "https://www.demoblaze.com/index.html"
    driver.get(url)
    wait = WebDriverWait(driver, 5)
    cards = wait.until(ec.visibility_of_all_elements_located((By.CLASS_NAME, "card")))
    card_link = random.choice(cards).find_element(By.CLASS_NAME, 'hrefch')
    product_text = card_link.text
    ActionChains(driver).key_down(Keys.CONTROL).click(card_link).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    wait = WebDriverWait(driver, 5)
    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "btn-success"))).click()
    wait.until(ec.alert_is_present()).accept()
    driver.close()
    driver.switch_to.window(tabs[0])

    driver.find_element(By.ID, 'cartur').click()
    product_in_car_text = (wait.until(ec.visibility_of_all_elements_located((By.CLASS_NAME, "success")))[0].
                           find_elements(By.TAG_NAME, "td"))[1].text
    assert product_text == product_in_car_text
