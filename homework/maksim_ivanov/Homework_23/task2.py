import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

data = {
    "firstName": "Petr",
    "lastName": "Petrov",
    "userEmail": "user1@example.com",
    "gender": "Male",
    "userNumber": "8800100101",
    "dateOfBirthInput": "19 May 2009",
    "subjects": "History",
    "hobbies": ("Sports","Music"),
    "currentAddress": "Russia, Moskow",
    "state": "Haryana",
    "city": "Panipat"
}

url = "https://www.qa-practice.com/elements/input/simple"


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("start-maximized")
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()


def test_form(driver):
    url = "https://demoqa.com/automation-practice-form"

    driver.get(url)

    first_name = driver.find_element(By.ID, 'firstName')
    first_name.send_keys(data["firstName"])

    last_name = driver.find_element(By.ID, 'lastName')
    last_name.send_keys(data["lastName"])

    email = driver.find_element(By.ID, 'userEmail')
    email.send_keys(data["userEmail"])

    genders = driver.find_elements(By.CSS_SELECTOR, "label[for^='gender-radio']")
    for gender in genders:
        if gender.text == data["gender"]:
            gender.click()
            break

    phone_number = driver.find_element(By.ID, 'userNumber')
    phone_number.send_keys(data["userNumber"])

    date_of_birth = driver.find_element(By.ID, 'dateOfBirthInput')
    driver.execute_script("arguments[0].select();", date_of_birth)
    date_of_birth.send_keys(data["dateOfBirthInput"])
    date_of_birth.send_keys(Keys.RETURN)

    subjects = driver.find_element(By.ID, 'subjectsInput')
    subjects.send_keys(data["subjects"])
    subjects.send_keys(Keys.RETURN)

    hobbies = driver.find_elements(By.CSS_SELECTOR, "label[for^='hobbies-checkbox']")
    for hobby in hobbies:
        if hobby.text in data["hobbies"]:
            hobby.click()

    address = driver.find_element(By.ID, "currentAddress")
    address.send_keys(data["currentAddress"])

    state = driver.find_element(By.ID, "react-select-3-input")
    state.send_keys(data["state"])
    state.send_keys(Keys.RETURN)

    city = driver.find_element(By.ID, "react-select-4-input")
    city.send_keys(data["city"])
    city.send_keys(Keys.RETURN)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    submit = driver.find_element(By.ID, "submit")
    submit.click()

    time.sleep(3)

    tbody = driver.find_element(By.CSS_SELECTOR, "table tbody")
    lines = tbody.find_elements(By.TAG_NAME, "tr")
    for line in lines:
        print(line.get_attribute("innerText"))
