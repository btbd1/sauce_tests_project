from conftest import driver
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from tests.form_test import test_login_form_correct


def test_add_two_items_to_cart(driver):
    inventory_page = InventoryPage(driver)
    test_login_form_correct(driver)
    inventory_page.add_two_elements_to_cart()
    inventory_page.open_cart()


def test_add_one_item_to_cart(driver):
    inventory_page = InventoryPage(driver)
    test_login_form_correct(driver)
    inventory_page.add_one_element_to_cart()
    inventory_page.open_cart()


def test_check_cart_list_with_items(driver):
    cart_page = CartPage(driver)
    test_add_two_items_to_cart(driver)
    cart_page.check_items_in_list()


def test_should_be_empty_cart_after_delete(driver):
    cart_page = CartPage(driver)
    test_add_one_item_to_cart(driver)
    cart_page.delete_item_from_cart()


def test_create_successful_checkout(driver):
    cart_page = CartPage(driver)
    test_add_one_item_to_cart(driver)
    cart_page.make_checkout(driver)
