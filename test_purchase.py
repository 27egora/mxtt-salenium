"""
Часть 3: Тест покупки товара с проверкой успешного завершения заказа.

Использует фикстуры driver и base_url из conftest.py.
"""

from selenium.webdriver.common.by import By

USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def test_successful_purchase(driver, base_url):
    # 1. Переход на сайт
    driver.get(base_url)

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

    # 6. Проверка успешности заказа
    success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "Thank you for your order!" in success_message
