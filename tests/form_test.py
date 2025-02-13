from pages.form_page import FormPage
from conftest import driver
from time import sleep


def test_login_form_correct(driver):
    form_page = FormPage(driver)
    form_page.open('https://www.saucedemo.com')
    form_page.fill_fields_correct()


def test_login_form_incorrect(driver):
    form_page = FormPage(driver)
    form_page.open('https://www.saucedemo.com')
    form_page.fill_fields_incorrect()
    sleep(1)
    form_page.find_error_button()
