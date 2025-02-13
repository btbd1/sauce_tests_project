from pages.base_page import BasePage
from pages.checkout_pages import CheckoutPages
from locators.cart_page_locators import CartPageLocators as Locators


class CartPage(BasePage):
    def check_items_in_list(self):
        backpack = self.find_element(Locators.ITEM_BACKPACK)
        bike_light = self.find_element(Locators.ITEM_BIKE_LIGHT)
        items_in_list = [backpack, bike_light]
        if items_in_list:
            result_items = f"{items_in_list[0].text, items_in_list[1].text}"
        else:
            result_items = "Items in list not found!"
        assert result_items == "('Sauce Labs Backpack', 'Sauce Labs Bike Light')", f"Items not found!"

        backpack_quantity = self.find_element(Locators.BACKPACK_QUANTITY)
        bike_light_quantity = self.find_element(Locators.BIKE_LIGHT_QUANTITY)
        product_quantity = [backpack_quantity, bike_light_quantity]
        if product_quantity:
            result_items_quantity = f"{product_quantity[0].text, product_quantity[1].text}"
        else:
            result_items_quantity = "Items quantity not found!"
        assert result_items_quantity == "('1', '1')", f"Incorrect items quantity!"

    def delete_item_from_cart(self):
        self.find_element(Locators.REMOVE_BIKE_LIGHT_BUTTON).click()
        cart_badge = self.find_elements(Locators.CART_BADGE)
        cart_item = self.find_elements(Locators.ITEM_BIKE_LIGHT)
        assert len(cart_item) == 0, f'Item Bike light still in cart'
        assert len(cart_badge) == 0, f'Cart badge is visible after item deleting'

    def make_checkout(self, driver):
        self.find_element(Locators.CHECKOUT_BUTTON).click()
        checkout_page = CheckoutPages(driver)
        checkout_page.fill_checkout_fields_right()
        checkout_page.finish_checkout_successful()
