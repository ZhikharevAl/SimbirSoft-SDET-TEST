[![Actions status](https://github.com/ZhikharevAl/SimbirSoft-SDET-TEST/actions/workflows/ruff_check.yml/badge.svg)](https://github.com/ZhikharevAl/SimbirSoft-SDET-TEST/actions/workflows/ruff_check.yml)

# SimbirSoft-SDET-TEST

Этот проект представляет собой набор автоматизированных тестов для веб-приложения с использованием Selenium и Pytest. Проект включает тестирование различных функциональностей, включая загрузку изображений в форме регистрации.

## Содержание

- [Описание](#описание)
- [Требования](#требования)
- [Установка](#установка)
- [Использование](#использование)
- [Запуск тестов](#запуск-тестов)
- [Генерация отчетов Allure](#генерация-отчетов-allure)
- [Ссылки](#ссылки)
- [Лицензия](#лицензия)

## Описание

Проект разработан для автоматизированного тестирования веб-приложения. Включает тесты на загрузку изображений, проверку форм и другие функциональные тесты.

## Требования

- Python 3.12
- Selenium
- Pytest
- Allure
- Google Chrome и ChromeDriver

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/ZhikharevAl/SimbirSoft-SDET-TEST.git
    cd SimbirSoft-SDET-TEST
    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

## Использование

Для использования проекта вам необходимо иметь установленный Google Chrome и ChromeDriver соответствующей версии.

## Запуск тестов

```bash
pytest --alluredir=allure-results
pytest -n auto --alluredir=allure-results # позволяет выполнять тесты параллельно, распределяя их по нескольким процессорам или машинам.
```

https://github.com/user-attachments/assets/9432cb62-16de-4f6a-aeb9-c36f963e403f

## Генерация отчетов Allure

```bash
allure serve ./allure-results
```
![Screenshot 2024-08-07 144931](https://github.com/user-attachments/assets/5020df27-7a55-4646-ae47-6e75a2166333)

### История запусков


## Ссылки

Этот же проект на Kotlin с использованием Playwright находится в стадии разработки. Вы можете следить за его прогрессом по следующей ссылке: [Проект на Kotlin с Playwright (в разработке)](https://github.com/ZhikharevAl/demoQAPlaywright).
## Лицензия

Этот проект лицензирован под лицензией MIT. Подробности смотрите в файле [LICENSE](LICENSE.md)
