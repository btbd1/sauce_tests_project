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

    def sort_elements_low_high_price(self):
        self.element_is_visible(Locators.SORT_BUTTON_LOW_HIGH).click()
        price_list = self.find_elements(Locators.ITEM_PRICE)
        # переводим в числа с точкой и убираем знак $
        modified_prices = [float(price.text.replace("$", "")) for price in price_list]
        # Для каждого i в списке, начиная со второго элемента, проверяем, больше ли он или равен предыдущему
        result = all(modified_prices[i] >= modified_prices[i-1] for i in range(1, len(modified_prices)))

        assert result == True, f'Sorting low to high is broken'
