from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
xpath_button = '//button[@type=\"submit\"]'

try:

    browser.get(link)
    button = browser.find_element_by_xpath(xpath_button)
    button.click()
    new_window = browser.window_handles[-1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    #check = browser.find_element_by_id("robotCheckbox")
    #check.click()
    #radio = browser.find_element_by_id("robotsRule")
    #radio.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath(xpath_button)
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    try:
        alert = browser.switch_to.alert
        print(alert.text)
    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()