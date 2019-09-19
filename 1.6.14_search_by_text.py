from selenium import webdriver
import time
import math
import submit_web_form

link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
text = str(math.ceil(math.pow(math.pi, math.e)*10000))

def form(url, string, webdriver):
    try:

        webdriver.get(url)
        clink = webdriver.find_element_by_partial_link_text(string)
        clink.click()
        time.sleep(2)
        submit_web_form.form_data(webdriver)

    finally:
        # успеваем скопировать код за 10 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        webdriver.quit()
    return


form(link, text, browser)