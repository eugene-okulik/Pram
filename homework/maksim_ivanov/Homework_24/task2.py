import random

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("start-maximized")
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()


def test_add_to_compare(driver):
    url = 'https://magento.softwaretestingboard.com/gear/bags.html'
    driver.get(url)
    wait = WebDriverWait(driver, 5)
    products = wait.until(ec.visibility_of_all_elements_located((By.CLASS_NAME, "product-item-info")))
    product = random.choice(products)
    product_text = product.find_element(By.CLASS_NAME, "product-item-link").text
    button_compare = product.find_element(By.CLASS_NAME, "tocompare")
    actions = ActionChains(driver)
    actions.move_to_element(product)
    actions.scroll_by_amount(0, 200)
    actions.move_to_element(button_compare)
    actions.click()
    actions.perform()

    wait = WebDriverWait(driver, 5)
    compared_products = wait.until(ec.visibility_of_all_elements_located((By.ID, "compare-items")))
    compared_product_text = compared_products[0].find_element(By.CLASS_NAME, "product-item-link").text
    assert product_text == compared_product_text
