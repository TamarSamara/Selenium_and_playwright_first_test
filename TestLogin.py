import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import logging
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")


def startTest():
    url = "http://automationpractice.com/index.php"
    driver.get(url)

    element1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,
                                                                               "login")))
    element1.click()
    # time.sleep(3)


def login(**kwargs):
    # if "name" in kwargs.keys():
    #     driver.find_element(By.ID, kwargs["param"]).send_keys(kwargs["id"])

    if "id" in kwargs.keys():
        driver.find_element(By.ID, kwargs["param"]).send_keys(kwargs["id"])

        # time.sleep(3)


def email_try_except(username, password):
    try:
        login(id=username, param="email")
        time.sleep(1)
        login(id=password, param="passwd")
        time.sleep(1)
    except Exception as e:
        print("error in code: {}".format(e))

    finally:
        element1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,
                                                                                   "SubmitLogin")))
        element1.click()
        elem_page_heading = driver.find_element(By.CLASS_NAME, "page-heading")
        print(f'page-headinggggggggggg {elem_page_heading.text}')
        elemerror = driver.find_element(By.TAG_NAME, "ol")
        print(f'elemerror.text {elemerror.text}')
        logging.info(f'Successful Login')
        logging.warning(f'Error message: {elemerror.text}')
        assert elem_page_heading.text == "MY ACCOUNT"

        time.sleep(3)


        # assert elemerror.text == "Invalid email address."
        driver.quit()


@pytest.mark.passed
def test_wrong_email_wrong_password():  # -> Error
    '''
    Wrong email check and wrong password
    :return: Error message: "Invalid email address."
    passed
    '''
    startTest()
    username = "tamarsamara"
    password = "ttttt"
    email_try_except(username, password)

    # logging.info(f'Successful Login')
    # logging.warning(f'Error message: {elemerror.text}')
    # assert elemerror.text == "Invalid email address."
@pytest.mark.passed
def test_valid_email_wrong_password():  # -> Error
    '''
    Check valid email and wrong password
    :return: Error message: "Invalid email address."
    passed
    '''
    startTest()
    username = "tamar.samara@gmail.com"
    password = "ttttt"
    email_try_except(username, password)




