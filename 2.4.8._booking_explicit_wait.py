from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)
xpath_button = '//button[@type=\"submit\"]'

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element_by_id("book")
    if WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    ):
        button.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    # check = browser.find_element_by_id("robotCheckbox")
    # check.click()
    # radio = browser.find_element_by_id("robotsRule")
    # radio.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath(xpath_button)
    button.click()
    #message = browser.find_element_by_id("verify_message")

    #button = WebDriverWait(browser, 5).until_not(
    #    EC.element_to_be_clickable((By.ID, "verify"))
    #)

    #assert "successful" in message.text
    #time.sleep(5)
finally:
    try:
        alert = browser.switch_to.alert
        print(alert.text)
    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()

