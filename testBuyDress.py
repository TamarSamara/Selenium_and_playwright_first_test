import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import logging
from selenium.webdriver.support import expected_conditions as EC

url = "http://automationpractice.com/index.php"
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.get(url)


@pytest.mark.passed
def test_buy_dress_summer():
    try:
        element1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "login")))
        msg1 = driver.find_element(By.CLASS_NAME, "page-heading").text
        logging.warning("Error: 'Page Login'")
        assert msg1 == "AUTHENTICATION"
        driver.find_element(By.ID, "search_query_top").send_keys("summer")
        driver.find_element(By.NAME, "submit_search").click()
        msg2 = driver.find_element(By.CLASS_NAME, "lighter").text
        logging.warning("Error: 'Page Search 'summer'")
        assert msg2 == "summer"
        # time.sleep(3)
        price = driver.find_elements(By.CLASS_NAME, 'content_price')
        # 'for' for all price items, cut off all '$', and take only 5 places from the string
        list1 = []
        for i in range(len(price) - 1):
            if '$' in price[i + 1].text:
                price2 = price[i + 1].text.replace('$', '')[0:5]
                list1.append(price2)

        print(list1)
        minp = float(list1[0])
        index = 0
        # "for" for all prices and convert them from a string to an integer, and take the cheapest price
        for i in range(len(list1)):
            floatPrice = float(list1[i])
            if minp > floatPrice:
                minp = floatPrice

        # driver.find_element(By.XPATH, f'//*[@id="center_column"]/ul/li[{index}]/div/div[2]/div[2]/a[1]/span').click()

        # Click on the item with the help of index
        if index == 0:
            driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div[2]/div[2]/a[1]/span').click()
        if index == 1:
            driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li[2]/div/div[2]/div[2]/a[1]/span').click()
        if index == 2:
            driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li[3]/div/div[2]/div[2]/a[1]/span').click()
        if index == 3:
            driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li[4]/div/div[2]/div[2]/a[1]/span').click()

        msg3 = driver.find_element(By.CLASS_NAME, "icon-ok")
        logging.warning("Error: 'Page: Product successfully added to your shopping cart")
        assert msg3 == "Product successfully added to your shopping cart"

        time.sleep(7)
        # Click on the Close window
        driver.find_element(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[1]/span').click()
        msg4 = driver.find_element(By.CLASS_NAME, "lighter").text
        logging.warning("Error: 'Page Search 'summer'")
        assert msg4 == "summer"

        # Click on the Card
        driver.find_element(By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/a').click()
        msg5 = driver.find_element(By.CLASS_NAME, "page-heading").text
        logging.warning("Error: 'Page Shopping-cart summary'")
        assert msg5 == "Shopping-cart summary"

        time.sleep(5)

    except Exception as e:
        print("error in code: {}".format(e))

    finally:
        driver.quit()
