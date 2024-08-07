from dataclasses import asdict

import pytest
import allure
import os
from allure_commons.types import Severity
from logger_config import configure_logger
from pages.registration_page import RegistrationPage
from data.data import PersonData

logger = configure_logger(__name__, "test.log")


@allure.epic("Тестирование формы регистрации")
@allure.description_html("""
<h2>Тестирование формы регистрации на сайте DemoQA</h2>
<p>Этот набор тестов проверяет функциональность формы регистрации, включая:</p>
<ul>
    <li>Заполнение всех полей формы</li>
    <li>Отправку формы</li>
    <li>Проверку корректности отображения введенных данных в модальном окне</li>
</ul>
""")
class TestRegistrationForm:

    @pytest.fixture(scope="function")
    def page(self, browser):
        return RegistrationPage(browser)

    @allure.feature("Заполнение формы регистрации")
    @allure.story("Полное заполнение формы и проверка результатов")
    @allure.severity(Severity.BLOCKER)
    @allure.title("Тест заполнения и отправки формы регистрации")
    @allure.description("""
    Этот тест выполняет следующие шаги:
    1. Открывает страницу регистрации
    2. Заполняет все поля формы
    3. Отправляет форму
    4. Проверяет успешность отправки
    5. Верифицирует корректность отображения всех введенных данных в модальном окне
    """)
    def test_fill_registration_form(self, page):
        logger.info("Начало теста заполнения формы регистрации")

        with allure.step("Открытие страницы регистрации"):
            logger.info("Открытие страницы регистрации")
            page.open()

        person = PersonData()
        allure.dynamic.parameter("test_data", asdict(person))

        with allure.step("Заполнение всех полей формы"):
            self._fill_form_fields(page, person)

        with allure.step("Отправка формы"):
            logger.info("Отправка формы")
            page.submit_form()

        with (allure.step("Проверка успешной отправки формы")):
            logger.info("Проверка успешной отправки формы")
            assert page.EXPECTED_SUCCESS_MESSAGE in page.label_text(), \
                f"Заголовок не совпадает {page.label_text()}"
            assert page.is_submission_successful(), "Форма не была успешно отправлена"

        with allure.step("Проверка корректности отображения данных в модальном окне"):
            self._verify_modal_content(page, person)

        logger.info("Все проверки пройдены успешно")
        logger.info("Тест заполнения формы регистрации завершен")

    @allure.step("Заполнение полей формы")
    def _fill_form_fields(self, page, person):
        logger.info(f"Заполнение поля 'Имя' значением {person.first_name}")
        page.fill_first_name(person.first_name)

        logger.info(f"Заполнение поля 'Фамилия' значением {person.last_name}")
        page.fill_last_name(person.last_name)

        logger.info(f"Заполнение поля 'Email' значением {person.email}")
        page.fill_email(person.email)

        gender = "Male"
        logger.info(f"Выбор пола: {gender}")
        page.select_gender(gender)

        logger.info(f"Заполнение поля 'Мобильный телефон' значением {person.mobile}")
        page.fill_mobile(person.mobile)

        hobbies = ["Sports", "Reading"]
        logger.info(f"Выбор хобби: {hobbies}")
        page.select_hobbies(hobbies)

        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(project_root, "images", "Battlestar_Galactica.jpg")
        logger.info(f"Загрузка изображения {file_path}")
        page.upload_picture(file_path)

        date_of_birth = "08-March-1987"
        logger.info(f"Заполнение поля 'Дата рождения' значением {date_of_birth}")
        page.fill_date_of_birth(date_of_birth)

        subjects = ["Maths", "Computer Science"]
        logger.info(f"Выбор предметов: {subjects}")
        page.fill_subjects(subjects)

        logger.info(f"Заполнение поля 'Текущий адрес' "
                    f"значением {person.current_address}")
        page.fill_current_address(person.current_address)

        state, city = "NCR", "Delhi"
        logger.info(f"Выбор штата: {state} и города: {city}")
        page.select_state(state)
        page.select_city(city)

    @allure.step("Проверка содержимого модального окна")
    def _verify_modal_content(self, page, person):
        actual_modal_content = page.get_submitted_data()
        logger.info(f"Фактическое содержимое модального окна: {actual_modal_content}")

        expected_content = [
            (f"Student Name {person.first_name} {person.last_name}", "Имя студента"),
            (f"Student Email {person.email}", "Email студента"),
            ("Gender Male", "Пол"),
            (f"Mobile {person.mobile}", "Мобильный телефон"),
            ("Date of Birth 08 March,1987", "Дата рождения"),
            ("Subjects Maths, Computer Science", "Предметы"),
            ("Hobbies Sports, Reading", "Хобби"),
            ("Picture Battlestar_Galactica.jpg", "Изображение"),
            ("State and City NCR Delhi", "Штат и город"),
            ("Address {}".format(person.current_address.replace('\n', ' ')), "Адрес"),
        ]

        for content, description in expected_content:
            assert content in actual_modal_content, \
                f"{description} не найден в модальном окне"
            logger.info(f"Проверка пройдена: {description}")

        logger.info("Все проверки содержимого модального окна пройдены успешно")
