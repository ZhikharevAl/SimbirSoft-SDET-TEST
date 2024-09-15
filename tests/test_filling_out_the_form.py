from dataclasses import asdict

import pytest
import allure
import os
from allure_commons.types import Severity
from pages.registration_page import RegistrationPage
from data.data import PersonData



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
    def test_fill_registration_form(self, page, caplog, logger):
        logger.info("Начало теста заполнения формы регистрации")

        with allure.step("Открытие страницы регистрации"):
            page.open()

        person = PersonData()
        allure.dynamic.parameter("test_data", asdict(person))

        with allure.step("Заполнение всех полей формы"):
            self._fill_form_fields(page, person)

        with allure.step("Отправка формы"):
            page.submit_form()

        with (allure.step("Проверка успешной отправки формы")):
            assert page.EXPECTED_SUCCESS_MESSAGE in page.label_text(), \
                f"Заголовок не совпадает {page.label_text()}"
            assert page.is_submission_successful(), "Форма не была успешно отправлена"

        with allure.step("Проверка корректности отображения данных в модальном окне"):
            self._verify_modal_content(page, person)

        logger.info("Тест заполнения формы регистрации завершен")

    @allure.step("Заполнение полей формы")
    def _fill_form_fields(self, page, person):

        page.fill_first_name(person.first_name)
        page.fill_last_name(person.last_name)
        page.fill_email(person.email)
        page.select_gender('Male')
        page.fill_mobile(person.mobile)
        page.select_hobbies(["Sports", "Reading"])

        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(project_root, "images", "Battlestar_Galactica.jpg")
        page.upload_picture(file_path)

        date_of_birth = "08-March-1987"
        page.fill_date_of_birth(date_of_birth)

        subjects = ["Maths", "Computer Science"]
        page.fill_subjects(subjects)
        page.fill_current_address(person.current_address)

        state, city = "NCR", "Delhi"
        page.select_state(state)
        page.select_city(city)

    @allure.step("Проверка содержимого модального окна")
    def _verify_modal_content(self, page, person):
        actual_modal_content = page.get_submitted_data()

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
