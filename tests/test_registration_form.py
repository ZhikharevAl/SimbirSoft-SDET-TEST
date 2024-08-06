import os

import pytest
import time

from data.data import PersonData
from pages.registration_page import RegistrationPage


class TestRegistrationForm:

    @pytest.fixture(scope="function")
    def page(self, browser):
        return RegistrationPage(browser)

    def test_first_name(self, page):
        page.open()
        person = PersonData()
        page.fill_first_name(person.first_name)
        assert page.get_first_name() == person.first_name, (f"Name {person.first_name} "
                                                            f"was not filled correctly")

    def test_last_name(self, page):
        page.open()
        person = PersonData()
        page.fill_last_name(person.last_name)
        assert page.get_last_name() == person.last_name, (f"Name {person.last_name} "
                                                          f"was not filled correctly")

    def test_email(self, page):
        page.open()
        person = PersonData()
        page.fill_email(person.email)
        assert page.get_email() == person.email, (f"Email {person.email} "
                                                  f"was not filled correctly")

    @pytest.mark.parametrize("gender", ["Male", "Female", "Other"])
    def test_gender(self, page, gender):
        page.open()
        page.select_gender(gender)
        assert page.is_gender_selected(gender), (f"Gender {gender} "
                                                 f"was not selected correctly")

    def test_mobile(self, page):
        page.open()
        person = PersonData()
        page.fill_mobile(person.mobile)
        time.sleep(1)
        assert page.get_mobile() == person.mobile, (f"Mobile {person.mobile} "
                                                    f"was not filled correctly")

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
        page.open()
        page.select_hobbies(hobbies)
        assert page.are_hobbies_selected(hobbies), (f"Hobbies {hobbies} "
                                                    f"were not selected correctly")

    def test_upload_picture(self, page):
        page.open()
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(project_root, "images", "Battlestar_Galactica.jpg")
        assert os.path.exists(file_path), f"File {file_path} does not exist"
        page.upload_picture(file_path)
        assert page.is_picture_uploaded(file_path), (f"Picture {file_path} "
                                                     f"was not uploaded correctly")

    def test_date_of_birth(self, page):
        page.open()
        date_of_birth = "08-March-1987"
        page.fill_date_of_birth(date_of_birth)
        expected_date = "08 Mar 1987"
        assert page.get_date_of_birth() == expected_date, \
            (f"Date of Birth {date_of_birth} "
             f"was not filled correctly")

    @pytest.mark.parametrize("subjects", [
        ["Maths"],
        ["Computer Science"],
        ["English", "Chemistry", "Biology", "Social Studies", "Physics"]
    ])
    def test_subjects(self, page, subjects):
        page.open()
        page.fill_subjects(subjects)
        assert page.get_subjects() == subjects

    def test_current_address(self, page):
        page.open()
        person = PersonData()
        page.fill_current_address(person.current_address)
        assert page.get_current_address() == person.current_address, \
            (f"Address {person.current_address} was not "
             f"filled correctly")

    @pytest.mark.parametrize("state, city", [
        ("NCR", "Delhi"),
        ("Uttar Pradesh", "Lucknow"),
        ("Haryana", "Karnal"),
        ("Rajasthan", "Jaipur")
    ])
    def test_state_city(self, page, state, city):
        page.open()
        page.select_state(state)
        page.select_city(city)
        assert page.is_state_selected(state), (f"State {state} was not selected "
                                               f"correctly")
        assert page.is_city_selected(city), f"City {city} was not selected correctly"
