from selenium import webdriver
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()

def form(link, webdriver):
    try:

        webdriver.get(link)
        form_data(browser)

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

    return

def form_data(webdriver):
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    return

form(link, browser)