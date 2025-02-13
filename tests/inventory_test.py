from conftest import driver
from time import sleep
from pages.inventory_page import InventoryPage
from tests.form_test import test_login_form_correct


def test_sorting_items_low_to_high(driver):
    inventory_page = InventoryPage(driver)
    test_login_form_correct(driver)
    inventory_page.sort_elements_low_high_price()
