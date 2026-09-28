# Автотест покупки товара на saucedemo.com

Проект с автотестом покупки товара в интернет-магазине https://www.saucedemo.com/ с использованием Selenium и pytest.

## Структура проекта

| Файл | Описание |
|------|----------|
| `purchase_script.py` | Часть 1: самостоятельный скрипт покупки товара (стартует браузер, логинится, добавляет товар в корзину, заполняет форму, покупает, закрывает браузер) |
| `conftest.py` | Часть 2: фикстура `driver` для работы с браузером, фикстура `base_url` для получения URL, хук `pytest_addoption` |
| `test_purchase.py` | Часть 3: тест покупки с проверкой появления текста «Thank you for your order!» |

## Установка

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск

### Часть 1: скрипт покупки

```bash
python purchase_script.py
```

### Часть 2 + 3: тесты

Запуск в Chrome (браузер по умолчанию):

```bash
pytest -v
```

Мультибраузерность — запуск в Edge:

```bash
pytest -v --browser=edge
```

Передача URL через опцию `--url` (хук `pytest_addoption`):

```bash
pytest -v --url=https://www.saucedemo.com/
```

Комбинация опций:

```bash
pytest -v --browser=edge --url=https://www.saucedemo.com/
```
