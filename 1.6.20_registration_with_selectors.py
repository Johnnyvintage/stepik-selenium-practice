from selenium import webdriver, common
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
xpath_name = '//div[contains(@class,"first")]/div[contains(@class,"first")]/input'
xpath_surname = '//div[contains(@class,"first")]/div[contains(@class,"second")]/input'
xpath_email = '//div[contains(@class,"first")]/div[contains(@class,"third")]/input'
xpath_phone = '//div[contains(@class,"second")]/div[contains(@class,"first")]/input'
xpath_address = '//div[contains(@class,"second")]/div[contains(@class,"second")]/input'
xpath_button = '//button[@type=\"submit\"]'


def registration_fill(link):
    browser = webdriver.Chrome()
    try:
        # Переходим по ссылке
        browser.get(link)

        # Код, который заполняет обязательные поля
        input_name = browser.find_element_by_xpath(xpath_name)
        input_name.send_keys("Ivan")
        input_surname = browser.find_element_by_xpath(xpath_surname)
        input_surname.send_keys("Petrov")
        input_email = browser.find_element_by_xpath(xpath_email)
        input_email.send_keys("user@qa.ru")


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

    # вывод текста ошибки в консоль
    except common.exceptions.NoSuchElementException as nsee:
        print(repr(nsee))
        print("Finished with mistakes")
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


registration_fill(link1)
registration_fill(link2)

