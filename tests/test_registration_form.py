import os
import pytest
import time
import allure
from allure_commons.types import Severity

from data.data import PersonData
from logger_config import configure_logger
from pages.registration_page import RegistrationPage

logger = configure_logger(__name__, "test.log")


@allure.epic("Тестирование формы регистрации")
@allure.description_html("""
<h2>Тестирование формы регистрации на сайте</h2>
<p>Этот набор тестов проверяет функциональность формы регистрации, включая:</p>
<ul>
    <li>Заполнение всех полей формы</li>
    <li>Выбор различных опций (пол, хобби, предметы)</li>
    <li>Загрузку изображения</li>
    <li>Выбор даты рождения</li>
    <li>Выбор штата и города</li>
</ul>
""")
class TestRegistrationForm:

    @pytest.fixture(scope="function")
    def page(self, browser):
        return RegistrationPage(browser)

    @allure.feature("Тестирование поля 'Имя'")
    @allure.severity(Severity.BLOCKER)
    @allure.title("Тест заполнения поля 'Имя'")
    @allure.description("Этот тест проверяет корректность "
                        "заполнения поля 'Имя' в форме регистрации.")
    def test_first_name(self, page):
        logger.info("Тестирование поля 'Имя' начато")
        with allure.step("Открытие страницы регистрации"):
            logger.info("Открытие страницы регистрации")
            page.open()
        person = PersonData()
        with allure.step(f"Заполнение поля 'Имя' значением {person.first_name}"):
            logger.info(f"Заполнение поля 'Имя' значением {person.first_name}")
            page.fill_first_name(person.first_name)
        with allure.step("Проверка корректности заполнения поля 'Имя'"):
            logger.info("Проверка корректности заполнения поля 'Имя'")
            assert page.get_first_name() == person.first_name, \
                f"Name {person.first_name} was not filled correctly"
        logger.info("Тестирование поля 'Имя' завершено")

    @allure.feature("Тестирование поля 'Фамилия'")
    @allure.severity(Severity.BLOCKER)
    @allure.title("Тест заполнения поля 'Фамилия'")
    @allure.description("Этот тест проверяет корректность заполнения "
                        "поля 'Фамилия' в форме регистрации.")
    def test_last_name(self, page):
        logger.info("Тестирование поля 'Фамилия' начато")
        with allure.step("Открытие страницы регистрации"):
            logger.info("Открытие страницы регистрации")
            page.open()
        person = PersonData()
        with allure.step(f"Заполнение поля 'Фамилия' значением {person.last_name}"):
            logger.info(f"Заполнение поля 'Фамилия' значением {person.last_name}")
            page.fill_last_name(person.last_name)
        with allure.step("Проверка корректности заполнения поля 'Фамилия'"):
            logger.info("Проверка корректности заполнения поля 'Фамилия'")
            assert page.get_last_name() == person.last_name, \
                f"Name {person.last_name} was not filled correctly"
        logger.info("Тестирование поля 'Фамилия' завершено")

    @allure.feature("Тестирование поля 'Email'")
    @allure.severity(Severity.BLOCKER)
    @allure.title("Тест заполнения поля 'Email'")
    @allure.description("Этот тест проверяет корректность "
                        "заполнения поля 'Email' в форме регистрации.")
    def test_email(self, page):
        logger.info("Тестирование поля 'Email' начато")
        with allure.step("Открытие страницы регистрации"):
            logger.info("Открытие страницы регистрации")
            page.open()
        person = PersonData()
        with allure.step(f"Заполнение поля 'Email' значением {person.email}"):
            logger.info(f"Заполнение поля 'Email' значением {person.email}")
            page.fill_email(person.email)
        with allure.step("Проверка корректности заполнения поля 'Email'"):
            logger.info("Проверка корректности заполнения поля 'Email'")
            assert page.get_email() == person.email, \
                f"Email {person.email} was not filled correctly"
        logger.info("Тестирование поля 'Email' завершено")

    @allure.feature("Тестирование выбора пола")
    @allure.severity(Severity.BLOCKER)
    @allure.title("Тест выбора пола")
    @allure.description("Этот тест проверяет корректность "
                        "выбора пола в форме регистрации.")
    @pytest.mark.parametrize("gender", ["Male", "Female", "Other"])
    def test_gender(self, page, gender):
        logger.info("Тестирование выбора пола начато")
        with allure.step("Открытие страницы регистрации"):
            logger.info("Открытие страницы регистрации")
            page.open()
        with allure.step(f"Выбор пола: {gender}"):
            logger.info(f"Выбор пола: {gender}")
            page.select_gender(gender)
        with allure.step(f"Проверка корректности выбора пола {gender}"):
            logger.info(f"Проверка корректности выбора пола {gender}")
            assert page.is_gender_selected(gender), \
                f"Gender {gender} was not selected correctly"
        logger.info("Тестирование выбора пола завершено")

    @allure.feature("Тестирование поля 'Мобильный телефон'")
    @allure.severity(Severity.BLOCKER)
    @allure.title("Тест заполнения поля 'Мобильный телефон'")
    @allure.description("Этот тест проверяет корректность заполнения поля "
                        "'Мобильный телефон' в форме регистрации.")
    def test_mobile(self, page):
        logger.info("Тестирование поля 'Мобильный телефон' начато")
        with allure.step("Открытие страницы регистрации"):
            logger.info("Открытие страницы регистрации")
            page.open()
        person = PersonData()
        with allure.step(f"Заполнение поля 'Мобильный телефон' "
                         f"значением {person.mobile}"):
            logger.info(f"Заполнение поля 'Мобильный телефон' "
                        f"значением {person.mobile}")
            page.fill_mobile(person.mobile)
        time.sleep(1)
        with allure.step("Проверка корректности заполнения поля 'Мобильный телефон'"):
            logger.info("Проверка корректности заполнения поля 'Мобильный телефон'")
            assert page.get_mobile() == person.mobile, \
                f"Mobile {person.mobile} was not filled correctly"
        logger.info("Тестирование поля 'Мобильный телефон' завершено")

    @allure.feature("Тестирование выбора хобби")
    @allure.severity(Severity.TRIVIAL)
    @allure.title("Тест выбора хобби")
    @allure.description("Этот тест проверяет корректность "
                        "выбора хобби в форме регистрации.")
    @pytest.mark.parametrize("hobbies", [
        ["Sports"],
        ["Reading"],
        ["Music"],
        ["Sports", "Reading"],
        ["Sports", "Music"],
        ["Reading", "Music"],
        ["Sports", "Reading", "Music"]
    ])
    def test_hobbies(self, page, hobbies):
        logger.info("Тестирование выбора хобби начато")
        with allure.step("Открытие страницы регистрации"):
            logger.info("Открытие страницы регистрации")
            page.open()
        with allure.step(f"Выбор хобби: {hobbies}"):
            logger.info(f"Выбор хобби: {hobbies}")
            page.select_hobbies(hobbies)
        with allure.step("Проверка корректности выбора хобби"):
            logger.info("Проверка корректности выбора хобби")
            assert page.are_hobbies_selected(hobbies), \
                f"Hobbies {hobbies} were not selected correctly"
        logger.info("Тестирование выбора хобби завершено")

    @allure.feature("Тестирование загрузки изображения")
    @allure.severity(Severity.TRIVIAL)
    @allure.title("Тест загрузки изображения")
    @allure.description("Этот тест проверяет корректность "
                        "загрузки изображения в форме регистрации.")
    def test_upload_picture(self, page):
        logger.info("Тестирование загрузки изображения начато")
        with allure.step("Открытие страницы регистрации"):
            logger.info("Открытие страницы регистрации")
            page.open()
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(project_root, "images", "Battlestar_Galactica.jpg")
        with allure.step(f"Проверка существования файла {file_path}"):
            logger.info(f"Проверка существования файла {file_path}")
            assert os.path.exists(file_path), f"File {file_path} does not exist"
        with allure.step(f"Загрузка изображения {file_path}"):
            logger.info(f"Загрузка изображения {file_path}")
            page.upload_picture(file_path)
        with allure.step("Проверка корректности загрузки изображения"):
            logger.info("Проверка корректности загрузки изображения")
            assert page.is_picture_uploaded(file_path), \
                f"Picture {file_path} was not uploaded correctly"
        logger.info("Тестирование загрузки изображения завершено")

    @allure.feature("Тестирование поля 'Дата рождения'")
    @allure.severity(Severity.NORMAL)
    @allure.title("Тест заполнения поля 'Дата рождения'")
    @allure.description("Этот тест проверяет корректность "
                        "заполнения поля 'Дата рождения' в форме регистрации.")
    def test_date_of_birth(self, page):
        logger.info("Тестирование поля 'Дата рождения' начато")
        with allure.step("Открытие страницы регистрации"):
            logger.info("Открытие страницы регистрации")
            page.open()
        date_of_birth = "08-March-1987"
        with allure.step(f"Заполнение поля 'Дата рождения' значением {date_of_birth}"):
            logger.info(f"Заполнение поля 'Дата рождения' значением {date_of_birth}")
            page.fill_date_of_birth(date_of_birth)
        expected_date = "08 Mar 1987"
        with allure.step("Проверка корректности заполнения поля 'Дата рождения'"):
            logger.info("Проверка корректности заполнения поля 'Дата рождения'")
            assert page.get_date_of_birth() == expected_date, \
                f"Date of Birth {date_of_birth} was not filled correctly"
        logger.info("Тестирование поля 'Дата рождения' завершено")

    @allure.feature("Тестирование выбора предметов")
    @allure.severity(Severity.TRIVIAL)
    @allure.title("Тест выбора предметов")
    @allure.description("Этот тест проверяет "
                        "корректность выбора предметов в форме регистрации.")
    @pytest.mark.parametrize("subjects", [
        ["Maths"],
        ["Computer Science"],
        ["English", "Chemistry", "Biology", "Social Studies", "Physics"]
    ])
    def test_subjects(self, page, subjects):
        logger.info("Тестирование выбора предметов начато")
        with allure.step("Открытие страницы регистрации"):
            logger.info("Открытие страницы регистрации")
            page.open()
        with allure.step(f"Выбор предметов: {subjects}"):
            logger.info(f"Выбор предметов: {subjects}")
            page.fill_subjects(subjects)
        with allure.step("Проверка корректности выбора предметов"):
            logger.info("Проверка корректности выбора предметов")
            assert page.get_subjects() == subjects
        logger.info("Тестирование выбора предметов завершено")

    @allure.feature("Тестирование поля 'Текущий адрес'")
    @allure.severity(Severity.TRIVIAL)
    @allure.title("Тест заполнения поля 'Текущий адрес'")
    @allure.description("Этот тест проверяет корректность"
                        " заполнения поля 'Текущий адрес' в форме регистрации.")
    def test_current_address(self, page):
        logger.info("Тестирование поля 'Текущий адрес' начато")
        with allure.step("Открытие страницы регистрации"):
            logger.info("Открытие страницы регистрации")
            page.open()
        person = PersonData()
        with allure.step(f"Заполнение поля 'Текущий адрес' "
                         f"значением {person.current_address}"):
            logger.info("Заполнение поля 'Текущий адрес'")
            page.fill_current_address(person.current_address)
        with allure.step("Проверка корректности заполнения поля 'Текущий адрес'"):
            logger.info("Проверка корректности заполнения поля 'Текущий адрес'")
            assert page.get_current_address() == person.current_address, \
                f"Address {person.current_address} was not filled correctly"
        logger.info("Тестирование поля 'Текущий адрес' завершено")

    @allure.feature("Тестирование выбора штата и города")
    @allure.severity(Severity.TRIVIAL)
    @allure.title("Тест выбора штата и города")
    @allure.description("Этот тест проверяет корректность выбора штата "
                        "и соответствующего ему города в форме регистрации.")
    @pytest.mark.parametrize("state, city", [
        ("NCR", "Delhi"),
        ("Uttar Pradesh", "Lucknow"),
        ("Haryana", "Karnal"),
        ("Rajasthan", "Jaipur")
    ])
    def test_state_city(self, page, state, city):
        logger.info(f"Тестирование выбора штата {state} и города {city} начато")
        with allure.step("Открытие страницы регистрации"):
            logger.info("Открытие страницы регистрации")
            page.open()
        with allure.step(f"Выбор штата: {state}"):
            logger.info(f"Выбор штата: {state}")
            page.select_state(state)
        with allure.step(f"Выбор города: {city}"):
            logger.info(f"Выбор города: {city}")
            page.select_city(city)
        with allure.step(f"Проверка корректности выбора штата {state}"):
            logger.info(f"Проверка корректности выбора штата {state}")
            assert page.is_state_selected(state), \
                f"State {state} was not selected correctly"
        with allure.step(f"Проверка корректности выбора города {city}"):
            logger.info(f"Проверка корректности выбора города {city}")
            assert page.is_city_selected(city), \
                f"City {city} was not selected correctly"
        logger.info(f"Тестирование выбора штата {state} и города {city} завершено")
