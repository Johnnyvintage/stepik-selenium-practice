from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
xpath_button = '//button[@type=\"submit\"]'

try:

    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = int(x_element.text)
    y_element = browser.find_element_by_id("num2")
    y = int(y_element.text)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(x+y))  # ищем элемент с текстом "Python"

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath(xpath_button)
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    alert = browser.switch_to.alert
    print(alert.text)
    # закрываем браузер после всех манипуляций
    browser.quit()