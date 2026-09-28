"""
Часть 1: Скрипт покупки товара на https://www.saucedemo.com/

Шаги:
1. Старт браузера и переход на сайт
2. Авторизация (standard_user)
3. Добавление товара в корзину
4. Заполнение формы оформления заказа
5. Покупка товара (завершение заказа)
6. Закрытие браузера
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def main():
    # 1. Старт браузера и переход на сайт
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    try:
        driver.get(BASE_URL)

        # 2. Авторизация
        driver.find_element(By.ID, "user-name").send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "login-button").click()

        # 3. Добавление товара в корзину
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Переход к оформлению заказа
        driver.find_element(By.ID, "checkout").click()

        # 4. Заполнение формы
        driver.find_element(By.ID, "first-name").send_keys("Ivan")
        driver.find_element(By.ID, "last-name").send_keys("Petrov")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        # 5. Покупка товара
        driver.find_element(By.ID, "finish").click()

        # Проверка успешного завершения заказа
        success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert "Thank you for your order!" in success_message, (
            f"Ожидалось сообщение 'Thank you for your order!', получено: {success_message!r}"
        )
        print("Заказ успешно оформлен:", success_message)

    finally:
        # 6. Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    main()
