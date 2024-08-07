import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from logger_config import configure_logger

from pages.base_page import BasePage

logger = configure_logger(__name__, "test.log")


class RegistrationPage(BasePage):
    URL = "https://demoqa.com/automation-practice-form"

    FIRST_NAME = ("xpath", "//*[@id='firstName']")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER = (By.CSS_SELECTOR, "label[for='gender-radio-{}']")
    MOBILE = (By.ID, "userNumber")
    DATE_OF_BIRTH = (By.ID, "dateOfBirthInput")
    SUBJECTS = ("xpath", "//input[@id='subjectsInput']")
    SUBJECTS_ELEMENTS = (By.CSS_SELECTOR, ".subjects-auto-complete__multi-value__label")
    HOBBIES = {
        "Sports": (By.XPATH, '//label[@for="hobbies-checkbox-1"]'),
        "Reading": (By.XPATH, '//label[@for="hobbies-checkbox-2"]'),
        "Music": (By.XPATH, '//label[@for="hobbies-checkbox-3"]'),
    }

    PICTURE_UPLOAD = (By.ID, "uploadPicture")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea#currentAddress")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    STATE_SELECTOR = "//div[@class=' css-1hwfws3'][.//*[@id='react-select-3-input']]"
    CITY_SELECTOR = "//div[@class=' css-1hwfws3'][.//*[@id='react-select-4-input']]"
    SUBMIT = (By.ID, "submit")
    MODAL_CONTENT = ("xpath", "//*[@id='example-modal-sizes-title-lg']")
    TABLE = (By.CLASS_NAME, "table-responsive")

    EXPECTED_SUCCESS_MESSAGE = "Thanks for submitting the form"

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Открытие страницы регистрации")
    def open(self):
        super().open(self.URL)

    @allure.step("Заполнение поля 'Имя': {first_name}")
    def fill_first_name(self, first_name):
        self.input_text(self.FIRST_NAME, first_name)

    @allure.step("Получение значения поля 'Имя'")
    def get_first_name(self):
        return self.browser.find_element(*self.FIRST_NAME).get_attribute('value')

    @allure.step("Заполнение поля 'Фамилия': {name}")
    def fill_last_name(self, name):
        self.input_text(self.LAST_NAME, name)

    @allure.step("Получение значения поля 'Фамилия'")
    def get_last_name(self):
        return self.browser.find_element(*self.LAST_NAME).get_attribute('value')

    @allure.step("Заполнение поля 'Email': {email}")
    def fill_email(self, email):
        self.input_text(self.EMAIL, email)

    @allure.step("Получение значения поля 'Email'")
    def get_email(self):
        return self.browser.find_element(*self.EMAIL).get_attribute('value')

    @allure.step("Выбор пола: {gender}")
    def select_gender(self, gender):
        gender_map = {
            "Male": "1",
            "Female": "2",
            "Other": "3"
        }
        gender_value = gender_map[gender]
        self.click((self.GENDER[0], self.GENDER[1].format(gender_value)))

    @allure.step("Проверка выбранного пола: {gender}")
    def is_gender_selected(self, gender):
        gender_map = {
            "Male": "1",
            "Female": "2",
            "Other": "3"
        }
        gender_value = gender_map[gender]
        return self.browser.find_element(By.ID,
                                         f"gender-radio-{gender_value}").is_selected()

    @allure.step("Заполнение поля 'Мобильный телефон': {mobile}")
    def fill_mobile(self, mobile):
        self.input_text(self.MOBILE, mobile)

    @allure.step("Получение значения поля 'Мобильный телефон'")
    def get_mobile(self):
        return self.browser.find_element(*self.MOBILE).get_attribute('value')

    @allure.step("Заполнение поля 'Дата рождения': {date}")
    def fill_date_of_birth(self, date):
        self.click(self.DATE_OF_BIRTH)
        day, month, year = date.split('-')
        self.select_from_dropdown((By.CLASS_NAME,
                                   'react-datepicker__year-select'), year)
        self.select_from_dropdown((By.CLASS_NAME,
                                   'react-datepicker__month-select'), month)
        self.click((By.XPATH, f"//div[contains(@class, "
                              f"'react-datepicker__day') and text()='{int(day)}']"))

    @allure.step("Выбор значения из выпадающего списка: {value}")
    def select_from_dropdown(self, locator, value):
        dropdown = self.browser.find_element(*locator)
        for option in dropdown.find_elements(By.TAG_NAME, 'option'):
            if option.text == value:
                option.click()
                break

    @allure.step("Получение значения поля 'Дата рождения'")
    def get_date_of_birth(self):
        return self.browser.find_element(*self.DATE_OF_BIRTH).get_attribute('value')

    @allure.step("Заполнение поля 'Предметы': {subjects}")
    def fill_subjects(self, subjects):
        for subject in subjects:
            self.click(self.SUBJECTS)
            self.input_text(self.SUBJECTS, subject)
            self.find_element(self.SUBJECTS).send_keys(Keys.ENTER)

    @allure.step("Получение выбранных предметов")
    def get_subjects(self):
        subject_elements = self.browser.find_elements(*self.SUBJECTS_ELEMENTS)
        return [element.text for element in subject_elements]

    @allure.step("Выбор хобби: {hobbies}")
    def select_hobbies(self, hobbies):
        for hobby in hobbies:
            self.click(self.HOBBIES[hobby])

    @allure.step("Проверка выбранных хобби: {hobbies}")
    def are_hobbies_selected(self, hobbies):
        hobbies_map = {
            "Sports": "1",
            "Reading": "2",
            "Music": "3"
        }
        for hobby in hobbies:
            hobby_value = hobbies_map[hobby]
            checkbox = self.browser.find_element(By.ID,
                                                 f"hobbies-checkbox-{hobby_value}")
            if not checkbox.is_selected():
                return False
        return True

    @allure.step("Загрузка изображения: {file_path}")
    def upload_picture(self, file_path):
        self.input_text(self.PICTURE_UPLOAD, file_path)

    @allure.step("Проверка загрузки изображения: {file_path}")
    def is_picture_uploaded(self, file_path):
        uploaded_file_name = self.browser.find_element(By.ID,
                                                       "uploadPicture").get_attribute('value').split("\\")[-1]
        return uploaded_file_name == file_path.split("\\")[-1]

    @allure.step("Заполнение поля 'Текущий адрес': {address}")
    def fill_current_address(self, address):
        self.input_text(self.CURRENT_ADDRESS, address)

    @allure.step("Получение значения поля 'Текущий адрес'")
    def get_current_address(self):
        return self.browser.find_element(*self.CURRENT_ADDRESS).get_attribute('value')

    @allure.step("Выбор штата: {state}")
    def select_state(self, state):
        self.click(self.STATE)
        self.click((By.XPATH, f"//div[text()='{state}']"))

    @allure.step("Выбор города: {city}")
    def select_city(self, city):
        self.click(self.CITY)
        self.click((By.XPATH, f"//div[text()='{city}']"))

    @allure.step("Проверка выбранного штата: {state}")
    def is_state_selected(self, state):
        selected_state = self.browser.find_element(By.XPATH, self.STATE_SELECTOR).text
        return selected_state == state

    @allure.step("Проверка выбранного города: {city}")
    def is_city_selected(self, city):
        selected_city = self.browser.find_element(By.XPATH, self.CITY_SELECTOR).text
        return selected_city == city

    @allure.step("Отправка формы")
    def submit_form(self):
        self.click(self.SUBMIT)

    def is_submission_successful(self):
        is_visible = self.is_element_visible(self.MODAL_CONTENT)
        modal_text = self.get_text(self.MODAL_CONTENT) if is_visible else ""
        logger.info(f"Модальное окно видимо: {is_visible}")
        logger.info(f"Текст модального окна: {modal_text}")
        return is_visible and "Thanks for submitting the form" in modal_text

    @allure.step("Получение отправленных данных")
    def get_submitted_data(self):
        return self.get_text(self.TABLE)

    @allure.step("Создание скриншота")
    def make_screenshot(self):
        return self.take_screenshot()

    @allure.step("Получение текста модального окна")
    def label_text(self):
        return self.get_text(self.MODAL_CONTENT)

    @allure.step("Сролл вниз браузера")
    def scroll_to_bottom_page(self):
        return self.scroll_to_bottom()

    @allure.step("Плавная прокрутка страницы")
    def scroll_to_down(self):
        return self.smooth_scroll_to_bottom()