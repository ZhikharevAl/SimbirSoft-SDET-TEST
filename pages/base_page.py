import os
import time
import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step("Открытие страницы {url}")
    def open(self, url):
        self.browser.get(url)

    @allure.step("Поиск элемента {locator}")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    @allure.step("Поиск элементов {locator}")
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    @allure.step("Получение атрибута {attribute} элемента {locator}")
    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    @allure.step("Клик по элементу {locator}")
    def click(self, locator):
        self.find_element(locator).click()

    @allure.step("Ввод текста '{text}' в поле {locator}")
    def input_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step("Проверка видимости элемента {locator}")
    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Получение текста элемента {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Создание скриншота")
    def take_screenshot(self, name=None):
        if name is None:
            name = time.strftime("%Y%m%d-%H%M%S")

        file_name = f"{name}.png"
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        screenshot_directory = os.path.join(base_dir, 'screenshots')

        if not os.path.exists(screenshot_directory):
            os.makedirs(screenshot_directory)

        screenshot_path = os.path.join(screenshot_directory, file_name)
        self.browser.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name=file_name,
                           attachment_type=allure.attachment_type.PNG)
        return screenshot_path

    @allure.step("Ожидание кликабельности элемента {locator}")
    def element_to_be_clickable(self, locator):
        return WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Прокрутка вниз до конца страницы")
    def scroll_to_bottom(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
