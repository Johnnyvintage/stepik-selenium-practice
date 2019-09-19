from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
xpath_button = '//button[@type=\"submit\"]'

try:

    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    y = calc(int(x))
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    check = browser.find_element_by_id("robotCheckbox")
    check.click()
    radio = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath(xpath_button)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    alert = browser.switch_to.alert
    print(alert.text)
    # закрываем браузер после всех манипуляций
    browser.quit()