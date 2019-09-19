from selenium import webdriver
import time

link = " http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()
xpath = '//button[@type=\"submit\"]'

def form(link, webdriver):
    try:

        webdriver.get(link)
        form_data(webdriver)

    finally:
        # успеваем скопировать код за 30 секунд
        alert = browser.switch_to.alert
        print(alert.text)
        # закрываем браузер после всех манипуляций
        browser.quit()

    return

def form_data(webdriver):
    input1 = webdriver.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = webdriver.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = webdriver.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = webdriver.find_element_by_id("country")
    input4.send_keys("Russia")
    button = webdriver.find_element_by_xpath(xpath)
    button.click()
    return

form(link, browser)