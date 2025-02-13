from pages.base_page import BasePage
from locators.inventory_page_locators import InventoryPageLocators as Locators


class InventoryPage(BasePage):  # наследуем от другого класса
    def get_title(self):
        return self.find_element(Locators.CURRENT_TITLE)

    def add_two_elements_to_cart(self):
        self.element_is_visible(Locators.BUTTON_BACKPACK).click()
        self.element_is_visible(Locators.BUTTON_BIKE_LIGHT).click()

    def add_one_element_to_cart(self):
        self.element_is_visible(Locators.BUTTON_BIKE_LIGHT).click()

    def open_cart(self):
        self.element_is_visible(Locators.BUTTON_CART).click()
