from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import time
import math


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
xpath_name = '//input[contains(@class, "first") and contains (@placeholder, "name")]'
xpath_surname = '//input[contains(@class, "second") and contains (@placeholder, "name")]'
xpath_email = "//input[contains (@placeholder, 'email')]"
xpath_button = '//button[@type=\"submit\"]'

try:

    browser.get(link)

    input_name = browser.find_element_by_name("firstname")
    input_name.send_keys("Ivan")
    input_surname = browser.find_element_by_name("lastname")
    input_surname.send_keys("Petrov")
    input_email = browser.find_element_by_name("email")
    input_email.send_keys("user@qa.ru")
    sendfile = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    print(str(file_path))
    sendfile.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath(xpath_button)
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    alert = browser.switch_to.alert
    print(alert.text)
    # закрываем браузер после всех манипуляций
    browser.quit()
