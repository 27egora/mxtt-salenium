"""
Часть 2: Фикстуры и хук pytest_addoption.

- Фикстура для работы с браузером (driver)
- Фикстура для получения url (base_url)
- Хук pytest_addoption для передачи url и выбора браузера через командную строку
- Мультибраузерность (Chrome / Edge) через параметр --browser
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

DEFAULT_URL = "https://www.saucedemo.com/"


def pytest_addoption(parser):
    """Хук: добавляем свои опции командной строки."""
    parser.addoption(
        "--url",
        action="store",
        default=DEFAULT_URL,
        help="Базовый URL тестируемого сайта (по умолчанию https://www.saucedemo.com/)",
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "edge"],
        help="Браузер для запуска тестов: chrome или edge (по умолчанию chrome)",
    )


@pytest.fixture
def base_url(request):
    """Фикстура: возвращает URL, переданный через --url."""
    return request.config.getoption("--url")


@pytest.fixture
def driver(request):
    """Фикстура: создаёт WebDriver для выбранного браузера и закрывает его после теста."""
    browser = request.config.getoption("--browser")

    if browser == "edge":
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        web_driver = webdriver.Edge(options=options)
    else:
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        web_driver = webdriver.Chrome(options=options)

    web_driver.implicitly_wait(5)
    yield web_driver
    web_driver.quit()
