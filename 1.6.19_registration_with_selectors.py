from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
xpath_name = '//input[contains(@class, "first") and contains (@placeholder, "name")]'
xpath_surname = '//input[contains(@class, "second") and contains (@placeholder, "name")]'
xpath_email = "//input[contains (@placeholder, 'email')]"
xpath_phone = "//input[contains (@placeholder, 'phone')]"
xpath_address = "//input[contains (@placeholder, 'address')]"
xpath_button = '//button[@type=\"submit\"]'
try:

    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_name = browser.find_element_by_xpath(xpath_name)
    input_name.send_keys("Ivan")
    input_surname = browser.find_element_by_xpath(xpath_surname)
    input_surname.send_keys("Petrov")
    input_email = browser.find_element_by_xpath(xpath_email)
    input_email.send_keys("user@qa.ru")
    input_phone = browser.find_element_by_xpath(xpath_phone)
    input_phone.send_keys("79245194437")
    input_address = browser.find_element_by_xpath(xpath_address)
    input_address.send_keys("London")


    # Отправляем заполненную форму
    button = browser.find_element_by_xpath(xpath_button)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()